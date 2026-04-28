# Short-term Memory Management

## Overview

Short-term memory (also called working memory) manages the information immediately available to an agent during a task or conversation. It lives in the LLM's context window — the most expensive and capacity-constrained part of the memory system. Effective short-term memory management is critical for maintaining coherent conversations, avoiding context overflow errors, and controlling inference costs.

## The Core Challenge

LLMs have a fixed context window (ranging from 4K to 200K+ tokens depending on the model). As conversations grow longer, you must decide:
- What to keep in the context window
- What to summarize or compress
- What to offload to external storage
- What to discard entirely

## Short-term Memory Techniques

### Sliding Window
**Logic**: Retains only a fixed number of the most recent messages, discarding the oldest once the limit is reached.

**Primary Benefit**: Prevents context overflow errors and maintains low latency.

**Tradeoff**: Loses older context entirely — the agent "forgets" early parts of the conversation.

**Best For**: Simple chatbots and task agents where recent context is most relevant.

```python
# LangChain ConversationBufferWindowMemory
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=5)  # Keep last 5 exchanges
```

---

### Token Trimming
**Logic**: Dynamically calculates and removes the minimum number of tokens from the start of the history to fit the model's context limit.

**Primary Benefit**: Maximizes use of the available context window without crashing.

**Tradeoff**: May cut off important early context mid-sentence.

**Best For**: Applications where you want to use as much context as possible without manual tuning.

---

### Recursive Summarization
**Logic**: Periodically condenses older parts of the conversation into a short paragraph while keeping recent messages in full.

**Primary Benefit**: Preserves long-term narrative context while saving significant token space.

**Tradeoff**: Summarization introduces information loss and adds latency.

**Best For**: Long-running conversations where early context matters but verbatim recall is not required.

```python
# LangChain ConversationSummaryMemory
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI

memory = ConversationSummaryMemory(llm=ChatOpenAI())
```

---

### Message Selection
**Logic**: Uses a "supervisor" model to retrieve only the past messages that are relevant to the current user query.

**Primary Benefit**: Highly efficient for complex, non-linear tasks where only specific historical facts matter.

**Tradeoff**: Adds latency and cost for the retrieval step; may miss relevant context.

**Best For**: Long-running agents with diverse conversation history where most past messages are irrelevant to the current query.

---

### Scratchpad / Working Memory
**Logic**: Provides a dedicated space (like a file or hidden block) for the agent to store intermediate thoughts and calculations.

**Primary Benefit**: Offloads technical complexity from the main chat history to keep the conversation clean.

**Tradeoff**: Requires explicit agent behavior to use the scratchpad effectively.

**Best For**: Multi-step reasoning tasks, code generation, and complex problem-solving where intermediate steps should not pollute the conversation.

---

### Context Pinning
**Logic**: Locks vital information (like system instructions or core user preferences) so they are never discarded by trimming or sliding window operations.

**Primary Benefit**: Ensures the agent never forgets its primary persona, mission, or critical user preferences.

**Tradeoff**: Reduces available space for dynamic context.

**Best For**: All production agents — always pin system instructions and critical user context.

---

## Short-term Memory Solutions

| Category | Solution | Memory Philosophy | Best For |
|----------|----------|-------------------|----------|
| Frameworks | LangGraph Checkpoints | Stateful Threads | Saving the exact "snapshot" of a multi-step workflow |
| Frameworks | LangChain Window | Sliding Buffer | Keeping only the last N interactions to save tokens |
| Frameworks | Letta (MemGPT) | Virtual Context | Dynamically swapping info in/out of the context window |
| In-Memory | Redis / Upstash | Ephemeral Cache | Low-latency session storage for high-speed chat apps |
| Managed | OpenAI Threads | Stateful API | Hands-off management of current conversation history |
| Technique | Summarization | Recursive Compression | Condensing old messages into a brief "recap" to save space |
| Technique | Scratchpad | Working Draft | Agent-written notes used only for the current task logic |

## LangGraph Checkpoints

LangGraph's checkpointing system is the most powerful short-term memory solution for stateful agent workflows. It saves the complete state of a graph execution at each step, enabling:

- **Pause and Resume**: Stop a long-running agent and resume later
- **Human-in-the-Loop**: Pause for human approval before continuing
- **Time Travel**: Replay from any previous checkpoint for debugging
- **Fault Tolerance**: Recover from failures without restarting from scratch

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph

checkpointer = MemorySaver()
graph = StateGraph(AgentState)
# ... add nodes and edges ...
app = graph.compile(checkpointer=checkpointer)

# Run with thread ID for persistence
config = {"configurable": {"thread_id": "user-123"}}
result = app.invoke({"messages": [...]}, config=config)
```

## Letta (MemGPT) — OS-Inspired Memory

[Letta](https://www.letta.com/) (formerly MemGPT) implements an OS-inspired memory architecture where the agent manages its own context window like an operating system manages RAM:

- **Main Context** (RAM): The active context window — fast but limited
- **Archival Storage** (Disk): External storage for overflow — unlimited but requires retrieval
- **Recall Storage**: Searchable history of past interactions

The agent uses special memory management functions (`core_memory_append`, `archival_memory_search`) to explicitly manage what stays in context and what gets offloaded.

## Best Practices

1. **Always pin system instructions**: Use context pinning to ensure the agent's persona and core instructions are never trimmed
2. **Choose the right technique for your use case**: Sliding window for simple chatbots, summarization for long conversations, checkpoints for complex workflows
3. **Monitor context utilization**: Track what percentage of the context window is being used to identify optimization opportunities
4. **Test edge cases**: Verify behavior when context is nearly full — does the agent degrade gracefully?
5. **Consider cost**: Longer contexts cost more per inference — balance quality with cost

## See Also

- [Functional Memory Tiers](functional-tiers.md)
- [Long-term Memory Strategies](ltm-strategies.md)
- [Agent Memory README](README.md)
