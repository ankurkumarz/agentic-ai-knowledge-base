# Agent Harness Engineering: Survey & Taxonomy

## Overview

This page synthesizes two related 2026 surveys that together define the harness engineering discipline:

**Survey A — "Agent Harness Engineering: A Survey"** (Picrew et al., submitted to TMLR, 2026) establishes harness engineering as an independent system discipline and proposes the **ETCLOVG seven-layer taxonomy** for classifying how language models are integrated into production application frameworks. The survey covers 110+ papers and analyzes 23+ deployed systems.

**Survey B — "Agent Harness for Large Language Model Agents: A Survey"** (Meng, Wang, Chen, Wu, Li, Jiang, Wang, Lu, Gao, Wu, Hu; arXiv:2605.29682, 2026) provides a formal six-component harness model **H=(E,T,C,S,L,V)** with labeled-transition-system semantics distinguishing safety and liveness properties, a structured Harness Completeness Matrix, and a HuggingFace dataset of 110+ annotated papers spanning 23 systems.

The shared central claim: **the agent execution harness — not the model — is the primary determinant of agent reliability at scale.** Tool format optimization alone moved SWE-bench performance from 6.7% to 68.3% — more than any model upgrade in the same period.

- Survey A page: https://picrew.github.io/LLM-Harness/
- Survey A OpenReview: https://openreview.net/forum?id=3hXEPbG0dh
- Survey B arXiv: https://arxiv.org/pdf/2605.29682
- Survey B GitHub catalog: https://github.com/Gloriaameng/Awesome-Agent-Harness
- Survey B HuggingFace dataset: https://huggingface.co/datasets/GloriaaaM/LLM-Agent-Harness-Survey

---

## The ETCLOVG Seven-Layer Taxonomy

The taxonomy separates harness concerns into four structural pillars and three control-plane layers.

### Structural Pillars (E, T, C, L)

| Layer | Name | Description |
|---|---|---|
| **E** | Execution | Code runner, browser, filesystem, sandbox — the execution environment around the model |
| **T** | Tooling | Tool protocols (MCP, A2A), tool definitions, action-space management, schema validation |
| **C** | Context | Context window management, compaction, retrieval, caching, skill injection |
| **L** | Lifecycle | State machine, authorization, logging, policy enforcement, hooks, session management |

### Control Plane (O, V, G)

| Layer | Name | Description |
|---|---|---|
| **O** | Observability | System-wide monitoring, tracing, metrics, dashboards, alerting across all structural layers |
| **V** | Verification | Evaluation and feedback across components: LLM-as-judge, trajectory scoring, benchmarking |
| **G** | Governance | Security constraints, human handoff points, HITL policy, audit trails, compliance enforcement |

The structural layers (E,T,C,L) determine what an agent *can do*; the control-plane layers (O,V,G) determine how confidently and safely it operates.

---

## Formal Model: H=(E,T,C,S,L,V)

Survey B (Meng et al., arXiv:2605.29682) formalizes agent execution harnesses as an architectural tuple with **labeled-transition-system semantics**, distinguishing safety properties (invariants that must always hold) from liveness properties (eventual-progress guarantees). Each component boundary is made explicit:

| Symbol | Component | Responsibility |
|---|---|---|
| **E** | Execution Loop | Observe–think–act cycles, termination, error recovery |
| **T** | Tool Registry | Typed catalogs, routing, monitoring, schema validation |
| **C** | Context Manager | Context window management, compaction, retrieval |
| **S** | State Store | Persistence across turns and sessions, crash recovery |
| **L** | Lifecycle Hooks | Authorization, logging, policy enforcement, instrumentation |
| **V** | Evaluation Interface | Action trajectories, intermediate states, success signals |

Mapping to ETCLOVG: S maps into ETCLOVG's C/L layers; O and G represent additional control-plane concerns not explicit in the six-component model.

---

## Empirical Evidence

The survey aggregates concrete evidence that harness design determines outcome more than model selection in production settings:

| Finding | Detail | Source |
|---|---|---|
| Tool format optimization | SWE-bench performance from 6.7% → 68.3% via format change alone | Pi Research |
| Benchmark–merge gap | Benchmark-passing PRs show 24.2 pp lower human merge rates; gap widens 9.6 pp/year | METR |
| Tool reduction outperforms upgrades | Removing 80% of tools outperforms model upgrade alone | Vercel practitioner report |
| Zero hand-written code at scale | 1,300 PRs/week; failure attributed to underspecified environments, not model capability | Stripe Minions / OpenAI Codex |
| Memory efficiency | Mem0 achieves 90% token reduction versus full-context approaches | Mem0 evaluation |
| Throughput gains | AIOS kernel achieves 2.1× throughput speedup | AIOS evaluation |

