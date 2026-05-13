# The Four Memory Types of Agent Memory

## Overview

The canonical taxonomy for agent memory comes from the **Cognitive Architectures for Language Agents (CoALA)** paper (Sumers et al., Princeton, 2023 — [arXiv:2309.02427](https://arxiv.org/abs/2309.02427)). Drawing on cognitive science, CoALA defines one active memory type and three long-term memory types. The three long-term types differ in *what kind of information* they store, not just how long they store it.

The key design challenge is deciding what to keep in the expensive, high-speed context window versus what to offload to external storage — and which external store is the right home for each type of knowledge.

## Memory Type 1: Working Memory

**Analogy**: RAM — fast, limited, and cleared when the session ends.

### Definition
The active state the agent is reasoning over right now. This is the running conversation and the scratchpad the model sees at inference time — everything currently in the LLM's context window.

### Characteristics
- **Speed**: Immediate (already in context — no retrieval step)
- **Capacity**: Limited by the model's context window (4K–1M+ tokens depending on model)
- **Persistence**: Temporary — cleared at the end of a session or task
- **Cost**: Most expensive per token (LLM inference cost)

### What It Contains
- Current conversation history
- Active task state and intermediate results
- Recently retrieved documents or tool outputs
- System instructions and agent persona
- Scratchpad notes for multi-step reasoning

### Management Strategies
- **Sliding Window**: Keep only the last N messages, discard oldest
- **Token Trimming**: Remove messages to stay within token limits
- **Recursive Summarization**: Compress older messages into a summary
- **Context Pinning**: Lock critical information (system prompt, user preferences) so it is never discarded

### Solutions
- **LangGraph Checkpoints**: Save and restore conversation state
- **LangChain ConversationBufferWindowMemory**: Fixed-size sliding window
- **OpenAI Threads**: Managed conversation history via API
- **Redis / Upstash**: Low-latency session storage for high-speed applications

---

## Memory Type 2: Semantic Memory

**Analogy**: An encyclopedia or knowledge graph — durable facts about the world.

### Definition
The durable facts and knowledge the agent accumulates about users, entities, and the world: preferences, canonical definitions, structured reference data. This is the "what is true" store — knowledge that persists across all sessions and does not depend on when or how it was learned.

### Characteristics
- **Speed**: Moderate — requires retrieval (vector search, graph query, or key-value lookup)
- **Capacity**: Very large — can store millions of facts
- **Persistence**: Permanent — survives indefinitely
- **Abstraction**: High-level facts and relationships, not raw conversation logs

### What It Contains
- User preferences and profile information ("The user prefers Python over JavaScript")
- Domain knowledge and facts relevant to the agent's purpose
- Entity relationships ("User X manages Project Y, which has budget Z")
- Product catalog, pricing, canonical definitions
- Organizational knowledge (policies, procedures, reference data)

### Management Strategies
- **Vector RAG**: Embed knowledge as vectors for semantic retrieval
- **Knowledge Graphs**: Model relationships between entities (Neo4j, FalkorDB)
- **Entity Extraction**: Extract and store structured facts from conversations
- **Contradiction Resolution**: Update or overwrite facts when new information supersedes old

### Solutions
- **Mem0**: Automatic extraction and refinement of user facts and preferences
- **Zep**: Temporal knowledge graph for evolving facts over time
- **LangMem**: LangChain's long-term learning layer for LangGraph
- **AWS Bedrock Memory / Vertex Memory Bank**: Cloud-managed semantic memory

---

## Memory Type 3: Episodic Memory

**Analogy**: A searchable journal — records of specific past events with timestamps and context.

### Definition
Specific past experiences the agent can recall — what happened in a prior session, what the user asked three weeks ago, how a similar task resolved last time. This is the "what happened" store — time-indexed events rather than abstracted facts.

### Characteristics
- **Speed**: Moderate — requires retrieval (vector search or structured query)
- **Capacity**: Large — can store thousands of episodes
- **Persistence**: Session-to-session — survives across conversations
- **Granularity**: High-fidelity logs with timestamps, outcomes, and metadata

### What It Contains
- Records of past conversations and their outcomes
- Tool call logs with inputs, outputs, and success/failure status
- User feedback and corrections
- Task execution histories with timing and resource usage
- Error logs and debugging information ("Tool X failed on input Y last Tuesday")

### Management Strategies
- **Vector Embeddings**: Embed episode summaries for semantic search
- **Structured Metadata**: Store timestamps, session IDs, and outcome labels for filtering
- **Relevance Scoring**: Retrieve episodes most similar to the current context
- **Retention Policies**: Archive or delete old episodes based on age or relevance

### Storage Technologies
- **Vector Databases**: Pinecone, Chroma, Weaviate for semantic search over past events
- **Structured Logs**: PostgreSQL, MongoDB with metadata indexing
- **AgentFS**: SQLite-backed virtual filesystem for agent logs

---

## Memory Type 4: Procedural Memory

**Analogy**: A skills manual or employee handbook — rules and procedures that govern behavior.

### Definition
The behavioral rules, guidelines, and learned procedures that shape how the agent acts — how to handle customers, which tools to prefer, what not to do. This is the "how to behave" store. Unlike semantic memory (facts about the world), procedural memory encodes *how the agent should act* in various situations.

### Characteristics
- **Speed**: Immediate when baked into the system prompt; retrieval-based when stored externally
- **Capacity**: Varies — from a few hundred tokens in a system prompt to large rule libraries
- **Persistence**: Permanent — updated through explicit configuration or reflection-driven learning
- **Form**: Rules, guidelines, workflows, fine-tuned weights, or code

### What It Contains
- Behavioral rules ("Always escalate billing disputes to a human agent")
- Tool preferences ("Prefer tool A over tool B for tasks involving X")
- Negative constraints ("Never reveal internal pricing to external users")
- Agent personas and communication style guidelines
- Learned procedures extracted from past successes and failures ("Method A failed twice; use Method B")
- Workflow templates and standard operating procedures

### Management Strategies
- **System Prompt / AGENTS.md**: Encode rules directly in the agent's instructions
- **Reflection / Consolidation**: Background loop reviews episodic logs to extract generalizable rules
- **Fine-tuning**: Bake frequently-used procedures into model weights
- **Rule Libraries**: Store and retrieve procedures from external stores when the rule set is large

### Solutions
- **AGENTS.md / instruction files**: Explicit behavioral rules in the agent's repository
- **LangMem procedural store**: LangChain's support for procedural memory alongside semantic
- **Fine-tuned models**: Procedures encoded in weights via RLHF or supervised fine-tuning
- **Reflection agents**: Background agents that extract rules from episodic logs (as in Generative Agents)

---

## How the Four Types Work Together

```
User Input
    ↓
[Working Memory] ← Active context, current conversation, scratchpad
    ↓ (retrieve relevant past experiences)
[Episodic Memory] ← What happened last time, prior session outcomes
    ↓ (retrieve relevant facts and knowledge)
[Semantic Memory] ← User preferences, domain knowledge, entity facts
    ↓ (apply behavioral rules)
[Procedural Memory] ← How to act, which tools to use, what not to do
    ↓
LLM Reasoning → Response
    ↓
[Update all types as appropriate]
```

### Information Flow
1. **Ingestion**: New information enters working memory (context window)
2. **Promotion**: Important facts → semantic memory; events → episodic memory; learned rules → procedural memory
3. **Retrieval**: Relevant memories are retrieved and injected into the context window (working memory)
4. **Consolidation**: Episodic memories are periodically reviewed to extract semantic facts and procedural rules

### Design Principles
- **Type-appropriate storage**: Match the storage technology to the memory type — vector DBs for semantic/episodic, instruction files or fine-tuning for procedural
- **Just-in-time loading**: Retrieve memories only when needed, not upfront
- **Selective persistence**: Not everything needs to be remembered — be selective about what gets promoted out of working memory
- **Graceful degradation**: Agents should function even when memory retrieval fails

## Memory Type Comparison

| Dimension | Working | Semantic | Episodic | Procedural |
|---|---|---|---|---|
| **What it stores** | Active reasoning state | Facts and knowledge | Past experiences | Behavioral rules |
| **Question it answers** | "What am I doing now?" | "What is true?" | "What happened before?" | "How should I act?" |
| **Persistence** | Session only | Permanent | Cross-session | Permanent |
| **Storage location** | Context window | Vector DB / Knowledge Graph | Vector DB / Logs | System prompt / Weights |
| **Updated by** | Each inference step | Entity extraction, RAG writes | Event logging | Reflection, fine-tuning |
| **Human analogy** | Working memory | Semantic memory | Autobiographical memory | Skill / habit memory |

## See Also

- [Agent Memory README](README.md)
- [Long-term Memory Strategies](ltm-strategies.md)
- [Short-term Memory Management](short-term.md)
- [Research Papers](research-papers.md)

## References

- [Cognitive Architectures for Language Agents (CoALA)](https://arxiv.org/abs/2309.02427) — Sumers et al. (Princeton, 2023). Defines the four-type memory taxonomy for language agents.
