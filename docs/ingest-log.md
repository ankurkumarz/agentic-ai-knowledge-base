# Ingest Log

Append-only record of all ingest, query, and lint operations on this wiki.
Format: `## [YYYY-MM-DD] <operation> | <source> | sections touched: <list>`

---

## [2026-07-10] ingest | AWS Marketplace — Building Agentic Systems on AWS: Agent Memory Systems (Module 7) | sections touched: AgentMemory/short-term.md, AgentMemory/functional-tiers.md, AgentMemory/ltm-strategies.md, ProductionBestPractices/state-memory.md, AgentPlatforms/aws-agentcore.md, AllThingsAWS/README.md, index.md

**Source**: `raw/awsmp-building-agentic-systems-module-7.pdf`
**Type**: Vendor workshop slide deck (35 pages, AWS Marketplace, 2026)
**Presenters**: Leonardo Murillo (Developer Relations, AWS Marketplace), Thaddeus Worsnop (Principal Solutions Architect, AWS)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentMemory/short-term.md` | Extended | Added context window token budget layout table, KV cache hit rate optimization note, semantic window strategy, progressive summarization strategy, windowing strategy comparison table, LangGraph checkpointer pattern detail, updated best practices with KV cache guidance, added References section |
| `docs/AgentMemory/functional-tiers.md` | Extended | Added AWS Duration × Scope Memory Taxonomy section mapping CoALA types to AWS services (in-context / session / cross-agent / semantic), session memory implementation patterns, shared cross-agent state notes; added References |
| `docs/AgentMemory/ltm-strategies.md` | Extended | Expanded HNSW vs IVF+PQ selection guide with memory-per-vector numbers and detailed parameter guidance; updated hybrid search section with full pipeline latency table (BM25+dense+RRF+reranker ~62ms end-to-end) and dense-only failure cases; added Strategy 9 (AgentCore Memory — extraction strategy tiers, event API, record types); added Strategy 10 (Three-Tier Partner Memory Stack — Redis Cloud, MongoDB Atlas, Neo4j AuraDB with hot/cold handoff pattern); updated References |
| `docs/ProductionBestPractices/state-memory.md` | Extended | Added Memory Governance section: data lineage (CloudTrail/DynamoDB Streams), retention policies by tier, PII detection (Bedrock Guardrails + Macie + field-level encryption), right-to-delete implementation patterns; updated See Also |
| `docs/AgentPlatforms/aws-agentcore.md` | Extended | Expanded Memory Management bullet with short-term/long-term architecture details and extraction strategy tiers; added Module 7 to References |
| `docs/AllThingsAWS/README.md` | Extended | Added two hub rows: AWS AgentCore Memory and Agent Memory Systems (Module 7 Workshop); added state-memory to See Also |
| `docs/index.md` | Extended | Updated State & Memory Management section to reflect new coverage: AWS taxonomy, context window budget, vector index selection guide, memory governance |

### Key Knowledge Added

- **AWS memory taxonomy**: Duration × Scope quadrant (in-context / session / cross-agent / semantic) complementing CoALA's functional types
- **Context window budget engineering**: Token region layout, KV cache hit rate (~85% cost savings for stable system prompts), four windowing strategies with latency comparison
- **HNSW vs IVF+PQ**: Memory-per-vector numbers (~120KB vs ~8–15KB per 1K vectors), parameter tuning guidance, selection decision tree
- **Hybrid search pipeline**: BM25 +5ms → HNSW dense +15ms → RRF +2ms → cross-encoder reranker +40ms = ~62ms end-to-end; dense-only failure cases for exact strings/CVEs/error codes
- **Amazon Bedrock Knowledge Bases**: Chunking strategies, metadata filtering for pre-ANN search space reduction, Retrieve vs RetrieveAndGenerate API patterns
- **GraphRAG with Neo4j AuraDB**: Blast-radius queries, dependency traversal at distance 1 and 2, when vector-only retrieval fails for structural facts
- **AgentCore Memory**: Session (CreateEvent/ListEvents), long-term (Extraction → Consolidation → Reflection), three extraction tiers (zero-config / guided / custom)
- **Partner memory stack**: Redis Cloud (CRDT active-active, Redis on Flash, session data structures), MongoDB Atlas (unified doc+vector, aggregation pipeline, change streams), Neo4j AuraDB (graph structural knowledge) — each at a distinct latency tier (< 2ms / ~18ms / ~30ms)
- **Hot/cold handoff**: Redis TTL expiry → EventBridge → Lambda → Bedrock (Haiku extraction) → Pydantic validation → MongoDB Atlas upsert (idempotent)
- **Memory governance**: Lineage per store, retention TTLs by tier (24h session / 90d workflow / 7yr archive), PII detect-and-mask via Guardrails + Macie, right-to-delete implementation with user_id indexes

---

## [2026-07-05] ingest | Kestra — Declarative Agentic Orchestration Platform | sections touched: WorkflowBuilders/orchestration.md, Standards/mcp.md, index.md

**Source**: Multi-source WebSearch/WebFetch research (kestra.io, github.com/kestra-io/kestra) — no raw document or user-supplied URL; task was to find the right bucket for Kestra and add coverage
**Type**: Vendor/tool research — new orchestration platform entry
**Processed by**: Claude Code

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/WorkflowBuilders/orchestration.md` | Extended | Added new "Kestra" subsection alongside Littlehorse/Temporal/Confluent: license (Apache 2.0), architecture, agentic AI capabilities (AI Agent task with memory/tools, MCP server + MCP-client support, human-in-the-loop guardrails, multi-agent composition), core features table, deployment options table, and considerations. Added Kestra row to the platform comparison section, plus References and See Also entries. |
| `docs/Standards/mcp.md` | Extended | Added backlink from MCP page to the new Kestra subsection (bidirectional link for knowledge graph) |
| `docs/index.md` | Extended | Extended the Workflow Engines bullet to mention Kestra's AI Agent tasks and MCP support |

**Note**: No raw source file or URL was supplied for this task; content was researched directly via WebSearch/WebFetch against Kestra's official site, docs, and GitHub repository. `kestra.io/1-0` and `kestra.io` returned HTTP 403 to direct WebFetch, so those facts are sourced via WebSearch snippets citing the same URLs (included in References) rather than full-page fetches.

## [2026-06-30] ingest | Memory Solutions Radar updates — Anthropic, Salesforce, Cloudflare, MinnsDB, agentmemory, framework-native memory | sections touched: AgentMemory/solutions.md, AgentPlatforms/claude-managed-agents.md, AgenticFrameworks/langchain.md, AgenticFrameworks/crewai.md, AgenticFrameworks/llamaindex.md, index.md

**Source**: Multi-source WebSearch/GitHub API research (no single raw document); user-supplied candidate list of 6 memory tools/vendors to evaluate for radar inclusion, verified against primary sources where accessible
**Type**: Vendor/tool research — Technology Radar update
**Processed by**: Claude Code

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentMemory/solutions.md` | Extended | Added 5 new radar entries: Anthropic Claude Managed Agents — Memory (🔵 Trial), Salesforce Agentic Memory/Agentforce (🔵 Trial), agentmemory by rohitg00 (🟡 Assess), Cloudflare Agent Memory (🟡 Assess), MinnsDB (🔴 Caution, unverified primary source — third-party listicle only). Added new "Framework-Native Memory" subsection comparing LangGraph Checkpointer/Store, LlamaIndex Memory module, and CrewAI's unified Memory class as baseline architectures. Updated both Mermaid radar charts, Radar Summary Table, Selection Guide, References, and See Also. Fixed a pre-existing missing `#### Azure AI Foundry Memory` heading. |
| `docs/AgentPlatforms/claude-managed-agents.md` | Extended | Added backlink to `../AgentMemory/solutions.md` in See Also (bidirectional link for knowledge graph) |
| `docs/AgenticFrameworks/langchain.md` | Extended | Added backlink to `../AgentMemory/solutions.md` in See Also |
| `docs/AgenticFrameworks/crewai.md` | Extended | Added backlink to `../AgentMemory/solutions.md` in See Also |
| `docs/AgenticFrameworks/llamaindex.md` | Extended | Added backlink to `../AgentMemory/solutions.md` in See Also |
| `docs/index.md` | Extended | Updated State & Memory Management bullet to reflect expanded radar coverage |

**Note**: WebFetch returned 403 for engineering.salesforce.com, blog.cloudflare.com, and dev.to; those three sources were summarized via WebSearch snippets rather than direct page reads. MinnsDB could not be independently verified beyond a single third-party dev.to listicle — no GitHub repository, company site, or other primary source was located; the radar entry is explicitly flagged Caution with unverified/unconfirmed placeholders rather than invented data.

## [2026-06-30] ingest | Semantic Data Layer Landscape — ThoughtWorks-style Technology Radar (pasted research) | sections touched: AgenticTechStack/semantic-data-layer-radar.md (new), AgenticTechStack/README.md, AgenticTechStack/thoughtworks-radar-vol34.md, AllThingsAWS/README.md, AllThingsGoogle/README.md, AllThingsMicrosoft/README.md, AgentPlatforms/microsoft-fabric-databases-2026.md, RAG/Readme.md, ProductionBestPractices/context-engineering.md, mkdocs.yml, index.md

## [2026-06-30] ingest | Gartner — AI Evaluation and Observability Platforms (AEOPs) | sections touched: EvaluationFrameworks/platforms.md, Observability/Readme.md

## [2025-12-04] ingest | AI Engineering: Building Applications with Foundation Models (Chip Huyen, O'Reilly) | sections touched: Concepts/ai-engineering.md (new), EvaluationFrameworks/ai-as-judge.md (new), ReferenceArchitecture/ai-engineering-architecture.md (new), PromptEngineering/README.md, RAG/Readme.md, Concepts/agent-definition.md, EvaluationFrameworks/llm-frameworks.md, ProductionBestPractices/cost-management.md, ProductionBestPractices/observability.md, mkdocs.yml, index.md