---

## Nine Technical Challenges

The survey identifies nine open challenges with empirical severity data:

| # | Challenge | Key Metric / Evidence |
|---|---|---|
| 1 | **Security & Sandboxing** | 15–35% frontier model container escape rates (SandboxEscapeBench) |
| 2 | **Evaluation & Benchmarking** | 28% false negative rate in automated evaluation (OSWorld) |
| 3 | **Protocol Standardization** | MCP (tool↔harness): 2–15 ms; A2A (agent↔agent): 50–200 ms |
| 4 | **Runtime Context Management** | Schema-based skill injection yields +16.2 pp improvement |
| 5 | **Tool Use & Registry** | Removing 80% of tools outperforms model upgrades alone |
| 6 | **Memory Architecture** | Mem0: 90% token reduction vs. full-context; benchmark: LoCoMo, MemoryBank |
| 7 | **Planning & Reasoning** | Interface design outweighs model capability as the primary performance factor |
| 8 | **Multi-Agent Coordination** | Byzantine fault tolerance remains unsolved for adversarial multi-agent settings |
| 9 | **Compute Economics** | 1M tokens/task average (AgencyBench); 13T tokens/week sector-wide growth rate |

---

## Harness Completeness Matrix

Survey B evaluates 23 systems against the six-component model (from arXiv:2605.29682):

| Category | Systems | Notes |
|---|---|---|
| **Full-Stack** (all 6 components) | Claude Code, PRISM/OpenClaw, AIOS, OpenHands, SWE-agent | Production-grade or research-grade full harness implementations |
| **Multi-Agent Harnesses** | MetaGPT, AutoGen, ChatDev, CAMEL, DeerFlow, DeepAgents | Strong on coordination; variable on individual E/C/V layers |
| **General Frameworks** | LangChain, LangGraph, LlamaIndex | Provide primitives; completeness depends on user configuration |
| **Evaluation Infrastructure** | HAL, AgentBench, OSWorld, BrowserGym | Specialized V-layer; not production execution harnesses |

**HAL evaluation infrastructure** (Kapoor et al., 2026) reached 21,730 agent rollouts across nine models and nine benchmarks at a total cost of approximately $40,000, representing the most comprehensive V-layer deployment in the survey period.

**AgencyBench** (Li et al., 2026) evaluates six agentic capabilities across 138 real-world tasks requiring an average of one million tokens per task — illustrating the compute scale required for long-horizon evaluation.

---

## Paper Coverage

The survey catalogs 110+ papers organized into lineages:

| Category | Representative Papers |
|---|---|
| Historical lineages | JUnit (test harnesses), OpenAI Gym (RL environments) |
| Core agent frameworks | ReAct, MemGPT, Voyager |
| Multi-agent systems | MetaGPT, AutoGen, ChatDev |
| Evaluation suites | AgentBench, SWE-bench, OSWorld |
| Security research | PRISM, InjecAgent, ToolHijacker |
| Memory systems | Mem0, MemoryBank, LoCoMo |

---

## Historical Timeline (1997–2026)

| Era | Period | Milestone |
|---|---|---|
| Software test harnesses | 1997–2015 | JUnit, xUnit — the harness as test scaffold around code under test |
| RL environments | 2016–2021 | OpenAI Gym — standardized E-layer (environment) for reinforcement learning |
| LLM-native frameworks | 2022–2023 | LangChain, LlamaIndex — tool registries and context managers for LLMs |
| Agentic production systems | 2024–2025 | SWE-agent, OpenHands, AutoGen — full harnesses for autonomous coding and multi-agent tasks |
| Harness-as-discipline | 2025–2026 | Explicit naming of harness engineering; automated harness optimization; formal taxonomy proposals |

---

## Eight Future Directions (Meng et al., arXiv:2605.29682)

Survey B identifies eight open research directions for harness engineering:

