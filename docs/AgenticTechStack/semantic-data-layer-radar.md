# Semantic Data Layer — Technology Radar

## Overview

A **semantic layer** is a data architecture technique that introduces a shared business-logic layer between raw data stores and consuming applications (BI tools, AI agents, APIs), centralizing metric definitions, joins, access rules, and business terminology. dbt Labs describes it as a unified, business-friendly representation of data that acts as an API for metrics and dimensions consumed by BI tools, LLMs, and other endpoints. AtScale and Databricks similarly frame the semantic layer as a "single source of truth" for metrics and dimensions sitting between the warehouse/lakehouse and analytics/AI tools. Thoughtworks' Technology Radar places "Semantic layer" in its **Techniques** quadrant, recommending teams start small and watch emerging interchange standards.

This page applies a Thoughtworks-style radar (quadrants × rings) to the **semantic data layer landscape specifically** — the hyperscaler/data-cloud-native capabilities (Snowflake, Databricks, Microsoft Fabric/Power BI, AWS QuickSight, Google Looker) and the universal/code-first semantic layer products (dbt Semantic Layer, Cube, AtScale, Denodo, Honeydew, and others) that compete with or complement them. It is relevant to agentic AI because semantic layers increasingly serve as the governed, business-meaningful query surface that LLM agents (text-to-SQL, natural-language BI, MCP-based data agents) consume instead of querying raw schemas directly.

## Three Architectural Patterns

Semantic layers today fall into three broad patterns:

| Pattern | Description | Examples |
|---|---|---|
| **Warehouse/lakehouse-native semantic objects** | Semantic definitions stored as first-class objects inside the data platform itself | Snowflake Semantic Views, Databricks Metric Views |
| **BI-native semantic models** | Semantic modeling layer built into a BI tool, scoped to that tool's consumers | Power BI semantic models, Looker (LookML), AWS QuickSight Topics |
| **Universal/standalone semantic layer platforms** | Cross-tool semantic engines that expose metrics via SQL/REST/GraphQL/XMLA to any consumer | dbt Semantic Layer (MetricFlow), Cube Core, AtScale, Denodo |

## Radar Model

This radar reframes Thoughtworks' generic quadrants into four landscape-specific ones, keeping the canonical three rings (Hold is omitted since no entries here warrant it):

**Quadrants:**

- **Cloud data platforms** — semantic features built into hyperscaler / data-cloud platforms
- **BI & analytics semantics** — semantic models native to BI tools
- **Universal semantic layers & metrics stores** — standalone, cross-tool semantic engines
- **Semantic knowledge stack** — knowledge graph / ontology tools underpinning richer semantics

**Rings:**

- 🟢 **Adopt** — proven in production; default choice in its niche
- 🔵 **Trial** — promising and production-ready; adopt for focused domains
- 🟡 **Assess** — emerging; watch, run POCs, but limit blast radius

