# AGENTS.md — Agentic AI Knowledge Base

This file governs how AI agents (Claude Code, Kiro, Gemini CLI, OpenAI Codex, or any other agent) maintain and extend this knowledge base. Read it fully before taking any action.

---

## What This Repository Is

This is a **persistent, compounding knowledge wiki** about Agentic AI, rendered via MkDocs Material and published to ReadTheDocs. The agent's job is to keep the wiki accurate, well-linked, and organized — not to answer questions in chat. Every insight should land in a file that persists.

The three layers:
- **`raw/`** — immutable source documents you drop in. The agent reads these but never modifies them.
- **`docs/`** — the wiki itself. The agent owns this layer. It creates pages, updates them, and maintains cross-references.
- **`mkdocs.yml`** — the site navigation. The agent updates this when new pages are added.

---

## Repository Layout

```
docs/
├── index.md                        # Home page — executive overview + structure map
├── Introduction/
├── Concepts/                       # Agent definitions, types, foundations
├── Architecture/                   # Architecture components, multi-agent, 12-factor
├── DesignPatterns/                 # OpenAI, Gartner patterns
├── AgenticFrameworks/              # LangChain, LangGraph, ADK, CrewAI, etc.
├── AgenticTechStack/               # Tech stack references
├── AgentPlatforms/                 # Vertex AI, AgentCore, Azure AI
├── WorkflowBuilders/               # Workflow engines (OSS, SaaS, etc.)
├── Standards/                      # MCP, A2A, AGENTS.md, OpenSpec, AG-UI
├── ReferenceArchitecture/          # AI Assistant, Automation, RAG, Self-learning
├── ContextEngineering/             # Context challenges, strategies, impl references
├── PromptEngineering/
├── AgentMemory/                    # Memory tiers, LTM strategies, solutions
├── EvaluationFrameworks/           # LLM eval frameworks and platforms
├── Benchmarks/                     # Agent and LLM benchmarks
├── Observability/                  # Goals, solutions, best practices
├── SecurityFrameworks/             # NIST AI RMF, Google SAIF, AWS
├── AgentOps/                       # GenOps, lifecycle management
├── MaturityModels/                 # Gartner, AWS, Google, IDC
├── Marketplace/                    # AWS Marketplace, AgentOps Marketplace
├── RAG/                            # RAG implementation
├── ProductionBestPractices/        # Cross-cutting production guidance
│   ├── README.md                   # Overview and vendor best practices table
│   ├── observability.md
│   ├── state-memory.md
│   ├── deployment.md
│   ├── testing-evaluations.md
│   ├── context-engineering.md
│   ├── security.md
│   └── cost-management.md
├── AllThingsAWS/                   # AWS vendor hub — one-liners + backlinks
├── AllThingsGoogle/                # Google vendor hub — one-liners + backlinks
├── AllThingsMicrosoft/             # Microsoft vendor hub — one-liners + backlinks
├── AllThingsAnthropic/             # Anthropic vendor hub — one-liners + backlinks
└── AllThingsOpenAI/                # OpenAI vendor hub — one-liners + backlinks
                                    # Note: AllThings* pages are index hubs, not content stores.
                                    # Detailed content lives in topical sections; vendor pages link back.

raw/                                # Drop source documents here — agent reads, never modifies
mkdocs.yml                          # Site nav — agent updates when pages are added
```

---

## Section Mapping Guide

When a raw source arrives, use this table to decide which `docs/` directory and which file to update or create.

