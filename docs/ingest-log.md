# Ingest Log

Append-only record of all ingest, query, and lint operations on this wiki.
Format: `## [YYYY-MM-DD] <operation> | <source> | sections touched: <list>`

---

## [2026-04-30] ingest | awsmp-buiding-agentic-systems-module-4.pdf | sections touched: Architecture/multi-agent-system, AgentPlatforms/aws-agentcore, Standards/agent2agent, ProductionBestPractices/deployment, ProductionBestPractices/security, ProductionBestPractices/observability, ProductionBestPractices/state-memory

**Source**: `raw/4. awsmp-buiding-agentic-systems-module-4.pdf`
**URL**: https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/multi-agent-architectures
**Type**: AWS Marketplace workshop slide deck (33 pages, 2026)
**Authors**: Dr. James Bland (WW Tech Lead, Data & AI, AWS), Mike Brugnoni (Sr. Solutions Architect, AWS)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Architecture/multi-agent-system.md` | Extended | Four planes, when-to-move-to-multi-agent triggers, four orchestration patterns, non-determinism compounding math, shared state design, MCP vs A2A distinction, failure modes, security at agent boundaries, distributed observability |
| `docs/AgentPlatforms/aws-agentcore.md` | Extended | 13-domain capability stack with AWS service mappings, See Also and References sections added |
| `docs/Standards/agent2agent.md` | Extended | AWS-specific MCP vs A2A guidance section added |
| `docs/ProductionBestPractices/deployment.md` | Extended | Orchestration loop detection, schema-first handoffs, handoff payload bloat rows added to best practices table |
| `docs/ProductionBestPractices/security.md` | Extended | Multi-agent boundary security rows: overprivileged subagents (AWS STS), prompt injection propagation, credential exposure in payloads, unauthorized agent discovery |
| `docs/ProductionBestPractices/observability.md` | Extended | Multi-agent cost attribution row; AWS multi-agent observability stack section (CloudWatch Traces, LangSmith, LangFuse); layered evaluation strategy |
| `docs/ProductionBestPractices/state-memory.md` | Extended | Multi-Agent Shared State (AWS Pattern) section with four-tier table and handoff payload principle |

### Summary

AWS Marketplace Module 4 workshop on multi-agent architectures. Key new concepts added: the four-plane model (control/execution/state/capability), four orchestration patterns with AWS implementations and watch-outs, non-determinism compounding math (90%^4 = 66%), the 13-domain agentic AI capability stack mapped to AWS services, and the explicit rule that MCP must not be used for agent-to-agent delegation. Zero-trust framing at every agent boundary is the central security principle.

---



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

---

## [2026-04-28] ingest | Context Engineering Meetup-Lance-Martin.pptx | sections touched: ContextEngineering

**Source**: `raw/Context Engineering Meetup-Lance-Martin.pptx`
**Type**: Conference/meetup slide deck (26 slides)
**Author**: Lance Martin, LangChain
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/ContextEngineering/README.md` | Rewritten | Replaced placeholder with structured section index and strategy summary table |
| `docs/ContextEngineering/challenges.md` | Rewritten | Replaced placeholder with full coverage of 5 failure modes (rot, poisoning, distraction, confusion, clash) with production examples |
| `docs/ContextEngineering/strategies.md` | Rewritten | Replaced placeholder with 5 strategies (offload, reduce, retrieve, isolate, cache) with production examples and comparison table |
| `docs/ContextEngineering/manus.md` | Rewritten | Replaced placeholder with 6 Manus production principles from primary source |
| `docs/ContextEngineering/anthropic.md` | Rewritten | Replaced placeholder with content from both Anthropic context engineering posts |
| `docs/ContextEngineering/langgraph.md` | Rewritten | Replaced placeholder with Lance Martin's framework, open-deep-research walkthrough, DeepAgent pattern |
| `docs/ContextEngineering/devin.md` | Rewritten | Replaced placeholder with Cognition's two core principles and architecture analysis |

### Summary

