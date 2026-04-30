# Context Graph

## Overview

A Context Graph (CG) is a knowledge structure that extends traditional triple-based Knowledge Graphs (KGs) by attaching rich contextual metadata — temporal validity, geographic location, provenance, confidence levels, and event-specific details — to both entities and the relations between them. Where a standard KG stores facts as `(head, relation, tail)` triples, a CG stores them as quadruples `(head, relation, tail, relation_context)` and pairs each entity with its own context bundle (descriptions, aliases, types, images, reference links).

The concept surfaces in two distinct but complementary contexts in agentic AI:

1. **As a knowledge representation structure** (academic/technical): CGs improve LLM reasoning over structured knowledge bases by providing the contextual information that triple extraction discards.
2. **As a business asset for agentic systems** (industry/VC): CGs are the durable artifact produced when agent orchestration layers capture decision traces — the "why" behind every automated action — turning ephemeral reasoning into replayable, auditable organizational memory.

---

## Part 1 — Technical Definition (IDEA Research, 2024)

### Limitations of Triple-Based Knowledge Graphs

Standard KGs represent knowledge as `(h, r, t)` triples. This structure loses contextual information in three critical ways:

- **Conflicting representations**: The same predicate can mean different things in different contexts. "A lives in Shanghai Hilton" and "A lives in Beijing Haidian" both map to `(A, lives_in, ?)` — the triple extraction strips the distinction between "staying" and "residing."
- **Incomplete representation**: Steve Jobs served as Apple chairman twice under very different circumstances. Both events collapse to `(Steve Jobs, chairman_of, Apple Inc.)`, losing the context that differentiates them.
- **Ineffective reasoning**: Rule-based KG reasoning learns patterns like `(X, works_in, Y) + (Y, city_of, Z) → (X, citizen_of, Z)` — but these probabilistic rules break in edge cases that context would resolve.

### Formal Definition

A Context Graph is defined as:

```
CG = {E, R, Q, EC, RC}
```

Where:
- `E` = entities, `R` = relations
- `Q` = set of factual quadruples `(h, r, t, rc)` where `rc ∈ RC` is the relation context
- `EC` = entity context set; each entity `e` is represented as `(e, ec)`
- `RC` = relation context set

### Categories of Contextual Data

| Category | Context Type | Examples |
|---|---|---|
| Entity Context | Attribute | Height, price, color |
| Entity Context | Type | Actor, scientist, landmark |
| Entity Context | Description | Biographical text |
| Entity Context | Alias | Istanbul / Constantinople |
| Entity Context | Reference Link | Wikipedia, official sites |
| Entity Context | Image / Speech / Video | Photos, audio, video clips |
| Relation Context | Temporal | Obama president of USA, 2009–2017 |
| Relation Context | Geographic | France won 2018 FIFA World Cup in Russia |
| Relation Context | Quantitative | Berkshire holds 790M Apple shares |
| Relation Context | Provenance | Source documents, news articles |
| Relation Context | Confidence Level | Extraction model accuracy |
| Relation Context | Event-specific | Argentina beat France in 2022 World Cup final |
| Relation Context | Supplementary | News topics, engagement metrics |

### CGR³ Reasoning Paradigm

The paper introduces **CGR³** (Context Graph Reasoning: Retrieve → Rank → Reason), a three-step LLM-augmented reasoning loop over CGs:

1. **Retrieve** — pull candidate entities and related contexts from the CG using both embedding-based KGC models and LLM-generated candidates from Wikipedia paragraphs
2. **Rank** — re-rank candidates using a fine-tuned LLM (Llama-3-8B with LoRA/SFT) that scores plausibility based on entity descriptions and contextual relevance
3. **Reason** — LLM determines whether sufficient context has been retrieved to answer; if not, the loop iterates with new reasoning paths

For **KG Question Answering**, CGR³ uses beam search (width M, depth D_max) to iteratively explore reasoning paths, pruning at each step using contextual relevance scores (bge-large-en-v1.5 embeddings).

### Benchmark Results

Evaluated on FB15k-237 and YAGO3-10 datasets:

| Model | Hits@1 (FB15k-237) | Improvement |
|---|---|---|
| ComplEx baseline | 0.158 | — |
| ComplEx + CGR³ | 0.263 | +66.5% |
| RotatE baseline | 0.241 | — |
| RotatE + CGR³ | 0.293 | +21.6% |
| GIE baseline | 0.271 | — |
| GIE + CGR³ | 0.301 | +11.1% |

Average Hits@1 improvement across models: **+33% on FB15k-237**, **+14.8% on YAGO3-10**.

For KGQA (QALD10-en and WikiWebQuestions), CGR³ achieves new SOTA among prompting-based methods:

| Method | QALD10-en EM | WWQ EM |
|---|---|---|
| Prior prompting SOTA | 50.2 | 72.6 |
| CGR³ | 54.7 | 78.8 |
| CGR³ w/o context | 38.1 | 67.3 |

Removing contextual information drops QALD10-en accuracy by 43.6% relative — the strongest signal for the value of context in KG reasoning.

### Context Extraction Pipeline

- **Entity contexts**: Map KG entity IDs to Wikidata QIDs via `owl:sameAs`; collect label, short description, aliases, and first Wikipedia paragraph
- **Relation contexts**: Aggregate Wikipedia pages of head and tail entities; use Sentence-BERT to extract top-γ supporting sentences that best reflect the triple's semantics

---

## Part 2 — Context Graphs as Agentic Business Assets (Foundation Capital, 2025)

### The Problem: Decision Traces Are Never Captured

