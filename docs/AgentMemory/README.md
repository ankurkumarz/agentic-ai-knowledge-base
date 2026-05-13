# Agent Memory Management

Memory management is the "engine" that enables an AI agent to move from a one-shot calculator to a persistent entity. It is essentially the art of deciding what to keep in the expensive, high-speed context window and what to offload to external storage.

## Overview

Agent memory management encompasses the strategies, techniques, and architectures that enable AI agents to maintain state, learn from experience, and accumulate knowledge over time. Effective memory management is crucial for building agents that can handle complex, multi-session interactions while maintaining performance and coherence.

The canonical taxonomy comes from the **Cognitive Architectures for Language Agents (CoALA)** paper (Sumers et al., Princeton, 2023), which draws on cognitive science to define four distinct memory types. This framework has become the standard reference for agent memory design.

## Core Concepts of Memory Management

| Concept | Description | Analogy |
|---|---|---|
| Statefulness | The ability to track where an agent is in a multi-step workflow. | A saved game in a video game. |
| Paging / Swapping | Moving data between the "Active Context" and "Long-term Storage" as needed. | RAM vs. Hard Drive. |
| Context Engineering | Curating the prompt dynamically so only the most relevant 1% of data is sent to the LLM. | A desk where you only keep the files for your current task. |
| Reflection | A background process where the agent "thinks" about past logs to update its own memory. | Journaling before bed to remember lessons learned. |

## The Four Memory Types (CoALA Taxonomy)

The CoALA framework defines one active memory type and three long-term memory types. The long-term types differ in *what kind of information* they store, not just *how long* they store it.

### Working Memory
The active state the agent is reasoning over right now. This is the running conversation and the scratchpad the model sees at inference time — everything currently in the LLM's context window.