**Source**: `raw/AIEngineering.pdf`
**Type**: Book (535 pages, O'Reilly, December 2024)
**Author**: Chip Huyen
**ISBN**: 978-1-098-16630-4
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Concepts/ai-engineering.md` | Created | AI Engineering discipline overview — rise of AI engineering, three-factor model, 8-category use case taxonomy, AI stack layers, AI engineering vs. ML engineering comparison table, application planning framework |
| `docs/EvaluationFrameworks/ai-as-judge.md` | Created | Comprehensive AI-as-judge guide — three usage patterns, prompt design principles, built-in criteria comparison table, limitations (inconsistency, length/positional bias, criteria ambiguity), judge model selection matrix, pairwise comparative evaluation, best practices table |
| `docs/ReferenceArchitecture/ai-engineering-architecture.md` | Created | Five-step production architecture — base → context enhancement → guardrails → router/gateway → caching → agent patterns; monitoring metrics (MTTD, MTTR, CFR); orchestration patterns |
| `docs/PromptEngineering/README.md` | Full rewrite | Added overview, prompting concepts (in-context learning, system/user prompt split), 6 best practices (clear instructions, context, task decomposition, CoT, iteration, versioning), defensive prompt engineering (injection, jailbreaking, defenses table), structured outputs |
| `docs/RAG/Readme.md` | Extended | Added full RAG Architecture section (retriever/generator components, retrieval algorithm comparison table, optimization strategies, RAG vs. finetuning vs. full-context comparison) |
| `docs/Concepts/agent-definition.md` | Extended | Added Huyen/AI Engineering definition — environment + actions framing, agent components (planning/tools/memory), three main failure modes |
| `docs/EvaluationFrameworks/llm-frameworks.md` | Extended | Added See Also link to new ai-as-judge.md page |
| `docs/ProductionBestPractices/cost-management.md` | Extended | Added Inference Optimization section — performance metrics (TTFT/TPOT/MFU/MBU), model-level optimizations (quantization/distillation/speculative decoding), service-level optimizations (continuous batching/KV cache/prompt caching), online vs. batch inference table |
| `docs/ProductionBestPractices/observability.md` | Extended | Added MTTD/MTTR/CFR framework section with evaluation-monitoring coupling principle |
| `mkdocs.yml` | Extended | Added Section 1.7 AI Engineering (Huyen); Section 7.2 AI Engineering Architecture; Section 10.2 AI as a Judge |
| `docs/index.md` | Extended | Added AI Engineering bullet to Concepts; added AI-as-judge bullet to Agent Testing & Evaluations |

### Summary

Chip Huyen's *AI Engineering* is the definitive practical reference for building production AI applications on top of foundation models. The book's 10 chapters cover the full lifecycle: understanding foundation models, evaluation methodology, prompt engineering, RAG, agents, finetuning, dataset engineering, inference optimization, and end-to-end production architecture.

Key concepts added to the wiki:
- **AI Engineering discipline** — how it differs from ML engineering; three-factor model of why it emerged; 8 use case categories with consumer/enterprise breakdown
- **Five-step production architecture** — progressive complexity model from bare model API through context augmentation, guardrails, routing/gateway, caching, and agent patterns
- **AI as a Judge** — comprehensive treatment of LLM-as-judge methodology including three usage patterns, prompt design, limitations, and judge selection
- **Prompt engineering best practices** — 6 principles distilled from Huyen + OpenAI/Anthropic/Google guides, with emphasis on task decomposition and defensive prompting
- **RAG architecture** — retrieval algorithm comparison (keyword/dense/hybrid/reranking), chunking strategies, RAG vs. finetuning decision framework
- **Inference optimization** — TTFT/TPOT/MFU/MBU metrics, quantization/distillation/speculative decoding, continuous batching/KV cache, online vs. batch API trade-offs
- **Observability metrics** — MTTD/MTTR/CFR framework for monitoring infrastructure health; evaluation-monitoring feedback loop

---

## [2026-06-04] ingest | Microsoft Build 2026 — Building Agentic Apps with Microsoft Fabric and Microsoft Databases | sections touched: AgentPlatforms/microsoft-fabric-databases-2026.md (new), AllThingsMicrosoft/README.md, AgentPlatforms/microsoft-azure.md, mkdocs.yml

**Sources**:
- https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/ — Primary Azure Blog announcement
- https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/The-Era-of-the-Agentic-Database-Developer-Microsoft-SQL/ba-p/5190062 — SQL/agentic developer era announcements
- https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/ — Cosmos DB Build 2026 announcements
- https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-IQ-The-shared-context-layer-for-AI-agents-and-real-time/ba-p/5191678 — Fabric IQ GA details
- https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Introducing-Rayfin-A-new-AI-first-way-to-build-deploy-and-govern/ba-p/5191676 — Rayfin introduction
- https://techcommunity.microsoft.com/blog/adforpostgresql/azure-horizondb-enterprise-ready-postgres-engineered-for-the-ai-era/4524094 — Azure HorizonDB details
**Type**: Vendor announcement — Microsoft Build 2026 data platform and database capabilities for agentic AI

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentPlatforms/microsoft-fabric-databases-2026.md` | Created | Full coverage of Build 2026: Azure HorizonDB, Rayfin, Fabric IQ, GPU Fabric Data Warehouse, Agent Skills for Power BI, Cosmos DB MCP Toolkit + Agent Memory Toolkit, SQL MCP Server, Microsoft IQ |
| `docs/AllThingsMicrosoft/README.md` | Extended | Added hub rows for HorizonDB, Rayfin, Fabric IQ, Microsoft IQ, Cosmos DB MCP Toolkit, SQL MCP Server, Microsoft Agent Framework 1.0 GA |
| `docs/AgentPlatforms/microsoft-azure.md` | Extended | Added Build 2026 Updates section summarising key announcements; expanded See Also |
| `mkdocs.yml` | Extended | Added 5.2.7 Microsoft Build 2026 — Fabric & Databases nav entry |

---

## [2026-06-02] synthesis | Claude Code Orchestration Primitives Decision Guide | sections touched: WorkflowBuilders/claude-orchestration-guide.md (new), WorkflowBuilders/dynamic-workflows.md, AllThingsAnthropic/README.md, Standards/mcp.md, mkdocs.yml

**Sources**:
- https://code.claude.com/docs/en/agents — Run agents in parallel (authoritative comparison)
- https://code.claude.com/docs/en/sub-agents — Subagents reference
- https://code.claude.com/docs/en/skills — Skills reference
- https://code.claude.com/docs/en/agent-teams — Agent Teams reference
- https://code.claude.com/docs/en/workflows — Dynamic Workflows reference
**Type**: Decision guide / synthesis — all Claude Code orchestration primitives (MCP, Skills, Subagents, Agent View, Agent Teams, Dynamic Workflows)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/WorkflowBuilders/claude-orchestration-guide.md` | Created | Full decision guide: capability-vs-orchestration framing (MCP is orthogonal), flowchart for choosing between all five primitives, per-primitive when-to-use guidance with token cost context, capability × orchestration composition patterns (MCP + Skills, Skills + Subagents, MCP + Workflows, Subagents + Worktrees, Workflows + Saved Commands), summary decision table, best practices |
| `docs/WorkflowBuilders/dynamic-workflows.md` | Extended | Added See Also link to new guide |
| `docs/AllThingsAnthropic/README.md` | Extended | Added hub row for Orchestration Primitives Guide |
| `docs/Standards/mcp.md` | Extended | Added See Also section with backlink to guide (clarifying MCP's role as capability layer, not orchestration) |
| `mkdocs.yml` | Extended | Added 5.3.7 Orchestration Primitives Decision Guide nav entry |

---

## [2026-06-02] ingest | Dynamic Workflows — Claude Code (code.claude.com/docs/en/workflows) | sections touched: WorkflowBuilders/dynamic-workflows.md (new), AllThingsAnthropic/README.md, RAG/search-as-code.md, AgentHarness/code-as-agent-harness.md, mkdocs.yml

**Source**: https://code.claude.com/docs/en/workflows
**Type**: Official product documentation — Claude Code, Anthropic

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/WorkflowBuilders/dynamic-workflows.md` | Created | Full coverage: orchestration primitive comparison table (subagents/skills/agent teams/workflows), plan-in-code architectural pattern, runtime constraints (16 concurrent/1,000 total agents), bundled workflows (/deep-research), ultracode mode, save/reuse as commands, detailed comparison with Perplexity Search as Code (shared "code as orchestrator" meta-pattern, different layers: retrieval vs. coordination) |
| `docs/AllThingsAnthropic/README.md` | Extended | Added hub row for Dynamic Workflows with backlink |
| `docs/RAG/search-as-code.md` | Extended | Added See Also backlink to dynamic-workflows.md with context note |
| `docs/AgentHarness/code-as-agent-harness.md` | Extended | Added See Also backlinks to dynamic-workflows.md and search-as-code.md |
| `mkdocs.yml` | Extended | Added 5.3.6 Dynamic Workflows (Claude Code) nav entry |

---

## [2026-06-02] ingest | Rethinking Search as Code Generation (Perplexity AI Research) | sections touched: RAG/search-as-code.md (new), Benchmarks/agent-benchmarks.md, ProductionBestPractices/context-engineering.md, RAG/Readme.md, mkdocs.yml, index.md

**Source**: https://research.perplexity.ai/articles/rethinking-search-as-code-generation
**Type**: Research article — Perplexity AI, September 2025. Introduces Search as Code (SaC) reference architecture, three-layer model, WANDR benchmark, and performance evaluation.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/RAG/search-as-code.md` | Created | Full SaC coverage: overview, three-layer architecture (Models as Control Plane / Compute Sandboxes / Agentic Search SDK), WANDR benchmark, CVE case study (100% accuracy, 85.1% token reduction), RAG comparison table, Python SDK, best practices |
| `docs/Benchmarks/agent-benchmarks.md` | Updated | Added WANDR benchmark under new "Research and Retrieval Benchmarks" section; added WANDR to benchmark selection guide; added See Also link |
| `docs/ProductionBestPractices/context-engineering.md` | Updated | Added "Fixed pipeline rigidity" row to best practices table; added Perplexity SaC row to Implementation References table |
| `docs/RAG/Readme.md` | Updated | Added Search as Code intro section with backlink to new page |
| `mkdocs.yml` | Updated | Added 7.9 Search as Code (Perplexity) nav entry |
| `docs/index.md` | Updated | Added SaC bullet under RAG Architecture in section 8 |

---

## [2026-06-02] ingest | microsoft/agentpex (GitHub) | sections touched: EvaluationFrameworks/llm-frameworks.md, ProductionBestPractices/testing-evaluations.md, AllThingsMicrosoft/README.md

**Source**: https://github.com/microsoft/agentpex
**Type**: Open-source tool (Microsoft, MIT license) — agent trace evaluation framework

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/llm-frameworks.md` | Updated | Added AgentPex section under Open Source Frameworks; added row to Selection Guide |
| `docs/ProductionBestPractices/testing-evaluations.md` | Updated | Added AgentPex row to Evaluation Frameworks table |
| `docs/AllThingsMicrosoft/README.md` | Updated | Added AgentPex row to Key Offerings table with backlink |

---

## [2026-06-02] ingest | Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents (arXiv:2605.30621) | sections touched: AgentHarness/harness-self-evolution.md (new), AgentHarness/agent-harness.md, AgentHarness/harness-engineering.md, AgentHarness/harness-optimization.md, mkdocs.yml

**Source**: https://arxiv.org/abs/2605.30621
**Type**: Research paper — Lin et al. (KDD 2026, Datasets and Benchmarks Track, oral); 24 pages, 9 figures, 12 tables

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/harness-self-evolution.md` | Created | New page covering harness self-evolution paradigm, HUC/HBC distinction, key findings, design implications, and best practices |
| `docs/AgentHarness/agent-harness.md` | Updated | Added See Also link and References entry for arXiv:2605.30621 |
| `docs/AgentHarness/harness-engineering.md` | Updated | Added See Also link to harness-self-evolution.md |
| `docs/AgentHarness/harness-optimization.md` | Updated | Added See Also link to harness-self-evolution.md |
| `mkdocs.yml` | Updated | Added 2.7 Harness Self-Evolution nav entry |

---

## [2026-06-01] ingest | The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management (arXiv:2605.23071) | sections touched: ContextEngineering/efficiency-frontier.md (new), ContextEngineering/strategies.md, ProductionBestPractices/cost-management.md, ProductionBestPractices/context-engineering.md, index.md

**Source**: https://arxiv.org/abs/2605.23071

## [2026-05-30] ingest | Agent Harness for Large Language Model Agents: A Survey (arXiv:2605.29682) | sections touched: AgentHarness/llm-harness-survey.md, AgentHarness/agent-harness.md, AgentHarness/harness-engineering.md

**Source**: https://arxiv.org/pdf/2605.29682
**Type**: Research survey paper — Meng, Wang, Chen, Wu, Li, Jiang, Wang, Lu, Gao, Wu, Hu (2026); 110+ papers, 23 systems; DOI: 10.20944/preprints202604.0428.v3

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/llm-harness-survey.md` | Updated | Added Survey A/B disambiguation; attributed H=(E,T,C,S,L,V) LTS semantics to arXiv:2605.29682; added DeerFlow and DeepAgents to completeness matrix; added AgencyBench/HAL cost details; added Eight Future Directions section; updated References |
| `docs/AgentHarness/agent-harness.md` | Updated | Updated Formal Taxonomy section to cite arXiv:2605.29682 and note LTS semantics; added arXiv citation to References |
| `docs/AgentHarness/harness-engineering.md` | Updated | Updated Nine Technical Challenges attribution; added arXiv:2605.29682 to References |

---

## [2026-05-24] ingest | Temporal — Durable Workflow Orchestration for Agentic AI | sections touched: WorkflowBuilders/orchestration.md (Temporal section added), index.md

**Sources**: https://temporal.io/ai/agentic-ai; https://youtu.be/GEXllEH2XiQ?si=2uQ0Ov0VPxjGPf_o; https://docs.temporal.io/evaluate/understanding-temporal#durable-execution

## [2026-05-24] ingest | Agent Memory Providers — Maximem (Synap + Vity) | sections touched: AgentMemory/solutions.md

**Sources**: https://www.maximem.ai/; https://www.maximem.ai/product; https://www.maximem.ai/vity; https://www.maximem.ai/compare/maximem-synap-vs-mem0-vs-zep-vs-letta-vs-supermemory-vs-cognee-vs-evermind; https://github.com/maximem-ai

## [2026-05-24] ingest | Agent Memory Providers — LanceDB, Cognee | sections touched: AgentMemory/solutions.md

**Sources**: https://github.com/lancedb/lancedb; https://github.com/CortexReach/memory-lancedb-pro; https://www.lancedb.com/blog/openclaw-lancedb-memory-layer; https://github.com/topoteretes/cognee; https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory; https://www.cognee.ai/blog/cognee-news/cognee-raises-seven-million-five-hundred-thousand-dollars-seed

## [2026-05-24] ingest | Agent Memory Providers — Honcho, Hindsight, Holographic, RetainDB, ByteRover + Redis context engine reference | sections touched: AgentMemory/solutions.md

**Sources**: https://github.com/plastic-labs/honcho; https://github.com/vectorize-io/hindsight; https://github.com/NeoVertex1/nuggets; https://www.retaindb.com/; https://github.com/campfirein/byterover-cli; https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/

## [2026-05-23] ingest | Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems (arXiv:2605.18747) | sections touched: AgentHarness/code-as-agent-harness.md (new), AgentHarness/agent-harness.md, AgentHarness/harness-engineering.md, index.md, mkdocs.yml

**Source**: https://arxiv.org/abs/2605.18747
**Type**: Research survey paper — Ning et al. (UIUC, Meta, Stanford), May 2026; 197 papers across 40+ subcategories

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/code-as-agent-harness.md` | Created | Full survey coverage: three-layer taxonomy (harness interface, harness mechanisms, harness scaling), code properties (executability/inspectability/statefulness), application domains, relationship to existing harness frameworks, best practices |
| `docs/AgentHarness/agent-harness.md` | Updated | Added "Code as the Harness Substrate" section; added survey to References and See Also |
| `docs/AgentHarness/harness-engineering.md` | Updated | Added new page to See Also and References |
| `docs/index.md` | Updated | Added Agent Harness section with Code as Agent Harness bullet |
| `mkdocs.yml` | Updated | Added Section 2.3: Code as Agent Harness |

---

## [2026-05-23] ingest | OpenViking (volcengine/OpenViking) | sections touched: AgentMemory/solutions.md

**Sources**: https://github.com/volcengine/OpenViking; https://openviking.ai/; https://www.marktechpost.com/2026/03/15/meet-openviking-an-open-source-context-database-that-brings-filesystem-based-memory-and-retrieval-to-ai-agent-systems-like-openclaw/; https://developers.redhat.com/articles/2026/04/23/deploy-openviking-openshift-ai-improve-ai-agent-memory

---

## [2026-05-23] ingest | Google Cloud Agent Gallery — Partner-Built Agents in Gemini Enterprise | sections touched: Marketplace/google-cloud-marketplace.md (new), Marketplace/anthropic-marketplace.md (new), Marketplace/Readme.md, AllThingsGoogle/README.md, AllThingsAnthropic/README.md, mkdocs.yml

**Sources**: https://cloud.google.com/blog/products/ai-machine-learning/partner-built-agents-available-in-gemini-enterprise; Anthropic marketplace presence (second URL provided was malformed — pic.com/news/finance-agents — could not be fetched; page created from known distribution channels)

## [2026-05-23] ingest | Agent Skills / SKILLS.md (Anthropic, 2025) | sections touched: Standards/skills-md.md (new), AllThingsAnthropic/README.md, mkdocs.yml

**Sources**: https://claude.com/blog/skills, https://claude.com/blog/skills-explained, https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
## [2026-05-22] ingest | AIDLC Workflows (AWS Labs) v0.1.8 | sections touched: Standards/aidlc.md (new), AllThingsAWS/README.md, ProductionBestPractices/testing-evaluations.md, Standards/openspec.md, index.md, mkdocs.yml

**Source**: https://github.com/awslabs/aidlc-workflows + https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
**Type**: Open-source framework (MIT-0), AWS Labs, v0.1.8, April 2026

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/aidlc.md` | Created | Full coverage: tenets, three-phase workflow (Inception/Construction/Operations), artifact structure, platform integration table (6 tools), extensions system, AIDLC Evaluator, Design Reviewer, comparison table vs OpenSpec and Kiro, best practices, See Also |
| `docs/AllThingsAWS/README.md` | Updated | Added AIDLC hub row |
| `docs/ProductionBestPractices/testing-evaluations.md` | Updated | Added AIDLC Evaluator to Evaluation Frameworks table |
| `docs/Standards/openspec.md` | Updated | Added AIDLC to See Also for bidirectional graph edge |
| `docs/index.md` | Updated | Added AIDLC bullet to section 6 |
| `mkdocs.yml` | Updated | Added Section 6.7: AIDLC Workflows (AWS) |

---

## [2026-05-22] update | OpenSpec (Fission AI) v1.3.1 | sections touched: Standards/openspec.md, AllThingsOpenAI/README.md

**Source**: https://github.com/Fission-AI/OpenSpec
**Type**: OSS framework update — rewrote page from stub/pre-release to production-grade v1.3.1 (50.1k stars, MIT)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/openspec.md` | Full rewrite | Updated from "upcoming standard / early development" to v1.3.1; added `/opsx` workflow, artifact structure table, comparison table (vs. Kiro, GitHub Spec Kit), best practices, correct attribution (Fission AI, not OpenAI) |
| `docs/AllThingsOpenAI/README.md` | Corrected | Removed incorrect OpenSpec row — OpenSpec is a Fission AI project with no OpenAI affiliation |

---

## [2026-05-17] ingest | OpenClaw | sections touched: AgentPlatforms/openclaw (new), AgentPlatforms/README, AgentPlatforms/hermes-agent, mkdocs.yml

**Source**: https://openclaw.ai/ + https://github.com/openclaw/openclaw + https://github.com/openclaw/clawhub
**Type**: Open-source local-first personal AI agent (MIT license, launched Jan 2026)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentPlatforms/openclaw.md` | Created | Full coverage: history (Clawdbot→Moltbot→OpenClaw), architecture, 20+ messaging integrations, skills/ClawHub, memory system, model support, security (toxic flow trifecta, ClawHavoc incident, 135k+ exposed instances), comparison with Hermes |
| `docs/AgentPlatforms/README.md` | Updated | Expanded OpenClaw entry to link to new page with richer description |
| `docs/AgentPlatforms/hermes-agent.md` | Updated | Added openclaw.md to See Also for bidirectional graph edge |
| `mkdocs.yml` | Updated | Added Section 5.6: OpenClaw |

---

## [2026-05-17] ingest | Hermes Agent (Nous Research) | sections touched: AgentPlatforms/hermes-agent (new), AgentPlatforms/README, AgenticTechStack/README, mkdocs.yml

**Source**: https://hermes-agent.nousresearch.com/ + https://github.com/NousResearch/hermes-agent + https://github.com/NousResearch/hermes-function-calling
**Type**: Open-source personal AI agent (Nous Research, launched Feb 2026)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentPlatforms/hermes-agent.md` | **New page** | Full coverage: capabilities, self-improvement loop, Hermes model family (Hermes-2-Pro, Hermes-3), GOAP reasoning, tool use architecture, comparison table, security considerations |
| `docs/AgentPlatforms/README.md` | Extended | Added Hermes Agent as lead entry under Personal AI Agents; added OpenClaw Thoughtworks Caution note |
| `docs/AgenticTechStack/README.md` | Extended | Added Hermes Agent reference in Agent Ecosystem section |
| `mkdocs.yml` | Extended | Added Section 5.5 navigation entry |

---

## [2026-05-17] ingest | Thoughtworks Technology Radar Vol. 34 (Apr 2026) — Agentic AI focus | sections touched: AgenticTechStack/thoughtworks-radar-vol34 (new), AgenticTechStack/README, AgenticFrameworks/solutions, Observability/tech-radar, mkdocs.yml

**Source**: PDF upload — https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/04/tr_technology_radar_vol_34_en.pdf
**Type**: Industry technology radar (118 blips, April 2026, Thoughtworks Technology Advisory Board)
**Scope**: Agentic AI, LLM tools, coding agents, context engineering, evaluation, observability, security, harness engineering

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgenticTechStack/thoughtworks-radar-vol34.md` | **New page** | Comprehensive digest of all agentic AI entries from the radar; organised by quadrant/ring with full descriptions, radar movement table, and key themes |
| `docs/AgenticTechStack/README.md` | Extended | Added reference link to new radar page |
| `docs/AgenticFrameworks/solutions.md` | Updated | LangGraph: Adopt→Trial (per Vol.34); PydanticAI: Assess→Adopt (per Vol.34); updated radar chart positions, summary table, selection guide, and references |
| `docs/Observability/tech-radar.md` | Extended | Added SigNoz (Trial); updated Langfuse entry noting v3 architecture + OTel-native SDKs; added radar chart entries |
| `mkdocs.yml` | Extended | Added Section 5.1.1 entry for new Thoughtworks Radar page |

### Key Radar Signals (Agentic AI)

- **New Adopt**: Context engineering, Structured output from LLMs (both Techniques); Instructor, Pydantic AI (L&F); Claude Code, Cursor (Tools)
- **Notable move — Adopt→Trial**: LangGraph (graph architecture not always the right fit; simpler agent patterns now viable)
- **Notable move — Trial→Adopt**: Context engineering (now foundational, not just optimization)
- **New cautions**: Agent instruction bloat, Coding agent swarms, Ignoring durability in agent workflows, MCP by default
- **Key new techniques**: Agent Skills, Feedback sensors for coding agents, Progressive context disclosure, Sandboxed execution

---

## [2026-05-17] ingest | A Practical Guide to Building Agents (OpenAI) | sections touched: DesignPatterns/openai-patterns, Concepts/agent-definition, ProductionBestPractices/security, AllThingsOpenAI/README

**Source**: PDF upload — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
**Type**: Vendor guide / whitepaper (33 pages)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/DesignPatterns/openai-patterns.md` | Major update | Rewrote with richer detail from PDF: use-case selection criteria, tool type table with examples, model selection steps, manager vs. decentralized pattern descriptions, guardrail type table, HITL trigger table; fixed reference URL |
| `docs/Concepts/agent-definition.md` | Extended | Added OpenAI's production-oriented agent definition with two core characteristics; clarified what is NOT an agent |
| `docs/ProductionBestPractices/security.md` | Extended | Added tool risk-rating row to best practices table (OpenAI tool safeguards pattern) |
| `docs/AllThingsOpenAI/README.md` | Extended | Added hub row for the Practical Guide to Building Agents |

### Summary

OpenAI's guide provides a practitioner-level framework for building production agents. Key additions to the wiki: a concrete "when to build an agent" checklist (complex decisions, brittle rules, unstructured data), a three-tier tool taxonomy (data/action/orchestration), a step-by-step model selection approach (baseline → accuracy → cost/latency), detailed manager vs. decentralized multi-agent patterns, a seven-type guardrail taxonomy with optimistic execution semantics, and HITL trigger criteria (failure thresholds and high-risk actions).

---

## [2026-05-10] ingest | agenttrace GitHub repository | sections touched: Observability/solutions, Observability/Readme, ProductionBestPractices/observability

**Source**: URL fetch — https://github.com/luoyuctl/agenttrace
**Type**: Open-source observability tool repository
**Processed by**: OpenAI Codex

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Observability/solutions.md` | Extended | Added agenttrace as a local-first AI coding-agent trace analysis option with cost, latency, health, and CI regression coverage |
| `docs/Observability/Readme.md` | Extended | Added agenttrace to specialized observability platforms and the platform comparison table |
| `docs/ProductionBestPractices/observability.md` | Extended | Added local coding-agent trace review as a production practice and tooling row |

### Summary

agenttrace covers the local developer workflow that hosted observability platforms do not always capture: post-run inspection of AI coding-agent session logs across cost, token usage, latency, tool failures, and session health. The update positions it as complementary to production tracing platforms rather than a replacement for real-time monitoring.

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

## [2026-05-10] ingest | The Anatomy of an Agent Harness — LangChain | sections touched: AgentHarness/agent-harness

**Source**: URL fetch — https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
**Type**: Blog post (LangChain, March 10, 2026)
**Author**: Vivek Trivedy
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/agent-harness.md` | Created | Full page: Agent = Model + Harness definition, five core components, why each exists (filesystem, bash, sandbox, memory, hooks), orchestration for long-horizon work, model–harness co-evolution loop |

### Summary

LangChain's foundational definition of the agent harness concept. Key contribution: the clean Agent = Model + Harness equation and the method of deriving harness components by working backwards from model limitations. Introduced the Ralph Loop pattern, skills/progressive disclosure for context rot prevention, and the observation that harness optimization for a specific task can outperform the model's native post-training harness.

---

## [2026-05-10] ingest | Harness Engineering: Leveraging Codex in an Agent-First World — OpenAI | sections touched: AgentHarness/agent-harness, AgentHarness/harness-engineering

**Source**: URL fetch — https://openai.com/index/harness-engineering
**Type**: Engineering blog post (OpenAI, February 11, 2026)
**Author**: Ryan Lopopolo
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/agent-harness.md` | Extended | Added OpenAI reference; OpenAI source informed the long-horizon execution and co-evolution sections |
| `docs/AgentHarness/harness-engineering.md` | Created | Architecture fitness harness section draws heavily on OpenAI's layered domain architecture, custom linters, garbage collection agents, and progressive disclosure patterns |

### Summary

OpenAI's account of building a million-line production codebase with zero manually-written code using Codex. Key contributions: repository-as-system-of-record (AGENTS.md as table of contents, not encyclopedia), agent legibility as the primary design goal, layered domain architecture enforced by custom linters, "golden principles" + recurring garbage collection agents for entropy management, and the Ralph Wiggum Loop for end-to-end autonomous PR delivery. Throughput metric: 3.5 PRs per engineer per day across ~1,500 merged PRs in 5 months.

---

## [2026-05-10] ingest | Harness Engineering for Coding Agent Users — martinfowler.com | sections touched: AgentHarness/harness-engineering

**Source**: URL fetch — https://martinfowler.com/articles/harness-engineering.html
**Type**: Technical article (martinfowler.com, April 2, 2026)
**Author**: Birgitta Böckeler (Thoughtworks Distinguished Engineer)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/harness-engineering.md` | Primary source | Full page built from this article: feedforward/feedback framework, computational vs. inferential controls, steering loop, timing/shift-left, three regulation categories (maintainability/architecture fitness/behaviour), harnessability, ambient affordances, harness templates, Ashby's Law, role of the human, open questions |
| `docs/AgentHarness/agent-harness.md` | Extended | Added Fowler reference to References section |

### Summary

Fowler.com's cybernetics-informed framework for harness engineering. Key contributions not in the LangChain/OpenAI sources: the feedforward/feedback distinction as a design principle; computational vs. inferential control taxonomy; the three regulation categories (maintainability, architecture fitness, behaviour) with explicit acknowledgment that the behaviour harness remains an unsolved problem; harnessability as a first-class codebase property; ambient affordances; harness templates as the evolution of service templates; and Ashby's Law as the theoretical justification for topology-based variety reduction.

## [2026-05-10] ingest | Mastering Multi-Agent Systems eBook.pdf | sections touched: Architecture/multi-agent-system, AgenticFrameworks/README, AgenticFrameworks/mastra, ContextEngineering/challenges, ContextEngineering/strategies, ProductionBestPractices/observability, Observability/solutions, index

**Source**: `raw/Mastering Multi-Agent Systems eBook.pdf`
**Type**: eBook (165 pages, 5 chapters, Galileo, 2026)
**Author**: Pratik Bhavsar (@ptkbhv)
**Publisher**: Galileo (galileo.ai) — Mastering GenAI Series
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Architecture/multi-agent-system.md` | Extended | Seven benefits table, when MAS actually works (3 patterns), coordination cost economics, concrete cost comparison ($0.05 vs $0.40), model evolution challenge + design-for-removal principle, 5-question decision framework, four primary architectures with performance characteristics, architecture selection matrix, framework comparison table for architecture selection |
| `docs/ContextEngineering/challenges.md` | Extended | Memory vs. context distinction (100:1 rule, decision matrix, four context types), empirical evidence for all four failure modes (DeepMind Pokémon agent, Gemini 2.5 team, Berkeley Function-Calling Leaderboard, Microsoft/Salesforce 39% drop), context size thresholds, common anti-patterns table |
| `docs/ContextEngineering/strategies.md` | Extended | Strategy selection by priority table, retrieval efficiency benchmark (40%/50-70%/80% thresholds), phased implementation roadmap (Week 1 / Month 1 / Advanced) |
| `docs/ProductionBestPractices/observability.md` | Extended | Galileo three-level tracking system, production performance benchmarks (Action Completion/Tool Selection Quality/Response Time/Routing Accuracy), continuous improvement cycle table, monitoring routine (daily/weekly/monthly), alert configuration, incident documentation pattern, custom business metrics |
| `docs/Observability/solutions.md` | Extended | Added Galileo platform entry (Graph Engine, Insights Engine, Trace/Graph/Timeline views, Log Stream Insights, custom metrics); added Galileo to platform comparison table |
| `docs/AgenticFrameworks/README.md` | Extended | Updated Agno entry with performance specs (~2μs, ~3.75 KiB); added Mastra entry |
| `docs/AgenticFrameworks/mastra.md` | Created | New page: TypeScript-first framework, graph-based state machines, existing API integration, e-commerce example, comparison table vs LangGraph/CrewAI |
| `docs/index.md` | Updated | Architecture section updated with four architectures; Frameworks section updated with Agno/Mastra; Context Engineering updated with empirical evidence and roadmap; Observability updated with Galileo and production benchmarks |
| `mkdocs.yml` | Updated | Added 4.15 Mastra entry |

### Summary

Galileo's *Mastering Multi-Agent Systems* eBook (165 pages, 5 chapters) provides a practitioner-focused treatment of multi-agent system design. Key new concepts added to the wiki:

**Chapter 1 (Benefits)**: Seven-benefit framework with concrete single-vs-multi-agent comparisons; Gartner's 40% cancellation prediction for 2027; three patterns where MAS actually works (parallelizable, read-heavy, explicit coordination rules).

**Chapter 2 (Failure Modes)**: Coordination cost economics with concrete dollar figures ($0.05 vs $0.40 for customer support); the Model Evolution Challenge (Rich Sutton's Bitter Lesson applied to MAS); design-for-removal principle; 5-question decision framework; framework comparison table (CrewAI/LangGraph/Swarm).

**Chapter 3 (Architectures)**: Four primary architectures with performance characteristics (token efficiency, latency, throughput, context distribution); architecture selection matrix; framework-to-architecture mapping (LangGraph→hierarchical/hybrid, Agno→decentralized high-throughput, Mastra→hybrid web-integrated, CrewAI→centralized, ADK→hierarchical, Strands→AWS production).

**Chapter 4 (Context Engineering)**: Memory vs. context distinction with the 100:1 rule; four context types (instructions/knowledge/tools/history); empirical evidence for all four failure modes with specific team citations; context size thresholds (10K/50K/100K); five anti-patterns; phased implementation roadmap.

**Chapter 5 (LangGraph Production)**: ConnectTel multi-agent architecture (Supervisor + Billing + Technical Support + Plan Advisor); Galileo observability integration via `GalileoAsyncCallback`; three-level tracking; production benchmarks; continuous improvement cycle; custom business metrics pattern.

## [2026-05-12] ingest | Cognitive Architectures for Language Agents (CoALA) — arXiv:2309.02427 | sections touched: AgentMemory/functional-tiers, AgentMemory/README, AgentMemory/ltm-strategies, AgentMemory/short-term, AgentMemory/research-papers, mkdocs.yml

**Source**: URL fetch — https://arxiv.org/abs/2309.02427
**Type**: Research paper (Princeton, 2023)
**Authors**: Sumers et al.
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentMemory/functional-tiers.md` | Rewritten | Replaced three-tier model with CoALA four-type taxonomy: working, semantic, episodic, procedural |
| `docs/AgentMemory/README.md` | Updated | Overview updated to four types; LTM strategies table updated with memory type column; management techniques updated |
| `docs/AgentMemory/ltm-strategies.md` | Updated | Added memory type labels to each strategy; added Procedural Memory Encoding as strategy 7; updated choosing-the-right-strategy table |
| `docs/AgentMemory/short-term.md` | Updated | Renamed to "Working Memory Management"; added CoALA framing in overview |
| `docs/AgentMemory/research-papers.md` | Updated | Expanded CoALA entry with definitions of all four memory types |
| `mkdocs.yml` | Updated | Section 9 nav labels updated: "Three Functional Tiers" → "The Four Memory Types", "Short-term Memory" → "Working Memory Management" |

### Summary

CoALA (Sumers et al., Princeton 2023) defines the canonical four-type memory taxonomy for language agents, grounded in cognitive science. The key change from the prior three-tier model: **procedural memory** is now a first-class type alongside semantic and episodic, and **working memory** is the precise term for in-context active state. The four types differ in *what kind of information* they store — not just duration:

- **Working memory**: Active reasoning state at inference time (context window)
- **Semantic memory**: Durable facts and knowledge — preferences, definitions, reference data ("what is true")
- **Episodic memory**: Specific past experiences — prior sessions, task outcomes, event logs ("what happened")
- **Procedural memory**: Behavioral rules, guidelines, learned procedures — how the agent acts ("how to behave")

## [2026-05-12] restructure | Agent Memory vendor consolidation + Technology Radar | sections touched: AgentMemory/solutions, AgentMemory/README, AgentMemory/ltm-strategies, mkdocs.yml

**Source**: Research synthesis — GitHub signals, vendor announcements, adoption data (May 2026)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentMemory/solutions.md` | Created | New consolidated vendor page with Thoughtworks-style Technology Radar (Adopt/Trial/Assess/Caution) |
| `docs/AgentMemory/README.md` | Trimmed | Removed inline vendor profiles and comparison table; replaced with pointer to solutions.md |
| `docs/AgentMemory/ltm-strategies.md` | Trimmed | Replaced full vendor comparison table with condensed quick-reference + pointer to solutions.md |
| `mkdocs.yml` | Updated | Added 9.3 Memory Solutions & Technology Radar; renumbered 9.4–9.6 |

### Radar Placements

| Solution | Ring | Key Signal |
|---|---|---|
| Mem0 | 🟢 Adopt | ~54K stars, $24M Series A, 186M API calls Q3 2025 |
| Graphiti (Zep) | 🟢 Adopt | ~25K stars, bi-temporal KG, Apache 2.0 |
| AWS AgentCore Memory | 🟢 Adopt | GA (AWS Summit NYC 2025), fully managed |
| Letta (MemGPT) | 🔵 Trial | ~21K stars, UC Berkeley research, OS-inspired |
| Vertex AI Memory Bank | 🔵 Trial | GA on GCP, native ADK integration |
| Azure AI Foundry Memory | 🔵 Trial | GA on Azure, enterprise compliance |
| LangMem | 🟡 Assess | ~1.5K stars, only library with procedural memory support |
| AgentFS | 🔴 Caution | ~2.5K stars, alpha, narrow scope (filesystem only) |

---

## [2026-05-17] ingest | Agentic Architectural Patterns for Building Multi-Agent Systems (Arsanjani & Bustos, Packt 2026, ISBN 978-1-80602-957-0) | sections touched: DesignPatterns, MaturityModels, Architecture, ProductionBestPractices/security, ProductionBestPractices/deployment, ProductionBestPractices/testing-evaluations, index, mkdocs.yml

**Source**: Local file — `raw/9781806029570-Multi-Agent-Systems.pdf`
**Type**: Book (Packt Publishing, January 2026)
**Authors**: Dr. Ali Arsanjani (Google Cloud, Director of Applied AI Engineering) and Juan Pablo Bustos (Google)
**Copyright**: © 2026 Packt Publishing. All rights reserved. Summaries used under fair-use/review provisions; no verbatim reproduction of book text in wiki pages.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/DesignPatterns/arsanjani-patterns.md` | Created | New page: full pattern catalog — Multi-Agent Coordination (Agent Router, Supervisor Architecture, Swarm Architecture, Blackboard Knowledge Hub, Contract-Net, Consensus, Negotiation, Conflict Resolution, Formation Control, Resource Allocation, Knowledge Sharing, Tool Routing); Explainability & Compliance (Instruction Fidelity Auditing, FCoT Embedding, Persistent Instruction Anchoring, Shared Epistemic Memory); Robustness (Parallel Execution Consensus, Delayed Escalation, Watchdog Timeout, Adaptive Retry, Auto-Healing, Incremental Checkpointing, Majority Voting, Causal Dependency Graph, Trust Decay, Canary Agent Testing, Rate-Limited Invocation, Fallback Model Invocation); Security (Agent Self-Defense, Agent Mesh Defense, Execution Envelope Isolation). Includes maturity-level mapping table. |
| `docs/MaturityModels/arsanjani-genai-maturity.md` | Created | New page: Arsanjani 7-level GenAI Maturity Model (Levels 0–6); Agentic AI Maturity Spectrum (6 sub-levels); agent anatomy (Sense, Reason, Plan, Act, Memory, Coordinate); the new agentic stack (Function Calling, MCP, A2A); production challenges table; practical rollout roadmap |
| `docs/Architecture/components-selection.md` | Extended | Added Agent Anatomy section with 7-component table, hierarchy of autonomy, technical considerations by component; updated See Also and References |
| `docs/Architecture/multi-agent-system.md` | Extended | Added Supervisor vs. Swarm comparison table; Agent Router pattern section; added book to References |
| `docs/ProductionBestPractices/security.md` | Extended | Added 3 new rows to Best Practices table: Agent Mesh Defense, Agent Self-Defense, Execution Envelope Isolation |
| `docs/ProductionBestPractices/deployment.md` | Extended | Added Fault Tolerance and Robustness Patterns section with 7 new rows: Watchdog Timeout, Adaptive Retry with Prompt Mutation, Auto-Healing, Incremental Checkpointing, Rate-Limited Invocation, Fallback Model Invocation, Delayed Escalation |
| `docs/ProductionBestPractices/testing-evaluations.md` | Extended | Added 2 new rows to Best Practices table: Parallel Execution Consensus, Canary Agent Testing |
| `docs/DesignPatterns/Readme.md` | Extended | Added reference entry for new Arsanjani patterns page |
| `docs/MaturityModels/README.md` | Extended | Added resource entry for new Arsanjani maturity page |
| `docs/index.md` | Extended | Updated Architecture and Design Patterns and Maturity Models section bullets |
| `mkdocs.yml` | Updated | Added entry 3.2.2 for arsanjani-patterns.md; added entry 14.7 for arsanjani-genai-maturity.md |

### Summary

This book presents a comprehensive pattern language for enterprise agentic AI. Key contributions to the wiki: (1) 25+ named patterns organized into four functional groups with Context–Problem–Solution–Consequences structure; (2) a 7-level GenAI Maturity Model that maps directly to patterns — maturity is a function of patterns implemented, not intent; (3) the agent anatomy framework (Sense → Reason → Plan → Act with Memory and Coordinate); (4) the three-layer agentic stack (Function Calling → MCP → A2A); (5) Supervisor vs. Swarm as the primary architectural choice axis for multi-agent systems; (6) explainability patterns (FCoT, Persistent Instruction Anchoring, Shared Epistemic Memory) addressing instruction drift in deep agent hierarchies; (7) a five-level robustness maturity spectrum with concrete fault-tolerance patterns for production deployments.

## [2026-05-17] ingest | The 8 Levels of Agentic Engineering — Bassim Eledath | sections touched: Concepts/agentic-engineering-levels, AgentHarness/harness-engineering, index, mkdocs.yml

**Source**: URL fetch — https://www.bassimeledath.com/blog/levels-of-agentic-engineering
**Type**: Blog post (March 2026)
**Author**: Bassim Eledath
**Processed by**: Claude Code (claude-sonnet-4-6)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Concepts/agentic-engineering-levels.md` | Created | New page: 8-level practitioner progression framework from tab complete to autonomous agent teams; compounding engineering loop; harness engineering as Level 6; Level 7 as current sweet spot |
| `docs/AgentHarness/harness-engineering.md` | Extended | Added See Also link pointing to the new levels page with context that harness engineering = Level 6 |
| `docs/index.md` | Extended | Added bullet for The 8 Levels of Agentic Engineering under Concepts section |
| `mkdocs.yml` | Updated | Added entry 1.7 for the new page; renumbered References to 1.8 |

### Summary

Bassim Eledath's 8-level framework is a practitioner-oriented progression model for teams adopting agentic AI in software engineering. Key contributions: the plan-delegate-assess-codify compounding loop (Level 4); context engineering as a prerequisite discipline (Level 3); the "levels 3–5 must be solid before levels 6–8" architectural constraint; harness engineering and automated feedback loops as the Level 6 inflection point; background agents (hub-and-spoke orchestration, cloud sandboxed VMs) as the current sweet spot for most teams (Level 7); and autonomous agent teams (Level 8) as an experimental frontier with unresolved coordination economics.

## [2026-05-18] ingest | AI Coding Agents (pi.dev, opencode.ai, thenewstack.io/claude-code-source-leak, goose-docs.ai, cline.bot, code.claude.com, chatgpt.com/codex, github.com/google-gemini/gemini-cli, devin.ai, kiro.dev) | sections touched: AgenticFrameworks, AllThingsAnthropic, AllThingsOpenAI, AllThingsGoogle, AllThingsAWS

## [2026-05-18] ingest | AI Coding Agents additions (factory.ai, warp.dev, IBM Bob) | sections touched: AgenticFrameworks

## [2026-05-20] ingest | Best Enterprise Level Agentic AI Platforms for 2026 (MarkTechPost) | sections touched: AgentPlatforms/enterprise-platforms-2026 (new), AllThingsMicrosoft/README, AllThingsGoogle/README, index.md, mkdocs.yml

**Source**: https://www.marktechpost.com/2026/05/19/best-enterprise-level-agentic-ai-platforms-for-2026/
**Type**: Vendor/platform comparison guide (May 2026, MarkTechPost)
**Note**: Direct URL returned HTTP 403; content extracted via WebSearch and supplementary searches across platform documentation and analyst sources.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentPlatforms/enterprise-platforms-2026.md` | Created | New page covering all 10 platforms ranked by production readiness: Salesforce Agentforce, Microsoft Copilot Studio, ServiceNow, Google Gemini Enterprise, LangGraph, Kore.ai, UiPath Maestro, Azure AI Foundry Agent Service, IBM watsonx Orchestrate, CrewAI Enterprise — with pricing, adoption data, strengths, limitations, and a use-case selection guide |
| `docs/AllThingsMicrosoft/README.md` | Extended | Added hub rows for Azure AI Foundry Agent Service and Microsoft Copilot Studio with backlinks |
| `docs/AllThingsGoogle/README.md` | Extended | Added hub row for Gemini Enterprise platform comparison with backlink |
| `docs/index.md` | Extended | Updated section 5 bullet to mention the new enterprise platform comparison |
| `mkdocs.yml` | Extended | Added 5.2.5 Enterprise Agentic AI Platforms (2026) nav entry |

## [2026-05-21] ingest | Microsoft Agent Governance Toolkit (GitHub) | sections touched: SecurityFrameworks/agent-governance-toolkit (new), SecurityFrameworks/Readme, ProductionBestPractices/security, AIGovernance/governance-solutions, AllThingsMicrosoft/README, index.md, mkdocs.yml

**Source**: https://github.com/microsoft/agent-governance-toolkit
**Type**: Open-source governance toolkit (Microsoft, MIT license, public preview, v3.7.0)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/SecurityFrameworks/agent-governance-toolkit.md` | Created | New page covering policy engine (YAML/OPA/Cedar, 0.012ms p50), zero-trust identity (Ed25519 + ML-DSA-65, SPIFFE/SVID), four execution rings, MCP Security Gateway, Agent SRE (circuit breakers, replay debugging, OpenTelemetry), audit/compliance (Merkle chains, EU AI Act/SOC2/HIPAA/GDPR), OWASP Agentic Top 10 full coverage, 992 conformance tests across 10 specs, 20+ framework adapters |
| `docs/SecurityFrameworks/Readme.md` | Extended | Added Microsoft Perspective section with AGT capability summary and updated See Also links |
| `docs/ProductionBestPractices/security.md` | Extended | Added AGT row to Security Frameworks Reference table; added 3 new Best Practices rows: deterministic policy enforcement, trust ceiling propagation, MCP tool tampering mitigation |
| `docs/AIGovernance/governance-solutions.md` | Extended | Added AGT row to Microsoft Azure vendor-native governance table |
| `docs/AllThingsMicrosoft/README.md` | Extended | Added hub row for Agent Governance Toolkit with backlink |
| `docs/index.md` | Extended | Updated Agent Security bullet to include Microsoft Perspective / AGT |
| `mkdocs.yml` | Extended | Added 11.4 Microsoft Perspective → 11.4.1 Agent Governance Toolkit nav entry |

## [2026-05-22] ingest | Memory and dreaming for self-learning agents (YouTube — Anthropic) | sections touched: AgentPlatforms/claude-managed-agents (new), AllThingsAnthropic/README, AgentMemory/ltm-strategies, ReferenceArchitecture/self-learning-agents, ProductionBestPractices/state-memory, mkdocs.yml

**Source**: https://youtu.be/RtywqDFBYnQ
**Type**: YouTube video — Anthropic product announcement, May 2026

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentPlatforms/claude-managed-agents.md` | Created | New page covering Claude Managed Agents platform: Memory (filesystem-based, public beta), Dreaming (scheduled memory consolidation inspired by hippocampal sleep, research preview), Outcomes (self-grading rubric loop with isolated grader, +10pp task success, 6× Harvey result), Multiagent Orchestration (parallel specialists on shared FS, public beta) |
| `docs/AllThingsAnthropic/README.md` | Extended | Added 4 new hub rows: Claude Managed Agents platform, Dreaming, Outcomes, Multiagent Orchestration; updated See Also |
| `docs/AgentMemory/ltm-strategies.md` | Extended | Added Strategy 6: Dreaming as a productized Reflection/Consolidation pattern; added Claude Managed Agents to LTM solutions table; updated See Also |
| `docs/ReferenceArchitecture/self-learning-agents.md` | Extended | Added Anthropic Dreaming vs Agent0 comparison table; added Dreaming Loop description; added See Also section |
| `docs/ProductionBestPractices/state-memory.md` | Extended | Added 2 new best practice rows (self-improvement without retraining, self-evaluation via Outcomes); added Claude Managed Agents to solutions table; updated See Also |
| `mkdocs.yml` | Extended | Added 5.2.6 Claude Managed Agents (Anthropic) nav entry |

## [2026-05-24] ingest | You.com | 2026 AI Predictions Whitepaper | sections touched: Concepts/ai-predictions-2026 (new), Concepts/agent-definition, AgentOps/genops, index.md, mkdocs.yml

**Source**: https://you.com/resources/2026-ai-predictions
**Type**: Industry whitepaper — You.com co-founders Richard Socher and Bryan McCann, 35 predictions for 2026

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Concepts/ai-predictions-2026.md` | Created | New page covering all major prediction themes: Chat-Engine vs Do-Engine framing, workforce transformation, reward engineering as emerging profession, 10-person unicorns, software development transformation, industry-specific vertical agents, search infrastructure value, space computing, biotech/biology engineering, consumer/media (AI music, short-form video, AI-targeted marketing), investment dynamics |
| `docs/Concepts/agent-definition.md` | Extended | Added Chat-Engine vs Do-Engine section with You.com framing; added See Also link to predictions page |
| `docs/AgentOps/genops.md` | Extended | Added Reward Engineering section covering role definition, key challenges table (specification completeness, reward hacking, multi-objective balancing, reward drift, evaluation coverage); updated Future Directions and See Also |
| `docs/index.md` | Extended | Updated Section 3 (Concepts) bullets to include Chat-Engine/Do-Engine note and new predictions page summary |
| `mkdocs.yml` | Extended | Added 1.8 2026 AI Predictions (You.com) nav entry |

## [2026-05-24] ingest | OpenHuman (TinyHumans AI) — https://tinyhumans.ai/openhuman | sections touched: AgentPlatforms

| File | Action | Notes |
|---|---|---|
| `docs/AgentPlatforms/openhuman.md` | Created | New page: overview, NeoCortex memory (1B tokens, 4k tokens/sec, SQLite + Obsidian vault), 118+ OAuth integrations via Composio, TokenJuice compression (up to 80% reduction), automatic model routing (200+ models), agent toolbelt (web search, coding, voice, Google Meet mascot), architecture (Rust + Tauri + TypeScript), installation, privacy/data model, security considerations (toxic flow trifecta, curl-pipe risk, managed backend trust), full comparison table vs OpenClaw and Hermes, suitable for / limitations, see also, references |
| `docs/AgentPlatforms/README.md` | Extended | Added OpenHuman one-liner to Personal AI Agents list; added to See Also |
| `docs/AgentPlatforms/hermes-agent.md` | Extended | Added See Also backlink to openhuman.md |
| `docs/AgentPlatforms/openclaw.md` | Extended | Added See Also backlink to openhuman.md |
| `mkdocs.yml` | Extended | Added 5.7 OpenHuman (TinyHumans AI) nav entry |

## [2026-05-26] ingest | https://github.com/anthropic-experimental/sandbox-runtime | sections touched: SecurityFrameworks, ProductionBestPractices/security, AllThingsAnthropic, Standards/mcp, mkdocs.yml

## [2026-05-27] ingest | E2B, Daytona, Modal, Firecracker, gVisor, Kata Containers, nsjail (web research) | sections touched: SecurityFrameworks/agent-sandboxing.md (new), SecurityFrameworks/Readme.md, SecurityFrameworks/anthropic-sandbox-runtime.md, mkdocs.yml

## [2026-05-28] ingest | Meta-Harness: End-to-End Optimization of Model Harnesses (arXiv:2603.28052, Lee et al., March 2026) | sections touched: AgentHarness/harness-optimization.md (new), AgentHarness/agent-harness.md, AgentHarness/harness-engineering.md, Benchmarks/agent-benchmarks.md, ContextEngineering/strategies.md, ProductionBestPractices/context-engineering.md, docs/index.md, mkdocs.yml

## [2026-05-29] update | Benchmark additions: OSWorld-Verified, SWE-bench Pro, Terminal-Bench 2.1, Finance Agent v2, Humanity's Last Exam | sections touched: Benchmarks/agent-benchmarks.md, Benchmarks/llm-benchmarks.md

## [2026-05-29] ingest | Agent Harness Engineering: A Survey — https://picrew.github.io/LLM-Harness/ (OpenReview/TMLR, 2026) | sections touched: AgentHarness/llm-harness-survey.md (new), AgentHarness/agent-harness.md, AgentHarness/harness-engineering.md, docs/index.md, mkdocs.yml

## [2026-05-29] ingest | https://flueframework.com/ | sections touched: AgenticFrameworks/flue.md (new), AgenticFrameworks/README.md, AgentHarness/agent-harness.md, mkdocs.yml

## [2026-05-30] ingest | ALE-Bench (Sakana AI) — https://sakanaai.github.io/ALE-Bench-Leaderboard/ | sections touched: Benchmarks/agent-benchmarks.md

## [2026-05-30] ingest | agents-best-practices — https://github.com/DenisSergeevitch/agents-best-practices | sections touched: AgentHarness/agent-harness.md, AgentHarness/harness-engineering.md, ProductionBestPractices/security.md, ProductionBestPractices/observability.md, ProductionBestPractices/testing-evaluations.md, ProductionBestPractices/context-engineering.md, ProductionBestPractices/deployment.md

## [2026-05-31] ingest | cisco-ai-defense/skill-scanner + nvidia/skillspector | sections touched: SecurityFrameworks/skill-scanners.md (new), SecurityFrameworks/Readme.md, ProductionBestPractices/security.md, Standards/skills.md, mkdocs.yml

## [2026-05-31] reference | Provider Skills Repositories (Anthropic, Google, Microsoft, OpenAI, AWS, Cloudflare, Vercel) | sections touched: Standards/skills.md, AllThingsAnthropic/README.md, AllThingsGoogle/README.md, AllThingsMicrosoft/README.md, AllThingsOpenAI/README.md, AllThingsAWS/README.md

**Sources**: https://github.com/anthropics/skills, https://github.com/google/skills, https://github.com/microsoft/azure-skills, https://github.com/openai/skills, npx skills add aws/agent-toolkit-for-aws/skills, https://github.com/cloudflare/skills, https://github.com/vercel-labs/skills

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/skills.md` | Extended | Added "Provider Skills Repositories" section with 7-provider comparison table and install guidance |
| `docs/AllThingsAnthropic/README.md` | Extended | Added hub row for Anthropic Skills Repository |
| `docs/AllThingsGoogle/README.md` | Extended | Added hub row for Google Skills Repository |
| `docs/AllThingsMicrosoft/README.md` | Extended | Added hub row for Azure Skills Repository |
| `docs/AllThingsOpenAI/README.md` | Extended | Added hub row for OpenAI Skills Repository |
| `docs/AllThingsAWS/README.md` | Extended | Added hub row for AWS Skills Registry |

## [2026-06-01] ingest | Hyperagent (https://www.hyperagent.com/) | sections touched: AgentPlatforms/saas-platforms.md

## [2026-06-01] ingest | SkillOpt: Executive Strategy for Self-Evolving Agent Skills (microsoft.github.io/SkillOpt, arXiv:2605.23904) | sections touched: PromptEngineering/skillopt.md (new), AllThingsMicrosoft/README.md, Standards/skills.md, mkdocs.yml

**Source**: https://microsoft.github.io/SkillOpt/ (+ https://arxiv.org/abs/2605.23904, https://github.com/microsoft/SkillOpt)
**Type**: Research paper + open-source tool (Microsoft + Chinese universities, May 2026, MIT license)
**Authors**: Yifan Yang et al.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/PromptEngineering/skillopt.md` | Created | Full coverage: text-space optimizer concept, training loop with weight-space analogies table, training hyperparameters, architecture diagram, benchmark results (52/52 wins, +23.5 pts GPT-5.5 direct chat), suitable for / limitations, relation to SKILLS.md convention, best practices table, See Also, References |
| `docs/AllThingsMicrosoft/README.md` | Extended | Added hub row for SkillOpt with backlink |
| `docs/Standards/skills.md` | Extended | Added bidirectional See Also link to skillopt.md |
| `mkdocs.yml` | Extended | Added 8.4.1 SkillOpt (Microsoft) nav entry under Prompt Engineering |

## [2026-06-01] ingest | pi.dev — Pi Coding Agent Harness | sections touched: AgentHarness, AgenticFrameworks

## [2026-06-02] ingest | https://xiaowu0162.github.io/long-mem-eval/ — LongMemEval benchmark (ICLR 2025) and LongMemEval-V2 (May 2026) | sections touched: Benchmarks, AgentMemory

## [2026-06-14] ingest | Open Knowledge Format (OKF) v0.1 — Google Cloud | sections touched: Standards/open-knowledge-format.md (new), AllThingsGoogle/README.md, mkdocs.yml, index.md, Standards/agents-md.md, Standards/skills.md, ContextEngineering/strategies.md, AgentMemory/README.md

**Source**: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing

**Type**: Vendor blog post / open specification announcement (Google Cloud Data Analytics, BI, and Database teams; authors Sam McVeety and Amir Hormati; OKF v0.1, June 12, 2026)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/open-knowledge-format.md` | Created | Overview, architecture (markdown + YAML frontmatter bundles), design principles, key features, use cases, reference implementations (Enrichment Agent, Static HTML Visualizer, sample bundles), suitable for / limitations, relation to AGENTS.md/SKILLS.md/Context Engineering/AgentMemory, best practices table, See Also, References |
| `docs/AllThingsGoogle/README.md` | Extended | Added hub row for Open Knowledge Format (OKF) |
| `mkdocs.yml` | Extended | Added 6.9 Open Knowledge Format (OKF) nav entry under Industry Standards |
| `docs/index.md` | Extended | Added OKF bullet to section 7 (Agentic AI Industry Standards) |
| `docs/Standards/agents-md.md` | Extended | Added bidirectional See Also link to open-knowledge-format.md |
| `docs/Standards/skills.md` | Extended | Added bidirectional See Also link to open-knowledge-format.md |
| `docs/ContextEngineering/strategies.md` | Extended | Added See Also link to open-knowledge-format.md (Offload/Write pattern) |
| `docs/AgentMemory/README.md` | Extended | Added See Also link to open-knowledge-format.md (semantic memory storage format) |

## [2026-06-14] ingest | https://deepresearch-bench.github.io/ — DeepResearch Bench (DRB) | sections touched: Benchmarks, ProductionBestPractices, index

**Source**: https://deepresearch-bench.github.io/ (project site returned HTTP 403; content sourced from the linked GitHub repo README at github.com/Ayanami0730/deep_research_bench, arXiv 2506.11763, and Hugging Face paper page)

**Type**: Academic benchmark project page / GitHub repository (USTC Agent Research Lab; Du, Xu, Zhu, Wang, Mao)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Benchmarks/agent-benchmarks.md` | Extended | Added DeepResearch Bench entry under Research and Retrieval Benchmarks (100 PhD-level tasks, 22 domains, RACE/FACT evaluation frameworks, evaluator migration to GPT-5.5/GPT-5.4-mini in May 2026, DRB II follow-up); added row to Benchmark Selection Guide table |
| `docs/ProductionBestPractices/testing-evaluations.md` | Extended | Added DeepResearch Bench row to Agent Benchmarks Reference table |

## [2026-06-17] ingest | https://addyosmani.com/blog/loop-engineering/ — Loop Engineering | sections touched: AgentHarness (new), WorkflowBuilders, AgenticFrameworks, AllThingsAnthropic, AllThingsOpenAI, ProductionBestPractices, index

**Source**: https://addyosmani.com/blog/loop-engineering/ (host blocked by this session's network egress allowlist; full article text supplied directly by the user)

**Type**: Blog post (Addy Osmani)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/loop-engineering.md` | New | Five-plus-one primitive framework (automations, worktrees, skills, connectors, sub-agents, state); Codex app vs. Claude Code mapping table; `/loop` vs `/goal`; composed example loop; unresolved risks (verification, comprehension rot, cognitive surrender) |
| `mkdocs.yml` | Extended | Added 2.8 Loop Engineering under Agent Harness section |
| `docs/AgentHarness/harness-engineering.md` | Extended | Added bidirectional See Also link to Loop Engineering |
| `docs/AgentHarness/agent-harness.md` | Extended | Added bidirectional See Also link to Loop Engineering |
| `docs/WorkflowBuilders/claude-orchestration-guide.md` | Extended | Added See Also link to Loop Engineering |
| `docs/AgenticFrameworks/ai-coding-agents.md` | Extended | Added `/loop`/`/goal` and Automations tab/Triage inbox details to Claude Code and Codex sections; See Also link |
| `docs/AllThingsAnthropic/README.md` | Extended | Added Loop Engineering (Claude Code) hub row |
| `docs/AllThingsOpenAI/README.md` | Extended | Added Loop Engineering (Codex app) hub row |
| `docs/ProductionBestPractices/deployment.md` | Extended | Added best-practice row on verifying self-feeding loops; See Also link |
| `docs/ProductionBestPractices/state-memory.md` | Extended | Added best-practice row on externalizing loop state between scheduled runs; See Also link |
| `docs/index.md` | Extended | Added Loop Engineering bullet under Agent Harness section |
| `docs/index.md` | Extended | Added DeepResearch Bench to Agent Benchmarks bullet under Agent Testing & Evaluations |

## [2026-06-17] ingest | A Guide to Event-Driven Design for Agents and Multi-Agent Systems (Confluent) | sections touched: DesignPatterns, Architecture, ProductionBestPractices, WorkflowBuilders, index, mkdocs

**Source**: Local PDF — *A Guide to Event-Driven Design for Agents and Multi-Agent Systems* by Sean Falconer, AI Entrepreneur in Residence, Confluent (ebook, © 2025 Confluent, Inc.)

**Type**: Vendor ebook / whitepaper (Confluent)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/DesignPatterns/event-driven-patterns.md` | Created | Confluent's nine-component agent anatomy; Orchestrator-Worker, Hierarchical, Blackboard, and Market-Based patterns in Traditional vs. Event-Driven form (Kafka partitioning, consumer groups, Rebalance Protocol, offset replay); event sourcing for state consistency; Stream/Connect/Process/Govern data streaming platform pillars; SDR and Agentic RAG worked examples; Reworkd/Airy/Agent Taskflow case studies; best practices table |
| `docs/DesignPatterns/Readme.md` | Extended | Added backlink row to event-driven-patterns.md |
| `docs/Architecture/multi-agent-system.md` | Extended | Added "Event-Driven Realizations of Multi-Agent Patterns (Confluent)" section mapping Kafka mechanics onto the four primary architectures plus the new Market-Based pattern; added bidirectional See Also link |
| `docs/Architecture/components-selection.md` | Extended | Added "Complementary Framing: Confluent's Nine-Component Anatomy" subsection under Agent Anatomy (Persona, Learning, Tool Interface vs. Arsanjani's 7-component table); added See Also/References entries |
| `docs/ProductionBestPractices/state-memory.md` | Extended | Added "Event Sourcing for Multi-Agent State Consistency (Confluent Pattern)" section; added See Also links |
| `docs/ProductionBestPractices/security.md` | Extended | Added Best Practices row for field-level encryption, Stream Governance, and GDPR-aligned retention in event-driven pipelines; added See Also/References entries |
| `docs/ProductionBestPractices/deployment.md` | Extended | Added Fault Tolerance table row for idempotent processing and dead-letter queues; added See Also/References entries |
| `docs/WorkflowBuilders/orchestration.md` | Extended | Added "Confluent Data Streaming Platform (Apache Kafka & Apache Flink)" subsection (Stream/Connect/Process/Govern, agentic patterns table, deployment options, best practices, considerations), following the existing Temporal subsection precedent; added comparison table row, See Also link, and References section |
| `mkdocs.yml` | Extended | Added 3.2.3 Event-Driven Design Patterns (Confluent) nav entry under Agentic Design Pattern Selection |
| `docs/index.md` | Extended | Updated Design Pattern Selection and Multi-agent Systems bullets (section 4) and Workflow Engines bullet (section 6) to reference Confluent's event-driven patterns |

## [2026-06-17] ingest | Agentic AI Red Teaming Guide (Cloud Security Alliance) | sections touched: SecurityFrameworks, Standards, ProductionBestPractices, EvaluationFrameworks, index, mkdocs

**Source**: https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide (PDF fetched via expiring signed S3 URL; canonical citation URL used per user instruction; text extracted locally with pdfminer.six after WebFetch native PDF parsing and pypdf both failed)

**Type**: Industry whitepaper / testing guide (Cloud Security Alliance, AI Organizational Responsibilities Working Group, Aug 2025)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/SecurityFrameworks/agentic-ai-red-teaming-guide.md` | Created | Full 12-category threat taxonomy (Agent Authorization and Control Hijacking through Agent Untraceability) with representative actionable test steps; four-phase testing methodology (Preparation/Execution/Analysis/Reporting) and effectiveness metrics; MAESTRO threat-modeling framework summary; red teaming tooling landscape table (AgentDojo, Agent-SafetyBench, AgentFence, SplxAI Agentic Radar, ASB, Promptfoo LLM Security DB, Pentest Copilot, Azure AI Red Teaming Agent, FuzzAI); Future Outlook bullets; general red-teaming background note citing IBM (https://www.ibm.com/think/topics/red-teaming) |
| `docs/Standards/csa.md` | Created | Introduces Cloud Security Alliance as an industry standards body — Red Teaming Guide, MAESTRO, AI Organizational Responsibilities artifact; comparison table vs. NIST AI RMF, Google SAIF, AAIF |
| `mkdocs.yml` | Extended | Added 6.10 Cloud Security Alliance (CSA) under Industry Standards; added 11.8 Agentic AI Red Teaming Guide (CSA) under Agentic AI Security |
| `docs/SecurityFrameworks/Readme.md` | Extended | Added "CSA Perspective" section (Agentic AI Red Teaming Guide summary); added See Also entries for the new guide page and Standards/csa.md |
| `docs/ProductionBestPractices/testing-evaluations.md` | Extended | Added "Agentic AI Red Teaming (CSA)" section with threat-category table and methodology mapping to launch gates; added See Also/References entries |
| `docs/ProductionBestPractices/security.md` | Extended | Added Red Teaming Guide row to Security Frameworks Reference table; added See Also/References entries |
| `docs/EvaluationFrameworks/Readme.md` | Extended | Added "Red Teaming / Adversarial Testing" section (AgentDojo, Agent-SafetyBench, ASB, SplxAI Agentic Radar, Promptfoo LLM Security DB, Azure AI Red Teaming Agent); added See Also entries |
| `docs/index.md` | Extended | Added CSA bullet under Industry Standards (section 7); added CSA Perspective bullet under Agent Security (Production Best Practices) |

## [2026-06-21] ingest | Agent Client Protocol (agentclientprotocol.com) | sections touched: Standards, AgenticFrameworks, AllThingsAnthropic, AllThingsGoogle, index, mkdocs

**Source**: https://agentclientprotocol.com/ (site returned HTTP 403 to direct WebFetch; canonical citation URL used per user instruction; content reconstructed from the project's GitHub repository (github.com/zed-industries/agent-client-protocol) and corroborating secondary sources via WebSearch/WebFetch)

**Type**: Industry standard / protocol specification (Zed Industries, August 2025)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/agent-client-protocol.md` | Created | JSON-RPC 2.0 over stdio transport; Client/Agent roles; session lifecycle (initialize, session/new, session/load, session/prompt, session/update); tool-call categories and permission requests; fs/* and terminal/* client capabilities; comparison table vs. MCP; SDK list (TS/Python/Rust/Kotlin/Java); native vs. adapter-based agent support (Gemini CLI, Claude Code, Codex CLI, etc.); JetBrains/Zed ACP Agent Registry |
| `docs/Standards/mcp.md` | Extended | Added See Also link to the new ACP page |
| `docs/Standards/agent2agent.md` | Extended | Added See Also link to the new ACP page |
| `docs/AgenticFrameworks/ai-coding-agents.md` | Extended | Added See Also link to ACP page |
| `docs/AllThingsAnthropic/README.md` | Extended | Added hub row noting Claude Code's ACP adapter |
| `docs/AllThingsGoogle/README.md` | Extended | Added hub row noting Gemini CLI's native ACP integration |
| `docs/index.md` | Extended | Added ACP bullet under Industry Standards (section 7) |
| `mkdocs.yml` | Extended | Added 6.11 Agent Client Protocol (ACP) under Industry Standards |

## [2026-06-22] ingest | NVIDIA/skills (github.com/NVIDIA/skills) | sections touched: Standards/skills.md

**Source**: https://github.com/NVIDIA/skills

**Type**: Provider skills repository (NVIDIA)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/skills.md` | Extended | Added NVIDIA row to the "Provider Skills Repositories" table — catalog of ~200+ NVIDIA-verified, product-prefixed skills (cuopt-, nemo-, tao-, etc.), each with SKILL.md, skill-card.md, and an OMS-format cryptographic signature for supply-chain verification; dual Apache-2.0/CC-BY-4.0 licensing; installable via `npx skills` CLI. Added matching reference link. No new page created per task instruction. |

## [2026-06-22] ingest | Kagent / kagent.dev, Agentic Ops Framework (AOF), KAOS | sections touched: AgentOps, Standards, AllThingsGoogle, index.md, mkdocs.yml

**Sources**:
- https://kagent.dev/ (WebFetch blocked 403; supplemented via WebSearch + https://github.com/kagent-dev/kagent)
- https://aof.sh/ (WebFetch blocked 403; supplemented via WebSearch + https://github.com/agenticdevops/aof)
- https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html (WebFetch blocked 403; content reconstructed via WebSearch)

**Note on KAOS naming**: the task description paired "KAOS (K8s Agent Orchestration System)" with the Google Open Source Blog URL above. Research found the Google blog actually announces a distinctly-named Kubernetes SIG Apps subproject called "Agent Sandbox" (Sandbox/SandboxTemplate/SandboxClaim CRDs) — it does not use the term "KAOS". A separate, unrelated independent OSS project (`github.com/axsaucedo/kaos`) is literally named "K8s Agent Orchestration System" (KAOS). Both were documented as distinct projects, with an explicit cross-reference note flagging the naming overlap, rather than conflating them.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentOps/kagent.md` | Created | CNCF Sandbox project (Solo.io); architecture (Controller/Engine/UI/CLI), CRDs (Agent, ModelConfig, ToolServers), MCP/A2A composition, multi-provider LLM support, OTel tracing, 100-days community milestone |
| `docs/AgentOps/agentic-ops-framework.md` | Created | Rust-based, kubectl-style CLI (`aofctl`) and YAML spec; Agent/AgentFleet/AgentFlow resources; integrations (Slack, PagerDuty, GitHub, MCP); human-in-the-loop approval gates; Beta status |
| `docs/AgentOps/kaos.md` | Created | Independent OSS project (`axsaucedo/kaos`); Go control plane + Python data plane (PAIS/Pydantic AI) + React UI; OpenAI-compatible per-agent endpoints; A2A discovery; explicit naming-overlap note vs. Google's Agent Sandbox |
| `docs/Standards/k8s-agent-sandbox.md` | Created | Google/Kubernetes SIG Apps "Agent Sandbox" subproject from the Google Open Source Blog; Sandbox/SandboxTemplate/SandboxClaim CRDs; WarmPools; KubeCon Atlanta Nov 2025 launch; explicit naming-overlap note vs. community KAOS project |
| `docs/AgentOps/README.md` | Extended | Added "Kubernetes-Native Agent Orchestration" subsection with a comparison table (kagent/AOF/KAOS) and a pointer to the separate Agent Sandbox standard; extended See Also |
| `docs/AllThingsGoogle/README.md` | Extended | Added hub row for Kubernetes Agent Sandbox |
| `docs/index.md` | Extended | Added Standards bullet for Kubernetes Agent Sandbox; extended Deployment bullet under Production Best Practices with Kubernetes-native agent orchestration tools |
| `mkdocs.yml` | Extended | Added 6.12 Kubernetes Agent Sandbox under Industry Standards; added 13.3 Kubernetes-Native Agent Orchestration (kagent, AOF, KAOS) under AgentOps |

## [2026-06-27] ingest | ByteChef (bytechef.io) | sections touched: WorkflowBuilders

**Source**: https://www.bytechef.io/

**Type**: Vendor/product page (open source workflow platform)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/WorkflowBuilders/open-source.md` | Extended | Added new "ByteChef" subsection (Apache-2.0, Java/Spring Boot + React) describing its AI-native low-code platform unifying workflow automation, API orchestration, and AI agent integration; added a row to the Comparison Matrix table; replaced the non-standard "Related Sections" footer with a proper "See Also" + "References" section citing the source URL |

## [2026-06-27] ingest | Google Cloud — Multi-tenant agentic AI system architecture | sections touched: Architecture

**Source**: https://docs.cloud.google.com/architecture/multi-tenant-agentic-ai-system

**Type**: Vendor reference architecture (Google Cloud Architecture Center)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Architecture/multi-agent-system.md` | Extended | Added "Multi-Tenant Multi-Agent Systems (Google Cloud)" section covering Cloud Run/GKE compute, Gemini Enterprise Agent Platform, Model Armor, ADK, and A2A; framed as orthogonal to (and composable with) the existing AWS Four Planes and four-architectures content; added a cross-link to Kubernetes Agent Sandbox and a new References entry |

## [2026-06-27] ingest | Eve (vercel/eve) | sections touched: AgenticFrameworks, Standards

**Source**: https://github.com/vercel/eve

**Type**: Framework repository (public preview)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgenticFrameworks/eve.md` | Created | Vercel's filesystem-first agent framework — `instructions.md` defines the agent, tools auto-registered from `tools/`, built-in durable execution, sandboxed compute, approvals, channels, tracing, evals |
| `docs/AgenticFrameworks/flue.md` | Extended | Added bidirectional See Also link to Eve |
| `docs/Standards/skills.md` | Extended | Added bidirectional See Also link to Eve, noting the parallel filesystem-discovery convention |
| `docs/AgenticFrameworks/README.md` | Extended | Added Eve row to the main framework comparison table |
| `mkdocs.yml` | Extended | Added 4.19 Eve under Agent Development Frameworks |

## [2026-06-27] ingest | AWS Lambda MicroVMs | sections touched: SecurityFrameworks, AllThingsAWS

**Source**: https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html

**Type**: Vendor documentation (AWS Lambda Developer Guide)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/SecurityFrameworks/agent-sandboxing.md` | Extended | Added "AWS Lambda MicroVMs" entry under Cloud-Hosted Sandboxes (Firecracker microVM per invocation, up to 8hr runtime, 10GB memory, ~100-200ms added cold start, 4x vertical burst scaling, configurable auto-suspend/resume); added rows to the Comparison Summary and Selection Guide tables; added References entry and a See Also link to AllThingsAWS |
| `docs/AllThingsAWS/README.md` | Extended | Added hub row for AWS Lambda MicroVMs |

## [2026-06-27] ingest | AWS Agent-EvalKit | sections touched: EvaluationFrameworks, AllThingsAWS

**Source**: https://aws.amazon.com/blogs/machine-learning/evaluate-ai-agents-systematically-with-agent-evalkit/

**Type**: Vendor blog post (AWS Machine Learning Blog)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/platforms.md` | Extended | Added "AWS Agent-EvalKit" subsection under Open Source and Developer Platforms (six-phase eval workflow, hybrid code-based + LLM-as-judge evaluators, Claude Code/Kiro CLI/Kilo Code integration); added comparison table row; added the missing References section (opportunistic gap fix) and a See Also link to AllThingsAWS |
| `docs/AllThingsAWS/README.md` | Extended | Added hub row for AWS Agent-EvalKit |

## [2026-06-27] ingest | AWS AgentOps Four-Pillar Framework | sections touched: AgentOps, AgentPlatforms, AllThingsAWS

**Source**: https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/

**Type**: Vendor blog post (AWS Machine Learning Blog)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentOps/README.md` | Extended | Added "AWS Perspective: Four-Pillar AgentOps Framework" section (Governance & Security / Build & Operations / Evaluation [tool/turn/session/system levels] / Observability & Monitoring [four telemetry layers]), parallel to the existing Google Cloud Perspective; added References section (new) and See Also links |
| `docs/AgentPlatforms/aws-agentcore.md` | Extended | Added cross-link to the new AWS AgentOps Four-Pillar Framework section |
| `docs/AllThingsAWS/README.md` | Extended | Added hub row for AWS AgentOps Four-Pillar Framework |

## [2026-06-27] ingest | Unblocked (getunblocked.com) | sections touched: AgenticTechStack

**Source**: https://getunblocked.com/

**Type**: Vendor product page

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgenticTechStack/README.md` | Extended | Added new "Context Engines for Coding Agents" subsection under Key Components; added the missing References section (opportunistic gap fix) citing the source URL |

## [2026-06-27] ingest | Novu / Agent Communication Infrastructure (novuhq/novu) | sections touched: AgenticTechStack

**Source**: https://github.com/novuhq/novu

**Type**: Open-source repository

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgenticTechStack/README.md` | Extended | Added new "Agent Communication Infrastructure" subsection under Key Components describing Novu's unified conversation model across Slack/Teams/Telegram/WhatsApp/email/in-app inbox; added References entry |

## [2026-06-27] ingest | GEPA (Genetic-Pareto) | sections touched: PromptEngineering, AgentHarness

**Source**: https://gepa-ai.github.io/gepa/

**Type**: Open-source project page / optimizer framework

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/PromptEngineering/gepa.md` | Created | Reflective Pareto-frontier prompt optimizer using full execution traces; outperforms GRPO by 10-20% with up to 35x fewer rollouts, beats MIPROv2 by >10%; DSPy-integrated |
| `docs/AgentHarness/harness-optimization.md` | Extended | Added GEPA row to the "Relationship to Prior Optimization Work" table (positioned between text-space optimizers and Meta-Harness); added a paragraph noting GEPA as the closest text-space predecessor; added cross-links |
| `docs/PromptEngineering/skillopt.md` | Extended | Added bidirectional See Also link to GEPA |
| `mkdocs.yml` | Extended | Added 8.4.2 GEPA under Prompt Engineering |

## [2026-06-27] ingest | Databricks Omnigent | sections touched: AgentHarness

**Source**: https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents

**Type**: Vendor blog post (product announcement)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/harness-optimization.md` | Extended | Added "Productization: Databricks Omnigent" subsection (Composition/Control/Collaboration, Apache 2.0) with an explicit naming-disambiguation note distinguishing the commercial Omnigent product from the academic Meta-Harness paper (arXiv:2603.28052) already documented on this page — following the same disambiguation pattern used for KAOS vs. Agent Sandbox; added References entry

## [2026-06-27] ingest | cobusgreyling/loop-engineering Claude Code examples | sections touched: AgentHarness

**Source**: https://github.com/cobusgreyling/loop-engineering/tree/main/examples/claude-code

**Type**: GitHub examples repository — Claude Code loop prompt definitions

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/loop-engineering.md` | Extended | Added "Example Implementations" section listing 7 example loops (changelog-drafter, ci-sweeper, daily-triage, dependency-sweeper, issue-triage, post-merge-cleanup, pr-babysitter); added References entry |

## [2026-06-27] verification | kagent.dev | sections touched: none (no-op)

**Source**: https://kagent.dev/

**Type**: Vendor/project page — verification only

Content already fully covered by `docs/AgentOps/kagent.md`, created during the 2026-06-22 KAOS/Kubernetes-native agent orchestration ingest (CNCF Sandbox project by Solo.io; Controller/Engine/UI/CLI architecture; Agent/ModelConfig/ToolServers CRDs; MCP/A2A composition; multi-provider LLM support; OTel tracing). No changes made.

## [2026-06-27] ingest | Dataiku — Enterprise AI Transformation | sections touched: MaturityModels

**Source**: https://www.dataiku.com/stories/blog/enterprise-ai-transformation (WebFetch blocked 403; content sourced via WebSearch)

**Type**: Vendor blog post (Dataiku)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/MaturityModels/README.md` | Extended | Added "Dataiku's Perspective" subsection under Industry Perspectives — five-phase maturity journey (Explore/Experiment/Establish/Expand/Embed), operating-model maturity axis (Decentralized → Centralized CoE → Hub and Spoke), five-stage governance maturity model (ad hoc → documented → operationalized → integrated → adaptive); added Resources entry |

## [2026-06-27] ingest | GKE Agent Sandbox GA + Agent Substrate (Google Cloud Blog) | sections touched: Standards, AllThingsGoogle, index.md

**Source**: https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate

**Type**: Vendor blog post (Google Cloud)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/k8s-agent-sandbox.md` | Extended | Updated Governance and Status to reflect GA (previously framed only as the KubeCon Atlanta launch); added "GKE Productization: GA and Agent Substrate" section with Pod Snapshots, sandbox provisioning latency (300/sec/cluster, 90% under 200ms), 30% price-performance gain on Axion, 16x adoption growth, and a new Agent Substrate subsection describing its minimal-control-plane architecture and relationship to Agent Sandbox |
| `docs/AllThingsGoogle/README.md` | Extended | Updated Kubernetes Agent Sandbox hub row with GA status; added new Agent Substrate hub row |
| `docs/index.md` | Extended | Updated Standards bullet (section 7) to mention GA status and Agent Substrate |

## [2026-06-27] ingest | Contrast Security — 8 Levels of Context Maturity (webinar) | sections touched: MaturityModels

**Source**: https://watch.getcontrast.io/register/context-maturity

**Type**: Registration-gated webinar (Contrast Security) — page returned HTTP 403 on fetch; cross-reference added based on title/topic only

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/MaturityModels/agentic-engineering-levels.md` | Extended | Added cross-reference note on the structural overlap between Eledath's 8-level framework and Contrast's context-maturity webinar; added References entry | |

## [2026-06-27] ingest | 20+ Agent Skills, Repos, and Marketplaces (Generative Programmer) | sections touched: Standards

**Source**: https://generativeprogrammer.com/p/20-agent-skills-repos-and-marketplaces (WebFetch blocked 403; content sourced via WebSearch)

**Type**: Blog post survey of community skills repositories and marketplaces

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/skills.md` | Extended | Added "Community Skills Marketplaces & Curated Lists" subsection (ComposioHQ/awesome-claude-skills, VoltAgent/awesome-agent-skills, Agent-Skills-for-Context-Engineering, Agensi, Claude Skills Marketplace, Smithery), cross-referencing the existing Provider Skills Repositories table; added References entry |

## [2026-07-04] fix + ingest | Mermaid quadrantChart fix + AWS Marketplace Agent Memory Systems (Module 7) | sections touched: AgentMemory/solutions.md, AgentMemory/ltm-strategies.md

**Source**: https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-memory-systems (WebFetch, rendered)
**Type**: Bug fix (Mermaid) + vendor/architecture guide ingest
**Processed by**: Kiro

### Changes

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentMemory/solutions.md` | Fixed + Extended | Fixed both quadrantChart Mermaid diagrams — quoted all multi-word labels (axis labels, quadrant names, data point labels with spaces) which caused rendering failure. Added new "AWS Memory Architecture Guide" section covering: memory taxonomy (duration × scope), context window management strategies, session memory backend selection (DynamoDB / ElastiCache / Redis Cloud), vector store selection (HNSW/IVF/flat, Pinecone/Weaviate/Qdrant/Zilliz/MongoDB Atlas), Graph RAG with Neo4j AuraDB, MongoDB Atlas unified document+vector model, shared cross-agent memory with DynamoDB access control, memory governance (data lineage, retention, PII handling with Bedrock Guardrails), and memory consolidation patterns (scheduled vs threshold-triggered). Updated See Also and References. |
| `docs/AgentMemory/ltm-strategies.md` | Extended | Added AWS consolidation implementation details to Reflection/Consolidation strategy (EventBridge → Step Functions pattern, scheduled vs threshold-triggered variants). Added vector index architecture comparison table and hybrid search + re-ranking notes to Vector RAG strategy. Added new Graph RAG strategy (2b) covering entity-first vs community-first traversal, Neo4j AuraDB implementation. Updated See Also with new backlinks and added References section. |

## [2026-07-06] ingest | Harbor Framework + LangSmith Sandboxes | sections touched: EvaluationFrameworks/platforms.md, Benchmarks/agent-benchmarks.md, SecurityFrameworks/agent-sandboxing.md, ProductionBestPractices/testing-evaluations.md, index.md

**Sources**: https://www.harborframework.com, https://github.com/harbor-framework/harbor, https://www.langchain.com/langsmith/sandboxes (WebFetch/WebSearch — harborframework.com and langchain.com blocked direct WebFetch with HTTP 403; content sourced from GitHub README fetch and WebSearch summaries of the LangChain/LangSmith blog and the tbench.ai Terminal-Bench 2.0 announcement)
**Type**: New tool/platform ingest (no local raw file)

### Changes

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/platforms.md` | Extended | Added new "Harbor" entry under Open Source and Developer Platforms — official Terminal-Bench 2.0/2.1 harness, distributed agent evaluation across cloud sandbox providers, RL/SFT rollout generation, Apache-2.0. Updated LangSmith entry with LangSmith Sandboxes (Private Preview). Added both to the platform comparison table, See Also, and References. |
| `docs/Benchmarks/agent-benchmarks.md` | Extended | Cross-referenced Harbor as the executing harness in the TerminalBench-2 and Terminal-Bench 2.1 sections; added See Also link. |
| `docs/SecurityFrameworks/agent-sandboxing.md` | Extended | Added new "LangSmith Sandboxes" cloud-hosted sandbox entry (microVM isolation, Authentication Proxy, Deep Agents integration) with comparison table row, selection guide row, See Also, and References updates. |
| `docs/ProductionBestPractices/testing-evaluations.md` | Extended | Added Harbor to the Evaluation Platforms table; added Agent Sandboxing cross-link to See Also. |
| `docs/index.md` | Extended | Updated Agent Testing & Evaluations bullets to mention Harbor; added new Agent Sandboxing bullet under Agent Security (page existed but had no index representation). |

## [2026-07-23] ingest | Google Cloud LLM EvalKit | sections touched: EvaluationFrameworks/platforms.md, AllThingsGoogle/README.md, index.md

**Sources**: https://cloud.google.com/blog/products/ai-machine-learning/introducing-llm-evalkit (WebFetch — succeeded)
**Not ingested**: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview and https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/ — both hosts (`docs.cloud.google.com`, `aws.amazon.com`) returned a hard 403 policy denial at the session's outbound proxy (confirmed via proxy status endpoint as `connect_rejected` / gateway policy denial, not a transient error). Per the environment's network guidance these are not to be retried or routed around. User was consulted and chose to proceed with only the reachable source; the two blocked URLs remain un-ingested pending network access.
**Type**: New tool/platform ingest (no local raw file)

### Changes

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/platforms.md` | Extended | Added new "Google LLM EvalKit" entry under Open Source and Developer Platforms — open-source, self-hostable, no-code prompt engineering + evaluation hub built on Vertex AI SDKs; metric-driven three-step methodology (define problem → build test dataset → define objective metrics); integrates with Vertex AI Evaluation. Added row to the platform comparison table, See Also (added AllThingsGoogle backlink), and References. |
| `docs/AllThingsGoogle/README.md` | Extended | Added "LLM EvalKit" row to the Key Offerings hub table with backlink to `EvaluationFrameworks/platforms.md`; added reciprocal See Also link. |
| `docs/index.md` | Extended | Updated Evaluation Platforms bullet to mention AWS Agent-EvalKit and Google LLM EvalKit. |

## [2026-07-23] ingest | AWS Bedrock Evaluations + Azure AI Foundry Evaluation + new Evaluation Tech Radar | sections touched: EvaluationFrameworks/platforms.md, EvaluationFrameworks/tech-radar.md (new), EvaluationFrameworks/llm-frameworks.md, EvaluationFrameworks/ai-as-judge.md, EvaluationFrameworks/Readme.md, AllThingsAWS/README.md, AllThingsMicrosoft/README.md, AllThingsGoogle/README.md, AgenticFrameworks/solutions.md, Observability/tech-radar.md, mkdocs.yml, index.md

**Sources**: https://aws.amazon.com/bedrock/evaluations/ and https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app — both hosts (`aws.amazon.com`, `learn.microsoft.com`) returned a hard 403 policy denial at the session's outbound proxy (confirmed via proxy status endpoint as `connect_rejected`). Per environment guidance these were not retried. Content for both was instead sourced via WebSearch, which surfaced and summarized the target pages plus adjacent official docs (AWS Bedrock LLM-as-judge GA announcement; Microsoft Foundry risk/safety evaluators page). The user-provided URLs are retained as the canonical citations.
**Type**: New tool ingest (2 sources, no local raw files) + new synthesis page (Evaluation Tech Radar), requested directly by the user

### Changes

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/platforms.md` | Extended | Added "AWS Bedrock Evaluations" (LLM-as-judge, bring-your-own-inference, Knowledge Bases RAG evaluation with citation metrics, human review via SageMaker Ground Truth) and "Azure AI Foundry Evaluation" (quality/NLP/risk-safety evaluator families, agent evaluation, Observability dashboard integration) entries under Enterprise Evaluation Platforms. Added both to the comparison table, See Also (added Microsoft hub + tech radar links), and References. |
| `docs/EvaluationFrameworks/tech-radar.md` | **New page** | Created an Adopt/Trial/Assess/Hold Evaluation Tech Radar (mirroring the Frameworks and Observability radars) with two Mermaid quadrant charts: open-source frameworks/toolkits (DeepEval, RAGAS, MLFlow LLM Evaluate, LangChain OpenEvals, Langfuse, Harbor, AgentPex, AWS Agent-EvalKit, Google LLM EvalKit) and managed/enterprise platforms (Galileo, Google Stax, LastMile AI, LangSmith, Braintrust, AWS Bedrock Evaluations, Azure AI Foundry Evaluation). Includes ring guidance tables, radar summary table, best practices, See Also, and References. Added to `mkdocs.yml` nav as 10.8. |
| `docs/EvaluationFrameworks/llm-frameworks.md`, `docs/EvaluationFrameworks/ai-as-judge.md`, `docs/EvaluationFrameworks/Readme.md` | Extended | Added See Also backlinks to the new tech radar page. |
| `docs/AllThingsAWS/README.md` | Extended | Added "AWS Bedrock Evaluations" row to the Key Offerings hub table; added Evaluation Tech Radar to See Also. |
| `docs/AllThingsMicrosoft/README.md` | Extended | Added "Azure AI Foundry Evaluation" row to the Key Offerings hub table; added Evaluation Tech Radar to See Also. |
| `docs/AllThingsGoogle/README.md` | Extended | Added reciprocal Evaluation Tech Radar link to See Also. |
| `docs/AgenticFrameworks/solutions.md`, `docs/Observability/tech-radar.md` | Extended | Added reciprocal See Also links to the new Evaluation Tech Radar for cross-radar navigation. |
| `docs/index.md` | Extended | Updated Evaluation Platforms bullet to include AWS Bedrock Evaluations and Azure AI Foundry Evaluation; added new Evaluation Tech Radar bullet. |
| `mkdocs.yml` | Extended | Added nav entry `10.8 Evaluation Tech Radar: 'EvaluationFrameworks/tech-radar.md'`. |

## [2026-07-13] ingest | Kubernetes Agent Sandbox (agent-sandbox.sigs.k8s.io) | sections touched: Standards/k8s-agent-sandbox.md, SecurityFrameworks/agent-sandboxing.md

**Source**: https://agent-sandbox.sigs.k8s.io/ and https://agent-sandbox.sigs.k8s.io/docs
**Type**: Official project documentation — kubernetes-sigs/agent-sandbox, Kubernetes SIG Apps subproject; CC BY 4.0

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/k8s-agent-sandbox.md` | Extended | Added Core CRD API Reference table (Sandbox/SandboxTemplate/SandboxClaim/SandboxWarmPool); Client SDKs section (Python + Go, filesystem/volume APIs); Use Cases table (code execution, coding agents, computer use, CI/CD, always-on OpenClaw, gVisor, Kata isolation patterns); updated References with official docs and GitHub links |
| `docs/SecurityFrameworks/agent-sandboxing.md` | Extended | Added Kubernetes Agent Sandbox entry under Cloud-Hosted Sandboxes with full attribute table and capability notes; added row to Comparison Summary table; added dedicated selection-guide row; updated See Also with backlink |

### Key Knowledge Added

- **SandboxWarmPool CRD**: pre-warmed pod pools enabling sub-millisecond sandbox assignment vs. cold pod scheduling
- **Hibernation & resume**: controller pauses idle sandboxes and resumes on incoming network connections; state preserved, compute cost drops to near-zero
- **Stable identity**: each Sandbox gets a persistent hostname and optional PVC-backed storage that survives restarts
- **Client SDKs**: first-class Python and Go libraries with Filesystem (read/write/list/transfer) and Volume attachment APIs
- **Use case catalog**: 7 canonical patterns documented — code execution (short), coding agents (medium), computer use (medium), CI/CD (short-to-medium), always-on OpenClaw environments (long), gVisor isolation, Kata Containers isolation
- **Isolation is deployment-time choice**: standard containers / gVisor / Kata Containers all pluggable via the same Sandbox API

---

## [2026-07-13] ingest | Docker Sandboxes (docker.com/products/docker-sandboxes) | sections touched: SecurityFrameworks/agent-sandboxing.md

**Source**: https://www.docker.com/products/docker-sandboxes/
**Type**: Product page — Docker Inc., 2026

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/SecurityFrameworks/agent-sandboxing.md` | Extended | Added Docker Sandboxes entry under Cloud-Hosted Sandboxes (before Kubernetes Agent Sandbox); added row to Comparison Summary table; added dedicated selection-guide row ("Run AI coding agents unattended on local machine"); renamed "Docker (standard)" to "Docker (standard containers)" to distinguish from Docker Sandboxes product; added References entries |

### Key Knowledge Added

- **Docker Sandboxes is a distinct product from Docker Desktop / standard containers**: microVM isolation per session, not just namespace-based containers
- **YOLO mode support**: `--dangerously-skip-permissions` is safe inside a Docker Sandbox because the microVM provides a hard host boundary
- **Agents can run Docker inside sandboxes**: nested container execution is supported
- **Supported agents**: Claude Code, Gemini CLI, Copilot CLI, Codex, OpenCode, Kiro
- **Local-first**: macOS (`brew install docker/tap/sbx`) and Windows (`winget install Docker.sbx`); no Docker Desktop dependency
- **Team/enterprise tier**: centralized network and filesystem policy management available via Docker sales channel

---

## [2026-07-13] ingest | Gartner — Emerging Market Quadrant for No-Code Agent Builders — Startup Vendors (May 2026) | sections touched: MaturityModels/gartner.md, WorkflowBuilders/README.md

**Source**: Attached image (Gartner report 850246, dated May 2026)
**Type**: Gartner market quadrant — no-code agent builder startup vendor landscape

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/MaturityModels/gartner.md` | Extended | Added new "Emerging Market Quadrant for No-Code Agent Builders" section with full vendor placement table (15 vendors across 4 quadrants), quadrant interpretation notes, and relationship mapping to existing WorkflowBuilders wiki coverage; added See Also section (was missing — knowledge graph now includes this page) |
| `docs/WorkflowBuilders/README.md` | Extended | Added market landscape callout in Overview paragraph linking to Gartner quadrant; added See Also section (was missing) with bidirectional links to Gartner maturity page, open-source/orchestration workflow pages, and agent sandboxing |

### Key Knowledge Added

- **Market Shapers**: Glean (enterprise AI search/agents), Pipefy (business process automation) — highest execution + disruption scores
- **Pace Setters**: WRITER (enterprise AI platform), n8n (open-source workflow builder) — high execution, lower disruption potential
- **Pioneers**: Airia, Dify, Dust, Relevance AI — high disruption potential, earlier execution maturity
- **Specialists cluster**: Sema4.ai, aiXplain, Tines, Relay.app, Botpress, Thunk.AI, Ema — focused-niche positions
- **n8n** is the only open-source project in the Pace Setters quadrant; developer adoption advantage could drive upward movement
- **Tines** (security automation SOAR) appearing in this quadrant signals AI agent capabilities expanding into security workflow automation

## [2026-08-07] ingest | AI tool rebranding updates (Gemini CLI→Antigravity, Vertex AI→Gemini Enterprise Agent Platform, Kiro replaces Amazon Q, Snowflake Cortex Code→CoCo, Databricks Genie family) | sections touched: AICodingAgents, AgenticFrameworks, AgentPlatforms, AllThingsGoogle, AllThingsAWS, AgenticTechStack, index

**Source**: WebSearch/WebFetch (no local raw file or single URL supplied by user — five distinct topic prompts researched independently)
**Type**: Multiple short vendor rebrand/announcement items, batched per the "short, clearly distinct sources" batch-ingest rule (5.1 Section Mapping / Batch vs. Single File guidance)

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AICodingAgents/ai-coding-agents.md` | Extended | Added Antigravity CLI/2.0/SDK/IDE section (successor to Gemini CLI, sunsetting Jun 18 2026 for Free/Pro/Ultra tiers); updated Kiro section with Amazon Q Developer EOL timeline, Pro Max tier, Claude Opus 4.7, iOS app; added new Snowflake CoCo and Databricks Genie Code sections; updated comparison table, positioning map, Best Practices table, See Also, and References |
| `docs/AgenticFrameworks/ai-coding-agents.md` | Extended | Mirrored the same content as the canonical `AICodingAgents/ai-coding-agents.md` (pre-existing duplicate file differing only in frontmatter `type`) |
| `docs/AgentPlatforms/gemini-enterprise-agent-platform.md` | Updated | Corrected announcement/GA timeline — GA April 22, 2026 at Google Cloud Next '26 (previous page text said "Announced in 2025"); added Agentspace consolidation into the sibling Gemini Enterprise app; added inline update note per contradiction-handling rule |
| `docs/AgentPlatforms/databricks-genie.md` | Created | New Platform-type page covering the full Genie family: Genie One (GA), Genie Agents (formerly Genie Spaces, renamed Jul 2026), Genie Code, Genie App Builder, Genie ZeroOps, Genie Ontology, Account-Level Genie |
| `docs/AgentPlatforms/README.md` | Extended | Added Antigravity CLI transition note to the existing Gemini CLI entry; added See Also links to AI Coding Agents and Databricks Genie |
| `docs/AllThingsGoogle/README.md` | Extended | Added Antigravity CLI/2.0/SDK/IDE hub row; updated Gemini CLI row to note sunset; updated Gemini Enterprise Agent Platform row with corrected GA date and Agentspace note |
| `docs/AllThingsAWS/README.md` | Extended | Updated Kiro row to note it replaces Amazon Q Developer, with EOL dates and Claude Opus 4.7 access |
| `docs/AgenticTechStack/semantic-data-layer-radar.md` | Extended | Added bidirectional See Also link to the new Databricks Genie platform page |
| `docs/index.md` | Extended | Added AI Coding Agents bullet to Section 5; updated Agentic AI Platforms bullet in Section 6 with Gemini Enterprise Agent Platform GA date/Agentspace and Databricks Genie family |
| `mkdocs.yml` | Extended | Added nav entry 5.2.8 for `AgentPlatforms/databricks-genie.md` |

### Key Knowledge Added

- **Gemini CLI → Antigravity CLI**: Google announced the transition May 19, 2026 at I/O; Gemini CLI stops serving Free/Pro/Ultra-tier requests June 18, 2026 (Enterprise/Cloud-billed/API-key users retain access). Antigravity spans four surfaces sharing one harness: Antigravity CLI (Go-based terminal tool), Antigravity 2.0 (standalone desktop app), Antigravity SDK, and Antigravity IDE (launched Nov 2025). Antigravity CLI retains Agent Skills/Hooks/Subagents from Gemini CLI (Extensions renamed to plugins) but is proprietary (not Apache 2.0 like its predecessor) and community feedback flags higher token consumption and fewer cost controls.
- **Vertex AI → Gemini Enterprise Agent Platform**: Announced and GA April 22, 2026 at Google Cloud Next '26 — not a 2025 announcement as the wiki previously stated. The same event absorbed Agentspace into a unified Gemini Enterprise app, ending the prior Vertex AI + Agentspace + Gemini API split. No forced migration for existing customers.
- **Kiro replaces Amazon Q Developer**: Kiro relaunched internationally May 7, 2026 as AWS's ground-up spec-driven-IDE replacement for Amazon Q Developer. Amazon Q Developer closed to new signups May 15, 2026; full end-of-support April 30, 2027. Kiro is the only AWS coding tool offering Claude Opus 4.7. New Kiro Pro Max tier ($100/month) and native iOS app announced at AWS Summit NYC, June 17, 2026.
- **Snowflake Cortex Code → CoCo**: Renamed at Snowflake Summit 2026 (June 2, 2026) — same product, same architecture, name change only (customers had already started calling it "CoCo" informally). Data-native coding agent reading Snowflake schemas/RBAC/lineage before generating code; available via Snowsight, CoCo Desktop, CLI, VS Code, Claude Code, and Slack; reported 72.1% pass rate on real-world analytics-engineering tasks.
- **Databricks Genie family**: Databricks One rebranded to Genie in April 2026. Family now spans Genie One (GA agentic coworker for business teams), Genie Agents (formerly Genie Spaces, renamed July 2026 — curated domain-specific autonomous agents), Genie Code (lakehouse-native coding agent, expanded with a command center and scheduled tasks at Data + AI Summit 2026), Genie App Builder, Genie ZeroOps, and Genie Ontology. Account-Level Genie is GA, giving one Genie instance across all workspaces.

### Notes on Sourcing

Several primary vendor blog URLs (Google Developers Blog, AWS Blog, Snowflake product page, Databricks Blog) returned HTTP 403 to WebFetch in this environment; content was corroborated via WebSearch result synthesis (which surfaces and cites the same primary URLs) and one successfully fetched primary source (the official `google-gemini/gemini-cli` GitHub Discussion #27274 announcing the Antigravity CLI transition). Reference sections cite the primary/official URLs identified by search rather than the secondary aggregator articles used for corroboration, per the citation rule.

## [2026-08-09] ingest | FreePHDLabor, LifeOS, Learn-Prompt-Hacking, Discovery Loop (four link ingest) | sections touched: AgenticFrameworks, AgentPlatforms, SecurityFrameworks, PromptEngineering, Architecture, ReferenceArchitecture, AgentMemory, AICodingAgents, index

**Source**: Four URLs supplied directly by the user; `freephdlabor.github.io` and `discoveryloop.com` were blocked by the network egress proxy, so those two were researched via WebSearch/WebFetch of secondary sources (GitHub mirror, arXiv paper, press coverage) instead of the primary page itself — content and citations below reflect that fallback.
**Type**: Four independent, non-overlapping short sources (project site, two GitHub repos, one company site) — batched per the "clearly distinct topics with no overlap" batch-ingest rule, processed sequentially.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgenticFrameworks/freephdlabor.md` | Created | New Framework-type page: FreePHDLabor's hierarchical ManagerAgent + Ideation/Experimentation/Writeup/Reviewer/Proofreading agent architecture, smolagents/AI-Scientist-v2 tech stack, dynamic-workflow and interrupt/resume features, MIT license |
| `docs/AgenticFrameworks/README.md` | Extended | Added FreePHDLabor bullet to "Other Frameworks/Platforms" list |
| `docs/Architecture/multi-agent-system.md` | Extended | Added See Also link to FreePHDLabor as a hierarchical multiagent example |
| `docs/AgentPlatforms/lifeos.md` | Created | New Platform-type page: LifeOS's Cortex/Synapse/Atlas/Ledger subsystems, seven-phase Algorithm loop, ISA goal artifact, Pulse daemon, 49+ skill library, TypeScript/Bun stack, MIT license |
| `docs/AgentPlatforms/README.md` | Extended | Added LifeOS to the "Personal AI Agents" list (alongside Hermes Agent, OpenClaw, OpenHuman) and to the section's See Also; added Discovery Loop under "Research Agents" |
| `docs/AICodingAgents/claude-code.md` | Extended | Added See Also link to LifeOS as a Claude Code skill-distributed personal AI OS |
| `docs/AgentMemory/ltm-strategies.md` | Extended | Added See Also link to LifeOS's Cortex knowledge-graph memory subsystem |
| `docs/SecurityFrameworks/learn-prompt-hacking.md` | Created | New Playbook-type page: Learn-Prompt-Hacking's offensive (jailbreaks, prompt injection against GPT Assistants/custom GPTs, adversarial ML) and defensive (blue team, inference reinforcement, eval benchmarks) course modules; mapped to CSA Agentic AI Red Teaming Guide threat categories 4.4/4.5 |
| `docs/SecurityFrameworks/Readme.md` | Extended | Added "Educational Resources" section summarizing Learn Prompt Hacking; added to top-level See Also list |
| `docs/SecurityFrameworks/agentic-ai-red-teaming-guide.md` | Extended | Added bidirectional See Also link to Learn Prompt Hacking |
| `docs/PromptEngineering/README.md` | Extended | Added See Also link to Learn Prompt Hacking from the Defensive Prompt Engineering section |
| `docs/AgentPlatforms/discovery-loop.md` | Created | New Platform-type page: Discovery Loop PBC — founders (Jeff Dean CEO, Sanjay Ghemawat, Oriol Vinyals, Quoc Le, ex-Google/DeepMind), massively parallel automated research-loop thesis, phased domain rollout (ML research → hardware/drug discovery/clean energy), Radical Ventures/Khosla Ventures/Alphabet backing |
| `docs/ReferenceArchitecture/self-learning-agents.md` | Extended | Added See Also links to LifeOS, FreePHDLabor, and Discovery Loop as related continual-improvement / automated-research architectures |
| `docs/index.md` | Extended | Added FreePHDLabor bullet to Section 5 frameworks list; added LifeOS and Discovery Loop mention to Section 6 Popular AI Agents bullet; added Learn Prompt Hacking mention to the Production Best Practices Agent Security bullet |
| `mkdocs.yml` | Extended | Added nav entries 4.19 (FreePHDLabor), 5.8 (LifeOS), 5.9 (Discovery Loop), 11.9 (Learn Prompt Hacking) |

### Key Knowledge Added

- **FreePHDLabor**: Open-source (MIT), smolagents-based multiagent framework automating the full scientific research lifecycle via a ManagerAgent orchestrating IdeationAgent, ExperimentationAgent (built on modified AI-Scientist-v2 components), WriteupAgent, ReviewerAgent, and ProofreadingAgent; dynamic real-time-reasoning-driven workflow (not a fixed pipeline); shared-workspace-directory communication; interrupt/resume state persistence; companion paper at arXiv:2510.15624.
- **LifeOS**: Daniel Miessler's MIT-licensed, harness-agnostic "personal operating system" distributed as a single Claude Code skill. Bundles Cortex (memory/knowledge graph), Synapse (intent routing), Atlas (asset management), Ledger (audit log), a seven-phase Algorithm loop (OBSERVE→THINK→PLAN→BUILD→EXECUTE→VERIFY→LEARN), an Ideal State Artifact goal document, the Pulse daemon (voice/scheduling/dashboards), and a 49+ item skill library. TypeScript/Bash on Bun; git-backed persistence; `curl | bash` install.
- **Learn-Prompt-Hacking**: TrustAI-laboratory's open-source, course-structured repository (Basics → Applications → Offensive → Red Team → Blue Team → Evaluation → Conference/paper collection) teaching ChatGPT jailbreaks, prompt injection against GPT Assistants/custom GPTs, adversarial ML techniques, and corresponding blue-team defenses and robustness benchmarks.
- **Discovery Loop**: New (announced Aug 5, 2026) Public Benefit Corporation founded by Jeff Dean (CEO), Sanjay Ghemawat, Oriol Vinyals, and Quoc Le after departing Google/Google DeepMind. Thesis: automate the research loop itself (AI proposes → runs → learns from → iterates on experiments) at massive parallel scale rather than serial human-run experimentation. Initial focus: ML research/engineering automation; stated future domains: hardware design, drug discovery, clean energy. Seed round (not yet closed) co-led by Radical Ventures and Khosla Ventures; Alphabet backs as founding investor and cloud compute partner.

### Notes on Sourcing

`freephdlabor.github.io` and `discoveryloop.com` were both blocked by the network egress proxy (`EGRESS_BLOCKED`). For FreePHDLabor, the GitHub mirror (`github.com/ltjed/freephdlabor`) and the arXiv abstract page were fetched directly as substitute primary sources, and the project site URL is retained as the canonical citation per the citation rule since it was the URL the user supplied. For Discovery Loop, no primary page content was retrievable; the page was built from WebSearch-surfaced press coverage (TechCrunch, GeekWire, Tech Times) and the Radical Ventures investment announcement, with `discoveryloop.com` retained as the canonical citation.

## [2026-08-09] ingest | Dosu, MindStudio, LlamaIndex Parse Gateway, OpenGeni, OpenWorker (extend-only batch) | sections touched: AgentPlatforms, AgenticFrameworks, AgentOps, SecurityFrameworks, index

**Source**: Five URLs supplied directly by the user, with explicit instruction not to create unnecessary new pages. All five were blocked by the network egress proxy (`dosu.dev`, `www.mindstudio.ai`, `www.llamaindex.ai`, `opengeni.ai`, `openworker.com`); content was sourced via WebSearch of the vendor sites, official blog posts, GitHub repos, and press coverage.
**Type**: Five short, independent items — batched per the "short reference documents" batch-ingest rule. Every one was mapped onto an existing page (list entry, subsection, or See Also link) rather than a new file, per the user's explicit "don't create pages unnecessarily" instruction.

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentPlatforms/README.md` | Extended | Added "Dosu" entry under Coding/Software Development Agents (AI GitHub/GitLab maintainer agent — issue triage, docs freshness, Dosu MCP Server); added "OpenWorker" entry under Personal AI Agents (Andrew Ng/Rohit Prasad's open-source, local-first desktop AI coworker) |
| `docs/AgentPlatforms/saas-platforms.md` | Extended | Added "MindStudio" entry under Development and Workflow Platforms (no-code AI agent builder, 200+ model access, 150k+ agents deployed) |
| `docs/AgenticFrameworks/llamaindex.md` | Extended | Added "Parse Gateway — Smart Page-Level Parser Routing" subsection describing LiteParse's `is_complex`-driven per-page routing between free local parsing and paid LlamaParse tiers; added References entries for LiteParse and the Parse Gateway blog post |
| `docs/AgentOps/README.md` | Extended | Added "Open-Source Agentic Runtimes" subsection covering OpenGeni (Cloudgeni-ai, Apache-2.0) — durable/replayable session API, human approvals, governed credentials/memory, managed-sandbox or self-hosted deployment; added See Also cross-link to Agent Sandboxing |
| `docs/SecurityFrameworks/agent-sandboxing.md` | Extended | Added bidirectional See Also link back to AgentOps' new Open-Source Agentic Runtimes section |
| `docs/index.md` | Extended | Added Parse Gateway clause to the LlamaIndex bullet (Section 5); added Dosu/MindStudio/OpenWorker mentions to the Popular AI Agents bullet (Section 6); added OpenGeni mention to the Lifecycle Management bullet (Production Best Practices → Deployment) |

### Key Knowledge Added

- **Dosu**: AI maintainer agent installed as a GitHub/GitLab bot; triages incoming issues (bug vs. feature request), answers contributor questions in 14+ languages, keeps docs synced with code changes; free Community Edition used by 50,000+ projects (Apache Airflow, LlamaIndex, BetterAuth); ships a Dosu MCP Server for token-efficient cross-tool context.
- **MindStudio**: No-code visual builder for AI-native agents (extensible with code); instant access to 200+ models without individual API key management; 100+ templates, 15-minute-to-1-hour typical build time; deploys as web apps, browser extensions, scheduled automations, or API endpoints; 150k+ agents deployed (Stanford/Harvard/BYU teaching use, ServiceNow sales workflows, Advance Local newsroom automation).
- **LlamaIndex Parse Gateway**: New (2026) routing layer in front of LlamaParse. Uses open-source LiteParse's `is_complex` page-level complexity estimator (flags *why* a page is hard — scanned, sparse text, garbled encoding, vector text, embedded images — and *how severely*) to send simple pages through free local parsing and only escalate genuinely hard pages to paid LlamaParse tiers. Gateway logic is open-source and also exposed as an MCP server so agents can self-select a parsing tier.
- **OpenGeni** (Cloudgeni-ai): Apache-2.0, self-hostable "agentic runtime" — a session-based API (create/steer/observe/interrupt/replay) agnostic to what the agent does, with durable/replayable event history, human-approval checkpoints, and governed credential/memory access. Runs in a managed sandbox (`app.opengeni.ai`) or fully on the operator's own hardware, keeping the control plane, sessions API, event history, and audit trail off third-party servers in the self-hosted mode.
- **OpenWorker**: Andrew Ng and Rohit Prasad's open-source, local-first desktop "AI coworker." Distinguishing design goal: returns finished deliverables (a document, a sent Slack message, an updated calendar entry) rather than chat replies, planning and executing multi-step tasks in the user's own tools with approval gates before important actions. Runs the agent loop locally; fully local and private when paired with Ollama; model-independent (GPT, Claude, Gemini, open-weight, Ollama, bring-your-own-key). macOS available at launch, Windows support in progress.

### Notes on Sourcing

All five URLs returned `EGRESS_BLOCKED` from the network proxy on direct WebFetch. Content was reconstructed via WebSearch synthesis of each vendor's own site copy (surfaced in search snippets), official blog posts (LlamaIndex, Cloudgeni), GitHub repositories (Dosu, OpenGeni, OpenWorker), and independent press coverage (OpenWorker via MarkTechPost/Medium). The user-supplied URLs are retained as the canonical citations in each case per the citation rule.

---

## [2026-09-13] ingest | W3C AI Agent Protocol Community Group | sections touched: Standards/w3c-agent-protocol.md, Standards/agentic-ai-foundation.md, Standards/README.md, mkdocs.yml

**Source**: https://www.w3.org/community/agentprotocol/
**Type**: Standards body community group page (W3C, active 2025–2026)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/w3c-agent-protocol.md` | Created | Full page: mission (inter-agent comms, agent identity, metadata formats, security, protocol interoperability), five scope areas table, published drafts table, relationship to MCP/A2A/ACP/NIST, strategic significance of W3C venue, engagement guidance, best practices table |
| `docs/Standards/agentic-ai-foundation.md` | Extended | Added See Also section with links to W3C, NIST, MCP, A2A, and security pages |
| `docs/Standards/README.md` | Extended | Added full See Also section linking to all major Standards pages including new ones |
| `mkdocs.yml` | Extended | Added 6.13 W3C AI Agent Protocol under Section 6 |

### Key Knowledge Added

- W3C AI Agent Protocol CG established to build open, royalty-free inter-agent protocols for the Web
- Five scope areas: inter-agent communication, agent identity (DID/VCs), metadata formats, security/privacy, protocol interoperability
- Published drafts: use case (2025-08-19), protocol draft (2025-08-19), white paper (2025-05-23)
- Positioned as vendor-neutral W3C home for concepts overlapping with A2A and ACP
- Aligns with NIST AI Agent Standards Initiative goals for community-led interoperable protocols

---

## [2026-09-13] ingest | DESIGN.md — Visual Identity Format for Coding Agents (google-labs-code) | sections touched: Standards/design-md.md, AllThingsGoogle/README.md, mkdocs.yml

**Source**: https://github.com/google-labs-code/design.md
**Type**: Open-source format specification (Google Labs, alpha, 2026)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/design-md.md` | Created | Full page: overview, file structure (YAML front matter + markdown body), token schema (colors/typography/rounded/spacing/components), token type table, minimal example, CLI tooling (lint + diff), relationship to AGENTS.md and other agent steering files, maturity (alpha), best practices |
| `docs/AllThingsGoogle/README.md` | Extended | Added hub row: "DESIGN.md — format spec for giving coding agents persistent visual identity understanding" → Standards/design-md.md |
| `mkdocs.yml` | Extended | Added 6.15 DESIGN.md (Google Labs) under Section 6 |

### Key Knowledge Added

- DESIGN.md is the design-system analogue to AGENTS.md: a well-known file agents read to understand visual identity conventions
- Two-layer format: normative YAML tokens (exact values) + markdown rationale prose (application context)
- Token types: Color (any CSS), Dimension (px/em/rem), Token Reference ({path.to.token}), Typography (object)
- CLI: `npx @google/design.md lint` (validates + WCAG contrast), `npx @google/design.md diff` (regression detection)
- Alpha maturity as of mid-2026; hosted at github.com/google-labs-code/design.md

---

## [2026-09-13] ingest | NIST AI Agent Standards Initiative | sections touched: Standards/nist-ai-agent-standards.md, SecurityFrameworks/nist-ai-rmf.md, mkdocs.yml

**Source**: https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative
**Type**: US federal standards initiative page (NIST, launched February 2026, updated August 2026)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Standards/nist-ai-agent-standards.md` | Created | Full page: three strategic pillars (industry-led standards, community-led protocols, research), active workstreams (CAISI RFI on agent security, NCCOE identity/authorization concept paper, listening sessions for healthcare/finance/education), scope/focus areas table, relationship to other standards, practitioner significance, best practices table |
| `docs/SecurityFrameworks/nist-ai-rmf.md` | Extended | Added See Also section linking to nist-ai-agent-standards.md, CSA, AI Governance, and agent security pages |
| `mkdocs.yml` | Extended | Added 6.14 NIST AI Agent Standards Initiative under Section 6 |

### Key Knowledge Added

- Initiative launched February 2026; official page updated August 14, 2026
- Three pillars: (1) NIST hosts technical convenings + gap analyses for voluntary guidelines; (2) NSF POSE funds open-source agent protocol ecosystem security; (3) fundamental research into agent authentication/identity
- Active CAISI RFI on AI agent security threats and mitigations (deadline March 9, 2026)
- NCCOE concept paper: applying identity standards to enterprise agent use cases
- Focus areas: agent authentication, authorization, multi-agent trust, human-agent security, interoperability
- Expected to inform regulated-sector baseline requirements (finance, healthcare, federal contracts)

---

## [2026-09-13] ingest | OpenTelemetry GenAI Semantic Conventions (open-telemetry/semantic-conventions-genai) | sections touched: Observability/otel-genai-conventions.md, Observability/solutions.md, ProductionBestPractices/observability.md, mkdocs.yml

**Source**: https://github.com/open-telemetry/semantic-conventions-genai
**Type**: Open-source specification repository (OpenTelemetry, active)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Observability/otel-genai-conventions.md` | Created | Full page: scope (GenAI client spans, MCP instrumentation, provider-specific conventions), repo structure (docs/model/reference), key span attributes table (gen_ai.system, gen_ai.operation.name, gen_ai.request.model, gen_ai.usage.input_tokens, gen_ai.usage.output_tokens, gen_ai.response.finish_reasons), MCP attributes (mcp.method, mcp.tool.name), structured events (system/user/assistant/tool messages), OTel pipeline diagram, tooling integration table, best practices |
| `docs/Observability/solutions.md` | Extended | Added "OpenTelemetry GenAI Semantic Conventions" subsection under Infrastructure-Level Observability; added otel-genai-conventions.md to See Also |
| `docs/ProductionBestPractices/observability.md` | Extended | Added OTel GenAI Conventions row to Tooling table; added "Span attribute standardization" best-practice row to Best Practices table; added otel-genai-conventions.md to See Also |
| `mkdocs.yml` | Extended | Added 12.5 OTel GenAI Semantic Conventions under Section 12 |

### Key Knowledge Added

- GenAI conventions extend core OTel spec with `gen_ai.*` and `mcp.*` attribute namespaces
- Key span attributes: `gen_ai.system` (provider), `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.response.finish_reasons`
- MCP instrumentation: `mcp.method` (e.g., tools/call), `mcp.tool.name`
- Structured events for full message content: gen_ai.system.message, gen_ai.user.message, gen_ai.assistant.message, gen_ai.tool.message
- YAML definitions in `model/` are normative; `docs/` is generated via Weaver toolchain
- Openlit and Langfuse v3 emit conformant spans natively; AWS ADOT, Datadog, New Relic also support
- Enables portable dashboards, cost attribution, and MCP tool latency visibility across any OTel-compatible backend

## [2026-09-13] ingest | OpenSandbox (open-sandbox.ai) | sections touched: AgentHarness/agent-harness.md

**Source**: https://open-sandbox.ai/
**Type**: Vendor/product page (Alibaba Cloud, CNCF-listed open-source project)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/agent-harness.md` | Extended | Added OpenSandbox description in the Sandboxes section: CNCF-listed universal sandbox infrastructure, Docker/K8s lifecycle management, multi-language SDKs (Python, JS/TS, Java/Kotlin, Go, C#/.NET), in-sandbox execution primitives (shell, code interpreters, file management, port exposure, log/metrics streaming); added to References |

### Key Knowledge Added

- OpenSandbox is a CNCF-listed sandbox infrastructure layer purpose-built for AI workloads by Alibaba Cloud
- Supports sandbox lifecycle management (provision, monitor, renew, pause/resume, terminate) via Docker and Kubernetes runtimes
- Multi-language SDK surface: Python, JavaScript/TypeScript, Java/Kotlin, Go, C#/.NET — standardized lifecycle and execution protocols across all
- In-sandbox execution: shell commands, multi-language code interpreters, file management, port exposure, log/metrics streaming
- Use cases: coding agents, browser automation, remote development, code execution sandboxes, reinforcement learning environments
- Positioned as a low-level infrastructure primitive that can underpin any agent harness needing managed, reproducible execution at scale

---

## [2026-09-13] ingest | Opengeni — Sovereign AI Harness (opengeni.ai) | sections touched: AgentHarness/agent-harness.md

**Source**: https://opengeni.ai/
**Type**: Vendor/product page (Cloudgeni-ai, open-source self-hosted harness)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AgentHarness/agent-harness.md` | Extended | Added Opengeni description as a self-sovereignty-focused harness: durable sessions, MCP tool integration, sandboxed execution, SDK/React surfaces, human approvals, access controls, usage/audit — fully self-hosted; added to References alongside OpenSandbox |

### Key Knowledge Added

- Opengeni positions itself as a "sovereign AI harness" — the full harness layer running on operator-controlled infrastructure
- Core features: durable sessions with history/recovery, MCP tool integration, sandboxed execution, SDK and React integration surfaces, human approval workflows, access controls, usage and audit logging
- Self-hosted: operator owns execution environment, session state, model routing, audit trail — no cloud dependency
- GitHub: github.com/Cloudgeni-ai/opengeni (Apache-2.0)
- Distinct from cloud-hosted harness products: designed for organizations with data sovereignty requirements or compliance constraints

---

## [2026-09-13] ingest | Gartner Magic Quadrant for Enterprise AI Coding Agents (May 2026) | sections touched: AICodingAgents/ai-coding-agents.md

**Source**: `raw/Gartner-Magic Quadrant for Enterprise AI Coding Agents-2026.pdf`
**Type**: Gartner Magic Quadrant research report (ID G00841434, May 20, 2026, 37 pages)
**Authors**: Philip Walsh, Keith Holloway, + 3 more
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/AICodingAgents/ai-coding-agents.md` | Extended | (1) Comparison table: added Gartner MQ 2026 column; added three new vendor rows (Atlassian Rovo Dev, BytePlus TRAE, JetBrains Junie/Air); (2) New vendor profiles for Atlassian Rovo Dev (Niche Player, Jira/Confluence/Bitbucket integration, Teamwork Graph), BytePlus TRAE (Niche Player, free in China, SOC 1/2/3), JetBrains Junie/Air/Central (Niche Player, large installed base, unclear product strategy); (3) New "Gartner Magic Quadrant for Enterprise AI Coding Agents (May 2026)" section with quadrant placement table, strategic planning assumptions table, mandatory features list, key market stats table, and pricing shift discussion; (4) Gartner MQ reference added to References; (5) Best Practices table updated with three new rows; (6) timestamp updated to 2026-09-13 |

### Key Knowledge Added

- **Quadrant placements**: Leaders — Anthropic (Claude Code), Cursor, GitHub (Copilot), OpenAI (Codex); Challengers — Alibaba Cloud (Qoder), AWS (Kiro), Cognition (Windsurf+Devin); Visionaries — Tabnine; Niche Players — Atlassian (Rovo Dev), BytePlus (TRAE), JetBrains (Junie/Air)
- **Added to this edition**: Anthropic, Atlassian, BytePlus, OpenAI
- **Dropped**: Augment Code, GitLab, Harness, IBM, Qodo, Tencent Cloud
- **Strategic assumptions**: 65% of teams will treat IDEs as optional by 2027; 70% of engineers will use AI agents by 2028; async workflows to deliver 30–50% productivity gain by 2028; AI coding costs to overtake avg developer salary by 2028
- **Mandatory Gartner features**: autonomous task execution, iterative verification/self-correction, extensible tool integration, advanced context awareness, MCP support, human oversight/auditability, enterprise controls/data protection
- **Market stats (2026)**: 90% of engineering leaders report productivity gains; net avg 19.3% productivity gain; GitHub Copilot 4.7M licensed seats (+75% YoY); OpenAI Codex 4M weekly active users; Cursor 50K+ customer organizations
- **Pricing shift**: industry-wide move from flat per-seat to hybrid seat + consumption pool + usage-based models; agentic/parallel/background workflows increase token consumption significantly
- **New vendor highlights**: Atlassian Rovo Dev is platform-locked (Jira/Confluence/Bitbucket) with Teamwork Graph differentiation; BytePlus TRAE is pricing-aggressive (free in China) with SOC 1/2/3 compliance; JetBrains has overlapping products (Junie/AI/Air/Central) with unclear strategic priority

---

## [2026-09-13] ingest | Evidently AI — Open-source AI Evaluation and Observability (evidentlyai.com) | sections touched: EvaluationFrameworks/platforms.md, Observability/solutions.md

**Source**: https://www.evidentlyai.com/
**Type**: Vendor/product page (open-source, Apache 2.0)
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/platforms.md` | Extended | Added new "Evidently AI" subsection under Open Source and Developer Platforms; added to comparison table; added to References |
| `docs/Observability/solutions.md` | Extended | Added new "Evidently AI" subsection under Specialized Observability Platforms; added to platform comparison table |

### Key Knowledge Added

- Open-source (Apache 2.0) AI evaluation and observability framework; 7,500+ GitHub stars, 40M+ downloads, 3,000+ community members
- Single framework covers LLMs, RAG applications, AI agents, and classical ML models — unusual breadth for an open-source tool
- 100+ built-in metrics: hallucinations/factuality, PII detection, retrieval quality/context relevance, sentiment/toxicity/trigger words, jailbreak detection, data drift, cascading error detection
- Custom evals: compose rule-based checks, ML classifiers, and LLM-as-judge evaluations together
- Online (production monitoring, real-time alerting) and offline (pre-production test datasets) evaluation modes
- Adopted at scale: DeepL (daily data quality/drift), Wise (production distribution monitoring), Plaid (continuous model monitoring), Databricks, Realtor.com, PlushCare, Western Governors University
- Differentiator from single-purpose tools: unified framework for both LLM/agent quality evaluation and classical ML observability (drift, data quality, predictive performance) in one install

## [2026-09-13] update | LLM App Evaluation Metrics (metrics.csv) | sections touched: EvaluationFrameworks/llm-frameworks.md

**Source**: `metrics.csv` (user-provided, 22 metrics)
**Type**: Metrics reference — LLM evaluation metrics catalogue covering trace, chat, tool, session, and retriever scopes
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/llm-frameworks.md` | Extended | Added "LLM App Metrics Reference" section with 22 metrics organized into five subsections: Trace-Level (4), LLM & Chat (13), Tool (1), Session (3), Retriever (1). Each metric includes its Level (all LLM except Precision@K which is Code) and a description. |

### Key Knowledge Added

- **Trace-Level Metrics**: Output Toxicity (Vision), Prompt Injection, Prompt Injection (Audio), Prompt Injection (Vision)
- **LLM & Chat Metrics**: Reasoning Coherence (base + Audio + Vision), SQL Adherence, SQL Correctness, SQL Efficiency, SQL Injection, Tool Selection Quality (base + Audio + Vision), Unsafe Output, Visual Fidelity, Visual Quality
- **Tool Metrics**: Tool Error Rate
- **Session Metrics**: User Intent Change (base + Audio + Vision)
- **Retriever Metrics**: Precision@K (Code-level)

## [2026-09-13] ingest | 7 RAG Benchmarks (Evidently AI Blog) | sections touched: Benchmarks/rag-benchmarks.md (new), Benchmarks/llm-benchmarks.md, RAG/Readme.md, mkdocs.yml

**Source**: https://www.evidentlyai.com/blog/rag-benchmarks
**Type**: Blog post / benchmark survey — Evidently AI, 2026. Lists seven RAG evaluation benchmarks.
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Benchmarks/rag-benchmarks.md` | Created | New page with all 7 benchmarks: NIAH, BeIR, FRAMES, RAGTruth, RULER, MMNeedle, FEVER. Each entry includes what it tests, how it works, why it matters for RAG, and resource links. Includes a benchmark selection guide table keyed to RAG failure modes. |
| `docs/Benchmarks/llm-benchmarks.md` | Extended | RULER entry updated to link to new rag-benchmarks.md; RAG Evaluation Benchmarks added to See Also |
| `docs/RAG/Readme.md` | Extended | Added RAG Evaluation Benchmarks backlink to See Also (bidirectional graph edge) |
| `mkdocs.yml` | Extended | Added 10.4.1 RAG Evaluation Benchmarks nav entry |

### Key Knowledge Added

- **NIAH** — 2D retrieval accuracy test (context length × needle depth); original Paul Graham essay corpus; configurable haystack
- **BeIR** — 18 datasets, 9 task types; zero-shot cross-domain retriever evaluation; covers dense, sparse, hybrid, and re-ranking systems
- **FRAMES** — 800+ multi-hop questions requiring 2–15 Wikipedia articles; numerical, tabular, temporal reasoning types
- **RAGTruth** — 18,000 annotated RAG responses; four hallucination types (evident/subtle × conflict/baseless)
- **RULER** — extends NIAH with multi-needle variants and 4 task categories; 4K–128K token range; synthetic generation
- **MMNeedle** — 40,000 images, 280,000 needle-haystack pairs; evaluates multimodal long-context retrieval
- **FEVER** — 185,000+ Wikipedia-based claims; Supported/Refuted/Not Enough Info labels; tests full retrieve-reason-decide pipeline

## [2026-09-13] ingest | DeepSWE — Long-Horizon Software Engineering Benchmark | sections touched: Benchmarks/agent-benchmarks.md

**Source**: https://deepswe.datacurve.ai/ | https://arxiv.org/abs/2607.07946 | https://github.com/datacurve-ai/deep-swe
**Type**: Benchmark — Datacurve AI, 2026. Contamination-free coding agent benchmark, 113 tasks.
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/Benchmarks/agent-benchmarks.md` | Extended | Added DeepSWE section under Software Development Benchmarks; added row to Benchmark Selection Guide; updated timestamp |

### Key Knowledge Added

- **113 original tasks** across 91 repos, 5 languages (TypeScript, Go, Python, JavaScript, Rust)
- Contamination-free: tasks written from scratch, not sourced from existing GitHub commits or PRs
- Solutions require ~5.5× more code and ~2× more output tokens than SWE-bench Pro tasks
- Hand-written behavior-based verifiers eliminate the high false-positive/false-negative rates in automated test graders
- Consistent scaffolding: all models run on mini-swe-agent
- Live leaderboard as of Sep 2026: gpt-6-astra 74%, gemini-3.8-flash 74%, claude-opus-5 74%
- Addresses SWE-bench Pro's 8% false-positive / 24% false-negative verifier misgrading rates

---

## [2026-09-13] ingest | Demystifying Evals for AI Agents — Anthropic Engineering | sections touched: EvaluationFrameworks/agent-evals-design.md, ProductionBestPractices/testing-evaluations.md, Benchmarks/agent-benchmarks.md, AllThingsAnthropic/README.md, index.md, mkdocs.yml

**Source**: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
**Type**: Engineering blog post — Anthropic (2026)
**Authors**: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe
**Processed by**: Kiro

### Files Modified

| File | Change Type | Notes |
|---|---|---|
| `docs/EvaluationFrameworks/agent-evals-design.md` | Created | New page: core eval terminology (task/trial/grader/transcript/outcome/harness), three grader types (code-based, model-based, human) with strengths/weaknesses tables, capability vs regression eval distinction, pass@k and pass^k non-determinism metrics, per-agent-type design patterns (coding, conversational, research, computer-use) with illustrative YAML examples, zero-to-trustworthy roadmap (8 steps), holistic methods comparison table (automated evals vs production monitoring vs A/B testing vs user feedback vs manual review vs systematic studies), eval frameworks reference table |
| `docs/ProductionBestPractices/testing-evaluations.md` | Extended | Added "Capability vs Regression Evals" section; added "Measuring Non-Determinism: pass@k and pass^k" section; added four new Best Practices rows (delayed eval adoption, brittle path-checking graders, flaky eval environments, LLM judge hallucination); added Harbor and Braintrust to Evaluation Frameworks table; added See Also link to agent-evals-design.md; added Anthropic reference; updated timestamp to 2026-09-13 |
| `docs/Benchmarks/agent-benchmarks.md` | Extended | Expanded τ-bench entry with additional detail; added τ2-bench as adversarial multi-turn successor with full Key Characteristics section; added BrowseComp under Research and Retrieval Benchmarks; added both to Benchmark Selection Guide table; added See Also link to agent-evals-design.md |
| `docs/AllThingsAnthropic/README.md` | Extended | Added hub row for "Demystifying Evals for AI Agents" → EvaluationFrameworks/agent-evals-design.md |
| `docs/index.md` | Extended | Enriched LLM Evaluation Frameworks bullet with link to agent-evals-design.md and Anthropic attribution; updated Agent Benchmarks bullet to add BrowseComp and τ2-bench |
| `mkdocs.yml` | Extended | Added 10.1.2 Designing Evaluations for AI Agents nav entry |

### Key Knowledge Added

- **Eval terminology standardised**: task / trial / grader / transcript / outcome / eval harness / agent harness / eval suite — all with precise definitions distinguishing outcome (DB state) from transcript (what the agent said)
- **Three grader types**: code-based (fast, cheap, brittle), model-based (flexible, requires calibration), human (gold standard, expensive) — with recommended combinations per agent type
- **Capability vs regression evals**: capability evals start low and track progress; regression evals run at ~100% and catch backsliding; saturation detection guidance
- **pass@k and pass^k**: complementary metrics for non-deterministic agents — pass@k for "one success sufficient" scenarios, pass^k for "consistent every time" customer-facing agents
- **Per-agent-type patterns**: coding (unit tests + LLM rubric + static analysis), conversational (LLM rubric + state checks + max_turns constraint + simulated user), research (groundedness + coverage + source quality checks), computer-use (env state verification + modality selection evals)
- **Zero-to-trustworthy roadmap**: 8 concrete steps from 20–50 initial tasks through harness isolation, grader design, saturation monitoring, and living artifact maintenance
- **Holistic evaluation model**: automated evals + production monitoring + A/B testing + user feedback + manual transcript review + systematic human studies — Swiss Cheese Model analogy
- **New benchmarks**: τ2-bench (adversarial multi-turn successor to τ-bench), BrowseComp (open-web needle-in-haystack for research agents)
- **Eval-driven development pattern**: build evals to define planned capabilities before agents can fulfil them; capability evals that start low make model upgrade bets visible
