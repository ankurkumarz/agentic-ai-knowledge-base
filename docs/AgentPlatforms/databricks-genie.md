---
type: Platform
title: Databricks Genie
description: "Databricks Genie is Databricks' agentic product family — an AI coworker platform spanning business-user, agent-building, coding, and operations surfaces, evolved from the Databricks One / AI-BI Genie rebrand"
tags: [platforms, databricks, agentic-ai]
timestamp: 2026-08-07T00:00:00Z
---
# Databricks Genie

## Overview

Databricks Genie is Databricks' agentic product family, rebuilt from the original "AI/BI Genie" natural-language query assistant into a full suite spanning business-user, agent-building, coding, and operations surfaces. **Databricks One was rebranded to Genie in April 2026** — described by Databricks as more than a naming change, since the surface was rebuilt around an agentic coworker model rather than a simple query assistant. The family now comprises **Genie One**, **Genie Agents** (formerly Genie Spaces), **Genie Code**, **Genie App Builder**, **Genie ZeroOps**, and **Genie Ontology**, all operating against the same governed Unity Catalog metadata layer.

## Key Components

| Product | Role | Status |
|---|---|---|
| **Genie One** | Flagship agentic coworker for business teams (marketing, finance, sales, ops) — answers questions, drafts documents, generates reports, schedules tasks, and orchestrates work across structured and unstructured data | GA |
| **Genie Agents** *(formerly Genie Spaces)* | Curated, domain-specific AI agents that take autonomous action, scoped to a business domain; renamed from Genie Spaces in July 2026 with unchanged underlying capability | GA (renamed Jul 2026) |
| **Genie Code** | Lakehouse-native coding agent for production data and ML engineering; see [AI Coding Agents — Databricks Genie Code](../AICodingAgents/ai-coding-agents.md#databricks-genie-code) for the full coding-agent profile | GA; expanded at Data + AI Summit 2026 |
| **Genie App Builder** | Builds internal applications atop lakehouse data without a separate app development stack | Announced 2026 |
| **Genie ZeroOps** | Automates operational maintenance tasks (pipeline health, cost, governance upkeep) with minimal human operator involvement | Announced 2026 |
| **Genie Ontology** | Business-semantic/ontology layer underpinning consistent entity and relationship definitions consumed by the other Genie products | Announced alongside Genie One and Genie Agents |

### Account-Level Genie

Account-Level Genie is GA, providing a single Genie instance across all workspaces in an account — one login and one URL rather than a per-workspace deployment.

## Architecture

Every Genie surface reads from the same governed foundation:

- **Unity Catalog** — schemas, permissions, and lineage that Genie Code, Genie Agents, and Genie One all query against, keeping business logic and access control consistent across surfaces.
- **Genie Ontology** — the shared business-semantic layer defining entities and relationships once, for reuse across Genie One's conversational answers, Genie Agents' domain actions, and Genie Code's generated pipelines.
- **Metric Views** — Databricks' existing Unity Catalog semantic-layer objects (see [Semantic Data Layer Radar](../AgenticTechStack/semantic-data-layer-radar.md#databricks-metric-views-unity-catalog-business-semantics)) feed governed metric definitions into Genie's natural-language and agentic surfaces.

## Suitable For (Pros)

- Organizations already standardized on the Databricks lakehouse and Unity Catalog governance model.
- Business teams needing a natural-language coworker without provisioning separate BI and automation tooling.
- Data/ML engineering teams wanting a coding agent (Genie Code) that shares governed context with the same platform's business-facing agents (Genie One, Genie Agents).

## Limitations (Cons)

- Tightly coupled to the Databricks platform and Unity Catalog — less useful for organizations with data spread across multiple, non-Databricks warehouses.
- The rapid rename cadence (Databricks One → Genie → Genie Spaces → Genie Agents, all within a few months of 2026) creates short-term documentation and tooling churn for teams tracking the platform closely.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Fragmented naming across a fast-evolving product family | Genie Spaces → Genie Agents rename (Jul 2026) and the broader Databricks One → Genie rebrand (Apr 2026) can leave internal docs and runbooks referencing stale names | Track the [Databricks Genie release notes](https://docs.databricks.com/aws/en/genie/) directly rather than caching product names in internal documentation |
| Business logic drift across Genie surfaces | Genie One, Genie Agents, and Genie Code each generating separate ad hoc business definitions | Route all surfaces through Genie Ontology and Unity Catalog Metric Views as the single source of truth for entities and metrics |
| Coding-agent scope creep | Using Genie Code for general-purpose software engineering outside the lakehouse | Reserve Genie Code for production data/ML engineering tasks; use a general-purpose coding agent (see [AI Coding Agents](../AICodingAgents/ai-coding-agents.md)) for non-data software work |

## See Also

- [AI Coding Agents — Databricks Genie Code](../AICodingAgents/ai-coding-agents.md#databricks-genie-code)
- [Semantic Data Layer Technology Radar — Databricks Metric Views](../AgenticTechStack/semantic-data-layer-radar.md#databricks-metric-views-unity-catalog-business-semantics)
- [Agent Platforms Overview](README.md)
- [Gemini Enterprise Agent Platform](gemini-enterprise-agent-platform.md)
- [AWS AgentCore](aws-agentcore.md)
- [Enterprise Agentic AI Platforms (2026)](enterprise-platforms-2026.md)

## References

- [Introducing Genie One, Genie Agents, and Genie Ontology — Databricks Blog](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) — official announcement of the expanded Genie family
- [The next generation of Databricks Genie — Databricks Blog](https://www.databricks.com/blog/next-generation-databricks-genie) — overview of the Genie rebuild
- [What's new in Genie Code at Data + AI Summit 2026 — Databricks Blog](https://www.databricks.com/blog/whats-new-genie-code-data-ai-summit-2026) — Genie Code command center and production engineering upgrades
- [Databricks Launches Genie One: All-New Agentic Coworker for Every Team — Databricks Newsroom](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team) — Genie One GA press release
- [Databricks Launches Genie Code, Bringing Agentic Engineering to Data — Databricks Newsroom](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-code-bringing-agentic-engineering-data) — Genie Code launch press release
- [Genie | Databricks on AWS](https://docs.databricks.com/aws/en/genie/) — product documentation
- [Genie Agents | Databricks on AWS](https://docs.databricks.com/aws/en/genie-agents/) — Genie Agents (formerly Genie Spaces) documentation
- [Databricks One is now Genie — Databricks Community](https://community.databricks.com/t5/mvp-articles/databricks-one-is-now-genie/td-p/155665) — community MVP write-up of the April 2026 rebrand
