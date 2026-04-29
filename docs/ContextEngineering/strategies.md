# Common Strategies for Context Management

## Overview

Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory. As Andrej Karpathy framed it, the LLM is like a CPU and its context window is like RAM — the operating system's job is to curate what fits.

Lance Martin (LangChain) groups the strategies into four buckets: **write, select, compress, and isolate**. This page maps those to the five strategies commonly referenced in production agent systems, with implementation examples from Manus, Anthropic, LangGraph, and others.

## Strategy 1: Offload Context (Write to File System)

**Core idea**: Save information outside the context window so it can be retrieved on demand, rather than keeping everything in active context.

**Usage**: Long-term memory, scratchpad notes, TODO lists, tool call references, research plans.

**How it works**: Agents write to files, databases, or structured state objects. They retrieve only what's needed at each step, keeping the active context lean.

**Production examples**:
- **Manus** treats the file system as the "ultimate context" — unlimited in size, persistent by nature, and directly operable by the agent. Web page content can be dropped from context as long as the URL is preserved; document contents can be omitted if the file path remains available. All compression strategies are designed to be restorable.
- **Anthropic's multi-agent researcher** has the LeadResearcher save its plan to Memory at the start, since context exceeding 200K tokens will be truncated. Subagents write outputs to external systems and pass lightweight references back to the coordinator, preventing information loss during multi-stage processing.
- **Claude Code** uses CLAUDE.md files and a memory tool (public beta) for structured note-taking. The Pokémon-playing Claude agent maintained precise tallies across thousands of game steps using this pattern.
- **Anthropic's "think" tool** provides a scratchpad space for the model to write notes that don't cloud the active context but remain available for later reference. Pairing this with domain-specific prompts yields up to 54% improvement on specialized agent benchmarks.

**Tradeoffs**: Requires the agent to learn when to write and what to write. Retrieval adds latency. Information must be organized well enough to be findable later.

## Strategy 2: Reduce Context (Compaction / Summarization)

**Core idea**: Compress accumulated context to retain essential meaning while reducing token count.

**Usage**: Summarization of long conversations, pruning tool call results, summarizing at agent-agent handoffs, removing irrelevant message history.

**How it works**: An LLM (or specialized model) distills the context, preserving key decisions, errors, and state while discarding redundant tool outputs and intermediate steps.

