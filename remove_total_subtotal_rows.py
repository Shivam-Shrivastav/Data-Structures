#!/usr/bin/env python3
"""Remove explicit total/subtotal rows from already-merged HTML and XLSX outputs.

Original input files are never modified. Outputs are written under a separate folder.
Designed primarily for html_table_merger.py output (merged/html and merged/xlsx).
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import re
from pathlib import Path
from typing import Any, Iterable

from bs4 import BeautifulSoup

LOG = logging.getLogger("remove_total_subtotal_rows")


def total_subtotal_reason(values: Iterable[Any]) -> str | None:
    """Identify aggregate rows while avoiding ordinary labels such as 'Total Return Fund'."""
    cells = [re.sub(r"\s+", " ", str(value or "")).strip() for value in values]
    nonempty = [value for value in cells if value]
    if not nonempty:
        return None

    if any(re.search(r"\bsub[\s-]?totals?\b", value, re.IGNORECASE) for value in nonempty):
        return "subtotal row removed"
    if any(re.search(r"\bgrand[\s-]+totals?\b", value, re.IGNORECASE) for value in nonempty):
        return "grand-total row removed"

    label_re = re.compile(
        r"^(?:(?:trade\s+date|settlement\s+date|account|portfolio|cash|market(?:\s+value)?|"
        r"net|gross|page|overall|running|opening|closing|ending|beginning|debit|credit|inflow|"
        r"outflow|quantity|transaction|interest|cost|proceeds|realized|unrealized|position|"
        r"share|security|holding|currency|period|calculated)\s+)?"
        r"total(?:\s+(?:amount|value|balance|debits?|credits?|inflows?|outflows?|quantity|cost|"
        r"market\s+value|proceeds|interest|assets|liabilities|equity|payments|cash|transactions|"
        r"positions|holdings|shares|gain|loss|gains|losses|income|expenses|deposits|withdrawals|"
        r"fees|charges|activity|units|for\s+period|for\s+the\s+period|of\s+above|for\s+(?:all|the|this)|"
        r"of\s+(?:all|the|this|these|above)))?(?:\s*[:\-])?$",
        re.IGNORECASE,
    )
    numeric_re = re.compile(
        r"^[\s$€£¥]*[+\-]?(?:\(?\s*\d[\d,]*(?:\.\d+)?%?\s*\)?|\d{4}-\d{2}-\d{2})"
        r"(?:\s*[A-Za-z]{3})?[\s$€£¥]*$"
    )
    date_re = re.compile(r"^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}$")
    total_ending_re = re.compile(r"^[A-Za-z][A-Za-z0-9 ,/&()\-]{0,55}\s+total(?:\s*[:\-])?$", re.IGNORECASE)
    for idx, value in enumerate(cells):
        if not value or not (label_re.fullmatch(value) or total_ending_re.fullmatch(value)):
            continue
        other_values = [v for j, v in enumerate(cells) if j != idx and v]
        if all(numeric_re.fullmatch(v) or date_re.fullmatch(v) for v in other_values):
            return "total/aggregate row removed"
    return None


def cell_values_from_html_row(row) -> list[str]:
    return [re.sub(r"\s+", " ", cell.get_text(" ", strip=True)).strip()
            for cell in row.find_all(["td", "th"], recursive=False)]


def clean_html_file(src: Path, dst: Path) -> dict[str, Any]:
    raw = src.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw, "html.parser")
    table = soup.find("table")
    removed: list[dict[str, Any]] = []
    if table is not None:
        for index, row in enumerate(list(table.find_all("tr"))):
            values = cell_values_from_html_row(row)
            reason = total_subtotal_reason(values)
            if reason:
                removed.append({"row_index_zero_based": index, "values": values, "reason": reason})
                row.decompose()
    dst.parent.mkdir(parents=True, exist_ok=True)
    # Preserve the entire HTML document (the parser may normalize whitespace/markup).
    dst.write_text(str(soup), encoding="utf-8")
    return {"input": str(src), "output": str(dst), "file_type": "html",
            "rows_removed": len(removed), "removed_rows": removed}


def value_for_report(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def clean_xlsx_file(src: Path, dst: Path, sheet_name: str = "Merged Table") -> dict[str, Any]:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise RuntimeError("For XLSX cleanup, install openpyxl: pip install openpyxl") from exc

    wb = load_workbook(src)
    target = wb[sheet_name] if sheet_name in wb.sheetnames else wb.active
    removed: list[dict[str, Any]] = []
    rows_to_delete: list[int] = []
    for row_idx in range(1, target.max_row + 1):
        values = [target.cell(row=row_idx, column=col).value for col in range(1, target.max_column + 1)]
        reason = total_subtotal_reason(values)
        if reason:
            rows_to_delete.append(row_idx)
            removed.append({"row_number_1_based": row_idx,
                            "values": [value_for_report(v) for v in values], "reason": reason})

    # Keep the merger's Provenance sheet aligned with the rows removed from Merged Table.
    # Its output_row field points to the one-based row index in Merged Table.
    provenance_removed: list[int] = []
    if rows_to_delete and target.title == "Merged Table" and "Provenance" in wb.sheetnames:
        provenance = wb["Provenance"]
        header_map = {
            str(provenance.cell(row=1, column=c).value or "").strip().casefold(): c
            for c in range(1, provenance.max_column + 1)
        }
        output_row_col = header_map.get("output_row")
        if output_row_col:
            to_match = set(rows_to_delete)
            for r in range(2, provenance.max_row + 1):
                val = provenance.cell(row=r, column=output_row_col).value
                try:
                    if int(val) in to_match:
                        provenance_removed.append(r)
                except (TypeError, ValueError):
                    continue
            for r in sorted(provenance_removed, reverse=True):
                provenance.delete_rows(r, 1)

    for r in sorted(rows_to_delete, reverse=True):
        target.delete_rows(r, 1)
    if target.max_row and target.max_column:
        target.auto_filter.ref = target.dimensions

    dst.parent.mkdir(parents=True, exist_ok=True)
    wb.save(dst)
    wb.close()
    return {"input": str(src), "output": str(dst), "file_type": "xlsx",
            "sheet_cleaned": target.title, "rows_removed": len(removed),
            "provenance_rows_removed": len(provenance_removed), "removed_rows": removed}


def run(input_dir: Path, output_dir: Path, sheet_name: str) -> list[dict[str, Any]]:
    if not input_dir.exists() or not input_dir.is_dir():
        raise NotADirectoryError(f"Input directory does not exist: {input_dir}")
    if input_dir.resolve() == output_dir.resolve() or input_dir.resolve() in output_dir.resolve().parents:
        # Output may not be nested inside input: otherwise later runs could recursively reprocess it.
        raise ValueError("Choose an output directory outside the input directory to keep runs reproducible.")

    paths = sorted(
        p for p in input_dir.rglob("*")
        if p.is_file() and p.suffix.casefold() in {".html", ".htm", ".xlsx"}
    )
    if not paths:
        raise FileNotFoundError(f"No .html, .htm, or .xlsx files found in {input_dir}")

    results: list[dict[str, Any]] = []
    for src in paths:
        dst = output_dir / src.relative_to(input_dir)
        try:
            if src.suffix.casefold() in {".html", ".htm"}:
                result = clean_html_file(src, dst)
            else:
                result = clean_xlsx_file(src, dst, sheet_name=sheet_name)
            results.append(result)
            LOG.info("%s: removed %s row(s)", src.name, result["rows_removed"])
        except Exception as exc:
            LOG.exception("Failed to clean %s", src)
            results.append({"input": str(src), "output": str(dst), "file_type": src.suffix,
                            "error": f"{type(exc).__name__}: {exc}"})

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "total_subtotal_cleanup_report.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (output_dir / "total_subtotal_cleanup_report.csv").open("w", newline="", encoding="utf-8-sig") as f:
        fields = ["input", "output", "file_type", "sheet_cleaned", "rows_removed", "provenance_rows_removed", "error"]
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for item in results:
            writer.writerow({k: item.get(k, "") for k in fields})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove total/subtotal rows from processed HTML and XLSX files.")
    parser.add_argument("input", help="Folder containing already-processed merged HTML and XLSX files")
    parser.add_argument("--output", default="cleaned_outputs", help="Separate destination folder (default: cleaned_outputs)")
    parser.add_argument("--sheet-name", default="Merged Table", help="Primary table worksheet name in generated workbooks")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(asctime)s | %(levelname)s | %(message)s")
    try:
        results = run(Path(args.input).expanduser().resolve(), Path(args.output).expanduser().resolve(), args.sheet_name)
        failed = sum("error" in x for x in results)
        removed = sum(int(x.get("rows_removed", 0)) for x in results)
        print(json.dumps({"files_processed": len(results), "files_failed": failed,
                          "total_rows_removed": removed,
                          "report_json": str((Path(args.output).expanduser().resolve() / "total_subtotal_cleanup_report.json"))}, indent=2))
        return 1 if failed else 0
    except Exception as exc:
        LOG.error("Cleanup failed: %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
