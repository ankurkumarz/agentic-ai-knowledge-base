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

**API-level primitives (Anthropic)**: The Claude API provides two first-party context-reduction primitives:
- `compact_20260112` (beta header `compact-2026-01-12`): server-side compaction triggered at a configurable token threshold (min 50K, default 150K). Returns a typed compaction block that replaces prior turns. The `instructions` parameter completely replaces the default summarization prompt — custom instructions must include the full framing, not just additions. High-level facts central to the task typically survive; obscure specifics (appendix table cells, exact phrasing) typically do not.
- `clear_tool_uses_20250919` (beta header `context-management-2025-06-27`): surgically replaces `tool_result` content blocks with a short placeholder while leaving `tool_use` records, user messages, and assistant reasoning untouched. No inference cost. Key knobs: `trigger` (token threshold), `keep` (most-recent results to retain, default 3), `clear_at_least` (minimum tokens per firing — important for cache invalidation economics), `exclude_tools` (exempt specific tools, e.g., the memory tool). When combining with the memory tool, always set `exclude_tools: ["memory"]` to prevent the agent from losing track of what it just saved.

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

## Cost-Performance Trade-offs Across Strategies

Shen et al. (2026) introduced the **Efficiency Frontier** framework — a unified, deployment-aware approach to choosing between strategies based on jointly optimized cost and performance. Key findings from evaluation on 5,000 HotpotQA instances:

- **Retrieval is preferred for low-reuse deployments** (few queries per corpus): avoids preprocessing overhead; cost-competitive with comparable F1
- **Memory compression is preferred for high-reuse deployments**: preprocessing cost amortizes over many queries, yielding >50% lower token cost vs. full-context at comparable quality
- **Full-context prompting** is rarely cost-optimal — ~25% token reduction is achievable at equivalent performance through deployment-aware selection
- **Transition points** exist between strategies and depend on the reuse parameter N (number of queries that share a preprocessing step)

See [Efficiency Frontier Framework](./efficiency-frontier.md) for the full decision guide.

## Strategy Selection by Priority

| Priority | Recommended Approach |
|---|---|
| Parallelizable tasks | Evaluate multi-agent isolation regardless of context size |
| Cost reduction | Prioritize caching and compression strategies |
| Low latency | Focus on cache optimization and parallel processing |
| High accuracy | Implement comprehensive retrieval and memory systems |

## Retrieval Efficiency Benchmark

When evaluating retrieval quality, track the ratio of used items to retrieved items:
- **Below 40% efficiency**: retrieving too much noise — tighten retrieval criteria
- **50–70% efficiency**: sweet spot with all critical information included
- **Above 80% but missing key information**: retrieving too narrowly — broaden retrieval

Windsurf achieves 3× better accuracy than single-technique retrieval by combining: embedding search (semantic similarity), grep (exact matches), knowledge graphs (concept relationships), and AST parsing (code structure).

## Implementation Roadmap

### Week 1: Foundation (Quick Wins)

Start with measurement — you can't optimize what you don't understand. Deploy comprehensive logging to capture every agent interaction, token usage, cache hit rates, and failure patterns.

High-impact, low-effort optimizations:
1. **Optimize tool descriptions** for clarity and distinctiveness so the agent can distinguish between similar tools
2. **Add basic error retention** — keep failed attempts in context to prevent repeated mistakes (costs nothing to implement)
3. **Deploy production guardrails** for safety and reliability

These changes often provide 80% of the benefit with 20% of the effort.

### Month 1: Infrastructure

1. **Implement dynamic tool retrieval** when you exceed 20 tools — agent sees only the most relevant options per query
2. **Add reversible compression** — store URLs instead of web pages, file paths instead of contents (token savings with recovery path)
3. **Deploy auto-summarization** at 80% context capacity to prevent hard failures
4. **Create a simple memory system** with basic file storage so agents can access information without loading it all into context

### Advanced Phase: Scale

Only after mastering fundamentals:
1. **Multi-agent architectures** for truly parallelizable tasks — Anthropic's research showed 90% improvement at 15× token cost
2. **Attention manipulation** through to-do lists and goal recitation to reduce drift in long-running tasks
3. **Evaluation insights** to catch emerging failure patterns before users notice them

## See Also

- [Efficiency Frontier: Cost-Performance Optimization](./efficiency-frontier.md)
- [Key Challenges in Context Management](./challenges.md)
- [Manus Context Engineering](./manus.md)
- [Anthropic Multi-Agent Research System](./anthropic.md)
- [LangGraph Context Engineering](./langgraph.md)
- [Cognition / Devin: Don't Build Multi-Agents](./devin.md)
- [Agent Memory Management](../AgentMemory/README.md)
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Harness Optimization](../AgentHarness/harness-optimization.md) — automated search over context management strategies; Meta-Harness discovers retrieval routing and context budgets that outperform hand-designed equivalents
- [Open Knowledge Format (OKF)](../Standards/open-knowledge-format.md) — standardized markdown+frontmatter substrate for the Offload (Write) pattern

## References

- [The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management](https://arxiv.org/abs/2605.23071) — Shen et al., May 2026
- [Context Engineering for Agents — Lance Martin, LangChain](https://rlancemartin.github.io/2025/06/23/context_engineering/)
- [How to Fix Your Context — Drew Breunig](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)
- [Effective Context Engineering for AI Agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Context Engineering for AI Agents: Lessons from Building Manus — Yichao 'Peak' Ji](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [How we built our multi-agent research system — Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Don't Build Multi-Agents — Cognition / Walden Yan](https://cognition.ai/blog/dont-build-multi-agents)
- [Tool Use Context Engineering Cookbook — Anthropic](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)
- [Mastering Multi-Agent Systems eBook](https://galileo.ai) — Galileo, 2026. Chapter 4 provides context size thresholds, priority-based strategy selection, anti-patterns, and a phased implementation roadmap.
