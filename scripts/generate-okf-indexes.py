#!/usr/bin/env python3
"""
generate-okf-indexes.py

Generates OKF-conformant index.md files for every subdirectory under docs/,
following the stackoverflow sample pattern from:
  https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf/samples/stackoverflow

OKF index.md rules (spec §6):
  - No frontmatter (reserved file)
  - Heading describing the directory's contents
  - One bullet per concept: * [Title](relative-file.md) - description
  - Subdirectories listed as * [Name](subdir/index.md) - description
  - Entries sorted: concept docs first (alphabetical), then subdirs

For each concept doc the title and description are pulled from its YAML frontmatter.
If a concept has no description, the first sentence of its Overview is used as fallback.
Files listed in SKIP_FILES are excluded from the index.

Run:
  .venv/bin/python3 scripts/generate-okf-indexes.py [--dry-run]
"""

import re
import sys
import pathlib
import yaml

REPO = pathlib.Path(__file__).parent.parent
DOCS = REPO / "docs"

# OKF reserved filenames — never listed as concept entries
RESERVED = {"index.md", "log.md", "ingest-log.md", "graph.md"}
# Image and other non-concept files
SKIP_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".json"}

# Friendly section headings for each top-level directory
DIR_HEADINGS = {
    "AICodingAgents":         "AI Coding Agents",
    "AIGovernance":           "AI Governance",
    "AgentHarness":           "Agent Harness",
    "AgentMemory":            "Agent Memory",
    "AgentOps":               "Agent Operations",
    "AgentPlatforms":         "Agent Platforms",
    "AgenticFrameworks":      "Agentic Frameworks",
    "AgenticTechStack":       "Agentic Tech Stack",
    "AllThingsAWS":           "AWS — Agentic AI",
    "AllThingsAnthropic":     "Anthropic — Agentic AI",
    "AllThingsGoogle":        "Google — Agentic AI",
    "AllThingsMicrosoft":     "Microsoft — Agentic AI",
    "AllThingsOpenAI":        "OpenAI — Agentic AI",
    "Architecture":           "Architecture",
    "Benchmarks":             "Benchmarks",
    "Concepts":               "Core Concepts",
    "ContextEngineering":     "Context Engineering",
    "DesignPatterns":         "Design Patterns",
    "EvaluationFrameworks":   "Evaluation Frameworks",
    "Introduction":           "Introduction",
    "Marketplace":            "Marketplaces",
    "MaturityModels":         "Maturity Models",
    "Observability":          "Observability",
    "ProductionBestPractices": "Production Best Practices",
    "PromptEngineering":      "Prompt Engineering",
    "RAG":                    "RAG (Retrieval-Augmented Generation)",
    "ReferenceArchitecture":  "Reference Architecture",
    "SecurityFrameworks":     "Security Frameworks",
    "Standards":              "Industry Standards",
    "Wizard":                 "Wizard",
    "WorkflowBuilders":       "Workflow Builders",
}


def read_frontmatter(path: pathlib.Path) -> dict:
    """Extract YAML frontmatter from a markdown file. Returns {} if absent."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    try:
        end = text.index("---", 3)
        return yaml.safe_load(text[3:end].strip()) or {}
    except (ValueError, yaml.YAMLError):
        return {}


def extract_first_sentence(path: pathlib.Path) -> str:
    """Pull first meaningful sentence from the body as a description fallback."""
    text = path.read_text(encoding="utf-8")
    # Skip frontmatter
    if text.startswith("---"):
        try:
            end = text.index("---", 3)
            text = text[end + 3:]
        except ValueError:
            pass
    for line in text.splitlines():
        line = line.strip()
        if (line and not line.startswith("#") and not line.startswith("|")
                and not line.startswith("!") and not line.startswith("```")
                and len(line) > 20):
            sentence = line.split(".")[0].strip()
            if len(sentence) > 20:
                return sentence[:200]
    return ""


def get_concept_info(path: pathlib.Path) -> tuple[str, str]:
    """Return (title, description) for a concept doc."""
    fm = read_frontmatter(path)
    title = fm.get("title") or " ".join(
        w.capitalize() for w in path.stem.replace("-", " ").split()
    )
    description = fm.get("description") or extract_first_sentence(path)
    # Strip YAML quotes and leading ** bold markers from description
    description = description.strip('"').strip("'")
    description = re.sub(r"^\*\*(.+?)\*\*", r"\1", description)
    return title, description


def dir_description(dirpath: pathlib.Path) -> str:
    """Get a one-line description for a subdirectory (from its README/index if present)."""
    for candidate in ("README.md", "Readme.md", "readme.md"):
        readme = dirpath / candidate
        if readme.exists():
            fm = read_frontmatter(readme)
            if fm.get("description"):
                return fm["description"].strip('"').strip("'")
            # fallback: first sentence
            desc = extract_first_sentence(readme)
            if desc:
                return desc
    return f"Concepts in the {dirpath.name} section."


def generate_index(dirpath: pathlib.Path, dry_run: bool = False) -> str:
    """Generate the index.md content for a directory."""
    # Heading
    dir_name = dirpath.name
    heading = DIR_HEADINGS.get(dir_name, dir_name.replace("-", " "))
    lines = [f"# {heading}", ""]

    # Collect concept docs (direct .md files, excluding reserved/non-md)
    concepts = []
    for f in sorted(dirpath.iterdir()):
        if f.is_file() and f.suffix == ".md" and f.name.lower() not in RESERVED:
            concepts.append(f)

    # Collect subdirectories that have content
    subdirs = sorted(
        d for d in dirpath.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )

    if concepts:
        lines.append("## Concepts")
        lines.append("")
        for f in concepts:
            title, description = get_concept_info(f)
            desc_suffix = f" - {description}" if description else ""
            lines.append(f"* [{title}]({f.name}){desc_suffix}")
        lines.append("")

    if subdirs:
        lines.append("## Subdirectories")
        lines.append("")
        for d in subdirs:
            sub_desc = dir_description(d)
            sub_heading = DIR_HEADINGS.get(d.name, d.name)
            lines.append(f"* [{sub_heading}]({d.name}/index.md) - {sub_desc}")
        lines.append("")

    return "\n".join(lines)


def process_directory(dirpath: pathlib.Path, dry_run: bool) -> str:
    """Generate and optionally write index.md for a directory."""
    content = generate_index(dirpath, dry_run)
    index_path = dirpath / "index.md"
    exists = index_path.exists()

    if not dry_run:
        index_path.write_text(content, encoding="utf-8")

    action = "UPDATED" if exists else "CREATED"
    return f"{action}: {index_path.relative_to(REPO)}"


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN — no files will be written\n")

    results = []

    # Generate index.md for each top-level subdirectory of docs/
    # Skip non-content directories
    SKIP_DIRS = {"assets", ".DS_Store"}
    for dirpath in sorted(DOCS.iterdir()):
        if dirpath.is_dir() and not dirpath.name.startswith(".") and dirpath.name not in SKIP_DIRS:
            status = process_directory(dirpath, dry_run)
            results.append(status)
            print(status)

    created = sum(1 for r in results if r.startswith("CREATED"))
    updated = sum(1 for r in results if r.startswith("UPDATED"))
    print(f"\nCreated: {created}  |  Updated: {updated}  |  Total: {len(results)}")


if __name__ == "__main__":
    main()
