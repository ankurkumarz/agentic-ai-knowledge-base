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

**Limitations**: Struggles with precise factual recall, multi-hop reasoning, and relational queries.

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

**Research Foundation**: Inspired by the [Generative Agents paper](https://arxiv.org/abs/2304.03442) (Park et al., Stanford/Google) which demonstrated agents that reflect on their experiences to form higher-level insights.

---

### 6. Episodic Logging

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

### 7. Procedural Memory Encoding

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

## LTM Solutions

For a full vendor comparison with Technology Radar ratings, see **[Memory Solutions](solutions.md)**.

Quick reference:

| Solution | Memory Types | Open Source | Best For |
|---|---|---|---|
| **Mem0** | Semantic, Episodic | Yes (Apache 2.0) | Personalization, cross-session user facts |
| **Graphiti (Zep)** | Semantic, Episodic | Yes (Apache 2.0) | Temporal/relational reasoning |
| **Letta** | Working, Semantic, Episodic | Yes (Apache 2.0) | OS-inspired autonomous agents |
| **LangMem** | Semantic, Episodic, Procedural | Yes (MIT) | LangGraph-native memory |
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
- [Research Papers](research-papers.md)
