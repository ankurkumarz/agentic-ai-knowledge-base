# Ingest Log

Append-only record of all ingest, query, and lint operations on this wiki.
Format: `## [YYYY-MM-DD] <operation> | <source> | sections touched: <list>`

---

## [2026-04-28] ingest | Prototype to Production.pdf | sections touched: AgentOps, ProductionBestPractices, Standards/agent2agent, AllThingsGoogle

**Source**: `raw/Prototype to Production.pdf`
**Type**: Google whitepaper (40 pages, November 2025)
**Authors**: Sokratis Kartakis, Gabriela Hernandez Larios, Ran Li, Elia Secchi, Huang Xia
**Processed by**: Claude Code (claude-sonnet-4-6)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/ProductionBestPractices/deployment.md` | Extended | Evaluation-gated deployment, 3-phase CI/CD pipeline, GitOps |
| `docs/ProductionBestPractices/testing-evaluations.md` | Extended | Behavioral quality gate, golden datasets, RAI testing (NPOV, parity, persona-based) |
| `docs/ProductionBestPractices/observability.md` | Extended | Observe→Act→Evolve loop, evolution workflow, evolving security, Google Cloud stack |
| `docs/ProductionBestPractices/security.md` | Extended | Three-layer defense model, security response playbook, memory poisoning |
| `docs/ProductionBestPractices/state-memory.md` | Extended | Stateless agent design, externalized state, Vertex AI Agent Engine vs. Cloud Run |
| `docs/ProductionBestPractices/cost-management.md` | Extended | Speed/reliability/cost triangle, idempotent tools, exponential backoff, batching |
| `docs/Standards/agent2agent.md` | Extended | A2A vs. MCP distinction, Agent Cards JSON format, ADK implementation (to_a2a/RemoteA2aAgent), hierarchical composition, registry architectures |
| `docs/AgentOps/README.md` | Extended | Full AgentOps lifecycle, "last mile" gap, people/process/technology model, environment types |
| `docs/AllThingsGoogle/README.md` | Extended | Prototype to Production whitepaper key details, Agent Starter Pack reference |

### Summary

Google's "Prototype to Production" whitepaper establishes a comprehensive AgentOps framework around a core insight: ~80% of production effort goes to infrastructure, security, and validation — not agent intelligence. Key new concepts added to the wiki: evaluation-gated deployment as the pre-production principle, the Observe→Act→Evolve operational loop, A2A protocol implementation details (Agent Cards, ADK `to_a2a()`, `RemoteA2aAgent`, hierarchical composition), MCP vs. A2A layered architecture, Tool/Agent Registry decision framework, and the three-layer security defense with a formal security response playbook.

---

## [2026-04-27] ingest | Agentic-AI-Knowledge-Base-2026-DRAFT.docx | sections touched: AgentMemory, AgenticFrameworks, Benchmarks, EvaluationFrameworks, Observability, ProductionBestPractices, index, mkdocs.yml

**Source**: `raw/Agentic-AI-Knowledge-Base-2026-DRAFT.docx`
**Type**: Internal knowledge base draft (Word document, ~24 MB)
**Processed by**: Claude Code (claude-sonnet-4-6)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentMemory/functional-tiers.md` | Updated | Three functional tiers of agent memory |
| `docs/AgentMemory/ltm-strategies.md` | Updated | Long-term memory strategies |
| `docs/AgentMemory/research-papers.md` | Updated | Research papers and technical whitepapers |
| `docs/AgentMemory/short-term.md` | Updated | Short-term memory management solutions |
| `docs/AgenticFrameworks/README.md` | Updated | Other/emerging frameworks section |
| `docs/AgenticFrameworks/autogpt.md` | Updated | AutoGPT framework coverage |
| `docs/AgenticFrameworks/haystack.md` | Updated | Haystack framework coverage |
| `docs/AgenticFrameworks/pydantic-ai.md` | Updated | PydanticAI framework coverage |
| `docs/AgenticFrameworks/spring-ai.md` | Updated | Spring AI framework coverage |
| `docs/Benchmarks/agent-benchmarks.md` | Updated | Agent evaluation benchmarks |
| `docs/Benchmarks/llm-benchmarks.md` | Updated | LLM evaluation benchmarks |
| `docs/EvaluationFrameworks/llm-frameworks.md` | Updated | LLM evaluation frameworks |
| `docs/EvaluationFrameworks/platforms.md` | Updated | Agent evaluation platforms |
| `docs/Observability/goals.md` | Updated | Observability goals and objectives |
| `docs/Observability/solutions.md` | Updated | Observability solutions and tooling |
| `docs/index.md` | Updated | Home page updated to reflect new sections |
| `mkdocs.yml` | Updated | Nav entries added for ProductionBestPractices section |

### Files Created (New)

| File | Notes |
|---|---|
| `docs/ProductionBestPractices/README.md` | New section overview — production readiness guidance |
| `docs/ProductionBestPractices/observability.md` | Tracing, metrics, logs, cost visibility, tooling |
| `docs/ProductionBestPractices/state-memory.md` | Memory tiers, LTM strategies, session persistence |
| `docs/ProductionBestPractices/deployment.md` | GenOps, canary rollouts, prompt versioning, durable execution |
| `docs/ProductionBestPractices/testing-evaluations.md` | LLM-as-judge, eval frameworks, benchmarks, platforms |
| `docs/ProductionBestPractices/context-engineering.md` | Context rot, compaction, retrieval, isolation, caching |
| `docs/ProductionBestPractices/security.md` | Prompt injection, HITL, least privilege, audit trails |
| `docs/ProductionBestPractices/cost-management.md` | Model routing, token budgets, cost monitoring, vendor guidance |

### Summary

Initial processing of the 2026 draft knowledge base document. Established the **Production Best Practices & Guidelines** section (16 in nav) as a new cross-cutting layer synthesizing production concerns from across the draft. Updated framework coverage for AutoGPT, Haystack, PydanticAI, and Spring AI. Extended Agent Memory section with LTM strategies and research papers. Expanded Evaluation and Benchmark coverage. Observability section updated with goals and solution landscape.

**Uncommitted as of log creation** — working tree changes pending commit.
