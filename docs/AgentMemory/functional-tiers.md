# The Three Functional Tiers of Agent Memory

## Overview

Agent memory is organized into three functional tiers that handle different aspects of information storage and retrieval. Each tier serves a distinct purpose in the agent's cognitive architecture, analogous to how human memory works — from immediate working memory to long-term knowledge stores.

The key challenge in agent memory management is deciding what to keep in the expensive, high-speed context window versus what to offload to external storage. The three-tier model provides a principled framework for making these decisions.

## Tier 1: Short-term (Working Memory)

**Analogy**: RAM in a computer — fast, limited, and cleared when the session ends.

### Purpose
Stores contextual information generated during the current task or conversation. This is the "active workspace" of the agent — everything currently in the LLM's context window.

### Characteristics
- **Speed**: Immediate access (already in context)
- **Capacity**: Limited by the model's context window (4K–200K tokens depending on model)
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
- **Context Pinning**: Lock critical information (system prompt, user preferences) so it's never discarded

### Solutions
- **LangGraph Checkpoints**: Save and restore conversation state
- **LangChain ConversationBufferWindowMemory**: Fixed-size sliding window
- **OpenAI Threads**: Managed conversation history via API
- **Redis/Upstash**: Low-latency session storage for high-speed applications

---

## Tier 2: Episodic Memory (Experience)

**Analogy**: A searchable journal — records of specific past events with timestamps and context.

### Purpose
Stores specific past events, interactions, and experiences as discrete "episodes." Enables the agent to answer questions like "What did we do last time?" or "Why did that tool fail yesterday?"

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
- Error logs and debugging information

### Management Strategies
- **Vector Embeddings**: Embed episode summaries for semantic search
- **Structured Metadata**: Store timestamps, session IDs, and outcome labels for filtering
- **Relevance Scoring**: Retrieve episodes most similar to the current context
- **Retention Policies**: Archive or delete old episodes based on age or relevance

### Storage Technologies
- **Vector Databases**: Pinecone, Chroma, Weaviate for semantic search
- **Structured Logs**: PostgreSQL, MongoDB with metadata indexing
- **AgentFS**: SQLite-backed virtual filesystem for agent logs

---

## Tier 3: Long-term / Semantic Memory (Knowledge)

**Analogy**: A knowledge graph or encyclopedia — abstracted facts and relationships that persist indefinitely.

### Purpose
Persists across all sessions to accumulate reusable knowledge, user preferences, and learned behaviors. Provides the agent with a consistent "personality" and set of core beliefs that don't change based on the current conversation.

### Characteristics
- **Speed**: Slower — requires retrieval and sometimes reasoning
- **Capacity**: Very large — can store millions of facts
- **Persistence**: Permanent — survives indefinitely
- **Abstraction**: High-level facts and rules, not raw conversation logs

### What It Contains
- User preferences and profile information ("The user prefers Python over JavaScript")
- Domain knowledge and facts relevant to the agent's purpose
- Learned patterns and heuristics ("Method A fails for inputs > 1000 items")
- Organizational knowledge (policies, procedures, product information)
- Relationships between entities (knowledge graph nodes and edges)

### Management Strategies
- **Vector RAG**: Embed knowledge as vectors for semantic retrieval
- **Knowledge Graphs**: Model relationships between entities (Neo4j, FalkorDB)
- **Entity Extraction**: Extract and store structured facts from conversations
- **Reflection/Consolidation**: Periodically review episodic memory to extract generalizable knowledge

### Solutions
- **Mem0**: Automatic extraction and refinement of user facts and preferences
- **Zep**: Temporal knowledge graph for evolving facts over time
- **LangMem**: LangChain's long-term learning layer for LangGraph
- **AWS Bedrock Memory / Vertex Memory Bank**: Cloud-managed semantic memory

---

## How the Tiers Work Together

```
User Input
    ↓
[Short-term Memory] ← Active context, current conversation
    ↓ (retrieve relevant history)
[Episodic Memory] ← Past interactions, tool logs
    ↓ (retrieve relevant knowledge)
[Long-term Memory] ← User preferences, domain knowledge
    ↓
LLM Reasoning → Response
    ↓
[Update all tiers as appropriate]
```

### Information Flow
1. **Ingestion**: New information enters short-term memory (context window)
2. **Promotion**: Important information is promoted to episodic or long-term memory
3. **Retrieval**: Relevant memories are retrieved and injected into the context window
4. **Consolidation**: Episodic memories are periodically consolidated into long-term knowledge

### Design Principles
- **Tiered Access**: Check short-term first, then episodic, then long-term
- **Just-in-Time Loading**: Retrieve memories only when needed, not upfront
- **Selective Persistence**: Not everything needs to be remembered — be selective
- **Graceful Degradation**: Agents should function even when memory retrieval fails

## See Also

- [Agent Memory README](README.md)
- [Long-term Memory Strategies](ltm-strategies.md)
- [Short-term Memory Management](short-term.md)
- [Research Papers](research-papers.md)
