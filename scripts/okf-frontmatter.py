#!/usr/bin/env python3
"""
okf-frontmatter.py — Add OKF v0.1 YAML frontmatter to all concept docs.

OKF spec rules applied:
- index.md files: NO frontmatter (bundle root index.md may get okf_version only).
- log.md / ingest-log.md: reserved update-history files, no frontmatter.
- graph.md: site-generated, skip.
- All other .md files: prepend YAML frontmatter with type, title, description, tags, timestamp.

Type mapping (by directory / filename pattern):
  Concepts/             → Concept
  AgentHarness/         → Playbook   (engineering guidance)
  AgentMemory/          → Reference
  AgentOps/             → Reference
  AgentPlatforms/       → Platform
  AgenticFrameworks/    → Framework
  AgenticTechStack/     → Reference
  AllThings*/           → Vendor Hub
  Architecture/         → Architecture
  Benchmarks/           → Benchmark
  ContextEngineering/   → Playbook
  DesignPatterns/       → Design Pattern
  EvaluationFrameworks/ → Reference
  Introduction/         → Reference
  Marketplace/          → Reference
  MaturityModels/       → Reference
  Observability/        → Playbook
  ProductionBestPractices/ → Playbook
  PromptEngineering/    → Playbook
  RAG/                  → Reference
  ReferenceArchitecture/ → Architecture
  SecurityFrameworks/   → Playbook
  Standards/            → Standard
  Wizard/               → Reference
  WorkflowBuilders/     → Reference
  AIGovernance/         → Playbook
"""

import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DOCS_ROOT = Path(__file__).parent.parent / "docs"
TIMESTAMP = "2026-07-17T00:00:00Z"

# Files that must NOT receive frontmatter (OKF reserved filenames)
RESERVED_NAMES = {"index.md", "log.md", "ingest-log.md"}
# Additional skip list (site-generated or non-concept docs)
SKIP_FILES = {"graph.md"}

# Directory → OKF type
DIR_TYPE_MAP = {
    "AIGovernance": "Playbook",
    "AgentHarness": "Playbook",
    "AgentMemory": "Reference",
    "AgentOps": "Reference",
    "AgentPlatforms": "Platform",
    "AgenticFrameworks": "Framework",
    "AgenticTechStack": "Reference",
    "AllThingsAWS": "Vendor Hub",
    "AllThingsAnthropic": "Vendor Hub",
    "AllThingsGoogle": "Vendor Hub",
    "AllThingsMicrosoft": "Vendor Hub",
    "AllThingsOpenAI": "Vendor Hub",
    "Architecture": "Architecture",
    "Benchmarks": "Benchmark",
    "Concepts": "Concept",
    "ContextEngineering": "Playbook",
    "DesignPatterns": "Design Pattern",
    "EvaluationFrameworks": "Reference",
    "Introduction": "Reference",
    "Marketplace": "Reference",
    "MaturityModels": "Reference",
    "Observability": "Playbook",
    "ProductionBestPractices": "Playbook",
    "PromptEngineering": "Playbook",
    "RAG": "Reference",
    "ReferenceArchitecture": "Architecture",
    "SecurityFrameworks": "Playbook",
    "Standards": "Standard",
    "Wizard": "Reference",
    "WorkflowBuilders": "Reference",
}

# Directory → base tags
DIR_TAGS_MAP = {
    "AIGovernance": ["governance", "agentic-ai", "production"],
    "AgentHarness": ["agent-harness", "engineering", "agentic-ai"],
    "AgentMemory": ["memory", "agentic-ai"],
    "AgentOps": ["agentops", "operations", "agentic-ai"],
    "AgentPlatforms": ["platforms", "agentic-ai"],
    "AgenticFrameworks": ["frameworks", "agentic-ai"],
    "AgenticTechStack": ["tech-stack", "agentic-ai"],
    "AllThingsAWS": ["aws", "vendor", "agentic-ai"],
    "AllThingsAnthropic": ["anthropic", "vendor", "agentic-ai"],
    "AllThingsGoogle": ["google", "vendor", "agentic-ai"],
    "AllThingsMicrosoft": ["microsoft", "vendor", "agentic-ai"],
    "AllThingsOpenAI": ["openai", "vendor", "agentic-ai"],
    "Architecture": ["architecture", "agentic-ai"],
    "Benchmarks": ["benchmarks", "evaluation", "agentic-ai"],
    "Concepts": ["concepts", "agentic-ai"],
    "ContextEngineering": ["context-engineering", "agentic-ai"],
    "DesignPatterns": ["design-patterns", "agentic-ai"],
    "EvaluationFrameworks": ["evaluation", "agentic-ai"],
    "Introduction": ["introduction", "agentic-ai"],
    "Marketplace": ["marketplace", "agentic-ai"],
    "MaturityModels": ["maturity", "agentic-ai"],
    "Observability": ["observability", "production", "agentic-ai"],
    "ProductionBestPractices": ["production", "best-practices", "agentic-ai"],
    "PromptEngineering": ["prompt-engineering", "agentic-ai"],
    "RAG": ["rag", "retrieval", "agentic-ai"],
    "ReferenceArchitecture": ["architecture", "reference", "agentic-ai"],
    "SecurityFrameworks": ["security", "agentic-ai"],
    "Standards": ["standards", "agentic-ai"],
    "Wizard": ["wizard", "agentic-ai"],
    "WorkflowBuilders": ["workflow", "orchestration", "agentic-ai"],
}


