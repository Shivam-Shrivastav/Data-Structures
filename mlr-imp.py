#!/usr/bin/env python3

import argparse
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import dspy
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

DEFAULT_AZURE_API_BASE_SUFFIX = "/openai/v1/"
DEFAULT_MODEL = "gpt-4.1"
DEFAULT_LOG_DIR = "logs"


# ============================================================
# PDF EXTRACTION
# ============================================================

def extract_pdf_text(pdf_path: str) -> str:
    """Extract PDF text while preserving page boundaries."""
    path = Path(pdf_path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, got: {path.suffix}")

    reader = PdfReader(str(path))

    if not reader.pages:
        raise ValueError("PDF contains no pages.")

    pages = []
    empty_pages = 0

    for page_number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:
            print(
                f"Warning: failed to extract page {page_number}: {exc}",
                file=sys.stderr,
            )
            text = ""

        if not text.strip():
            empty_pages += 1

        pages.append(
            f"\n\n===== PAGE {page_number} =====\n\n{text.strip()}"
        )

    document = "".join(pages).strip()

    if not document:
        raise ValueError(
            "No text could be extracted from the PDF. "
            "The PDF may be scanned/image-only and require OCR."
        )

    if empty_pages:
        print(
            f"Warning: {empty_pages}/{len(reader.pages)} "
            "pages had no extractable text.",
            file=sys.stderr,
        )

    return document


# ============================================================
# AZURE OPENAI V1
# ============================================================

def create_azure_openai_lm(
    model: str,
    endpoint: str,
    api_key: str,
    temperature: float,
):
    """
    Create a DSPy LM using the Azure OpenAI v1 OpenAI-compatible endpoint.

    The `model` value is the Azure deployment name.
    """
    api_base = f"{endpoint.rstrip('/')}{DEFAULT_AZURE_API_BASE_SUFFIX}"

    return dspy.LM(
        f"openai/{model}",
        api_base=api_base,
        api_key=api_key,
        model_type="chat",
        temperature=temperature,
    )


# ============================================================
# DOCUMENT RETRIEVAL TOOLS
# ============================================================

def _clip_text(text: str, max_chars: int) -> str:
    text = str(text)
    if len(text) <= max_chars:
        return text
    return (
        text[:max_chars]
        + f"\n\n[TRUNCATED: {len(text):,} total chars; "
          f"showing first {max_chars:,}]"
    )


def _split_pages(document: str) -> list[tuple[int, str]]:
    """Return [(page_number, page_text), ...] from our page markers."""
    matches = list(
        re.finditer(
            r"===== PAGE (\d+) =====",
            document,
            flags=re.IGNORECASE,
        )
    )

    if not matches:
        return [(1, document)]

    pages = []
    for i, match in enumerate(matches):
        page_number = int(match.group(1))
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(document)
        pages.append((page_number, document[start:end].strip()))

    return pages


def build_document_tools(
    document: str,
    max_tool_output_chars: int = 5000,
):
    """
    Build small, deterministic retrieval tools over the PDF text.

    The full document remains available as `document` inside RLM,
    but these tools make it easy for the model to retrieve bounded
    pieces instead of printing the entire document.
    """
    pages = _split_pages(document)

    def search_document(query: str, context_chars: int = 700) -> str:
        """
        Search the document for a keyword/phrase and return only
        bounded context around matching lines. Prefer this over
        print(document) for large documents.
        """
        query = str(query).strip()
        if not query:
            return "search_document: query is empty."

        terms = [t.lower() for t in re.findall(r"\w+", query) if len(t) > 1]
        if not terms:
            terms = [query.lower()]

        results = []
        total_matches = 0

        for page_number, page_text in pages:
            lines = page_text.splitlines()

            for i, line in enumerate(lines):
                line_lower = line.lower()

                if all(term in line_lower for term in terms):
                    total_matches += 1
                    lo = max(0, i - 3)
                    hi = min(len(lines), i + 4)

                    snippet = "\n".join(lines[lo:hi]).strip()

                    results.append(
                        f"[Page {page_number} | line {i + 1}]\n{snippet}"
                    )

        if not results:
            # Fallback: phrase search if tokenized AND search was too strict.
            phrase = query.lower()
            for page_number, page_text in pages:
                pos = page_text.lower().find(phrase)
                if pos >= 0:
                    lo = max(0, pos - context_chars)
                    hi = min(len(page_text), pos + len(query) + context_chars)
                    results.append(
                        f"[Page {page_number}]\n{page_text[lo:hi]}"
                    )

        if not results:
            return f"No matches found for: {query!r}"

        output = (
            f"Found {total_matches or len(results)} match(es) for {query!r}.\n\n"
            + "\n\n".join(results)
        )

        return _clip_text(output, max_tool_output_chars)

    def get_page(page_number: int) -> str:
        """
        Return one PDF page only. Use this when search_document()
        identifies a relevant page.
        """
        try:
            requested = int(page_number)
        except (TypeError, ValueError):
            return f"Invalid page number: {page_number!r}"

        for number, text in pages:
            if number == requested:
                return _clip_text(
                    f"[Page {number}]\n{text}",
                    max_tool_output_chars,
                )

        return f"Page {requested} does not exist. Available pages: {len(pages)}."

    def get_pages(start_page: int, end_page: int) -> str:
        """
        Return a bounded inclusive page range.
        Keep ranges small to avoid flooding the next RLM iteration.
        """
        try:
            start = int(start_page)
            end = int(end_page)
        except (TypeError, ValueError):
            return "start_page and end_page must be integers."

        if start > end:
            start, end = end, start

        # Hard safety cap: a tool call should never intentionally return
        # an unbounded chunk of the document.
        if end - start + 1 > 5:
            end = start + 4

        selected = [
            f"===== PAGE {number} =====\n{text}"
            for number, text in pages
            if start <= number <= end
        ]

        if not selected:
            return f"No pages found in range {start}-{end}."

        return _clip_text(
            "\n\n".join(selected),
            max_tool_output_chars,
        )

    return [search_document, get_page, get_pages]


def make_interpreter_factory():
    """
    Add explicit execution guidance to DSPy's RLM action prompt.

    Current DSPy RLM supports factories exposing an
    `execution_instructions` attribute.
    """
    instructions = """
AZURE OPENAI MODEL NOTE:

The root/sub model names configured for this run are Azure OpenAI deployment
names, not necessarily the underlying model IDs.

DOCUMENT RETRIEVAL / CONTEXT EFFICIENCY RULES:

The full input document is available as the Python variable `document`.
Do NOT use `print(document)` or otherwise print the entire document unless
the document is demonstrably tiny.

For large documents, prefer:
  1. search_document("specific keyword or phrase")
  2. get_page(page_number)
  3. get_pages(start_page, end_page)

Only print small, relevant snippets. Keep REPL output focused because
everything printed becomes part of the next RLM iteration's working context.

Start with search_document(query) for entity/fact lookup tasks. If the
search identifies a page, use get_page(page_number) only when more context
is needed. Use llm_query() on a small relevant snippet when semantic
reasoning is required.

Do not dump the entire document merely to understand its structure.
"""

    def factory():
        return dspy.PythonInterpreter()

    factory.execution_instructions = instructions
    return factory


# ============================================================
# CREATE RLM
# ============================================================

def create_rlm(
    model: str,
    sub_model: str | None,
    endpoint: str,
    api_key: str,
    temperature: float,
    max_iters: int,
    max_llm_calls: int,
    max_output_chars: int,
    verbose: bool,
    document: str,
    max_tool_output_chars: int,
):
    root_lm = create_azure_openai_lm(
        model=model,
        endpoint=endpoint,
        api_key=api_key,
        temperature=temperature,
    )

    dspy.configure(
        lm=root_lm,
        track_usage=True,
    )

    sub_lm = None

    if sub_model:
        sub_lm = create_azure_openai_lm(
            model=sub_model,
            endpoint=endpoint,
            api_key=api_key,
            temperature=temperature,
        )

    tools = build_document_tools(
        document=document,
        max_tool_output_chars=max_tool_output_chars,
    )

    return dspy.RLM(
        "document, query -> answer",
        max_iters=max_iters,
        max_llm_calls=max_llm_calls,
        max_output_chars=max_output_chars,
        verbose=verbose,
        sub_lm=sub_lm,
        tools=tools,
        interpreter_factory=make_interpreter_factory(),
    ), root_lm, sub_lm


# ============================================================
# TRACE HELPERS
# ============================================================

def make_json_safe(value: Any) -> Any:
    """Convert arbitrary DSPy values into JSON-safe values."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, dict):
        return {
            str(k): make_json_safe(v)
            for k, v in value.items()
        }

    if isinstance(value, (list, tuple)):
        return [make_json_safe(v) for v in value]

    try:
        return str(value)
    except Exception:
        return repr(value)


def extract_trajectory(result) -> list[dict[str, Any]]:
    """
    Extract the official DSPy RLM trajectory.

    DSPy documents this as a list of dictionaries containing:
      - reasoning
      - code
      - output
    """
    trajectory = getattr(result, "trajectory", None)

    if not trajectory:
        return []

    steps = []

    for index, raw_step in enumerate(trajectory, start=1):
        if isinstance(raw_step, dict):
            reasoning = raw_step.get("reasoning")
            code = raw_step.get("code")
            output = raw_step.get("output")
            step = {
                "iteration": index,
                "reasoning": make_json_safe(reasoning),
                "code": make_json_safe(code),
                "output": make_json_safe(output),
                "raw": make_json_safe(raw_step),
            }
        else:
            step = {
                "iteration": index,
                "reasoning": None,
                "code": None,
                "output": None,
                "raw": make_json_safe(raw_step),
            }

        steps.append(step)

    return enrich_trajectory(steps)


def get_usage(result) -> Any:
    """Best-effort extraction of DSPy LM usage information."""
    try:
        if hasattr(result, "get_lm_usage"):
            return make_json_safe(result.get_lm_usage())
    except Exception:
        pass

    for attr in ("lm_usage", "usage"):
        try:
            value = getattr(result, attr, None)
            if value is not None:
                return make_json_safe(value)
        except Exception:
            pass

    return None



# ============================================================
# EFFICIENCY / USAGE METRICS
# ============================================================

def estimate_tokens(text: Any) -> int:
    """
    Rough token estimate for trace diagnostics only.

    This is NOT provider billing data. Actual usage is preferred
    when the LM exposes usage metadata.
    """
    if text is None:
        return 0
    value = str(text)
    return max(0, (len(value) + 3) // 4)


def step_efficiency(step: dict[str, Any]) -> dict[str, Any]:
    reasoning = step.get("reasoning") or ""
    code = step.get("code") or ""
    output = step.get("output") or ""

    return {
        "reasoning_chars": len(str(reasoning)),
        "code_chars": len(str(code)),
        "output_chars": len(str(output)),
        "estimated_reasoning_tokens": estimate_tokens(reasoning),
        "estimated_code_tokens": estimate_tokens(code),
        "estimated_output_tokens": estimate_tokens(output),
        "estimated_visible_step_tokens": (
            estimate_tokens(reasoning)
            + estimate_tokens(code)
            + estimate_tokens(output)
        ),
    }


def enrich_trajectory(trajectory: list[dict[str, Any]]) -> list[dict[str, Any]]:
    enriched = []

    for step in trajectory:
        item = dict(step)
        item["efficiency"] = step_efficiency(item)
        enriched.append(item)

    return enriched


def extract_lm_history(lm) -> list[dict[str, Any]]:
    """
    Best-effort extraction of DSPy's recorded LM history.

    The exact history shape can vary across DSPy versions/providers,
    so we preserve useful fields without assuming a fixed schema.
    """
    if lm is None:
        return []

    try:
        history = getattr(lm, "history", None)
    except Exception:
        return []

    if not history:
        return []

    result = []

    for index, entry in enumerate(history, start=1):
        if not isinstance(entry, dict):
            result.append({
                "call": index,
                "raw": make_json_safe(entry),
            })
            continue

        usage = (
            entry.get("usage")
            or entry.get("response_usage")
            or entry.get("token_usage")
        )

        result.append({
            "call": index,
            "model": make_json_safe(entry.get("model")),
            "usage": make_json_safe(usage),
            "prompt_tokens": make_json_safe(
                (usage or {}).get("prompt_tokens")
                if isinstance(usage, dict)
                else None
            ),
            "completion_tokens": make_json_safe(
                (usage or {}).get("completion_tokens")
                if isinstance(usage, dict)
                else None
            ),
            "total_tokens": make_json_safe(
                (usage or {}).get("total_tokens")
                if isinstance(usage, dict)
                else None
            ),
            "finish_reason": make_json_safe(entry.get("finish_reason")),
        })

    return result


def summarize_usage(history: list[dict[str, Any]]) -> dict[str, Any]:
    prompt = 0
    completion = 0
    total = 0
    observed = 0

    for item in history:
        for key, target in (
            ("prompt_tokens", "prompt"),
            ("completion_tokens", "completion"),
            ("total_tokens", "total"),
        ):
            value = item.get(key)
            if isinstance(value, int):
                if target == "prompt":
                    prompt += value
                elif target == "completion":
                    completion += value
                else:
                    total += value

        if any(
            isinstance(item.get(k), int)
            for k in ("prompt_tokens", "completion_tokens", "total_tokens")
        ):
            observed += 1

    return {
        "calls_with_observed_token_usage": observed,
        "prompt_tokens": prompt,
        "completion_tokens": completion,
        "total_tokens": total,
    }


# ============================================================
# JSON TRACE
# ============================================================

def save_json_trace(
    run_dir: Path,
    *,
    started_at: str,
    duration_seconds: float,
    pdf_path: str,
    query: str,
    model: str,
    sub_model: str | None,
    max_iters: int,
    max_llm_calls: int,
    max_output_chars: int,
    temperature: float,
    document_chars: int,
    result,
    trajectory: list[dict[str, Any]],
    root_lm=None,
    sub_lm=None,
    max_tool_output_chars: int = 5000,
):
    trace = {
        "trace_version": 1,
        "started_at_utc": started_at,
        "duration_seconds": round(duration_seconds, 3),
        "pdf": str(Path(pdf_path).expanduser().resolve()),
        "query": query,
        "root_model": model,
        "sub_model": sub_model,
        "api_endpoint": f"{os.getenv('AZURE_OPENAI_ENDPOINT', '').rstrip('/')}{DEFAULT_AZURE_API_BASE_SUFFIX}",
        "config": {
            "max_iters": max_iters,
            "max_llm_calls": max_llm_calls,
            "max_output_chars": max_output_chars,
            "temperature": temperature,
        },
        "document": {
            "characters": document_chars,
            "estimated_tokens": estimate_tokens("x" * document_chars),
        },
        "retrieval": {
            "max_tool_output_chars": max_tool_output_chars,
            "strategy": "search_document/get_page/get_pages",
        },
        "iterations": len(trajectory),
        "steps": trajectory,
        "estimated_visible_tokens": sum(
            step.get("efficiency", {}).get(
                "estimated_visible_step_tokens", 0
            )
            for step in trajectory
        ),
        "final_answer": make_json_safe(getattr(result, "answer", None)),
        "final_reasoning": make_json_safe(
            getattr(result, "final_reasoning", None)
        ),
        "lm_usage": get_usage(result),
        "root_lm_history": extract_lm_history(root_lm),
        "sub_lm_history": extract_lm_history(sub_lm),
        "usage_summary": {
            "root": summarize_usage(extract_lm_history(root_lm)),
            "sub": summarize_usage(extract_lm_history(sub_lm)),
        },
    }

    path = run_dir / "trace.json"
    path.write_text(
        json.dumps(trace, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return path, trace


# ============================================================
# HTML VISUALIZER
# ============================================================

def code_block(value: Any, empty_text: str = "(none)") -> str:
    if value is None or str(value).strip() == "":
        return f'<div class="empty">{empty_text}</div>'

    return f"<pre>{html.escape(str(value))}</pre>"


def render_step(step: dict[str, Any]) -> str:
    iteration = html.escape(str(step.get("iteration", "?")))
    reasoning = step.get("reasoning")
    code = step.get("code")
    output = step.get("output")
    efficiency = step.get("efficiency", {})
    visible_tokens = efficiency.get("estimated_visible_step_tokens", 0)
    output_chars = efficiency.get("output_chars", 0)

    return f"""
    <section class="step">
      <div class="step-header">
        <span class="badge">ITERATION {iteration}</span>
        <span style="float:right;color:#667085;font-size:12px">
          ~{visible_tokens:,} visible tokens · {output_chars:,} output chars
        </span>
      </div>

      <details open>
        <summary>RLM action / reasoning field</summary>
        {code_block(reasoning)}
      </details>

      <details open>
        <summary>Generated REPL code</summary>
        {code_block(code)}
      </details>

      <details open>
        <summary>REPL output</summary>
        {code_block(output)}
      </details>
    </section>
    """


def create_html_visualizer(
    run_dir: Path,
    trace: dict[str, Any],
) -> Path:
    steps = trace.get("steps", [])
    rendered_steps = "\n".join(render_step(step) for step in steps)

    answer = html.escape(str(trace.get("final_answer") or "(no answer)"))
    query = html.escape(str(trace.get("query", "")))
    pdf = html.escape(str(trace.get("pdf", "")))
    model = html.escape(str(trace.get("root_model", "")))
    sub_model = html.escape(str(trace.get("sub_model") or "(same root model)"))
    started = html.escape(str(trace.get("started_at_utc", "")))
    duration = html.escape(str(trace.get("duration_seconds", "")))
    iterations = html.escape(str(trace.get("iterations", 0)))
    usage = trace.get("lm_usage")
    usage_summary = trace.get("usage_summary", {})
    estimated_visible_tokens = trace.get("estimated_visible_tokens", 0)
    document_chars = trace.get("document", {}).get("characters", 0)
    document_estimated_tokens = trace.get("document", {}).get(
        "estimated_tokens", 0
    )
    root_usage = usage_summary.get("root", {})
    sub_usage = usage_summary.get("sub", {})

    usage_html = code_block(
        json.dumps(usage, indent=2, ensure_ascii=False)
        if usage is not None
        else None,
        empty_text="Usage information was not exposed by this DSPy version.",
    )

    root_prompt = int(root_usage.get("prompt_tokens") or 0)
    root_completion = int(root_usage.get("completion_tokens") or 0)
    root_total = int(root_usage.get("total_tokens") or 0)
    sub_total = int(sub_usage.get("total_tokens") or 0)

    document_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DSPy RLM Trace</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: #f5f7fa;
    color: #172033;
  }}
  .container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 32px 20px 60px;
  }}
  h1 {{ margin-bottom: 8px; }}
  .subtitle {{ color: #667085; margin-bottom: 24px; }}
  .card {{
    background: white;
    border: 1px solid #dfe3e8;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,.04);
  }}
  .meta {{
    display: grid;
    grid-template-columns: 150px 1fr;
    gap: 8px 16px;
    font-size: 14px;
  }}
  .meta strong {{ color: #475467; }}
  .answer {{
    border-left: 4px solid #475467;
    background: #f8fafc;
  }}
  .answer pre {{ white-space: pre-wrap; }}
  .step {{
    background: white;
    border: 1px solid #dfe3e8;
    border-radius: 12px;
    margin: 18px 0;
    overflow: hidden;
  }}
  .step-header {{
    padding: 14px 18px;
    border-bottom: 1px solid #eaecf0;
  }}
  .badge {{
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .04em;
  }}
  details {{
    border-bottom: 1px solid #eaecf0;
  }}
  details:last-child {{ border-bottom: 0; }}
  summary {{
    cursor: pointer;
    padding: 14px 18px;
    font-weight: 600;
  }}
  pre {{
    margin: 0;
    padding: 16px 18px;
    overflow-x: auto;
    background: #111827;
    color: #e5e7eb;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 13px;
    line-height: 1.55;
    white-space: pre-wrap;
    word-break: break-word;
  }}
  .empty {{
    padding: 14px 18px;
    color: #667085;
    font-style: italic;
  }}
  .timeline {{
    border-left: 3px solid #d0d5dd;
    margin-left: 12px;
    padding-left: 20px;
  }}
  .section-title {{
    margin-top: 30px;
  }}
  @media (max-width: 700px) {{
    .meta {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>
<div class="container">

  <h1>DSPy RLM Execution Trace</h1>
  <div class="subtitle">
    Generated locally from the RLM trajectory returned by DSPy.
  </div>

  <div class="card">
    <h2>Run Information</h2>
    <div class="meta">
      <strong>Started (UTC)</strong><span>{started}</span>
      <strong>Duration</strong><span>{duration} seconds</span>
      <strong>Iterations</strong><span>{iterations}</span>
      <strong>Root model</strong><span>{model}</span>
      <strong>Sub model</strong><span>{sub_model}</span>
      <strong>PDF</strong><span>{pdf}</span>
      <strong>Query</strong><span>{query}</span>
    </div>
  </div>

  <div class="card">
    <h2>Context / Token Efficiency</h2>
    <div class="meta">
      <strong>Document size</strong><span>{document_chars:,} chars (~{document_estimated_tokens:,} estimated tokens)</span>
      <strong>Visible trace output</strong><span>~{estimated_visible_tokens:,} estimated tokens</span>
      <strong>Root LM prompt tokens</strong><span>{root_prompt:,}</span>
      <strong>Root LM completion tokens</strong><span>{root_completion:,}</span>
      <strong>Root LM total tokens</strong><span>{root_total:,}</span>
      <strong>Sub LM total tokens</strong><span>{sub_total:,}</span>
    </div>
    <p class="subtitle">
      Estimated values use ~4 characters/token and are diagnostic only.
      Provider-reported usage is shown when DSPy exposes it.
    </p>
  </div>

  <div class="card answer">
    <h2>Final Answer</h2>
    <pre>{answer}</pre>
  </div>

  <h2 class="section-title">RLM Iterations</h2>

  <div class="timeline">
    {rendered_steps if rendered_steps else
     '<div class="card">No trajectory steps were returned.</div>'}
  </div>

  <div class="card">
    <h2>LM Usage</h2>
    {usage_html}
  </div>

</div>
</body>
</html>
"""

    path = run_dir / "trace.html"
    path.write_text(document_html, encoding="utf-8")
    return path


def save_latest_pointer(log_root: Path, run_dir: Path):
    """Create a small pointer file to make the latest run easy to find."""
    latest = log_root / "LATEST.txt"
    latest.write_text(str(run_dir.resolve()), encoding="utf-8")


# ============================================================
# TERMINAL TRACE
# ============================================================

def show_trajectory(result):
    trajectory = getattr(result, "trajectory", None)

    if not trajectory:
        print("\nNo RLM trajectory available.")
        return

    print("\n")
    print("=" * 90)
    print("RLM TRAJECTORY")
    print("=" * 90)

    for index, step in enumerate(trajectory, start=1):
        print(f"\n--- ITERATION {index} ---")

        if not isinstance(step, dict):
            print("\n[RAW STEP]")
            print(step)
            continue

        reasoning = step.get("reasoning")
        code = step.get("code")
        output = step.get("output")

        if reasoning:
            print("\n[RLM ACTION / REASONING FIELD]")
            print(reasoning)

        if code:
            print("\n[GENERATED REPL CODE]")
            print(code)

        if output:
            print("\n[REPL OUTPUT]")
            print(output)

    final_reasoning = getattr(result, "final_reasoning", None)

    if final_reasoning:
        print("\n[FINAL REASONING]")
        print(final_reasoning)


# ============================================================
# ARGUMENTS
# ============================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="PDF Q&A using DSPy RLM and Azure OpenAI v1."
    )

    parser.add_argument("--pdf", required=True, help="Path to input PDF.")
    parser.add_argument("--query", required=True, help="Question to ask about the PDF.")

    parser.add_argument(
        "--model",
        default=os.getenv("AZURE_OPENAI_DEPLOYMENT", DEFAULT_MODEL),
        help="Azure OpenAI root deployment name.",
    )

    parser.add_argument(
        "--sub-model",
        default=os.getenv("AZURE_OPENAI_SUB_DEPLOYMENT", "") or None,
        help="Optional Azure OpenAI deployment for recursive llm_query() calls.",
    )

    parser.add_argument(
        "--max-iters",
        type=int,
        default=20,
        help="Maximum RLM iterations. Default: 20.",
    )

    parser.add_argument(
        "--max-llm-calls",
        type=int,
        default=50,
        help="Maximum recursive LLM calls. Default: 50.",
    )

    parser.add_argument(
        "--max-output-chars",
        type=int,
        default=10000,
        help="Maximum RLM REPL output characters. Default: 10000.",
    )

    parser.add_argument(
        "--temperature",
        type=float,
        default=float(os.getenv("AZURE_OPENAI_TEMPERATURE", "0.0")),
        help="LLM temperature.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show DSPy RLM execution information.",
    )

    parser.add_argument(
        "--show-trajectory",
        action="store_true",
        help="Also print generated REPL code and intermediate outputs in terminal.",
    )

    parser.add_argument(
        "--log-dir",
        default=os.getenv("RLM_LOG_DIR", DEFAULT_LOG_DIR),
        help="Directory where trace folders are stored. Default: logs",
    )

    parser.add_argument(
        "--no-html",
        action="store_true",
        help="Do not create the HTML visualizer.",
    )

    parser.add_argument(
        "--no-json",
        action="store_true",
        help="Do not create the JSON trace.",
    )

    parser.add_argument(
        "--max-tool-output-chars",
        type=int,
        default=int(os.getenv("RLM_MAX_TOOL_OUTPUT_CHARS", "5000")),
        help=(
            "Maximum output returned by document retrieval tools. "
            "Default: 5000."
        ),
    )

    return parser.parse_args()