| Topic in Source | Primary Section | File(s) to Update |
|---|---|---|
| Agent definition, terminology, types | `Concepts/` | `agent-definition.md`, `agent-types.md`, `agent-foundational.md` |
| Architecture components, system design | `Architecture/` | `components-selection.md`, `multi-agent-system.md` |
| Design patterns (OpenAI, Gartner, etc.) | `DesignPatterns/` | `openai-patterns.md`, `gartner-patterns.md`, `Readme.md` |
| Development framework (LangChain, LangGraph, CrewAI, etc.) | `AgenticFrameworks/` | `<framework-name>.md` (create if new), `README.md` |
| Cloud platforms (Vertex AI, AgentCore, Azure AI) | `AgentPlatforms/` | `<platform>.md` |
| Workflow engines / builders | `WorkflowBuilders/` | `open-source.md`, `self-hosted.md`, `orchestration.md`, `README.md` |
| Industry standards (MCP, A2A, AGENTS.md) | `Standards/` | `<standard>.md` |
| Reference architectures, blueprints | `ReferenceArchitecture/` | `<architecture-type>.md` |
| Context management, prompt engineering | `ContextEngineering/` or `PromptEngineering/` | Relevant `.md` files |
| Memory management (short-term, LTM, episodic) | `AgentMemory/` | `functional-tiers.md`, `ltm-strategies.md`, `short-term.md`, `README.md` |
| Evaluation frameworks, benchmarks | `EvaluationFrameworks/` or `Benchmarks/` | Relevant `.md` files |
| Observability, tracing, monitoring | `Observability/` **and** `ProductionBestPractices/observability.md` | Both |
| Security, risk management, prompt injection | `SecurityFrameworks/` **and** `ProductionBestPractices/security.md` | Both |
| MLOps / AgentOps / GenOps / deployment | `AgentOps/` **and** `ProductionBestPractices/deployment.md` | Both |
| Testing, evals, red-teaming | `EvaluationFrameworks/` **and** `ProductionBestPractices/testing-evaluations.md` | Both |
| Cost optimization, token budgets | `ProductionBestPractices/cost-management.md` | Plus any relevant section |
| State, memory in production | `ProductionBestPractices/state-memory.md` | Plus `AgentMemory/` if conceptual |
| Maturity models | `MaturityModels/` | `gartner.md`, `aws.md`, `google.md`, `idc.md` |
| Agent marketplaces | `Marketplace/` | `aws-marketplace.md`, `agentops.md`, `Readme.md` |
| RAG, retrieval patterns | `RAG/` and `ReferenceArchitecture/rag-architecture.md` | Both |
| AWS-specific content (Strands, AgentCore, Marketplace, maturity) | `AllThingsAWS/README.md` | Add a backlink row to the hub table; detailed content goes in the topical section |
| Google-specific content (ADK, Vertex AI, SAIF, GenOps, maturity) | `AllThingsGoogle/README.md` | Add a backlink row to the hub table; detailed content goes in the topical section |
| Microsoft-specific content (Azure AI, Semantic Kernel, AutoGen) | `AllThingsMicrosoft/README.md` | Add a backlink row to the hub table; detailed content goes in the topical section |
| Anthropic-specific content (Claude, MCP, context engineering) | `AllThingsAnthropic/README.md` | Add a backlink row to the hub table; detailed content goes in the topical section |
| OpenAI-specific content (design patterns, AutoGPT, OpenSpec) | `AllThingsOpenAI/README.md` | Add a backlink row to the hub table; detailed content goes in the topical section |

**Vendor hub rule:** `AllThings*` pages are index hubs — each row contains a one-liner and a relative backlink to the topical wiki page that holds the full content. Do **not** write detailed content in hub pages. If a vendor offering has no existing topical page, create one in the appropriate section first, then add the hub row.

**When in doubt:** Look at the existing file closest to the topic and extend it. Only create a new file if the topic has no existing home.

---

## Ingest Workflow

Follow these steps in order when processing a raw source.

### Step 1 — Identify the source

Resolve the source using this priority order:
1. **Local file first** — look for the file in `raw/`. If it exists, read it.
2. **WebFetch fallback** — if no local file exists but a URL is provided, fetch the URL and treat the fetched content as the source. Do not save the fetched content into `raw/`.

**Citation rule:** If a URL is provided (either as the fetch target or alongside a local file), use that URL as the canonical citation in the `References` section of every wiki page updated during this ingest. Do not omit or substitute it with a generic title link.

Then determine:
- **Source type**: research paper, vendor doc, blog post, whitepaper, framework doc, standard, benchmark report
- **Primary topic**: what section does this primarily belong to?
- **Secondary topics**: which other sections will it inform?
- **Is this new information or an update** to something already in the wiki?

### Step 2 — Extract key knowledge

