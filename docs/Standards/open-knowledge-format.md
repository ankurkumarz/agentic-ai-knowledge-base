# Open Knowledge Format (OKF)

## Overview

The **Open Knowledge Format (OKF)** is an open specification published by Google Cloud's Data Analytics, BI, and Database teams (authored by Sam McVeety and Amir Hormati) on June 12, 2026, at version **v0.1**. It formalizes the "LLM-wiki" pattern — first conceptualized by Andrej Karpathy — into a portable, interoperable format for representing the metadata, context, and curated knowledge that AI agents and humans share.

OKF targets the fragmented context landscape problem: AI agents must currently assemble context from scattered, incompatible sources — metadata catalogs, internal wikis, code comments, tribal knowledge — leading to redundant effort and inconsistent results across teams and agent deployments. OKF is explicitly a **format, not a platform**: it requires no proprietary account, runtime, compression scheme, or SDK. Google has stated that contributions, alternative implementations, and adoption beyond Google products are welcome, and the spec is versioned for backward-compatible growth.

## Key Concepts / Architecture

### Structure

An OKF bundle is **a directory of markdown files with YAML frontmatter**, organized as a navigable hierarchy:

```
sales/
├── index.md
├── datasets/
│   ├── index.md
│   └── orders_db.md
├── tables/
│   ├── index.md
│   ├── orders.md
│   └── customers.md
└── metrics/
    ├── index.md
    └── weekly_active_users.md
```

### Document Format

Each document combines a small set of structured YAML frontmatter fields with a free-form markdown body. Example:

```yaml
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---
# Schema
| Column | Type | Description |
|--------|------|-------------|
| `order_id` | STRING | Globally unique order identifier. |
| `customer_id` | STRING | FK to [customers](/tables/customers.md). |

# Joins
Joined with [customers](/tables/customers.md) on `customer_id`.
```

### Core Components

- **Frontmatter fields**: `type` is the only required field; `title`, `description`, `resource`, `tags`, and `timestamp` are common optional fields, and producers may add custom fields freely.
- **Graph structure**: ordinary markdown links between documents form a navigable knowledge graph (e.g., a table document links to the customer table it joins with).
- **`index.md`**: optional per-directory entry point enabling progressive disclosure — an agent reads a high-level index before drilling into detail files.
- **`log.md`**: optional chronological history file for a given knowledge area.

## Design Principles

- **Minimally opinionated** — only the `type` field is required; everything else is left to the producer's own schema conventions.
- **Producer/consumer independence** — the format is the contract; tooling on the writing side and the reading side can evolve independently.
- **Format, not platform** — not tied to any cloud, database, model provider, or agent framework; never requires proprietary accounts or SDKs.

## Key Features

| Feature | Description |
|---|---|
| Just markdown | Readable in any editor, renders on GitHub, indexable by standard search tools |
| Just files | Shippable as a tarball, hostable in a git repo, mountable on any filesystem |
| Just YAML frontmatter | Small set of structured, queryable fields |
| Cross-linking | Standard markdown links create knowledge-graph relationships between documents |
| Human + agent readable | The same file serves both audiences without translation |

## Use Cases

OKF is designed to capture "knowledge atoms" such as:

- Table and dataset schemas
- Business metric definitions
- Incident runbooks
- Join paths between systems
- API deprecation notices

Typical workflow: an agent (or human) answering a question like "How do I compute weekly active users from our event stream?" can traverse an OKF bundle's graph of metric, table, and join definitions instead of re-deriving this context from scratch each time.

## Reference Implementations

Google published three reference implementations alongside the spec, all in the [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) repository:

| Implementation | Description |
|---|---|
| Enrichment Agent | Walks BigQuery datasets, drafts OKF documents, and enriches them with citations |
| Static HTML Visualizer | Converts an OKF bundle into an interactive graph view; self-contained, no backend required |
| Sample bundles | GA4 e-commerce, Stack Overflow, and Bitcoin public datasets |

OKF is also the ingest format for the [Google Cloud Knowledge Catalog](https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog), which uses it to serve curated knowledge to Google's agents.

## Suitable For (Pros)

- Teams that want version-controlled, git-native knowledge alongside code
- Organizations seeking to avoid vendor lock-in for agent context and metadata
- Bridging human documentation (wikis) and agent-consumable context with a single artifact
- Portable knowledge bases that can move across products, organizations, and agent frameworks

## Limitations (Cons)

- v0.1, published June 12, 2026 — very early; ecosystem tooling, validators, and adoption outside Google are not yet established
- No formal governance body identified (e.g., not yet donated to a foundation, unlike AGENTS.md → AAIF)
- No published benchmarks quantifying retrieval quality or agent performance gains
- Minimal opinionation means consistency across large organizations depends on internal conventions rather than the spec itself

## Relation to Other Conventions

| Convention | Focus | Relationship to OKF |
|---|---|---|
| [AGENTS.md](./agents-md.md) | Persistent, always-on agent instructions for a repo/project | Same "markdown + structured metadata" philosophy, applied to *behavioral* instructions rather than *knowledge/metadata* |
| [Agent Skills / SKILLS.md](./skills.md) | On-demand, triggerable workflows | Complementary on-demand convention; OKF is for reference knowledge rather than executable procedures |
| [Context Engineering — Offload (Write) strategy](../ContextEngineering/strategies.md) | Saving information outside the active context window for on-demand retrieval | OKF is a standardized substrate for the "offload" pattern — a structured, linkable file tree agents can read just-in-time |
| [Agent Memory — Semantic Memory](../AgentMemory/README.md) | Durable facts and knowledge agents accumulate | OKF bundles are a portable storage format for semantic-memory content (schemas, definitions, entity relationships) |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Avoiding context fragmentation | Knowledge scattered across catalogs, wikis, code comments | Consolidate into an OKF bundle versioned alongside code |
| Agent + human dual audience | Docs written for humans are often hard for agents to parse, and vice versa | Use OKF's markdown + minimal frontmatter so a single file serves both |
| Knowledge graph navigation | Agents need to find related entities (tables, metrics, joins) efficiently | Use ordinary markdown links between documents to build a traversable graph; add `index.md` files for progressive disclosure |
| Keeping knowledge current | Static docs go stale as systems evolve | Use an enrichment agent (e.g., the reference Enrichment Agent) to walk live systems and draft/update OKF documents with citations |

## See Also

- [AGENTS.md Standard](./agents-md.md)
- [Agent Skills / SKILLS.md](./skills.md)
- [Common Strategies for Context Management](../ContextEngineering/strategies.md)
- [Agent Memory Management](../AgentMemory/README.md)
- [Google — Agentic AI Overview](../AllThingsGoogle/README.md)

## References

- [How the Open Knowledge Format can improve data sharing — Google Cloud](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) — primary source, OKF v0.1 announcement (June 12, 2026)
- [GoogleCloudPlatform/knowledge-catalog (okf) — GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) — spec, sample bundles, reference implementations
- [Introducing the Google Cloud Knowledge Catalog — Google Cloud](https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog) — related product that ingests OKF
- [The LLM-wiki — Andrej Karpathy (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — conceptual foundation for OKF