# ============================================================
# MAIN
# ============================================================

def main():
    args = parse_args()

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    if not endpoint:
        print(
            "ERROR: AZURE_OPENAI_ENDPOINT is not set.",
            file=sys.stderr,
        )
        print(
            '\nSet it with: export AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE-NAME.openai.azure.com"',
            file=sys.stderr,
        )
        return 1

    if not api_key:
        print(
            "ERROR: AZURE_OPENAI_API_KEY is not set.",
            file=sys.stderr,
        )
        print(
            '\nSet it with: export AZURE_OPENAI_API_KEY="your-key"',
            file=sys.stderr,
        )
        return 1

    if args.max_iters <= 0:
        raise ValueError("--max-iters must be greater than 0")

    if args.max_llm_calls <= 0:
        raise ValueError("--max-llm-calls must be greater than 0")

    started_dt = datetime.now(timezone.utc)
    started_at = started_dt.isoformat()

    # Create a unique directory before running so every invocation
    # gets its own immutable trace.
    timestamp = started_dt.strftime("%Y%m%d_%H%M%S_%f")[:-3]
    log_root = Path(args.log_dir).expanduser().resolve()
    run_dir = log_root / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)

    try:
        print("=" * 90)
        print("DSPy RLM + Azure OpenAI v1")
        print("=" * 90)
        print(f"\nPDF:          {args.pdf}")
        print(f"Query:        {args.query}")
        print(f"Root model:   {args.model}")
        print(f"Sub model:    {args.sub_model or '(same root model)'}")
        print(f"API endpoint: {endpoint.rstrip("/")}{DEFAULT_AZURE_API_BASE_SUFFIX}")
        print(f"Max iters:    {args.max_iters}")
        print(f"Max calls:    {args.max_llm_calls}")
        print(f"Tool output:  {args.max_tool_output_chars:,} chars")
        print(f"Trace dir:    {run_dir}")

        # ----------------------------------------------------
        # 1. PDF
        # ----------------------------------------------------

        print("\n[1/3] Extracting PDF...")

        document = extract_pdf_text(args.pdf)

        print(f"      Extracted {len(document):,} characters.")

        # ----------------------------------------------------
        # 2. RLM
        # ----------------------------------------------------

        print("\n[2/3] Creating DSPy RLM...")

        rlm, root_lm, sub_lm = create_rlm(
            model=args.model,
            sub_model=args.sub_model,
            endpoint=endpoint,
            api_key=api_key,
            temperature=args.temperature,
            max_iters=args.max_iters,
            max_llm_calls=args.max_llm_calls,
            max_output_chars=args.max_output_chars,
            verbose=args.verbose,
            document=document,
            max_tool_output_chars=args.max_tool_output_chars,
        )

        # ----------------------------------------------------
        # 3. Execute
        # ----------------------------------------------------

        print("\n[3/3] Running RLM...")

        start_time = time.perf_counter()

        result = rlm(
            document=document,
            query=args.query,
        )

        duration = time.perf_counter() - start_time

        trajectory = extract_trajectory(result)

        if trajectory:
            first_output = trajectory[0].get("output") or ""
            if len(str(first_output)) > args.max_tool_output_chars:
                print(
                    "\nWARNING: First RLM output exceeded the configured "
                    "retrieval-tool budget. "
                    "Prefer search_document()/get_page() for large PDFs."
                )

        # ----------------------------------------------------
        # Answer
        # ----------------------------------------------------

        print("\n")
        print("=" * 90)
        print("FINAL ANSWER")
        print("=" * 90)
        print()
        print(result.answer)

        # ----------------------------------------------------
        # Save trace
        # ----------------------------------------------------

        trace_json_path = None
        trace_html_path = None

        if not args.no_json:
            trace_json_path, trace = save_json_trace(
                run_dir,
                started_at=started_at,
                duration_seconds=duration,
                pdf_path=args.pdf,
                query=args.query,
                model=args.model,
                sub_model=args.sub_model,
                max_iters=args.max_iters,
                max_llm_calls=args.max_llm_calls,
                max_output_chars=args.max_output_chars,
                temperature=args.temperature,
                document_chars=len(document),
                result=result,
                trajectory=trajectory,
                root_lm=root_lm,
                sub_lm=sub_lm,
                max_tool_output_chars=args.max_tool_output_chars,
            )
        else:
            trace = {
                "final_answer": make_json_safe(result.answer),
                "steps": trajectory,
                "iterations": len(trajectory),
                "query": args.query,
                "pdf": args.pdf,
                "root_model": args.model,
                "sub_model": args.sub_model,
                "started_at_utc": started_at,
                "duration_seconds": round(duration, 3),
                "document": {
                    "characters": len(document),
                    "estimated_tokens": estimate_tokens("x" * len(document)),
                },
                "estimated_visible_tokens": sum(
                    step.get("efficiency", {}).get(
                        "estimated_visible_step_tokens", 0
                    )
                    for step in trajectory
                ),
                "usage_summary": {
                    "root": summarize_usage(extract_lm_history(root_lm)),
                    "sub": summarize_usage(extract_lm_history(sub_lm)),
                },
            }

        if not args.no_html:
            trace_html_path = create_html_visualizer(
                run_dir,
                trace,
            )

        save_latest_pointer(log_root, run_dir)

        print("\n" + "=" * 90)
        print("TRACE SAVED")
        print("=" * 90)
        print(f"Iterations captured: {len(trajectory)}")
        print(f"Trace directory:     {run_dir}")

        if trace_json_path:
            print(f"JSON log:            {trace_json_path}")

        if trace_html_path:
            print(f"HTML visualizer:     {trace_html_path}")

        print(
            "\nOpen the HTML visualizer with:\n"
            f"  open {trace_html_path}"
            if trace_html_path
            else ""
        )

        if args.show_trajectory:
            show_trajectory(result)

        return 0

    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130

    except Exception as exc:
        print(
            f"\nERROR: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        print(
            f"Partial trace directory: {run_dir}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