- **Scope**: Current task or conversation turn
- **Storage**: In-context (the LLM's context window itself)
- **Managed via**: Checkpointers, sliding windows, summarization, context pinning
- **Cleanup**: Summarized or truncated when the window fills

### Semantic Memory
The durable facts and knowledge the agent accumulates about users, entities, and the world: preferences, canonical definitions, structured reference data. This is the "what is true" store.

- **Scope**: Persistent across all sessions
- **Storage**: Vector databases, knowledge graphs, structured key-value stores
- **Examples**: "This user prefers Python", "Product X costs $49", entity relationship graphs
- **Managed via**: Entity extraction, vector RAG, knowledge graph updates

### Episodic Memory
Specific past experiences the agent can recall — what happened in a prior session, what the user asked three weeks ago, how a similar task resolved last time. This is the "what happened" store.

- **Scope**: Persistent, time-indexed event log
- **Storage**: Vector DBs with timestamp metadata, structured logs, AgentFS
- **Examples**: Past conversation summaries, tool call outcomes, task execution histories
- **Managed via**: Embedding + semantic search, temporal filtering, retention policies

### Procedural Memory
The behavioral rules, guidelines, and learned procedures that shape how the agent acts — how to handle customers, which tools to prefer, what not to do. This is the "how to behave" store.

- **Scope**: Persistent, updated through learning or explicit configuration
- **Storage**: System prompts, AGENTS.md / instruction files, fine-tuned model weights, code
- **Examples**: "Always escalate billing disputes to a human", "Prefer tool A over tool B for X", agent personas
- **Managed via**: Prompt engineering, fine-tuning, reflection-driven rule extraction

![Memory Architecture](../assets/images/agent-memory-architecture.png)

*Agent Memory Architecture — four memory types working together*

## Management Techniques

### Explicit Management
The agent uses a tool (e.g., `save_memory("user prefers dark mode")`) to consciously store a fact into semantic or procedural memory.

### Implicit Management
A separate, smaller LLM monitors the conversation in the background, extracts key insights, and updates the memory database automatically.

### Just-In-Time (JIT) Context
Instead of giving the agent a massive prompt, the agent uses tools to "lookup" what it needs (e.g., searching its own AgentFS files) only when a question requires it.

## Long-Term Memory (LTM) Strategies

| Strategy | Mechanism | Memory Type | Best For | Storage |
|---|---|---|---|---|
| Vector RAG | Text embedded into vectors; retrieved by semantic similarity. | Semantic / Episodic | Fuzzy matching, knowledge retrieval, past experience search. | Vector DB (Pinecone, Chroma) |
| Knowledge Graphs | Nodes (entities) and edges (relationships). | Semantic | Relational reasoning, multi-hop questions, factual rigor. | Graph DB (Neo4j, FalkorDB) |
| Entity Extraction | LLM extracts structured facts from conversations. | Semantic | Personalization, fixed attributes ("user is allergic to peanuts"). | SQL / NoSQL (Postgres, Redis) |
| Incremental Summary | Condenses old interaction logs into a running narrative. | Episodic | Long-term context without verbatim logs. | Text / Markdown files |
| Reflection / Consolidation | Background loop reviews logs to extract learnings and rules. | Procedural | Self-correction, rule extraction ("Method A failed twice; use B"). | AgentFS / Specialized DB |
| Episodic Log | Stores specific past events as discrete episodes with timestamps. | Episodic | Temporal reasoning, recalling prior session outcomes. | Structured Logs / Metadata |
| System Prompt / AGENTS.md | Behavioral rules and guidelines baked into the agent's instructions. | Procedural | Consistent agent behavior, tool preferences, escalation rules. | Prompt / Instruction files |

## Memory Solutions

For a full vendor comparison with Technology Radar ratings (Adopt / Trial / Assess / Caution), see the dedicated **[Memory Solutions page](solutions.md)**.

Quick reference for working memory techniques:

| Technique | Logic | Primary Benefit |
|---|---|---|
| Sliding Window | Retains only the last N messages, discarding oldest. | Prevents context overflow; low latency. |
| Token Trimming | Removes minimum tokens to stay within context limit. | Maximizes context window use without crashing. |
| Recursive Summarization | Condenses older messages into a summary paragraph. | Preserves narrative context while saving tokens. |
| Scratchpad | Dedicated space for intermediate thoughts and calculations. | Keeps conversation clean; offloads reasoning state. |
| Context Pinning | Locks critical info so it is never discarded by trimming. | Agent never forgets persona or core instructions. |

## Implementation Best Practices

### Memory Architecture Design

1. **Four-type approach**: Implement all four memory types (working, semantic, episodic, procedural) for comprehensive coverage
2. **Appropriate storage**: Match storage technology to memory type and access patterns
3. **Efficient retrieval**: Design indexing and search strategies for fast memory access
4. **Memory lifecycle**: Implement clear policies for memory creation, update, and deletion

### Performance Optimization

1. **Caching Strategies**: Cache frequently accessed memory elements
2. **Lazy Loading**: Load memory content only when needed
3. **Compression**: Use appropriate compression for long-term storage
4. **Indexing**: Maintain efficient indexes for fast retrieval

### Privacy and Security

1. **Access Control**: Implement proper permissions for memory access
2. **Encryption**: Encrypt sensitive memory content
3. **Isolation**: Ensure memory isolation between different users/sessions
4. **Audit Trails**: Maintain logs of memory access and modifications

## Future Directions

### Emerging Trends

- **Adaptive Memory Management**: AI-driven optimization of memory strategies
- **Cross-Agent Memory Sharing**: Standardized protocols for memory exchange
- **Federated Memory**: Distributed memory systems across multiple agents
- **Memory Compression**: Advanced techniques for efficient memory storage

### Research Opportunities

- **Memory Quality Metrics**: Standardized measures for memory effectiveness
- **Automated Memory Optimization**: Self-tuning memory management systems
- **Memory Interoperability**: Standards for memory sharing across platforms
- **Cognitive Memory Models**: Brain-inspired memory architectures for AI agents

## Related Topics

- [Context Engineering](../ContextEngineering/README.md): For context management strategies
- [Self-Learning Agents](../ReferenceArchitecture/self-learning-agents.md): For adaptive memory systems
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md): For retrieval-based memory patterns

## See Also

- **[Memory Solutions & Technology Radar](solutions.md)**: Vendor comparison with Adopt/Trial/Assess/Caution ratings
- **[The Four Memory Types](functional-tiers.md)**: CoALA taxonomy — working, semantic, episodic, procedural
- **[Long-term Memory Strategies](ltm-strategies.md)**: Strategy patterns per memory type
- **[Working Memory Management](short-term.md)**: In-context memory techniques
- **[Research Papers](research-papers.md)**: Foundational papers
- **[Context Engineering](../ContextEngineering/README.md)**: Context management strategies
- **[Agent Development Frameworks](../AgenticFrameworks/README.md)**: Framework support for memory management
