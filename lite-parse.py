import argparse
import re
from html import escape
from pathlib import Path

from liteparse import LiteParse


def cell_text(cell):
    if isinstance(cell, dict):
        return str(cell.get("text", "") or "")
    return str(getattr(cell, "text", "") or "")


def get_value(obj, key, default=None):
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def normalize_header(header):
    return tuple(
        re.sub(r"\s+", " ", cell_text(cell)).strip().casefold()
        for cell in header
    )


def extract_page_tables(page):
    tables = []

    for block in get_value(page, "blocks", []) or []:
        if get_value(block, "kind", "") != "table":
            continue

        header = get_value(block, "header", []) or []
        rows = get_value(block, "rows", []) or []

        header = [cell_text(cell) for cell in header]
        rows = [[cell_text(cell) for cell in row] for row in rows]

        if header or rows:
            tables.append({
                "page": get_value(page, "page_num"),
                "header": header,
                "rows": rows,
            })

    return tables


def merge_continued_tables(page_tables):
    """Merge consecutive-page tables when their normalized headers match."""
    merged = []

    for table in page_tables:
        header = table["header"]
        rows = table["rows"]

        if not merged:
            merged.append({
                "header": header,
                "rows": rows[:],
                "pages": [table["page"]],
            })
            continue

        previous = merged[-1]
        same_header = (
            bool(header)
            and bool(previous["header"])
            and normalize_header(header) == normalize_header(previous["header"])
        )
        consecutive_page = (
            table["page"] is not None
            and previous["pages"][-1] is not None
            and table["page"] == previous["pages"][-1] + 1
        )

        if same_header and consecutive_page:
            previous["rows"].extend(rows)
            previous["pages"].append(table["page"])
        else:
            merged.append({
                "header": header,
                "rows": rows[:],
                "pages": [table["page"]],
            })

    return merged


def table_to_html(table):
    """Return plain table HTML without styling or extra document markup."""
    output = ["<table>"]

    if table["header"]:
        output.append("<thead><tr>")
        for value in table["header"]:
            output.append(f"<th>{escape(value)}</th>")
        output.append("</tr></thead>")

    if table["rows"]:
        output.append("<tbody>")
        for row in table["rows"]:
            output.append("<tr>")
            for value in row:
                output.append(f"<td>{escape(value)}</td>")
            output.append("</tr>")
        output.append("</tbody>")

    output.append("</table>")
    return "\n".join(output)


def process_pdf(pdf_path, output_dir, parser):
    result = parser.parse(str(pdf_path))
    page_tables = []

    for page in result.pages:
        page_tables.extend(extract_page_tables(page))

    tables = merge_continued_tables(page_tables)

    pdf_output = output_dir / pdf_path.stem
    pdf_output.mkdir(parents=True, exist_ok=True)

    for index, table in enumerate(tables, start=1):
        pages = [p for p in table["pages"] if p is not None]

        if pages:
            page_label = (
                f"pages_{pages[0]:04d}-{pages[-1]:04d}"
                if len(pages) > 1
                else f"page_{pages[0]:04d}"
            )
        else:
            page_label = "pages_unknown"

        filename = f"table_{index:04d}_{page_label}.html"
        (pdf_output / filename).write_text(
            table_to_html(table),
            encoding="utf-8",
        )

    print(f"{pdf_path.name}: saved {len(tables)} tables")


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("--input", required=True, help="PDF file or folder")
    cli.add_argument("--output", default="output", help="Output directory")
    cli.add_argument("--recursive", action="store_true")
    args = cli.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()

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

    parser = LiteParse(
        output_format="json",
        extract_blocks=True,
        ocr_enabled=True,
        continue_on_page_error=True,
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_path in pdf_files:
        try:
            process_pdf(pdf_path, output_dir, parser)
        except Exception as exc:
            print(f"Failed: {pdf_path.name}: {exc}")


if __name__ == "__main__":
    main()
