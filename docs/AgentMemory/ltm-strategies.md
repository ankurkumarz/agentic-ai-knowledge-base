# Long-Term Memory (LTM) Strategies

## Overview

Long-term memory for AI agents spans three distinct types from the CoALA taxonomy: **semantic memory** (durable facts and knowledge), **episodic memory** (specific past experiences), and **procedural memory** (behavioral rules and learned procedures). Each type has different retrieval patterns, storage requirements, and update mechanisms. The right strategy depends on which type of long-term memory you are building.

## Memory Type → Strategy Mapping

| Memory Type | Primary Strategies | Storage Technologies |
|---|---|---|
| **Semantic** | Vector RAG, Knowledge Graphs, Entity Extraction | Vector DB, Graph DB, SQL/NoSQL |
| **Episodic** | Episodic Logging, Incremental Summary, Vector Search over events | Structured Logs, Vector DB with timestamps |
| **Procedural** | System Prompt encoding, Reflection/Consolidation, Fine-tuning | Instruction files, Model weights, Rule libraries |

## Core LTM Strategies

### 1. Vector RAG (Retrieval-Augmented Generation)

**Memory type**: Semantic and Episodic

**Mechanism**: Text is embedded into high-dimensional numerical vectors. Retrieval is based on mathematical "closeness" (cosine similarity or dot product) between the query vector and stored vectors.

**Best For**: Fuzzy matching, semantic search, and general knowledge retrieval where exact keyword matching is insufficient.

**Storage**: Vector databases (Pinecone, Chroma, Weaviate, FAISS, pgvector)

**How It Works**:
1. Text chunks are embedded using an embedding model (e.g., OpenAI text-embedding-3, Cohere embed)
2. Embeddings are stored in a vector database with metadata
3. At retrieval time, the query is embedded and nearest neighbors are found
4. Top-k results are injected into the agent's context

**Limitations**: Struggles with precise factual recall, multi-hop reasoning, and relational queries. For relationship-aware retrieval, combine with Knowledge Graphs (see Graph RAG below).

**Vector index architectures** (relevant for store selection):

| Index | Recall | Scale | Memory per 1K vectors (d=1536) | Best For |
|---|---|---|---|---|
| Flat | Exact | < 100K docs | — | Dev/prototype |
| HNSW (M=16, ef default) | ~95–99% | Up to ~100M vectors (RAM-bound) | ~120 KB | < 5ms P99 SLA; native incremental inserts; default for session memory retrieval |
| IVF + PQ (nlist/nprobe tuned) | ~90–95% (recoverable with re-ranker) | > 100M–1B+ vectors | ~8–15 KB | Billion-scale corpora; batch nightly rebuild pattern |

**HNSW key parameters**: `M` (edges per node, default 16): ↑M = ↑recall, ↑memory. `ef_construction` (build recall): ↑ = ↑quality, ↑build time. Best for latency-sensitive workloads (sub-5ms P99). Weakness: memory-heavy; rebuild required on major updates.

