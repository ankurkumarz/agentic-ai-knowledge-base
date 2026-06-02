# Research Papers & Technical White Papers on Agent Memory

## Overview

This section curates key research papers and technical white papers that have shaped the field of agent memory management. These works provide the theoretical foundations and practical implementations that underpin modern memory systems for AI agents.

## Foundational Research Papers

### MemGPT: Towards LLMs as Operating Systems
**Authors**: Packer et al. (UC Berkeley)
**Resource**: [ArXiv Paper](https://arxiv.org/abs/2310.08560)

Introduced the concept of treating LLMs like operating systems that manage their own memory hierarchy. MemGPT implements a virtual context management system where the LLM can explicitly move data between a limited "main context" (analogous to RAM) and unlimited "external storage" (analogous to disk). This paper established the foundation for the Letta framework.

![MemGPT Architecture](../assets/images/memgpt-os.jpg)

**Key Contributions**:
- OS-inspired memory hierarchy for LLMs
- Self-directed memory management via function calls
- Demonstrated that LLMs can manage their own context window
- Enabled unbounded conversation length without context overflow

---

### Generative Agents: Interactive Simulacra of Human Behavior
**Authors**: Park et al. (Stanford / Google)
**Resource**: [ArXiv Paper](https://arxiv.org/abs/2304.03442)

Landmark paper demonstrating AI agents with believable human-like behavior in a simulated environment. Introduced the concept of agents that maintain a memory stream, perform reflection to extract higher-level insights, and use retrieved memories to plan future actions.

**Key Contributions**:
- Memory stream architecture (comprehensive log of agent experiences)
- Reflection mechanism: agents periodically synthesize memories into higher-level insights
- Retrieval function combining recency, importance, and relevance
- Demonstrated emergent social behaviors from memory-driven agents

---

### Cognitive Architectures for Language Agents (CoALA)
**Authors**: Sumers et al. (Princeton)
**Resource**: [ArXiv Paper](https://arxiv.org/abs/2309.02427)

Provides a systematic framework for understanding and designing cognitive architectures for language agents. Defines the canonical four-type memory taxonomy — working memory, semantic memory, episodic memory, and procedural memory — drawing directly on cognitive science. This taxonomy has become the standard reference for agent memory design.

**Key Contributions**:
- **Working memory**: The active in-context state the agent reasons over at inference time
- **Semantic memory**: Durable facts and knowledge about users, entities, and the world (preferences, definitions, reference data)
- **Episodic memory**: Specific past experiences — what happened in prior sessions, how similar tasks resolved
- **Procedural memory**: Behavioral rules, guidelines, and learned procedures that shape how the agent acts
- Unified framework for comparing different agent architectures
- Analysis of existing systems (ReAct, Reflexion, AutoGPT) through the CoALA lens

---

### MemoryBank: Enhancing LLMs with Long-Term Memory
**Authors**: Zhong et al.
**Resource**: [ArXiv Paper](https://arxiv.org/abs/2305.10250)

Proposes MemoryBank, a novel memory mechanism that equips LLMs with long-term memory capabilities. Implements a memory updating mechanism inspired by the Ebbinghaus Forgetting Curve — memories decay over time unless reinforced.

**Key Contributions**:
- Long-term memory storage and retrieval for LLMs
- Forgetting curve-inspired memory decay and reinforcement
- Demonstrated improved personalization in long-term interactions
- Memory summarization and consolidation strategies

---

---

### LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory
**Authors**: Wu et al. (UCLA NLP)
**Resource**: [Paper (ICLR 2025)](https://arxiv.org/abs/2410.10813) | [GitHub](https://github.com/xiaowu0162/LongMemEval) | [Website](https://xiaowu0162.github.io/long-mem-eval/)

Introduces a rigorous benchmark for evaluating long-term memory in LLM-powered chat assistants. Formalizes a three-stage memory architecture (Indexing → Retrieval → Reading) and establishes five core memory abilities as evaluation axes: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. The 500-question dataset uses timestamped multi-session chat histories generated via an attribute-controlled pipeline.

**Key Contributions**:
- Three-stage memory architecture formalization (Indexing, Retrieval, Reading) as an evaluation framework
- Five-ability taxonomy covering the full spectrum of long-term memory demands on chat assistants
- Revealed that retrieval systems struggle most with temporal reasoning and knowledge updates
- Key expansion strategies (summarization, keyphrase extraction, user facts) shown to improve retrieval precision in RAG pipelines

---

### LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
**Authors**: Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang (UCLA NLP)
**Resource**: [Paper (arXiv 2605.12493, May 2026)](https://arxiv.org/abs/2605.12493) | [Website](https://xiaowu0162.github.io/long-mem-eval/)

Extends LongMemEval to the agentic domain, evaluating whether memory systems enable web agents to accumulate environment-specific procedural knowledge across long task trajectories. The benchmark uses 451 manually curated questions paired with up to 500 agent trajectories (up to 115M tokens) drawn from real web environments (WebArena, WorkArena). Introduces five agentic memory abilities: static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness.

**Key Contributions**:
- Shift in evaluation focus from episodic/conversational memory to procedural/environmental memory for agents
- Environments: Magento shopping, shopping admin, Postmill forum, ServiceNow — representing realistic enterprise and e-commerce agent deployments
- Reveals that current memory systems fail to effectively internalize environment-specific operational experience at scale
- Establishes the "knowledgeable colleague" framing: the goal is not recall accuracy but actionable operational expertise

---

## Technical White Papers and Blogs

### AgentFS: The Missing Abstraction for the Agentic World
**Source**: Turso
**Resource**: [Technical Blog](https://turso.tech/blog/agentfs-the-missing-abstraction-for-the-agent-ic-world)

Introduces AgentFS, a portable SQLite-backed virtual filesystem that acts as a persistent "hard drive" for AI agents. Argues that agents need a filesystem abstraction — not just a vector database — to manage files, key-value state, and tool logs in a structured way.

**Key Contributions**:
- Filesystem metaphor for agent persistent storage
- SQLite-backed implementation for portability
- Framework-agnostic design
- Single movable .db file architecture

---

### The Mem0 Memory Layer Architecture
**Source**: Mem0.ai
**Resource**: [Technical Documentation](https://docs.mem0.ai/overview) | [Research Paper](https://arxiv.org/abs/2504.19413)

Describes Mem0's architecture for providing a universal, self-improving memory layer for AI agents. The system automatically extracts user preferences and facts from conversations, stores them in a hybrid vector + graph store, and retrieves relevant memories for future interactions.

**Key Contributions**:
- Automatic memory extraction without explicit agent instructions
- Hybrid storage combining vector search and knowledge graphs
- Cross-session memory persistence
- Self-improving memory through contradiction resolution

---

### Graphiti: Temporal Knowledge Graphs for Agent Memory
**Source**: Zep
**Resource**: [GitHub Documentation](https://github.com/getzep/graphiti)

Introduces Graphiti, an open-source temporal knowledge graph framework that tracks how facts and relationships evolve over time. Unlike static knowledge graphs, Graphiti maintains the history of fact changes, enabling agents to reason about when information was true.

**Key Contributions**:
- Temporal knowledge graph with fact versioning
- Bi-temporal data model (valid time + transaction time)
- Efficient graph traversal for multi-hop reasoning
- Integration with Zep's memory platform

---

### LangMem: Long-term Learning for LangGraph
**Source**: LangChain
**Resource**: [Technical Blog](https://blog.langchain.dev/langmem/)

Describes LangMem, LangChain's approach to long-term memory for LangGraph agents. Provides a managed service for storing and retrieving memories across sessions, with support for different memory types (semantic, episodic, procedural).

**Key Contributions**:
- Integrated long-term memory for LangGraph workflows
- Multiple memory storage backends
- Automatic memory extraction and consolidation
- Memory namespacing for multi-user applications

---

### Awesome-LLM-Memory (Curated List)
**Source**: GitHub Community
**Resource**: [GitHub Repository](https://github.com/mshumer/Awesome-LLM-Memory)

A community-maintained curated list of papers, tools, and resources related to LLM memory. Provides a comprehensive overview of the field with regular updates.

---

## Key Research Themes

### Memory Retrieval
How agents decide what to retrieve from memory:
- **Recency**: Prefer more recent memories
- **Relevance**: Semantic similarity to current context
- **Importance**: Salience score assigned at storage time
- **Combined scoring**: Weighted combination of multiple factors (as in Generative Agents)

### Memory Consolidation
How agents transform raw experiences into reusable knowledge:
- **Summarization**: Compress multiple episodes into a summary
- **Reflection**: Extract higher-level insights from patterns
- **Abstraction**: Generalize from specific examples to rules
- **Forgetting**: Decay or remove low-importance memories

### Memory Architecture Patterns
- **Flat memory**: Single undifferentiated store (simple but doesn't scale)
- **Hierarchical memory**: Multiple tiers with different access speeds and capacities
- **Associative memory**: Content-addressable retrieval based on similarity
- **Structured memory**: Typed stores for different information categories

## See Also

- [Functional Memory Tiers](functional-tiers.md)
- [Long-term Memory Strategies](ltm-strategies.md)
- [Short-term Memory Management](short-term.md)
- [Agent Memory README](README.md)
- [Agent Evaluation Benchmarks](../Benchmarks/agent-benchmarks.md) — LongMemEval benchmark details and selection guide
