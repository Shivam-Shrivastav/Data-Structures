import argparse
import re
import subprocess
from html import escape
from pathlib import Path


def split_markdown_row(line):
    """Split a Markdown table row into cells."""
    line = line.strip()

    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]

    cells = []
    current = []
    escaped = False

    for char in line:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)

        if char == "\\" and not escaped:
            escaped = True
        else:
            escaped = False

    cells.append("".join(current).strip())
    return [cell.replace(r"\|", "|").replace("<br>", "\n") for cell in cells]


def is_separator(line):
    """Identify a Markdown table separator row."""
    cells = split_markdown_row(line)
    return bool(cells) and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", ""))
        for cell in cells
    )


def extract_markdown_tables(markdown):
    """Extract consecutive Markdown table blocks."""
    lines = markdown.splitlines()
    tables = []
    index = 0

    while index < len(lines):
        if (
            "|" not in lines[index]
            or index + 1 >= len(lines)
            or "|" not in lines[index + 1]
            or not is_separator(lines[index + 1])
        ):
            index += 1
            continue

        header = split_markdown_row(lines[index])
        index += 2
        rows = []

        while index < len(lines) and "|" in lines[index]:
            row = split_markdown_row(lines[index])

            if is_separator(lines[index]):
                index += 1
                continue

            # Keep the row structure consistent with the header.
            if len(row) < len(header):
                row.extend([""] * (len(header) - len(row)))
            elif len(row) > len(header):
                row = row[:len(header)]

            rows.append(row)
            index += 1

        tables.append({"header": header, "rows": rows})

    return tables


def table_to_html(table):
    """Create simple HTML containing only the table."""
    html = ["<table>", "<thead>", "<tr>"]

    for cell in table["header"]:
        html.append(f"<th>{escape(cell)}</th>")

    html.extend(["</tr>", "</thead>", "<tbody>"])

    for row in table["rows"]:
        html.append("<tr>")
        for cell in row:
            html.append(f"<td>{escape(cell)}</td>")
        html.append("</tr>")

    html.extend(["</tbody>", "</table>"])
    return "\n".join(html)


def process_pdf(pdf_path, output_dir, workspace_root):
    workspace = workspace_root / pdf_path.stem

    # Use olmOCR's official CLI to process the PDF and produce Markdown.
    command = [
        "olmocr",
        str(workspace),
        "--markdown",
        "--pdfs",
        str(pdf_path),
    ]

    subprocess.run(command, check=True)

    markdown_files = list((workspace / "markdown").rglob("*.md"))

    if not markdown_files:
        raise FileNotFoundError(
            f"olmOCR did not produce Markdown for {pdf_path.name}"
        )

    # Each workspace contains one input PDF.
    markdown = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(markdown_files)
    )

    tables = extract_markdown_tables(markdown)

    pdf_output = output_dir / pdf_path.stem
    pdf_output.mkdir(parents=True, exist_ok=True)

    for number, table in enumerate(tables, start=1):
        filename = f"table_{number:04d}.html"
        (pdf_output / filename).write_text(
            table_to_html(table),
            encoding="utf-8",
        )

    print(f"{pdf_path.name}: extracted {len(tables)} tables")


def main():
    cli = argparse.ArgumentParser(
        description="Extract PDF tables using olmOCR and save simple HTML."
    )
    cli.add_argument("--input", required=True, help="PDF file or folder")
    cli.add_argument("--output", default="output", help="HTML output folder")
    cli.add_argument(
        "--workspace",
        default="olmocr_workspace",
        help="olmOCR processing workspace",
    )
    cli.add_argument("--recursive", action="store_true")
    args = cli.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    workspace_root = Path(args.workspace).expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input not found: {input_path}")

    if input_path.is_file():
        if input_path.suffix.lower() != ".pdf":
            raise ValueError("Input must be a PDF file")
        pdf_files = [input_path]
    else:
        pattern = "**/*.pdf" if args.recursive else "*.pdf"
        pdf_files = sorted(input_path.glob(pattern))

    if not pdf_files:
        raise FileNotFoundError(f"No PDFs found in {input_path}")

    for pdf_path in pdf_files:
        try:
            process_pdf(
                pdf_path,
                output_dir,
                workspace_root,
            )
        except Exception as exc:
            print(f"Failed: {pdf_path.name}: {exc}")


if __name__ == "__main__":
    main()