**Production examples**:
- **Claude Code** runs auto-compact after exceeding 95% of the context window, summarizing the full trajectory of user-agent interactions. It preserves architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs. After compaction, the agent continues with the compressed context plus the five most recently accessed files.
- **LangGraph's DeepAgent** uses summarization as middleware — a dedicated summarization step between agent turns.
- **Cognition (Devin)** uses a fine-tuned model specifically for summarization at agent-agent boundaries, underscoring how much investment this step can require. Their principle: share full agent traces, not just individual messages.
- **Context Pruning** (lighter-weight alternative): Rather than LLM-based summarization, pruning uses heuristics or specialized models to filter irrelevant content. [Provence](https://huggingface.co/naver/provence-reranker-debertav3-v1) is a 1.75GB trained context pruner for QA that can cut 95% of irrelevant content from documents. Tool result clearing — removing raw tool outputs once they've been processed — is one of the safest, lightest-touch forms of compaction.

**Tradeoffs**: Risk of information loss. Knowing what to keep vs. discard is hard to get right. Cognition recommends fine-tuning a smaller model for this task in production. Anthropic recommends starting by maximizing recall, then iterating to improve precision.

## Strategy 3: Retrieve Context (RAG and Just-in-Time Loading)

**Core idea**: Pull relevant context into the window on demand rather than pre-loading everything.

**Usage**: Retrieve contextual data using RAG, populate prompts with retrieved data, just-in-time file loading.

**How it works**: Agents maintain lightweight identifiers (file paths, URLs, stored queries) and use tools to dynamically load data at runtime. This mirrors human cognition — we don't memorize entire corpuses, we use filing systems and bookmarks.

**Production examples**:
- **Claude Code** uses a hybrid approach: CLAUDE.md files are loaded up front, while glob and grep allow just-in-time file retrieval, bypassing stale indexing issues.
- **Tool RAG**: Applying RAG to tool descriptions to select only the most relevant tools for a given task. Research shows this improves tool selection accuracy by up to 3x when tool counts exceed 30. The "Less is More" paper found a 44% performance improvement on Llama 3.1 8b using dynamic tool selection.
- **Windsurf** uses AST parsing, embedding search, grep/file search, knowledge graph retrieval, and re-ranking for code context retrieval at scale.

**Tradeoffs**: Runtime exploration is slower than pre-computed retrieval. Agents need good heuristics to avoid chasing dead ends. Metadata (file names, folder structure, timestamps) provides important signals that help agents navigate efficiently.

## Strategy 4: Isolate Context (Multi-Agent / Quarantine)

**Core idea**: Split context across multiple agents or threads, each with a focused, clean context window.

**Usage**: Parallel research tasks, separation of concerns in complex workflows, preventing context clash between unrelated subtasks.

**How it works**: A lead agent decomposes work into subtasks and spawns subagents, each with their own context window. Subagents return condensed summaries (typically 1,000–2,000 tokens) rather than full traces.

**Production examples**:
- **Anthropic's multi-agent researcher**: Subagents operate in parallel with isolated context windows, each exploring a different aspect of a query. This outperformed single-agent Claude Opus 4 by 90.2% on their internal research eval. Token usage is ~15x higher than chat, so this pattern is best for high-value tasks.
- **HuggingFace's CodeAgent**: Uses a sandbox environment to isolate tool call results from the LLM context. Code runs in the sandbox; only selected return values are passed back. This is especially effective for token-heavy objects like images or audio.
- **Agent runtime state**: A Pydantic-schema state object can isolate context — only the `messages` field is exposed to the LLM each turn, while other fields hold information for selective use.

**Important caveats** (from Cognition/Walden Yan):
- Subagents that lack shared context make decisions based on conflicting assumptions. Principle: share full agent traces, not just individual messages.
- Actions carry implicit decisions. When subagents work in parallel without seeing each other's work, their outputs can be inconsistent.
- Claude Code's subagents are deliberately limited to answering questions, not writing code, precisely because they lack the main agent's full context.
- Multi-agent parallelism is best suited to breadth-first tasks (research, information gathering) rather than tasks with many interdependencies (most coding tasks).

## Strategy 5: Cache Context

**Core idea**: Store frequently used context elements (system prompts, tool descriptions, agent instructions) in a cache to reduce cost and latency.

**Usage**: Cached input tokens, caching agent instructions and tool descriptions as a stable prefix.

**How it works**: Providers like Anthropic and Google offer prompt caching. Cached tokens cost significantly less — with Claude Sonnet, cached input tokens cost $0.30/MTok vs. $3.00/MTok uncached (10x difference).

**Production examples**:
- **Manus** identifies KV-cache hit rate as the single most important metric for a production agent. Key practices: keep the prompt prefix stable (even a single-token difference invalidates the cache), make context append-only, use deterministic serialization, and mark cache breakpoints explicitly.
- **Gemini** offers [Context Caching](https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview) for large, stable prefixes.
- **Manus's mask-don't-remove pattern**: Rather than dynamically adding/removing tools (which invalidates the KV-cache), Manus uses a context-aware state machine to mask token logits during decoding, constraining tool selection without modifying tool definitions.

**Tradeoffs**: Cache invalidation is subtle — timestamps in system prompts, non-deterministic JSON serialization, and dynamic tool lists all silently break cache hit rates. Requires discipline in prompt and context design.

## Strategy Comparison

| Strategy | Best For | Key Risk | Examples |
|---|---|---|---|
| Offload (Write) | Long tasks, persistent memory, large tool outputs | Retrieval overhead, organization complexity | Manus file system, Anthropic memory tool, Claude Code CLAUDE.md |
| Reduce (Compaction) | Long conversations, agent handoffs | Information loss | Claude Code auto-compact, LangGraph DeepAgent, Cognition fine-tuned summarizer |
| Retrieve (RAG) | Large knowledge bases, dynamic data, many tools | Latency, retrieval quality | Claude Code just-in-time, Tool RAG, Windsurf code retrieval |
| Isolate (Multi-agent) | Breadth-first research, parallelizable tasks | Context clash, 15x token cost | Anthropic researcher, HuggingFace CodeAgent |
| Cache | Stable system prompts, repeated tool descriptions | Cache invalidation, prefix instability | Manus KV-cache, Gemini Context Caching |

## See Also

- [Key Challenges in Context Management](./challenges.md)
- [Manus Context Engineering](./manus.md)
- [Anthropic Multi-Agent Research System](./anthropic.md)
- [LangGraph Context Engineering](./langgraph.md)
- [Cognition / Devin: Don't Build Multi-Agents](./devin.md)
- [Agent Memory Management](../AgentMemory/README.md)
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md)

## References

- [Context Engineering for Agents — Lance Martin, LangChain](https://rlancemartin.github.io/2025/06/23/context_engineering/)
- [How to Fix Your Context — Drew Breunig](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)
- [Effective Context Engineering for AI Agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Context Engineering for AI Agents: Lessons from Building Manus — Yichao 'Peak' Ji](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [How we built our multi-agent research system — Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Don't Build Multi-Agents — Cognition / Walden Yan](https://cognition.ai/blog/dont-build-multi-agents)
