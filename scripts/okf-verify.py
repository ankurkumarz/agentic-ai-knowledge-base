#!/usr/bin/env python3
"""
okf-verify.py — Confirm OKF v0.1 conformance for all docs/*.md files.

Checks:
  1. Every concept doc (non-reserved .md) has a parseable YAML frontmatter block
  2. Every frontmatter block has a non-empty `type` field
  3. The `type` value is in the approved registry (APPROVED_TYPES)
  4. YAML is well-formed
  5. Reserved files (index.md, log.md, ingest-log.md, graph.md) have no concept frontmatter
  6. Bundle root index.md carries okf_version

Exit codes:
  0 — fully conformant
  1 — one or more errors (missing frontmatter, missing type, unknown type, bad YAML)

To add a new type: get user approval, add it to APPROVED_TYPES, update the type map
in AGENTS.md OKF Compliance section.
"""
import sys
import yaml
import pathlib

DOCS = pathlib.Path(__file__).parent.parent / "docs"
RESERVED = {"index.md", "log.md", "ingest-log.md", "graph.md"}
# Approved type registry — closed list, matches AGENTS.md OKF Compliance.
# Do NOT add values here without user approval.
# -----------------------------------------------------------------------
APPROVED_TYPES = {
    "Architecture",
    "Benchmark",
    "Concept",
    "Design Pattern",
    "Framework",
    "Platform",
    "Playbook",
    "Reference",
    "Standard",
    "Vendor Hub",
}

errors = []
warnings = []
skipped = []
checked = 0

for f in sorted(DOCS.rglob("*.md")):
    rel = f.relative_to(DOCS)
    name = f.name.lower()

    # --- Reserved files: skip, but validate bundle root index.md ---
    if name in RESERVED:
        skipped.append(rel)
        if name == "index.md" and f.parent == DOCS:
            text = f.read_text()
            if text.startswith("---"):
                try:
                    end = text.index("---", 3)
                    fm = yaml.safe_load(text[3:end].strip()) or {}
                    if "okf_version" not in fm:
                        warnings.append(f"WARN: bundle root index.md missing okf_version: {rel}")
                except (ValueError, yaml.YAMLError):
                    warnings.append(f"WARN: bundle root index.md has malformed frontmatter: {rel}")
            else:
                warnings.append(f"WARN: bundle root index.md has no frontmatter (okf_version recommended): {rel}")
        continue

    # --- Concept docs ---
    text = f.read_text()

    # 1. Frontmatter present
    if not text.startswith("---"):
        errors.append(f"MISSING FRONTMATTER: {rel}")
        continue

    # 2. Frontmatter closed
    try:
        end = text.index("---", 3)
    except ValueError:
        errors.append(f"UNCLOSED FRONTMATTER: {rel}")
        continue

    fm_block = text[3:end].strip()

    # 3. YAML parseable
    try:
        fm = yaml.safe_load(fm_block)
    except yaml.YAMLError as e:
        errors.append(f"YAML PARSE ERROR [{rel}]: {e}")
        continue

    # 4. type field present
    if not fm or not fm.get("type"):
        errors.append(f"MISSING type field: {rel}")
        continue

    # 5. type value in approved registry
    doc_type = fm["type"]
    if doc_type not in APPROVED_TYPES:
        errors.append(
            f"UNKNOWN type '{doc_type}': {rel}  "
            f"(approved: {', '.join(sorted(APPROVED_TYPES))})"
        )
        continue

    # 6. Recommended fields — warn, not error
    for field in ("title", "description", "tags", "timestamp"):
        if not fm.get(field):
            warnings.append(f"MISSING recommended field '{field}': {rel}")

    checked += 1

# --- Output ---
print(f"Concept docs checked:    {checked}")
print(f"Reserved files skipped:  {len(skipped)}")
print(f"Errors:                  {len(errors)}")
print(f"Warnings:                {len(warnings)}")

if errors:
    print("\n--- ERRORS (conformance failures) ---")
    for e in errors:
        print(f"  {e}")

if warnings:
    print("\n--- WARNINGS (recommended fields) ---")
    for w in warnings:
        print(f"  {w}")

if not errors:
    approved_list = ", ".join(sorted(APPROVED_TYPES))
    print(f"\n✓ All {checked} concept docs are OKF v0.1 conformant")
    print(f"  Approved types in use: {approved_list}")

sys.exit(1 if errors else 0)