def extract_title(content: str, fallback: str) -> str:
    """Extract the first H1 heading from markdown content."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def extract_description(content: str) -> str:
    """
    Extract a one-line description from the Overview section or
    the first non-empty, non-heading paragraph after the H1.
    """
    lines = content.splitlines()
    in_overview = False
    past_h1 = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Enter Overview section
        if re.match(r'^##\s+Overview', stripped, re.IGNORECASE):
            in_overview = True
            continue

        if in_overview:
            # Stop at next heading
            if stripped.startswith("#"):
                in_overview = False
                break
            if stripped and not stripped.startswith("!") and not stripped.startswith("|"):
                # Take first non-empty sentence
                sentence = stripped.split(".")[0].strip()
                if len(sentence) > 20:
                    return (sentence[:197] + "...") if len(sentence) > 200 else sentence
            continue

        # Fallback: first substantive paragraph after H1
        if stripped.startswith("# "):
            past_h1 = True
            continue

        if past_h1 and stripped and not stripped.startswith("#") \
                and not stripped.startswith("!") and not stripped.startswith("|") \
                and not stripped.startswith("```"):
            sentence = stripped.split(".")[0].strip()
            if len(sentence) > 20:
                return (sentence[:197] + "...") if len(sentence) > 200 else sentence

    return ""


def slug_to_title(stem: str) -> str:
    """Convert a filename stem like 'agent-harness' to 'Agent Harness'."""
    return " ".join(word.capitalize() for word in stem.replace("-", " ").replace("_", " ").split())


def yaml_str(value: str) -> str:
    """Quote a YAML string value if it contains special characters."""
    # Characters that require quoting in YAML
    if any(c in value for c in [':', '#', '[', ']', '{', '}', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]):
        # Use double-quote, escaping any existing double-quotes
        escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return value


def build_frontmatter(file_path: Path) -> str:
    """Build the YAML frontmatter block for a given file."""
    content = file_path.read_text(encoding="utf-8")

    # Determine directory name (top-level subdir of docs/)
    rel = file_path.relative_to(DOCS_ROOT)
    parts = rel.parts
    dir_name = parts[0] if len(parts) > 1 else ""

    # Type
    okf_type = DIR_TYPE_MAP.get(dir_name, "Reference")

    # Title: try H1 first, then slug from stem
    fallback_title = slug_to_title(file_path.stem)
    title = extract_title(content, fallback_title)

    # Description
    description = extract_description(content)

    # Tags: base from dir + any extras from filename
    tags = list(DIR_TAGS_MAP.get(dir_name, ["agentic-ai"]))

    lines = ["---"]
    lines.append(f"type: {yaml_str(okf_type)}")
    lines.append(f"title: {yaml_str(title)}")
    if description:
        lines.append(f"description: {yaml_str(description)}")
    if tags:
        tag_str = ", ".join(tags)
        lines.append(f"tags: [{tag_str}]")
    lines.append(f"timestamp: {TIMESTAMP}")
    lines.append("---")
    lines.append("")  # blank line after closing ---
    return "\n".join(lines)


def has_frontmatter(content: str) -> bool:
    """Return True if the file already starts with a YAML frontmatter block."""
    return content.lstrip().startswith("---")


def process_file(file_path: Path, dry_run: bool = False) -> str:
    """Add frontmatter to file if not already present. Returns status string."""
    content = file_path.read_text(encoding="utf-8")

    if has_frontmatter(content):
        return f"SKIP (already has frontmatter): {file_path.relative_to(DOCS_ROOT)}"

    fm = build_frontmatter(file_path)
    new_content = fm + content

    if not dry_run:
        file_path.write_text(new_content, encoding="utf-8")
    return f"ADDED: {file_path.relative_to(DOCS_ROOT)}"


def should_skip(file_path: Path) -> bool:
    """Return True if this file should NOT receive frontmatter."""
    name = file_path.name.lower()
    # OKF reserved filenames
    if name in RESERVED_NAMES:
        return True
    # Additional site-specific skips
    if name in SKIP_FILES:
        return True
    return False


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN — no files will be modified\n")

    processed = 0
    skipped = 0
    added = 0

    for md_file in sorted(DOCS_ROOT.rglob("*.md")):
        if should_skip(md_file):
            print(f"SKIP (reserved): {md_file.relative_to(DOCS_ROOT)}")
            skipped += 1
            continue

        status = process_file(md_file, dry_run=dry_run)
        print(status)
        processed += 1
        if status.startswith("ADDED"):
            added += 1

    print(f"\n--- Summary ---")
    print(f"Files processed (concept docs): {processed}")
    print(f"Frontmatter added:              {added}")
    print(f"Already had frontmatter:        {processed - added}")
    print(f"Reserved files skipped:         {skipped}")


if __name__ == "__main__":
    main()