> **Editorial note.** Ring placements below are opinionated, based on current GA/preview status and ecosystem signals as of mid-2026 — they are not official Thoughtworks Radar entries (Thoughtworks' own radar has a single generic "Semantic layer" blip in Techniques, not per-vendor placements).

---

## Cloud Data Platform-Native Semantic Layers

### Snowflake — Semantic Views
**Ring: Trial→Adopt · Quadrant: Cloud data platforms**

Snowflake **Semantic Views** store business-meaningful concepts (entities, metrics, dimensions, relationships) as schema-level objects, queryable via both SQL and Cortex Analyst natural-language APIs. They act as the governed bridge from AI/BI consumers to raw data. Snowflake also launched the **Open Semantic Interchange (OSI)** initiative — a vendor-neutral, YAML-based spec for semantic models, with mapping modules targeting Apache open-source projects and an expanding partner roster. GA features plus strong ecosystem momentum place this in Trial for most orgs, trending to Adopt where Snowflake is already the enterprise data backbone. Define domain semantic views (Customer, Orders, Revenue) and expose them to Cortex Analyst and BI via semantic SQL.

### Databricks — Metric Views & Unity Catalog Business Semantics
**Ring: Trial · Quadrant: Cloud data platforms**

Databricks **Metric Views** are first-class semantic-layer objects in Unity Catalog defining governed, reusable business metrics and dimensions in YAML — measures, dimensions, relationships, display names, formats, synonyms — consumed via SQL, dashboards, and AI notebooks. Unity Catalog Business Semantics is now GA, and the core implementation has been open-sourced into Apache Spark to extend semantic capabilities beyond a single platform. GA but early in enterprise adoption; strong fit for lakehouse-centric orgs. Start with a small set of high-value metrics, organize metric views clearly in Unity Catalog, and validate outputs before deprecating legacy "one-big-table" designs.

### Microsoft — Power BI Semantic Models & Fabric OneLake Integration
**Ring: Adopt · Quadrant: BI & analytics semantics / Cloud data platforms**

**Power BI semantic models** provide a mature, tabular, in-memory semantic layer (dimensions, measures, relationships, row-level security). With **Microsoft Fabric** and **OneLake**, imported semantic model data is automatically written out as Delta tables in OneLake, and Direct Lake mode supports building semantic models directly on OneLake lakehouses/warehouses, including multi-artifact models spanning several Fabric sources. Mature, widely deployed in enterprise BI, now integrated with Fabric's data platform. Use Power BI semantic models as the "BI semantic surface" and progressively align metric definitions with warehouse-level semantics (e.g., dbt Semantic Layer or OSI-aligned models). See also [Microsoft Fabric IQ](../AgentPlatforms/microsoft-fabric-databases-2026.md), which builds a shared agent-facing context layer on top of this semantic foundation.

### AWS — QuickSight Topics & Amazon Q in QuickSight
**Ring: Assess→Trial · Quadrant: BI & analytics semantics**

AWS QuickSight's **Topics** feature is explicitly described as a semantic layer sitting atop data: define business terms and metrics in end-user language, add friendly names/descriptions/synonyms, specify field roles (measure vs. dimension), default aggregations, semantic types (currency, percentage, location, person, organization), and value formats. Amazon Q in QuickSight (generative BI) leverages these definitions for natural-language Q&A. Feature-complete for AWS-centric BI but less "platform-level" than Semantic Views or Metric Views. Good fit to pilot semantic-aware generative BI with Amazon Q for QuickSight-committed teams; limited as a cross-tool semantic engine.

### Google Cloud — Looker Semantic Layer (LookML)
**Ring: Adopt · Quadrant: BI & analytics semantics**

Looker's semantic layer, via **LookML**, defines dimensions, measures, joins, and logic as a single source of truth for business metrics consumed across Looker and other tools — explicitly positioned to ground AI and analytics in consistent reference definitions. Google is also an OSI participant, pushing toward open, interchangeable semantic model specs that can span platforms. Stable, widely used, strong semantic modeling expressiveness. Treat LookML as a core semantic layer for analytics, planning for eventual OSI alignment if semantic portability beyond Looker/GCP is needed.

---

## Universal / Standalone Semantic Layers & Metrics Stores

### dbt Semantic Layer (MetricFlow)
**Ring: Trial · Quadrant: Universal semantic layers**

Powered by **MetricFlow** (post-Transform acquisition), the dbt Semantic Layer is a translation layer between business and data teams: metrics are codified centrally in YAML, version-controlled in Git, and exposed to multiple endpoints (BI tools, APIs, LLMs) via a hub-and-spoke architecture acting as an API for data. dbt is a core OSI participant; practitioners report using it to power MCP-style agent servers. Production-ready for dbt-mature teams; strong alignment with emerging OSI standards. Start with a single business domain (e.g., revenue) to avoid over-modeling.

### Cube Core / Cube Cloud
**Ring: Trial→Adopt · Quadrant: Universal semantic layers**

**Cube Core** is an open-source, standalone semantic layer defining metrics, dimensions, joins, and access rules once in code, exposed via SQL, REST, and GraphQL to BI tools, custom apps, and AI agents — managing data modeling, access, caching, and pre-aggregations as a centralized control panel for data. Cube Cloud adds observability, compliance, developer tooling, and pre-aggregation management for enterprise use, often implemented atop AWS, Snowflake, and other platforms. Widely adopted in API-oriented analytics stacks. Particularly attractive for semantic APIs feeding AI agents, embedded analytics, and multiple BI tools without replicating models per tool.

### AtScale — Universal Semantic Layer
**Ring: Adopt · Quadrant: Universal semantic layers**

AtScale delivers governed business logic and multidimensional analytics across cloud data platforms (Snowflake, Databricks, BigQuery), centralizing metric definitions and business terms and exposing them via standard interfaces (XMLA, JDBC, REST) for consistent metrics across Power BI, Tableau, Excel, Python notebooks, and AI agents. AtScale has joined OSI, bringing a decade of semantic-layer experience to vendor-neutral standards work. Enterprise-grade, proven, strong multi-tool interoperability — a default choice for large orgs wanting centralized governance and multi-cloud/multi-BI semantics without building their own semantic APIs.

### Denodo — Universal Semantic Layer (Data Virtualization)
**Ring: Trial · Quadrant: Semantic knowledge stack / universal layer**

Denodo's **Universal Semantic Layer**, built on its data virtualization platform, centralizes and harmonizes semantics across disconnected definitions in different sources and tools, emphasizing AI-ready data semantics that align metadata with business terms for business users, analytics tools, applications, and AI agents. Denodo is also part of Snowflake's OSI ecosystem. Strong fit for virtualization-centric architectures; still niche compared to dbt/Cube/AtScale in typical modern data-warehouse-centric stacks. Most attractive where semantics must span heterogeneous sources without centralizing all data into a single warehouse/lakehouse.

### Honeydew — Semantic Layer for AI+BI
**Ring: Assess→Trial · Quadrant: Universal semantic layers**

Honeydew positions itself similarly to Snowflake Semantic Views in intent but at organization scope rather than per-schema, creating a single place for business logic atop Snowflake and serving multiple data models/semantic views for diverse workloads, focused on semantically consistent AI and BI experiences. Relatively young compared to dbt/Cube/AtScale; pilot in a single AI-heavy domain to validate benefit vs. using Snowflake Semantic Views directly, especially for Snowflake-committed, AI-forward teams.

### Bright Analytics — Marketing Semantic Layer
**Ring: Assess · Quadrant: Universal semantic layers**

Bright Analytics offers a marketing-domain semantic layer that connects to multiple cloud providers and databases (AWS, GCP, Azure, Snowflake, Redshift, RDS, BigQuery, Azure SQL) without moving data, harmonizing disparate sources into a central model for unified reporting. Domain-specific; emphasizes multi-source connectivity and harmonization rather than general-purpose enterprise semantics. Useful when marketing stacks are fragmented and rapid unification is needed without a broader semantic program.

---

## Semantic Knowledge Stack

Beyond metrics-focused semantic layers, Thoughtworks situates semantic layers alongside **vector search** and **knowledge graphs** as the technologies that make organizational data meaningfully accessible. Knowledge-graph and ontology platforms form a related quadrant, important when extending semantics beyond tabular metrics into entity-relationship reasoning over unstructured content:

| Tool | Ring | Notes |
|---|---|---|
| **OntoText** | Assess→Trial | Knowledge graph platform with rich semantic modeling |
| **PoolParty** | Assess→Trial | Taxonomy/ontology management and semantic search |
| **Sinequa** | Assess→Trial | Enterprise search with semantic enrichment |
| **Semaphore** | Assess→Trial | Semantic metadata and classification platform |

---

## Standards & Ecosystem — Open Semantic Interchange (OSI)

The **Open Semantic Interchange (OSI)** initiative, led by Snowflake with partners including dbt Labs, Sigma, Omni, Hex, and later Google and AWS, aims to create a vendor-neutral specification for semantic model exchange (a YAML-based OSI model plus mapping modules). Before OSI, each tool implemented its own proprietary semantic layer (metrics store, context layer, headless BI), producing semantic fragmentation even where metric logic was well defined within a single tool. Participants in OSI working groups now include Alation, Atlan, BlackRock, Cube, dbt Labs, Elementum AI, Hex, Honeydew, Mistral AI, Omni, RelationalAI, Salesforce, Select Star, Sigma, and ThoughtSpot — framed as a "universal translator" letting platforms understand business-specific definitions like "revenue" or "active user" consistently across embedded analytics and AI experiences.

**Ring: Assess→Trial · Quadrant: Cross-cutting technique/standard overlaying all quadrants above.** Strategically important; still evolving; worth aligning new semantic-layer work to its emerging shape.

---

## Radar Summary Table

| Provider / Tool | Quadrant | Ring | Primary Context |
|---|---|---|---|
| Snowflake Semantic Views | Cloud data platforms | Trial→Adopt | Warehouse-native semantics for AI/BI |
| Databricks Metric Views | Cloud data platforms | Trial | Lakehouse-native semantic metrics |
| Power BI semantic models + Fabric | BI semantics / Cloud data platforms | Adopt | Mature BI semantics, OneLake integration |
| AWS QuickSight Topics | BI semantics | Assess→Trial | BI-native semantic Q&A terms & metrics |
| Looker (LookML) | BI semantics | Adopt | GCP-centric semantic modeling language |
| dbt Semantic Layer (MetricFlow) | Universal semantic layers | Trial | Code-first metrics store integrated with dbt |
| Cube Core / Cube Cloud | Universal semantic layers | Trial→Adopt | Open semantic layer APIs across tools |
| AtScale Universal Semantic Layer | Universal semantic layers | Adopt | Enterprise semantic governance across BI |
| Denodo Universal Semantic Layer | Semantic knowledge stack / universal | Trial | Virtualized semantics across platforms |
| Honeydew Semantic Layer | Universal semantic layers | Assess→Trial | AI+BI semantic layer on Snowflake |
| Bright Analytics semantic layer | Universal semantic layers | Assess | Marketing-centric semantic harmonization |
| OntoText / PoolParty / Sinequa / Semaphore | Semantic knowledge stack | Assess→Trial | Ontology/knowledge-graph semantics |
| OSI (Open Semantic Interchange) | Cross-cutting standard | Assess→Trial | Vendor-neutral semantic model spec |

---

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Enterprise-wide rollout risk | Attempting to semantically model the whole enterprise at once causes dual-track reporting where legacy and new definitions coexist | Start in a single domain (e.g., Revenue & Customer Analytics); wire two or three consuming tools to that semantic source before expanding |
| Platform lock-in for semantics | Warehouse/lakehouse-native semantic objects (Semantic Views, Metric Views) are powerful but tied to one platform | Pair platform-native semantics with a universal layer (dbt Semantic Layer, Cube, AtScale) when multiple BI tools or AI agents must consume the same metrics consistently |
| Semantic fragmentation across tools | Each BI/AI tool historically implements its own proprietary semantic layer, causing the same metric ("revenue") to be defined differently per tool | Track and align to the emerging OSI specification where vendors support it; otherwise centralize definitions in one universal layer and treat tool-native models as projections of it |
| AI agents querying raw schemas directly | LLM-based text-to-SQL/NL-BI agents that bypass the semantic layer reproduce inconsistent metric logic and risk hallucinated joins | Route agent data access through the governed semantic layer (Cortex Analyst over Semantic Views, MCP servers backed by dbt Semantic Layer/Cube) rather than raw warehouse schemas |

## Practical Adoption Guidance by Platform Bias

- **Snowflake-first**: Semantic Views (Trial→Adopt) combined with dbt Semantic Layer or AtScale/Cube for cross-tool semantics.
- **Databricks-first**: Metric Views (Trial) plus dbt Semantic Layer or Cube for semantic reuse outside Databricks.
- **Microsoft-centric**: Power BI semantic models + Fabric/OneLake integration (Adopt), then evaluate whether a universal layer (AtScale, Cube) is needed for non-Microsoft tools.
- **AWS-heavy**: QuickSight Topics for BI semantics (Assess→Trial); consider universal layers (Cube, AtScale) for DRY semantics across additional tools.
- **GCP-centric**: Continue adopting Looker semantic models (Adopt); monitor OSI alignment and universal-layer options as multi-tool needs grow.

## See Also

- [Agent Tech Stack References](README.md)
- [Thoughtworks Technology Radar Vol. 34 — Agentic AI Digest](thoughtworks-radar-vol34.md)
- [Microsoft Build 2026 — Fabric & Databases](../AgentPlatforms/microsoft-fabric-databases-2026.md)
- [RAG Implementation](../RAG/Readme.md)
- [Production Best Practices — Context Engineering](../ProductionBestPractices/context-engineering.md)
- [AllThingsAWS](../AllThingsAWS/README.md)
- [AllThingsGoogle](../AllThingsGoogle/README.md)
- [AllThingsMicrosoft](../AllThingsMicrosoft/README.md)

## References

- [Semantic layer | Technology Radar — Thoughtworks](https://www.thoughtworks.com/radar/techniques/semantic-layer)
- [What is Semantic Layer? — Databricks](https://www.databricks.com/blog/what-is-a-semantic-layer)
- [What is a Semantic Layer? Definition, Benefits, Types & More — AtScale](https://www.atscale.com/glossary/semantic-layer/)
- [Cube Core is open-source semantic layer for AI, BI and more — GitHub](https://github.com/cube-js/cube)
- [Build and centralize metrics with the dbt Semantic Layer — dbt Labs](https://www.getdbt.com/blog/build-centralize-and-deliver-consistent-metrics-with-the-dbt-semantic-layer)
- [Semantic Layer: What it is and when to adopt it — dbt Labs](https://www.getdbt.com/blog/semantic-layer-introduction)
- [Overview of semantic views — Snowflake Documentation](https://docs.snowflake.com/en/user-guide/views-semantic/overview)
- [Introduction to Metric Views (part 1 of 3) — Databricks Community](https://community.databricks.com/t5/community-articles/introduction-to-metric-views-part-1-of-3/td-p/157647)
- [How Looker's semantic layer enhances gen AI trustworthiness — Google Cloud](https://cloud.google.com/blog/products/business-intelligence/how-lookers-semantic-layer-enhances-gen-ai-trustworthiness)
- [How to Connect Your Semantic Models to Microsoft Fabric — Pragmatic Works](https://pragmaticworks.com/blog/how-to-connect-your-semantic-models-to-microsoft-fabric-power-bi-tutorial)
- [A Guide to generative BI Topics with AWS QuickSight — Superluminar](https://superluminar.io/2025/10/10/a-guide-to-generative-bi-topics-with-aws-quicksight/)
- [Snowflake's Semantic Layer: The Missing Link in Modernization — Hakkoda](https://hakkoda.io/resources/snowflake-semantic-layer/)
- [Open Semantic Interchange (OSI) Further Expands Partner Ecosystem — Snowflake](https://www.snowflake.com/en/blog/osi-initiative-expands-partners/)
- [Snowflake OSI: How the Open Semantic Interchange Initiative Will... — Brooklyn Data Co.](https://www.brooklyndata.co/ideas/2025/11/24/where-are-we-with-semantic-layers)
- [Open and Unified Business Semantics for BI and AI — Databricks](https://www.databricks.com/blog/redefining-semantics-data-layer-future-bi-and-ai)
- [Model metric views — Azure Databricks, Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/business-semantics/metric-views/basic-modeling)
- [OneLake integration for semantic models — Microsoft Learn](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/onelake-integration-overview)
- [Making QuickSight topics natural-language-friendly — Amazon QuickSight Docs](https://docs.aws.amazon.com/quick/latest/userguide/topics-natural-language.html)
- [Semantic Layer — Cube.dev](https://cube.dev/use-cases/semantic-layer)
- [How Cube's Universal Semantic Layer & AWS work together — Cube.dev](https://cube.dev/blog/how-cubes-universal-semantic-layer-and-amazon-web-services-aws-work-together)
- [AtScale Joins OSI to Advance Open Semantic Standards for AI — AtScale](https://www.atscale.com/press/atscale-joins-open-semantic-interchange-open-standards/)
- [Semantic Layer: Your Key to AI-Ready Data Insights — Denodo](https://www.denodo.com/en/solutions/by-capability/universal-semantic-layer)
- [Honeydew and Snowflake Semantic Views — Honeydew](https://honeydew.ai/blog/honeydew-and-snowflake-semantic-views/)
- [Marketing semantic layer for your data warehouse — Bright Analytics](https://brightanalytics.com/use-cases/semantic-layer-for-your-data-warehouse/)
- [The future of data is semantic — Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/data-strategy/future-data-semantic)
- [What Is Open Semantic Interchange? — ThoughtSpot](https://www.thoughtspot.com/data-trends/analytics/open-semantic-interchange)
- [What do you think about the Open Semantic Interchange (OSI)? — r/dataengineering](https://www.reddit.com/r/dataengineering/comments/1o25ss6/what_do_you_think_about_the_open_semantic/)
