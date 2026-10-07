import os
import io
import re
import json
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from llama_cloud import LlamaCloud


# ============================================================
# CONFIG
# ============================================================

load_dotenv()

PDF_PATH = "pdf-path.pdf"

OUTPUT_DIR = Path("output_tables2")

INDIVIDUAL_DIR = OUTPUT_DIR / "individual_tables"
MERGED_DIR = OUTPUT_DIR / "merged_tables"

XLSX_PATH = OUTPUT_DIR / "all_tables.xlsx"
METADATA_PATH = OUTPUT_DIR / "tables_metadata.csv"

# Recommended for complex / diverse PDFs.
LLAMA_TIER = "agentic"

# For very dense financial / difficult documents:
# LLAMA_TIER = "agentic_plus"


# ============================================================
# DIRECTORY SETUP
# ============================================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
INDIVIDUAL_DIR.mkdir(parents=True, exist_ok=True)
MERGED_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# LLAMAPARSE CLIENT
# ============================================================

client = LlamaCloud()

if not os.getenv("LLAMA_CLOUD_API_KEY"):
    raise RuntimeError(
        "LLAMA_CLOUD_API_KEY environment variable is not set."
    )


# ============================================================
# HELPERS
# ============================================================

def clean_filename(text: str, max_length: int = 80) -> str:
    """
    Make text safe for use as a filename.
    """
    text = str(text)

    text = re.sub(r"[^\w\s.-]", "_", text)
    text = re.sub(r"\s+", "_", text)

    return text[:max_length].strip("_")


def table_to_dataframe(table) -> pd.DataFrame:
    """
    Convert a LlamaParse table item into pandas DataFrame.

    LlamaParse documents `rows` as:
        list[list[str | number | null]]
    """

    rows = table.rows

    if not rows:
        return pd.DataFrame()

    # Convert rows to regular Python lists.
    rows = [list(row) for row in rows]

    # Determine maximum width.
    max_cols = max(len(row) for row in rows)

    # Normalize row lengths.
    normalized_rows = []

    for row in rows:
        row = row + [None] * (max_cols - len(row))
        normalized_rows.append(row)

    # First row is used as column names.
    #
    # IMPORTANT:
    # This is ONLY for creating a convenient pandas representation.
    # We are NOT using this to identify whether the table itself
    # is a continuation. LlamaParse has already identified the table.
    header = normalized_rows[0]

    # Make duplicate / empty column names safe.
    columns = []

    seen = {}

    for idx, value in enumerate(header):

        if value is None or str(value).strip() == "":
            name = f"column_{idx + 1}"
        else:
            name = str(value).strip()

        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 1

        columns.append(name)

    data = normalized_rows[1:]

    return pd.DataFrame(data, columns=columns)


def extract_table_preview(table, max_rows=3):
    """
    Return a small preview for metadata.
    """

    rows = table.rows or []

    preview = rows[:max_rows]

    return json.dumps(
        preview,
        ensure_ascii=False
    )


# ============================================================
# PARSE PDF
# ============================================================

print("=" * 80)
print("Uploading PDF...")
print("=" * 80)

uploaded_file = client.files.create(
    file=PDF_PATH,
    purpose="parse",
)

print(f"Uploaded file ID: {uploaded_file.id}")


print("\nStarting LlamaParse...")

result = client.parsing.parse(
    file_id=uploaded_file.id,

    tier=LLAMA_TIER,

    version="latest",

    output_options={
        "markdown": {
            "tables": {
                # IMPORTANT
                #
                # Ask LlamaParse to merge tables that continue
                # across page boundaries.
                "merge_continued_tables": False,

                # Keep normal markdown tables.
                "output_tables_as_markdown": True,
            }
        },

        # Optional:
        # Gives cell-level bounding boxes.
        #
        # Useful if later we need an additional validation layer.
        #
        # "granular_bboxes": ["cell"],
    },

    expand=[
        "items",
        "markdown",
    ],
)


print("\nLlamaParse completed.")


# ============================================================
# SAVE MARKDOWN FOR DEBUGGING / AUDIT
# ============================================================

markdown_dir = OUTPUT_DIR / "markdown"
markdown_dir.mkdir(exist_ok=True)

if result.markdown:

    for page in result.markdown.pages:

        if not page.success:
            continue

        page_number = page.page_number

        markdown_path = (
            markdown_dir /
            f"page_{page_number:05d}.md"
        )

        markdown_path.write_text(
            page.markdown or "",
            encoding="utf-8",
        )