Pull out:
- Core concepts, definitions, and claims
- Architectural patterns, diagrams described, or decision criteria
- Vendor/tool-specific details (version, maturity, licensing if mentioned)
- Concrete best practices, anti-patterns, or lessons learned
- Benchmark numbers or evaluation results (with date context)
- URLs, paper citations, or reference links in the source

### Step 3 — Map to sections

Using the Section Mapping Guide above, list every `docs/` file this source touches.

### Step 4 — Update wiki files

For each file identified in Step 3:
- If the file exists: integrate new knowledge. Do not duplicate content already present. Update claims that are superseded. Add new subsections if needed.
- If the file does not exist: create it using the Page Format below. Then add an entry to `mkdocs.yml`.

### Step 5 — Update `docs/index.md`

If the source materially enriches a section's coverage, update the corresponding bullet in `index.md` to reflect the new content. Keep bullets concise (one line each).

### Step 6 — Cross-link

Add `See Also` links in every updated page that points to related pages already in the wiki. Use relative paths (e.g., `../AgentMemory/ltm-strategies.md`).

### Step 7 — Update `mkdocs.yml` (if new file created)

Add the new page under the correct nav section. Match the numbering and indentation style already in use. Do not reorder existing entries.

### Step 8 — Log the ingest

Append one line to `docs/ingest-log.md` (create it if it does not exist):

```
## [YYYY-MM-DD] ingest | <source title or filename> | sections touched: <comma-separated list>
```

---

## Page Format

All wiki pages follow this structure. Adapt sections to what the source actually provides — do not invent content.

```markdown
# <Page Title>

## Overview

One paragraph: what this is, why it matters in the agentic AI context.

## Key Concepts / Architecture / Features

Bullet list or subsections. Use headers sparingly; prefer structured prose and bullets.

## <Domain-Specific Sections>

E.g., "Suitable for (Pros)", "Limitations (Cons)", "Evaluation Results", "Best Practices", etc.
Use whatever structure fits the content — look at existing pages in the same section for conventions.

## Best Practices

Use a table when there are 3+ practices. Preferred format:

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| ... | ... | ... |

Or bullet form for fewer items.

## See Also

- [Related Page](../Section/file.md)
- [Another Related Page](../OtherSection/file.md)

## References

- [Title](URL) — one-line description
```

**Do not add YAML frontmatter.** MkDocs Material does not require it for this site.

---

## ProductionBestPractices — Special Rules

This section is the highest-value synthesis layer. It consolidates cross-cutting production guidance across all sources. Every time a raw source contains production-relevant content (regardless of its primary topic), check these files:

| File | Update when source covers |
|---|---|
| `observability.md` | Tracing, logging, metrics, eval pipelines, dashboards, alerting |
| `state-memory.md` | Session state, memory tiers, persistence patterns, memory tooling |
| `deployment.md` | CI/CD for agents, canary rollouts, prompt versioning, durable execution, container orchestration |
| `testing-evaluations.md` | LLM-as-judge, eval harnesses, red-teaming, regression testing, benchmarks |
| `context-engineering.md` | Context rot, compaction, retrieval strategies, caching, isolation |
| `security.md` | Prompt injection, HITL, least privilege, audit trails, compliance |
| `cost-management.md` | Model routing, token budgets, caching for cost, cost monitoring tools |

The table format in ProductionBestPractices files is:

```markdown
| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
```

Always extend existing tables. Do not replace rows that are still valid.

---

## Batch vs. Single File Ingest — Best Practices

### Process one file at a time (recommended default)

**When to ingest one file at a time:**
- The source is substantive (whitepaper, research paper, long vendor doc)
- You want to review each summary before the next source is integrated
- Sources cover overlapping topics (batch risks conflating them)
- You are building up a new section from scratch

Processing one file at a time lets you verify the wiki update is accurate before moving on. It also produces cleaner git history — one commit per ingest.

### When batch ingest is acceptable

Batch multiple raw files in a single pass only when:
- Files are clearly distinct topics with no overlap (e.g., one on LangGraph, one on NIST AI RMF)
- Files are short reference documents (release notes, changelogs, brief blog posts)
- You are doing an initial bulk load and have explicitly decided to accept lower synthesis quality in exchange for speed