1. **Formal harness specification language (DSL)** — a domain-specific language for expressing harness contracts, enabling automated compliance checking
2. **Cross-harness benchmark portability** — test suites that run against any H=(E,T,C,S,L,V)-compliant harness without modification
3. **Security taxonomy extending OWASP Top 10** — harness-specific threat model covering tool hijacking, context poisoning, and agent impersonation
4. **MCP/A2A protocol interoperability bridging** — gateway layer to route between tool-call (MCP) and agent-coordination (A2A) protocols
5. **Long-horizon evaluation methodology** — evaluation approaches for tasks requiring 1M+ token contexts (cf. AgencyBench)
6. **Harness-aware fine-tuning** — training procedures that optimize model behavior conditioned on specific harness configurations
7. **Memory interface standardization** — common API for pluggable memory backends (S-layer), enabling portability across Mem0, LanceDB, and similar systems
8. **Harness transparency and auditability** — observability primitives that expose harness decisions (routing, compaction triggers, tool selection) to external audit

---

## Best Practices

| Area | Description | Recommendation |
|---|---|---|
| Tool registry design | More tools degrade performance | Start minimal; add tools only when needed; use skill injection (C layer) to gate exposure |
| Context management | Schema-based injection outperforms flat injection | Use structured skill schemas; inject by relevance, not exhaustively |
| Evaluation (V layer) | 28% false negative rate in automated evaluation | Combine automated metrics with human-verified test sets; do not rely solely on LLM-as-judge |
| Security (G layer) | 15–35% container escape rates | Treat sandboxing as a hard requirement; apply defense-in-depth; see [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md) |
| Memory (S layer) | Full-context approaches are 10× more expensive | Evaluate Mem0 or equivalent compression before full-context by default |
| Multi-agent fault tolerance | Byzantine fault tolerance unsolved | Avoid adversarial multi-agent topologies in production; gate on human approval for high-stakes coordination |
| Protocol selection | MCP < 15 ms; A2A < 200 ms | Prefer MCP for tool calls; use A2A only when inter-agent latency is acceptable |

---

## See Also

- [Agent Harness](./agent-harness.md) — foundational harness definition and core components
- [Harness Engineering](./harness-engineering.md) — feedforward/feedback controls, regulation categories, harnessability
- [Harness Optimization](./harness-optimization.md) — automated harness search with Meta-Harness (Lee et al., 2026)
- [Code as Agent Harness](./code-as-agent-harness.md) — executability, inspectability, statefulness as structural harness properties
- [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md) — sandbox security (E-layer security; see Challenge #1)
- [Agent Memory Management](../AgentMemory/functional-tiers.md) — memory tiers relevant to the S-layer
- [Context Engineering Strategies](../ContextEngineering/strategies.md) — C-layer strategies
- [Agent Benchmarks](../Benchmarks/agent-benchmarks.md) — SWE-bench, OSWorld, AgentBench, HAL
- [MCP Standard](../Standards/mcp.md) — T-layer protocol
- [A2A Standard](../Standards/agent2agent.md) — multi-agent T-layer protocol
- [Production Best Practices: Security](../ProductionBestPractices/security.md)
- [Production Best Practices: Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)

## References

- [Agent Harness for Large Language Model Agents: A Survey — Meng, Wang, Chen, Wu, Li, Jiang, Wang, Lu, Gao, Wu, Hu; arXiv:2605.29682 (2026)](https://arxiv.org/pdf/2605.29682) — primary source for H=(E,T,C,S,L,V) formal model with LTS semantics; Harness Completeness Matrix across 23 systems; 110+ papers surveyed; eight future directions; DOI: 10.20944/preprints202604.0428.v3
- [Agent Harness Engineering: A Survey — picrew et al., OpenReview / TMLR submission (2026)](https://openreview.net/forum?id=3hXEPbG0dh) — proposes the ETCLOVG seven-layer taxonomy; covers 110+ papers and 23+ systems; establishes harness design as the binding constraint on agent reliability
- [Agent Harness Engineering project page](https://picrew.github.io/LLM-Harness/) — companion site with paper, catalog, and BibTeX
- [Awesome-Agent-Harness catalog — Gloriaameng (GitHub)](https://github.com/Gloriaameng/Awesome-Agent-Harness) — companion GitHub repository; 251 stars; links to v4 PDF
- [LLM-Agent-Harness-Survey dataset — GloriaaaM (HuggingFace)](https://huggingface.co/datasets/GloriaaaM/LLM-Agent-Harness-Survey) — structured dataset of 110+ surveyed papers with annotations
