# Microsoft Build 2026 — Fabric & Databases for Agentic Apps

## Overview

At Microsoft Build 2026, Microsoft announced a set of data platform capabilities anchored on the thesis that the bottleneck for enterprise agentic AI is no longer model capability, but **consistent, shared data context** across the business. The announcements span a new PostgreSQL-compatible database (Azure HorizonDB), an open-source backend deployment SDK (Rayfin), a shared context layer for agents (Fabric IQ), GPU-accelerated analytics, and significant additions to Azure Cosmos DB and Azure SQL for agent tooling.

---

## Azure HorizonDB (Public Preview)

Azure HorizonDB is a fully managed, PostgreSQL-compatible database designed specifically for AI-era workloads. It combines PostgreSQL familiarity with a cloud-scale distributed architecture.

### Architecture and Scale

| Dimension | Specification |
|---|---|
| Compatibility | PostgreSQL-compatible (open-source tools work as-is) |
| Storage | Elastic up to 128 TB |
| Compute scale-out | Up to 3,072 vCores |
| Commit latency | Sub-millisecond, multi-zone |
| Availability | Zone-resilient by default |
| Performance vs. self-managed PostgreSQL | Up to 3x faster transactions and search |

### AI-Native Features

- **Hybrid vector + full-text search**: Combines DiskANN (vector similarity via pgvector) with full-text search (pg_textsearch extension) in a single query — the pattern most RAG applications require. Simultaneously matches semantic meaning and keyword relevance.
- **In-database model invocation**: The `azure_ai` extension brings model inference into the PostgreSQL engine via SQL, eliminating the external orchestration layer typical in current AI-database stacks.
- **Direct connectivity**: Native integration with Microsoft Foundry and Microsoft Fabric; GitHub Copilot in VS Code support for accelerated development.

HorizonDB's Web IQ integration (see Microsoft IQ below) already underpins both Microsoft Copilot and ChatGPT's live web grounding.

---

## Rayfin (Public Preview)

Rayfin is an open-source SDK and CLI that lets developers and coding agents define and deploy a complete application backend entirely in code, running directly on Microsoft Fabric.

### How It Works

1. Describe the app backend in code or natural language (to a coding agent).
2. Rayfin generates a typed, governed backend: database schema, business logic, APIs, identity, and access policies.
3. One CLI command ships it to Microsoft Fabric as a managed service.
4. App data lands in OneLake by default — no copy, no ETL.
5. The deployed backend inherits the tenant's existing security, governance, and compliance controls.

### Key Integrations

- **Replit partnership**: Build in Replit (natural language to running app), deploy with Rayfin — data and services remain in the organization's own Fabric tenant under existing identity and network controls.
- **Microsoft Fabric**: Acts as a production application backend; every Rayfin app gets enterprise-grade security and scale from day one.

### Problem Addressed

Moves agentic AI apps from prototype to production without teams having to build and manage backend infrastructure. Fabric becomes a viable application backend — not just a data warehouse.

---

## Fabric IQ (Generally Available)

Fabric IQ is Microsoft's shared context layer for AI agents and real-time intelligence within Microsoft Fabric. It gives all agents operating within the Fabric ecosystem a single, consistent, governed view of the organization's data.

### Components and GA Status

| Component | Status | Description |
|---|---|---|
| Operations Agents | GA (Build 2026) | Autonomous agents for operational workflows on Fabric data |
| Graph | GA (Build 2026) | Relationship-first modeling engine for organizational knowledge |
| Planning | GA (late June 2026) | Enterprise planning capability: budgets, forecasts, scenario models on semantic models |
| MCP Server | Preview | Exposes Fabric IQ ontologies to any agent from any vendor via the Model Context Protocol |

### Architecture Role

Fabric IQ's business ontology is now accessible via MCP to agents from any vendor — not just Microsoft's. This positions Fabric IQ as a **vendor-neutral shared context bus** rather than a proprietary data silo.

Planning complements ontologies with integrated planning, giving agents a complete, contextual view of historical, real-time, and forward planning data from a single source.

---

## GPU-Accelerated Fabric Data Warehouse

Query acceleration in Fabric Data Warehouse integrates NVIDIA accelerated computing to fundamentally change analytical query performance for AI-driven workloads.

- **Benchmark**: Up to 7x faster than three comparable external vendors for reporting and application workloads at 64-user concurrency (internal benchmarking, May 2026).
- **Purpose**: Designed for AI-driven analytical workloads where sub-second query response is required for agent reasoning loops.

---

## Agent Skills for Power BI

- **Agent Skills for Power BI**: Developers prompt an AI agent to build and refine semantic models and reports within Fabric.
- **Fabric Apps for Semantic Models**: AI agents can build and deploy Fabric-native web apps on top of semantic models — moving from data exploration to deployed application without leaving the semantic layer.

---

## Azure Cosmos DB Announcements

### New Capabilities (Build 2026)