**Even in batch mode:** process files sequentially within the session. Read file 1 → update wiki → read file 2 → update wiki. Do not read all files first and then write all updates at once — that degrades cross-reference quality.

### Rule of thumb

> One substantive source = one focused wiki update session. Two to three short, clearly distinct sources = acceptable batch. More than three sources at once = split into multiple sessions.

---

## Writing Style and Quality Rules

- **Neutral, encyclopedic tone.** No marketing language. No "revolutionary" or "game-changing".
- **Vendor-neutral framing** where possible. Represent tradeoffs, not advocacy.
- **Cite sources.** Every factual claim should trace back to a raw source or an existing reference link.
- **Be specific.** "LangChain has ~100K GitHub stars" is better than "LangChain is popular".
- **No duplicate content.** If a concept is already explained in `Concepts/agent-definition.md`, link to it rather than re-explaining.
- **Use relative links** for internal navigation (e.g., `../AgentMemory/ltm-strategies.md`), not absolute URLs.
- **Tables over long bullet lists** when comparing 3+ items along the same dimensions.
- **Do not remove existing content** unless it is factually wrong or directly contradicted by a new source. When superseding old claims, note the update inline: `*(Updated: previous claim was X; current evidence shows Y)*`.

---

## Handling Ambiguity

**Source doesn't fit any section cleanly?**
Put it in the closest section. Add a `See Also` link from the next closest section. Do not create a new top-level section without discussing with the user first.

**Source contradicts existing wiki content?**
Update the existing claim. Add a note like `*(Source A claims X; Source B [2025] reports Y — see References)*`. Do not silently overwrite.

**Source is about a framework not yet in the wiki?**
Create `docs/AgenticFrameworks/<framework-name>.md` using the standard page format. Add it to `mkdocs.yml` under section 4 with the next available number.

**Source is a raw `.docx`, `.pdf`, or image?**
Read it as best you can. Note in the log entry that the source was a binary document. If you cannot extract sufficient content, flag it to the user.

---

## What the Agent Must Never Do

- Modify any file inside `raw/`. Those are source-of-truth documents.
- Delete existing wiki pages or remove navigation entries from `mkdocs.yml`.
- Invent facts not present in the source or existing wiki. If uncertain, write "Details not available in current sources" rather than guessing.
- Add YAML frontmatter to doc files — this site does not use it.
- Rename existing files or directories without explicit user instruction.
- Push to remote or commit without explicit user instruction.

---

## Query Workflow (answering questions without a raw source)

If asked a question about the wiki's topic domain (not an ingest task):

1. Check `docs/index.md` to identify relevant sections.
2. Read the relevant wiki pages.
3. Synthesize an answer with page citations.
4. If the answer is substantive and not already captured in the wiki, offer to file it as a new page or extend an existing one. Good answers compound — they should not disappear into chat history.

---

## Lint Workflow (periodic health check)

When asked to lint the wiki:

1. Scan all pages for:
   - Broken relative links
   - Orphan pages (listed in `mkdocs.yml` but not linked from any other page)
   - Pages with no `See Also` section
   - Claims that reference specific version numbers or dates older than 12 months (flag for review)
   - Sections listed in `mkdocs.yml` that point to missing files
2. Report findings as a list: `[issue type] | file | description`.
3. Fix broken links and missing `See Also` sections. Flag dated claims to the user for decision.

---

## Agent Compatibility Note

This file is written in standard markdown and is intentionally tool-agnostic. The instructions apply equally whether you are running as:

- **Claude Code** (`claude`) — use Read, Edit, Write, Glob, Grep tools. Prefer Edit over full rewrites.
- **Kiro** — follow the same workflow using your available file and edit tools.
- **Gemini CLI** (`gemini`) — use file read/write tools per your toolset. This file doubles as GEMINI.md-compatible instruction.
- **OpenAI Codex** — treat this as AGENTS.md per the OpenAI Codex agents standard.
- **Any other agent** — the instructions in this file are sufficient. No additional configuration files are needed.

All agents: read this file at the start of every session before touching any other file.