**IVF+PQ key parameters**: `nlist` (# clusters): ↑ = finer partition. `nprobe` (cells to search): ↑ = ↑recall, ↑latency. Product Quantization compresses 1536-dim float32 → 8-byte code (8–32× size reduction). Lower recall than HNSW at same latency; PQ adds quantization error — add a re-ranking layer to recover.

**Selection guide**:
- Corpus < 10M vectors → HNSW (default)
- 10M–100M vectors → benchmark both
- > 100M vectors → IVF + PQ
- Corpus updates continuously (new records daily) → prefer HNSW (native incremental inserts avoid nightly full rebuild)
- Using a cross-encoder re-ranker downstream → IVF recall loss at ANN stage is recoverable; optimize the full pipeline together, not ANN in isolation

**Hybrid search**: Combining vector similarity with BM25 keyword search via Reciprocal Rank Fusion (RRF) improves recall for proper nouns, technical identifiers, and domain terminology the embedding model may not represent well. Full hybrid pipeline with latency breakdown:

| Stage | Component | Latency |
|---|---|---|
| Sparse retrieval | BM25 (term frequency × IDF) | +5ms |
| Dense retrieval | HNSW cosine similarity | +15ms |
| Fusion | RRF: score = 1/(60+r_dense) + 1/(60+r_sparse) | +2ms |
| Re-ranking | Cross-encoder full attention pass per (query, chunk) pair | +40ms |
| **Total** | End-to-end | **~62ms** |

Dense-only retrieval fails for DevOps-style queries involving exact version strings, error codes (e.g., `ERR_TOO_MANY_REDIRECTS`), or CVE identifiers — BM25 exact token match is essential for these cases.

**Re-ranking tradeoff**: +40ms is worth it when the query is ambiguous, the corpus has many near-duplicate chunks, or the interaction is not real-time (batch workflows, background research).

**Weaviate and Amazon Bedrock Knowledge Bases** (OpenSearch Serverless) both support hybrid search natively. Amazon Bedrock Knowledge Bases supports built-in reranking.

---

### 2. Knowledge Graphs

**Memory type**: Semantic

**Mechanism**: Data is represented as nodes (entities) and edges (relationships). Example: `User` → `owns` → `MacBook Pro`.

**Best For**: Relational reasoning, factual rigor, and multi-hop questions (e.g., "Who approved the budget for the project that Alice manages?").

**Storage**: Graph databases (Neo4j, FalkorDB, Amazon Neptune)

**How It Works**:
1. Entities and relationships are extracted from text using NLP or LLMs
2. Stored as a property graph with typed nodes and edges
3. Queries use graph traversal (Cypher, SPARQL) or LLM-guided navigation
4. Results are formatted and injected into context

**Advantages**: Precise factual recall, explainable reasoning paths, handles complex relationships.

**Solutions**: [Graphiti by Zep](https://github.com/getzep/graphiti) — a temporal knowledge graph that tracks how facts evolve over time.

---

### 2b. Graph RAG

**Memory type**: Semantic (relational)

**Mechanism**: Extends standard RAG with graph traversal — the query first matches an entity node via semantic vector search, then traverses the graph to collect structurally related entities. Agents receive both directly matched content and relationship-derived context.

**Best For**: Domains with many-to-many entity relationships that matter for answering queries — service dependency analysis, blast-radius assessment, ownership chains, root-cause investigation.

**Storage**: Property graph database (Neo4j AuraDB, Amazon Neptune) with co-located vector indexes on node properties

**How It Works**:
1. Entities and relationships are extracted and written to a graph database (nodes carry embedding vectors as properties)
2. At retrieval, the query is embedded and matched to the nearest entry-point nodes via vector similarity
3. Graph traversal expands from those nodes — first-degree relationships (direct dependencies) or multi-hop (second-order dependents)
4. Matched nodes + traversal-collected related entities are combined and injected into context

**Two traversal strategies:**
- **Entity-first**: Query anchors to a named entity, traversal expands from it. Best for "what depends on service X?"
- **Community-first**: Pre-processed graph clusters (communities) are identified; retrieval finds the most relevant community, then representative nodes. Best for open-ended structural queries.

**When Graph RAG is worth the complexity**: Three conditions must hold simultaneously — the domain has many-to-many relationships that matter for agent queries; those relationships are not well-expressed in free-text documents; agents regularly need to reason over relationship structure. If vector retrieval already answers queries well, graph infrastructure adds overhead without measurable gain.

**Solutions**: [Neo4j AuraDB](https://aws.amazon.com/marketplace/pp/prodview-xd42uzj2v7dae) on AWS Marketplace — native vector index on node properties, Cypher for composable graph + vector queries in one round-trip, native LangChain integration (`Neo4jVector`, `GraphCypherQAChain`). Graphiti (see above) also implements a temporal knowledge graph suitable for Graph RAG patterns.

---

### 3. Entity Extraction

**Memory type**: Semantic

**Mechanism**: An LLM extracts specific facts (names, dates, preferences, attributes) from conversations and stores them in structured tables.

**Best For**: Personalization and fixed attributes (e.g., "The user is allergic to peanuts", "The user's preferred language is Spanish").

**Storage**: SQL or NoSQL databases (PostgreSQL, Redis, DynamoDB)

**How It Works**:
1. After each interaction, an extraction LLM identifies key facts
2. Facts are stored as structured key-value pairs or records
3. At the start of each session, relevant facts are retrieved and injected into the system prompt
4. Facts are updated or overwritten when contradicted by new information

**Example**:
```json
{
  "user_id": "u123",
  "preferences": {
    "language": "Python",
    "timezone": "PST",
    "communication_style": "concise"
  },
  "facts": [
    "Works at Acme Corp as a senior engineer",
    "Prefers dark mode in all tools"
  ]
}
```

---

### 4. Incremental Summary

**Memory type**: Episodic

**Mechanism**: Periodically condenses old interaction logs into a running "narrative" or profile summary.

**Best For**: Long-term context without keeping every message word-for-word. Useful for maintaining a coherent user profile over hundreds of interactions.

**Storage**: Text files, document databases, or key-value stores

**How It Works**:
1. After N interactions or a time period, a summarization LLM processes recent history
2. The summary is merged with the existing profile summary
3. Old raw logs are archived or deleted
4. The summary is injected into the system prompt at session start

**Tradeoff**: Loses fine-grained detail in exchange for compact, persistent context.

---

### 5. Reflection / Consolidation

**Memory type**: Procedural (and Semantic)

**Mechanism**: A background process where the agent "thinks" about past logs to extract learnings, update beliefs, and improve future behavior.

**Best For**: Continuous improvement and self-correction (e.g., "Method A failed twice; use Method B next time").

**Storage**: Specialized databases or AgentFS

**How It Works**:
1. A reflection agent periodically reviews episodic memory logs
2. It identifies patterns, failures, and successful strategies
3. Extracted insights are stored as long-term knowledge
4. Future agent instances benefit from these consolidated learnings

**AWS implementation pattern**: An EventBridge Scheduler-triggered Step Functions workflow queries the session memory store for recently closed sessions, runs a consolidation LLM call (Amazon Bedrock text generation) for each session, writes the results as structured JSON records to the long-term semantic memory store, and marks the session as consolidated. The consolidation prompt targets specific extraction fields — user preferences, configuration facts, resolved problems, outstanding issues, key decisions — rather than producing a generic summary.

Two scheduling variants:
- **Scheduled consolidation**: Runs nightly on all closed sessions. Predictable and easy to operate; introduces a lag between session close and LTM availability.
- **Threshold-triggered consolidation**: Fires when a session exceeds a token count threshold; runs a partial consolidation on the oldest portion, replacing it with a compact structured summary. Keeps session memory bounded without discarding older context, and makes consolidated facts available within the same session.

**Research Foundation**: Inspired by the [Generative Agents paper](https://arxiv.org/abs/2304.03442) (Park et al., Stanford/Google) which demonstrated agents that reflect on their experiences to form higher-level insights.

---

### 6. Dreaming (Scheduled Memory Consolidation)

**Memory type**: Procedural and Semantic

**Mechanism**: A scheduled asynchronous job that runs **between** agent sessions — not during active task execution. The agent reviews its own episodic session transcripts alongside an existing memory store, deduplicates content, removes outdated or contradicted facts, and consolidates reusable learnings into a **new, reorganized memory store**. The input store is never modified (non-destructive). Named by Anthropic as a deliberate reference to hippocampal memory consolidation during biological sleep.

**Best For**: Long-running agents that accumulate experience over many sessions and need to self-improve without retraining. Particularly valuable when the same agent handles recurring workflows or team-level preferences need to propagate across sessions.

**Storage**: Filesystem-based memory stores (text/markdown files, addressed by path); managed as workspace-scoped collections

**How It Works (Anthropic Claude Managed Agents implementation)**:
1. Developer submits a dream job via `POST /v1/dreams` with an input memory store + 1–100 past session IDs
2. Dream runs asynchronously (minutes to tens of minutes); lifecycle: `pending → running → completed/failed/canceled`
3. While running, the pipeline can be watched in real time via the session event stream (`dream.session_id`)
4. On completion, a new output memory store is created — review it via API or Console, then either attach to future sessions or discard
5. The input memory store and input sessions are never modified

**Key operations performed during dreaming**:
- Merges new signal into existing topic files rather than creating near-duplicates
- Removes outdated or contradicted facts
- Converts relative dates to absolute dates for temporal durability
- Surfaces recurring patterns: repeated mistakes, team preferences, converged workflows

**Supported models**: `claude-opus-4-7`, `claude-sonnet-4-6`  
**Session input limit**: 100 sessions per dream  
**Billing**: Standard token rates; scales linearly with session count and length

**Production evidence**: Harvey (legal AI) reported ~6× jump in task completion rates using Dreaming + Outcomes on Claude Managed Agents (May 2026).

**Relationship to Reflection/Consolidation**: Dreaming is a productized, scheduled, and non-destructive implementation of the Reflection/Consolidation strategy from the CoALA taxonomy — same conceptual foundation, with concrete API controls, lifecycle management, and audit trail.

---

### 7. Episodic Logging

**Memory type**: Episodic

**Mechanism**: Stores specific past events as discrete "episodes" with timestamps and outcome metadata.

**Best For**: Temporal reasoning and recalling "What exactly happened last Tuesday?" or "What was the outcome of the last deployment?"

**Storage**: Structured logs with metadata indexing

**How It Works**:
1. Each significant event is stored as an episode with: timestamp, participants, actions taken, outcome, and context
2. Episodes are indexed by time, topic, and outcome
3. Retrieval uses temporal filters combined with semantic search
4. Retrieved episodes provide concrete examples for the agent to reason from

---

### 8. Procedural Memory Encoding

**Memory type**: Procedural

**Mechanism**: Behavioral rules, guidelines, and learned procedures are encoded into the agent's instruction layer — either as explicit text in a system prompt / AGENTS.md file, or baked into model weights via fine-tuning.

**Best For**: Consistent agent behavior across sessions — tool preferences, escalation rules, communication style, negative constraints ("never do X").

**Storage**: System prompts, instruction files (AGENTS.md), fine-tuned model weights, rule libraries

**How It Works**:
1. Rules are authored explicitly (by humans) or extracted by a reflection agent from episodic logs
2. High-frequency, stable rules go into the system prompt or instruction file (immediate, zero retrieval cost)
3. Large or dynamic rule sets are stored externally and retrieved at session start
4. Fine-tuning encodes deeply ingrained procedures into model weights for zero-latency access

**Example**:
```
# Behavioral rules (procedural memory in system prompt)
- Always escalate billing disputes to a human agent
- Prefer the search_knowledge_base tool over web_search for internal queries
- Never reveal internal cost structures to external users
- When a user expresses frustration, acknowledge before problem-solving
```

**Tradeoff**: Rules in the system prompt consume context window tokens. Large rule sets should be stored externally and retrieved selectively.

---

### 9. Amazon Bedrock AgentCore Memory — Managed Extraction Pipeline

**Memory type**: Episodic and Semantic

**Mechanism**: A fully managed service that stores raw turn-by-turn events per session (short-term) and asynchronously extracts insights via an Extraction → Consolidation → Reflection pipeline (long-term). Key insights — preferences, facts, summaries, episodes — persist across all future sessions.

**Event storage**: Agents call `CreateEvent` each turn; the full conversation history is reloaded via `ListEvents` on subsequent turns. Event retention: up to 365 days, KMS encryption, namespaced by `sessionId + actorId`.

**Long-term extraction**: `RetrieveMemoryRecords` provides semantic search over extracted records with metadata filters. Four record types produced by extraction:

| Record Type | Description |
|---|---|
| Semantic facts | Knowledge extracted from conversations |
| User preferences | Preferences retained across sessions |
| Summary | Session summaries for cross-session continuity |
| Episodic | Structured episodes: actor · action · outcome |

**Extraction strategy tiers** — choose based on control needs:

| Tier | Mode | Tradeoffs |
|---|---|---|
| Built-in (zero config) | AgentCore manages entire pipeline with predefined algorithms | Lowest cost, no customization; ideal for standard conversational agents |
| Built-in with overrides | Modify extraction prompts, keep managed pipeline | Moderate cost; targets customization without full DIY |
| Custom (self-managed) | Any model, any prompt, custom record schemas, external DB integration (MongoDB Atlas, Neo4j AuraDB) | Full control, highest operational cost |

---

### 10. Three-Tier Partner Memory Stack (Redis Cloud → MongoDB Atlas → Neo4j AuraDB)

**Memory type**: Session (hot path), Long-term document + vector, Graph

**Mechanism**: Three complementary data stores, each occupying a distinct tier of the memory stack. They are not alternatives — each has a different role.

| Tier | Store | Latency | Role |
|---|---|---|---|
| Session (hot path) | Amazon ElastiCache (default) or Redis Cloud | < 2ms | TTL-bounded, sub-millisecond session state; upgrade to Redis Cloud for geo-distribution or corpus exceeding DRAM |
| Long-term document + vector | Amazon Bedrock Knowledge Bases + OpenSearch (default) or MongoDB Atlas | ~18ms | Durable filtered semantic retrieval; MongoDB Atlas unifies document store + vector index in one collection |
| Graph structural knowledge | Amazon Neptune (default) or Neo4j AuraDB | ~30ms | Relationship traversal, topology queries; use when dependency/ownership relationships are structural facts, not prose |

**Redis Cloud for session state**: When ElastiCache limits are exceeded (multi-region active-active, session corpus > available DRAM), Redis Cloud adds CRDTs (active-active geo-replication), Redis on Flash, and enterprise clustering. Data structures fit for agent session state:
- `Hash` — O(1) read/write per field; atomic partial updates; no JSON parse on load
- `Sorted Set (ZADD/ZREVRANGEBYSCORE)` — timestamp-scored windowed turn history; retrieves latest k turns without full scan
- `Stream (XADD)` — append-only session event log; replay for debugging; consumer groups for async processing

Migration from ElastiCache to Redis Cloud requires only updating `REDIS_URL` — no application code changes.

**MongoDB Atlas for long-term memory**: Unifies structured metadata filtering + vector similarity in a single aggregation pipeline. A memory record contains both structured fields (`session_id`, `service`, `env`, `outcome`) and a 1024-dim embedding vector. The aggregation pipeline runs `$vectorSearch` over the embedding field, then `$match` on metadata fields, reducing the search space before ANN scoring (~18ms total). Change Streams propagate new memory records to downstream pipelines in real time without polling.

**Hot/cold handoff pattern**: When a Redis session expires (TTL or explicit close), an Amazon EventBridge rule fires a Lambda that reads the history, runs a structured extraction call via Amazon Bedrock (Claude Haiku — 5× cheaper than Sonnet for well-defined extraction), validates output with Pydantic schema enforcement, and upserts the consolidated record to MongoDB Atlas using `session_id` as an idempotency key. DynamoDB serves as a fallback source of truth if the Redis key has already expired when Lambda fires.

---

For a full vendor comparison with Technology Radar ratings, see **[Memory Solutions](solutions.md)**.

Quick reference:

| Solution | Memory Types | Open Source | Best For |
|---|---|---|---|
| **Mem0** | Semantic, Episodic | Yes (Apache 2.0) | Personalization, cross-session user facts |
| **Graphiti (Zep)** | Semantic, Episodic | Yes (Apache 2.0) | Temporal/relational reasoning |
| **Letta** | Working, Semantic, Episodic | Yes (Apache 2.0) | OS-inspired autonomous agents |
| **LangMem** | Semantic, Episodic, Procedural | Yes (MIT) | LangGraph-native memory |
| **Claude Managed Agents Memory + Dreaming** | Episodic, Semantic, Procedural | No | Filesystem-based memory with scheduled consolidation (dreaming) and self-grading (outcomes) |
| **AWS AgentCore Memory** | Working, Semantic, Episodic | No | AWS-native managed memory |
| **Vertex Memory Bank** | Semantic | No | GCP-native managed memory |
| **Azure Foundry Memory** | Working, Semantic | No | Azure-native managed memory |

## Hybrid Approaches

Most production systems combine multiple strategies:

- **Vector RAG + Knowledge Graph**: Use vector search for broad retrieval, knowledge graph for precise factual queries
- **Entity Extraction + Incremental Summary**: Extract structured facts while maintaining a narrative summary
- **Episodic + Semantic**: Store raw episodes for debugging, extract semantic knowledge for efficiency

## Implementation Considerations

### Choosing the Right Strategy

| Factor | Memory Type | Recommendation |
|--------|-------------|----------------|
| Need semantic search over knowledge | Semantic | Vector RAG |
| Need precise facts and relationships | Semantic | Entity Extraction or Knowledge Graph |
| Need relationship reasoning | Semantic | Knowledge Graph |
| Need to recall past events | Episodic | Episodic Logging + Vector search |
| Need temporal tracking of facts | Episodic | Zep (temporal knowledge graph) |
| Need personalization | Semantic | Mem0 or Entity Extraction |
| Need consistent agent behavior | Procedural | System prompt / AGENTS.md |
| Need self-improvement from experience | Procedural | Reflection/Consolidation |
| Need to encode deep skills | Procedural | Fine-tuning |

### Privacy and Security
- Encrypt sensitive user data at rest and in transit
- Implement access controls so agents only access their own memory
- Provide users with the ability to view and delete their stored memories
- Apply data retention policies to comply with regulations (GDPR, CCPA)

## See Also

- [Four Memory Types](functional-tiers.md)
- [Short-term / Working Memory Management](short-term.md)
- [Agent Memory README](README.md)
- [Memory Solutions Radar](solutions.md)
- [Research Papers](research-papers.md)
- [Claude Managed Agents — Dreaming & Outcomes](../AgentPlatforms/claude-managed-agents.md)
- [Self-Learning Agents Reference Architecture](../ReferenceArchitecture/self-learning-agents.md)
- [AWS AgentCore Platform](../AgentPlatforms/aws-agentcore.md)
- [RAG Architecture — Hybrid Search and Vector Indexes](../ReferenceArchitecture/rag-architecture.md)

## References

- [AWS Marketplace — Agent Memory Systems (Module 7)](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-memory-systems) — AWS "Building Agentic Systems on AWS" series; covers memory taxonomy, vector store selection (HNSW vs IVF+PQ), Graph RAG with Neo4j, Redis/MongoDB hot-cold handoff, AgentCore Memory extraction tiers, and memory governance
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — Park et al. (Stanford/Google, 2023); foundational paper for Reflection/Consolidation strategy
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — Packer et al. (UC Berkeley, 2023); OS-inspired working memory management, basis for Letta