print(f"Markdown saved to: {markdown_dir}")


# ============================================================
# EXTRACT TABLE ITEMS
# ============================================================

tables = []

for page in result.items.pages:

    if not page.success:
        print(
            f"WARNING: page {page.page_number} "
            f"failed: {page.error}"
        )
        continue

    for item_index, item in enumerate(page.items):

        if item.type != "table":
            continue

        tables.append(
            {
                "page_number": page.page_number,
                "item_index": item_index,
                "table": item,
            }
        )


print("\n" + "=" * 80)
print(f"TABLES FOUND: {len(tables)}")
print("=" * 80)


# ============================================================
# PROCESS TABLES
# ============================================================

metadata = []

for table_index, table_info in enumerate(tables, start=1):

    page_number = table_info["page_number"]
    item_index = table_info["item_index"]
    table = table_info["table"]

    # --------------------------------------------------------
    # Determine whether LlamaParse merged this table
    # --------------------------------------------------------

    merged_from_pages = table.merged_from_pages

    is_merged = (
        merged_from_pages is not None
        and len(merged_from_pages) > 1
    )

    # --------------------------------------------------------
    # DataFrame
    # --------------------------------------------------------

    df = table_to_dataframe(table)

    # --------------------------------------------------------
    # Name
    # --------------------------------------------------------

    if is_merged:

        page_label = "_".join(
            str(p)
            for p in merged_from_pages
        )

        filename = (
            f"table_{table_index:04d}"
            f"_pages_{page_label}"
            f"_MERGED.csv"
        )

        output_path = MERGED_DIR / filename

    else:

        filename = (
            f"table_{table_index:04d}"
            f"_page_{page_number:05d}.csv"
        )

        output_path = INDIVIDUAL_DIR / filename

    # --------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig",
    )

    # --------------------------------------------------------
    # Metadata
    # --------------------------------------------------------

    metadata.append(
        {
            "table_id": table_index,

            "source_page": page_number,

            "item_index": item_index,

            "is_merged": is_merged,

            "merged_from_pages": (
                json.dumps(merged_from_pages)
                if merged_from_pages
                else ""
            ),

            "num_rows": len(df),

            "num_columns": len(df.columns),

            "csv_path": str(output_path),

            "preview": extract_table_preview(table),
        }
    )

    print(
        f"[{table_index:04d}] "
        f"{'MERGED' if is_merged else 'SINGLE'} | "
        f"source page={page_number} | "
        f"pages={merged_from_pages} | "
        f"rows={len(df)} | "
        f"cols={len(df.columns)}"
    )


# ============================================================
# SAVE METADATA
# ============================================================

metadata_df = pd.DataFrame(metadata)

metadata_df.to_csv(
    METADATA_PATH,
    index=False,
    encoding="utf-8-sig",
)


# ============================================================
# CREATE XLSX
# ============================================================

print("\nCreating Excel workbook...")

with pd.ExcelWriter(
    XLSX_PATH,
    engine="openpyxl",
) as writer:

    for table_info in tables:

        table = table_info["table"]

        table_index = (
            tables.index(table_info) + 1
        )

        df = table_to_dataframe(table)

        if df.empty:
            continue

        merged_from_pages = table.merged_from_pages

        if merged_from_pages and len(merged_from_pages) > 1:

            sheet_name = (
                f"T{table_index}_MERGED"
            )

        else:

            sheet_name = (
                f"T{table_index}"
            )

        # Excel sheet names have a 31 character limit.
        sheet_name = sheet_name[:31]

        df.to_excel(
            writer,
            sheet_name=sheet_name,
            index=False,
        )


# ============================================================
# SUMMARY
# ============================================================

num_merged = sum(
    1
    for item in tables
    if item["table"].merged_from_pages
    and len(item["table"].merged_from_pages) > 1
)

num_single = len(tables) - num_merged


print("\n" + "=" * 80)
print("DONE")
print("=" * 80)

print(f"Total tables       : {len(tables)}")
print(f"Single-page tables : {num_single}")
print(f"Merged tables      : {num_merged}")

print(f"\nIndividual CSVs    : {INDIVIDUAL_DIR}")
print(f"Merged CSVs        : {MERGED_DIR}")
print(f"Metadata           : {METADATA_PATH}")
print(f"Excel workbook     : {XLSX_PATH}")
print(f"Markdown           : {markdown_dir}")