| Feature | Status | Description |
|---|---|---|
| Cosmos DB MCP Toolkit | Preview | Connects Cosmos DB data to AI agents and Copilots via the Model Context Protocol |
| Semantic Reranking | Preview | Improves search relevance using built-in contextual understanding — no extra model calls required |
| Global Secondary Indexes | Preview | Enables efficient querying on non-partition-key attributes at global scale |
| Linux Emulator | GA | Build, test, and validate Cosmos DB apps locally on Linux, macOS, and Windows without a cloud dependency |
| Agent Memory Toolkit | Preview | Standardizes persistent memory for AI agents using Cosmos DB + Azure Durable Functions + Foundry models |

The Agent Memory Toolkit addresses one of the most common production gaps in agentic systems: the absence of durable, portable memory that persists across sessions and agent invocations.

---

## Azure SQL / SQL Server — Agentic Tooling

| Feature | Status | Description |
|---|---|---|
| SQL MCP Server | Public Preview | Securely connects SQL data to AI agents and Copilots via Model Context Protocol |
| 160 / 192 vCore options | GA | Larger instance sizes for high-throughput agent workloads |
| Vector index enhancements | GA | Faster, more capable vector indexes with improved search performance and efficiency — no code changes required |

---

## Microsoft IQ — Unified Intelligence Layer

Microsoft IQ is the umbrella name for Microsoft's unified intelligence layer, announced at Build 2026 as generally available. It unifies four intelligence streams:

| Layer | Description |
|---|---|
| Work IQ | Intelligence grounded in Microsoft 365 organizational data |
| Foundry IQ | Intelligence from models, knowledge bases, and agent execution data |
| Fabric IQ | Intelligence grounded in organizational analytics and operational data |
| Web IQ | Live web grounding for real-time external information |

Foundry IQ knowledge bases unify Work IQ, Fabric IQ, File Search, Azure SQL, and MCP behind a single SLA-backed retrieval endpoint — simplifying multi-source retrieval for agent developers.

**Microsoft Agent Framework 1.0** also reached GA at Build 2026. **Copilot Credits** is the named consumption metering unit for agent work across the Microsoft platform.

---

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Shared context across agents | Multiple agents see inconsistent views of org data | Use Fabric IQ as the shared ontology layer; expose via MCP for vendor-neutral access |
| RAG retrieval quality | Vector search alone misses keyword-relevant results | Use HorizonDB's hybrid DiskANN + pg_textsearch in a single query |
| Prototype-to-production gap | Custom backend infrastructure delays agentic app deployment | Use Rayfin to define backends in code and deploy to Fabric in one CLI command |
| Agent memory persistence | Agent state lost between sessions | Use Cosmos DB Agent Memory Toolkit (Cosmos DB + Durable Functions + Foundry models) |
| SQL data in agent tools | Connecting relational data to agents requires custom integration | Use SQL MCP Server (Public Preview) for governed MCP-based access |
| Analytics latency in agent loops | Slow queries stall agent reasoning | GPU-accelerated Fabric Data Warehouse targets sub-second latency for agent-driven analytics |

## See Also

- [Microsoft Azure AI Agent Service](microsoft-azure.md)
- [Enterprise Agentic AI Platforms (2026)](enterprise-platforms-2026.md)
- [Microsoft Agent Framework](../AgenticFrameworks/microsoft-framework.md)
- [MCP Standard](../Standards/mcp.md)
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Agent Memory](../AgentMemory/README.md)
- [Context Engineering](../ContextEngineering/README.md)
- [Semantic Data Layer Technology Radar](../AgenticTechStack/semantic-data-layer-radar.md)
- [AllThingsMicrosoft](../AllThingsMicrosoft/README.md)
- [Production Best Practices — State and Memory](../ProductionBestPractices/state-memory.md)
- [Production Best Practices — Cost Management](../ProductionBestPractices/cost-management.md)

## References

- [Microsoft Build 2026: Building agentic apps with Microsoft Fabric and Microsoft Databases](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/) — Azure Blog, June 2026
- [The Era of the Agentic Database Developer: Microsoft SQL announcements at Build 2026](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/The-Era-of-the-Agentic-Database-Developer-Microsoft-SQL/ba-p/5190062) — Microsoft Fabric Community Blog, June 2026
- [Azure Cosmos DB: MCP Toolkit, Semantic Reranking, Global Secondary Indexes, and more](https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/) — Azure Cosmos DB Blog, June 2026
- [Fabric IQ: The shared context layer for AI agents and real-time intelligence](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-IQ-The-shared-context-layer-for-AI-agents-and-real-time/ba-p/5191678) — Microsoft Fabric Community Blog, June 2026
- [Introducing Rayfin: A new AI-first way to build, deploy, and govern application backends](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Introducing-Rayfin-A-new-AI-first-way-to-build-deploy-and-govern/ba-p/5191676) — Microsoft Fabric Community Blog, June 2026
- [Azure HorizonDB: Enterprise-Ready Postgres, Engineered for the AI Era](https://techcommunity.microsoft.com/blog/adforpostgresql/azure-horizondb-enterprise-ready-postgres-engineered-for-the-ai-era/4524094) — Microsoft Tech Community, June 2026
