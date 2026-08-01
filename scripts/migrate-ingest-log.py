#!/usr/bin/env python3
"""
migrate-ingest-log.py

Converts docs/ingest-log.md (wiki ingest history format) to OKF-conformant
docs/log.md format (OKF spec §7).

OKF log.md rules:
  - Flat list of date-grouped entries, newest first
  - Date headings: ## YYYY-MM-DD
  - Entries are prose with leading bold verb (**Ingest**, **Update**, etc.)
  - No frontmatter on log.md (OKF reserved filename)
  - Title: # Directory Update Log

Strategy:
  1. Parse every ## [YYYY-MM-DD] block from ingest-log.md
  2. Group by date, sort dates newest-first
  3. For each entry, emit one bullet: bold operation + source title + sections touched
  4. Where a "Files Modified" table exists, summarise as a compact sub-bullet list
  5. Write docs/log.md; keep docs/ingest-log.md unchanged
"""

import re
import pathlib
from collections import defaultdict

REPO = pathlib.Path(__file__).parent.parent
INGEST_LOG = REPO / "docs" / "ingest-log.md"
LOG_MD = REPO / "docs" / "log.md"

# ── Parse entries ────────────────────────────────────────────────────────────

ENTRY_RE = re.compile(
    r"^## \[(\d{4}-\d{2}-\d{2})\] (\w+) \| (.+?) \| sections touched: (.+)$",
    re.MULTILINE,
)

def parse_entries(text: str) -> list[dict]:
    """Return list of entry dicts parsed from ingest-log.md."""
    entries = []
    matches = list(ENTRY_RE.finditer(text))
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()

        date = m.group(1)
        operation = m.group(2).capitalize()
        title = m.group(3).strip()
        sections = [s.strip() for s in m.group(4).split(",")]

        # Extract source line if present
        source_match = re.search(r"\*\*Source[s]?\*\*[:\s]+(.+?)(?:\n|$)", block)
        source = source_match.group(1).strip() if source_match else ""

        # Extract Files Modified table rows (File | Change Type | Notes)
        file_rows = []
        in_table = False
        for line in block.splitlines():
            if "|---|" in line:
                in_table = True
                continue
            if in_table and line.startswith("|"):
                cols = [c.strip() for c in line.strip("|").split("|")]
                if len(cols) >= 2 and cols[0] and "File" not in cols[0]:
                    file_rows.append((cols[0], cols[1] if len(cols) > 1 else ""))
            elif in_table and not line.startswith("|"):
                in_table = False

        entries.append({
            "date": date,
            "operation": operation,
            "title": title,
            "sections": sections,
            "source": source,
            "files": file_rows,
        })
    return entries


def format_entry(e: dict) -> str:
    """Format a single entry as an OKF log bullet."""
    verb = f"**{e['operation']}**"
    lines = []

    # Primary bullet — trim source to first sentence / 120 chars
    source_display = ""
    if e["source"]:
        first = e["source"].split("\n")[0].split("—")[0].strip()
        if len(first) > 120:
            first = first[:117] + "..."
        source_display = f" — {first}"
    sections_short = ", ".join(e["sections"][:4])
    if len(e["sections"]) > 4:
        sections_short += f" + {len(e['sections']) - 4} more"
    lines.append(f"* {verb}: [{e['title']}] → {sections_short}{source_display}")

    # File sub-bullets (max 8 to keep log scannable)
    shown = e["files"][:8]
    for f_name, change_type in shown:
        lines.append(f"  * {change_type}: `{f_name.strip('`')}`")
    if len(e["files"]) > 8:
        lines.append(f"  * *(+ {len(e['files']) - 8} more files)*")

    return "\n".join(lines)


def build_log_md(entries: list[dict]) -> str:
    """Build the full log.md content."""
    # Group by date
    by_date: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_date[e["date"]].append(e)

    # Sort dates newest-first
    sorted_dates = sorted(by_date.keys(), reverse=True)

    lines = ["# Directory Update Log", ""]
    lines.append(
        "> OKF-conformant log (§7). "
        "Full ingest details remain in [ingest-log.md](ingest-log.md)."
    )
    lines.append("")

    for date in sorted_dates:
        lines.append(f"## {date}")
        lines.append("")
        for entry in by_date[date]:
            lines.append(format_entry(entry))
            lines.append("")

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    text = INGEST_LOG.read_text(encoding="utf-8")
    entries = parse_entries(text)

    if not entries:
        print("ERROR: No entries parsed. Check ingest-log.md format.")
        raise SystemExit(1)

    print(f"Parsed {len(entries)} entries across "
          f"{len({e['date'] for e in entries})} dates.")

    log_content = build_log_md(entries)
    LOG_MD.write_text(log_content, encoding="utf-8")
    print(f"Written → {LOG_MD.relative_to(REPO)}")
    print(f"Original ingest-log.md untouched ({INGEST_LOG.stat().st_size} bytes).")