The slide deck is Lance Martin's meetup companion to his June 2025 blog post. Key additions over the blog post: explicit framing of context engineering as successor to prompt engineering (with Google Trends data), the open-deep-research walkthrough demonstrating all four strategies (offload brief to state, summarize tool observations, isolate across subagents), and two explicit design decisions — preferring offloading over compression when information loss risk is high, and limiting subagent scope to avoid coordination problems. All seven ContextEngineering sub-files were rewritten from placeholder stubs to substantive content drawing on the slide deck plus the primary web sources (Manus blog, Anthropic engineering posts, Cognition post, Drew Breunig post).

## [2026-04-30] ingest | Tool Use Context Engineering Cookbook — Anthropic | sections touched: ContextEngineering/anthropic, ContextEngineering/strategies, ProductionBestPractices/context-engineering, AllThingsAnthropic

**Source**: URL fetch — https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools
**Type**: Anthropic developer cookbook (technical notebook with empirical benchmarks)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/ContextEngineering/anthropic.md` | Extended | New section: "Context Management API Primitives (Cookbook)" — covers all three primitives (compaction, tool-result clearing, memory tool) with API identifiers, empirical benchmark results, implementation guidance, workload-to-primitive mapping table, and note on 1M-token context windows |
| `docs/ContextEngineering/strategies.md` | Extended | Added API-level detail to the Reduce (Compaction) strategy section: `compact_20260112` and `clear_tool_uses_20250919` identifiers, knobs, and the `exclude_tools: ["memory"]` interaction rule; added cookbook to References |
| `docs/ProductionBestPractices/context-engineering.md` | Extended | Added 4 new best-practice rows: tool-result bloat, compaction fidelity loss, memory tool hygiene, clearing+memory interaction; added cookbook to Implementation References table |
| `docs/AllThingsAnthropic/README.md` | Extended | Added hub row for Context Management API Primitives |

### Summary

Anthropic's context engineering cookbook provides an empirical comparison of three first-party API primitives on a 328K-token research corpus. Key new concepts: the `compact_20260112` / `clear_tool_uses_20250919` / `memory_20250818` API identifiers and their beta headers; the distinction between whole-transcript (compaction) vs. sub-transcript (clearing) operations; the `exclude_tools: ["memory"]` rule when combining clearing with the memory tool; the workload-to-primitive mapping framework; and the finding that on a 1M-token window, context rot still degrades recall even without hitting the hard limit (96.3% of baseline tokens were stale file-read results).

## [2026-04-30] ingest | Context Graphs — Foundation Capital + arXiv:2406.11160v3 | sections touched: ContextEngineering/context-graph

**Sources**:
- URL fetch — https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity
- URL fetch — https://arxiv.org/html/2406.11160v3
**Types**: VC essay (Foundation Capital, 2025) + academic paper (Xu et al., IDEA Research / CUHK, 2024)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/ContextEngineering/context-graph.md` | Rewritten | Replaced stub with full two-part page: (1) technical definition — CG formal structure, entity/relation context taxonomy, CGR³ Retrieve→Rank→Reason paradigm, benchmark results on FB15k-237/YAGO3-10/QALD10-en/WWQ; (2) business/agentic framing — decision traces as durable artifacts, why incumbents can't build this, three startup paths, signals for where to build |

### Summary

Two complementary sources on context graphs ingested together. The arxiv paper (IDEA Research, 2024) provides the formal definition: CGs extend KG triples to quadruples by attaching relation contexts (temporal, geographic, provenance, quantitative, event-specific) and entity contexts (descriptions, aliases, types, images). The CGR³ paradigm achieves +33% Hits@1 on FB15k-237 and new SOTA on KGQA benchmarks. The Foundation Capital essay (2025) reframes context graphs as the strategic asset produced when agent orchestration layers capture decision traces — the "why" behind every automated action — arguing this is the trillion-dollar opportunity incumbents (Salesforce, Snowflake) structurally cannot capture because they sit outside the execution path at commit time.

## [2026-04-30] ingest | Introducing Gemini Enterprise Agent Platform (Google Cloud blog) | sections touched: AgentPlatforms, AllThingsGoogle, AgenticFrameworks, Concepts, Standards, ReferenceArchitecture, index