Enterprise systems of record (CRMs, ERPs, ticketing systems) store *current state* — what the opportunity looks like now, what the ticket says today. They do not store the *reasoning* that produced each state transition. Specifically, four categories of organizational knowledge are systematically lost:

- **Exception logic in people's heads**: "We always give healthcare companies an extra 10% because their procurement cycles are brutal." Not in the CRM.
- **Precedent from past decisions**: "We structured a similar deal for Company X last quarter." No system links those two deals or records why.
- **Cross-system synthesis**: A support lead checks ARR in Salesforce, open escalations in Zendesk, a Slack thread flagging churn risk, and decides to escalate. The ticket just says "escalated to Tier 3."
- **Approval chains outside systems**: A VP approves a discount on a Zoom call. The opportunity record shows the final price, not who approved the deviation or why.

### The Context Graph as Durable Artifact

When agent orchestration layers emit a **decision trace** on every run, they produce something enterprises almost never have: a structured, replayable history of how context turned into action.

A context graph in this sense connects the entities a business already cares about — accounts, renewals, tickets, incidents, policies, approvers, agent runs — via **decision events** (the moments that matter) and **"why" links** (the rationale). Over time:

- Captured decision traces become searchable precedent
- Every automated decision adds another trace to the graph
- Similar cases can be automated because the system has a structured library of prior decisions and exceptions
- Even human decisions grow the graph, because the workflow layer captures inputs, approval, and rationale as durable precedent instead of letting it die in Slack

### Why Incumbents Cannot Build This

| Player | Why They Fall Short |
|---|---|
| Salesforce / ServiceNow / Workday | Built on current-state storage; agents inherit the parent's architectural limitation — context that justified a decision isn't preserved, so you can't replay or audit it |
| Snowflake / Databricks | In the read path, not the write path; data arrives via ETL *after* decisions are made; decision context is already gone by the time it lands in the warehouse |
| Any incumbent | Capturing decision traces requires being in the execution path at commit time — you cannot bolt on governance after the fact |

### Three Startup Paths

| Path | Description | Example |
|---|---|---|
| Replace existing systems of record | CRM/ERP rebuilt around agentic execution with event-sourced state and policy capture native to the architecture | Regie (AI-native sales engagement replacing Outreach/Salesloft) |
| Replace modules, not entire systems | Target sub-workflows where exceptions and approvals concentrate; become the system of record for those decisions while syncing final state back to the incumbent | Maximor (finance: cash, close management, core accounting) |
| Create entirely new systems of record | Start as orchestration layer; persist what enterprises never stored — the decision-making trace; the agent layer becomes the place the business goes to answer "why did we do that?" | PlayerZero (production engineering: living model of how code, config, infrastructure, and customer behavior interact) |

### Signals for Where to Build

Two signals apply broadly:
- **High headcount on a workflow**: 50+ people doing manual routing, triage, or reconciliation signals decision logic too complex for traditional automation
- **Exception-heavy decisions**: Deal desks, underwriting, compliance reviews, escalation management — anywhere "it depends" is the honest answer

One signal points specifically to new system-of-record opportunities:
- **Organizations that exist at the intersection of systems**: RevOps (sales + finance + marketing + CS), DevOps (dev + IT + support), Security Ops (IT + engineering + compliance). These "glue functions" emerge precisely because no single system of record owns the cross-functional workflow.

---

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Context extraction quality | Triple-based KGs discard the sentences that gave a relation its meaning | Use Sentence-BERT to retrieve top-γ supporting sentences from Wikipedia as relation contexts; map entities to Wikidata QIDs for entity contexts |
| LLM ranking without fine-tuning | Vanilla LLMs perform poorly at entity ranking tasks even with context | Apply SFT with LoRA on a ranking objective; fine-tuned Llama-3-8B significantly outperforms ChatGPT on re-ranking |
| Long-tail entity coverage | Embedding models fail on entities with few neighbors | CGR³ reasoning module generates candidates from Wikipedia paragraphs, bypassing the structural sparsity of the KG |
| Decision trace capture | Agent reasoning evaporates into Slack/Zoom; no durable artifact | Instrument the orchestration layer to emit a structured decision trace on every run — inputs gathered, policies applied, exceptions granted, approvals, rationale |
| Incumbent lock-in | Existing systems of record will restrict API access and raise egress fees | Build in the execution path at commit time; incumbents cannot insert themselves into an orchestration layer they were never part of |
| Precedent reuse | Same edge cases re-litigated every quarter | Captured decision traces become searchable precedent; automate similar cases progressively as the library grows |

## See Also

- [Context Engineering Challenges](./challenges.md) — context rot, poisoning, distraction, confusion, clash
- [Context Engineering Strategies](./strategies.md) — offload, reduce, retrieve, isolate, cache
- [Agent Memory Management](../AgentMemory/README.md) — persistent memory strategies including episodic and semantic memory
- [Multi-Agent Systems](../Architecture/multi-agent-system.md) — orchestration layers where decision traces are generated
- [Production Best Practices: Context Engineering](../ProductionBestPractices/context-engineering.md) — production guidance
- [Production Best Practices: State & Memory](../ProductionBestPractices/state-memory.md) — durable state patterns
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md) — retrieval-based context management

## References

- [Context Graphs — AI's Trillion-Dollar Opportunity](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity) — Foundation Capital essay on context graphs as the durable decision-trace layer for agentic enterprise systems (2025)
- [Context Graph (arXiv:2406.11160v3)](https://arxiv.org/html/2406.11160v3) — Xu et al., IDEA Research: formal definition of Context Graphs, CGR³ reasoning paradigm, and benchmark results on KGC and KGQA tasks (2024)
