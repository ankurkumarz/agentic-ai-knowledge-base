# Ingest Log

Append-only record of all ingest, query, and lint operations on this wiki.
Format: `## [YYYY-MM-DD] <operation> | <source> | sections touched: <list>`

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
