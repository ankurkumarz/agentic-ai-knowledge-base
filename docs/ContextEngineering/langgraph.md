# LangGraph Context Engineering

## Overview

Lance Martin (LangChain) has been one of the most active voices synthesizing context engineering patterns across the industry. His blog post, meetup talk, and the open-deep-research reference implementation together form a practical framework for how LangGraph approaches context management in production agents.

The core framing: context engineering is the natural successor to prompt engineering, driven by the shift from one-shot tasks to long-running agents that accumulate tool call feedback across many turns.

## The Four-Strategy Framework

Martin groups context engineering into four buckets — **write, select, compress, isolate** — which map closely to the five strategies documented in [Common Strategies](./strategies.md). The framing comes from observing patterns across many production agents:

> "Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory." — Lance Martin, citing Andrej Karpathy

The LLM-as-OS analogy: the LLM is the CPU, the context window is RAM, and context engineering is the OS's job of curating what fits in working memory.

## open-deep-research: A Reference Implementation

The [open-deep-research](https://github.com/langchain-ai/open_deep_research) project ([blog post](https://blog.langchain.com/open-deep-research/)) is LangChain's open-source reference implementation that demonstrates all four strategies working together in a single agent:

### Offload: Brief saved to state
The agent creates a structured brief from the initial chat and saves it to state (external to the active context window). This brief is later retrieved to steer the writing and research phases — a clean example of write-then-retrieve context management.

### Reduce: Summarize tool call observations
After each research subagent completes its work, the raw tool call outputs and observations are summarized before being passed forward. This prevents token-heavy search results from accumulating in the main context.

### Isolate: Context split across subagents
Research tasks are decomposed and distributed to subagents, each with their own isolated context window. Subagents return condensed summaries rather than full traces.

### Key design decisions (from the meetup talk)
- **Information loss risk with compression favors offloading**: When in doubt between compressing and offloading, offloading is safer because it's restorable. Compression carries irreversible information loss risk.
- **Coordination problems with multi-agent are a real risk**: Subagents in open-deep-research are deliberately limited — they avoid making decisions that would conflict with the main agent's context. This directly addresses the concern raised by Cognition (see [Devin](./devin.md)).

## DeepAgent: Summarization as Middleware

LangGraph built DeepAgent with summarization as a dedicated middleware layer between agent turns. Rather than relying on the main LLM to manage its own context, a separate summarization step processes the accumulated history before each new turn. This is a more structured approach than Claude Code's threshold-triggered auto-compact.

## Context Engineering for Agents — Blog Post

Martin's [June 2025 blog post](https://rlancemartin.github.io/2025/06/23/context_engineering/) provides the most comprehensive public taxonomy of context engineering strategies, drawing on examples from:

- Anthropic's multi-agent researcher (scratchpads, context isolation)
- Claude Code (auto-compact summarization)
- Cognition/Devin (summarization at agent-agent handoffs)
- HuggingFace CodeAgent (environment-based context isolation)
- Windsurf (multi-method code retrieval)
- ChatGPT, Cursor, Windsurf (long-term memory patterns)

Key insight on memory selection: "Some popular agents simply use a narrow set of files that are always pulled into context." Claude Code uses CLAUDE.md; Cursor and Windsurf use rules files. For larger memory collections, embeddings and knowledge graphs are used for indexing, but selection remains hard.

Key insight on tool RAG: Applying RAG to tool descriptions to fetch the most relevant tools for a task improves tool selection accuracy by ~3x when tool counts are high.

## Retrieve Context: Windsurf's Approach

Martin highlights Varun (Windsurf) on the complexity of code retrieval at scale:

> "Indexing code ≠ context retrieval… embedding search becomes unreliable as the size of the codebase grows… we must rely on a combination of techniques like grep/file search, knowledge graph based retrieval, and a re-ranking step."

This underscores that retrieval for agents is not a solved problem — it requires layered approaches combining semantic search, structural parsing (AST), and re-ranking.

## Best Practices

| Area | Recommendation |
|---|---|
| Compression vs. offloading | Prefer offloading when information loss risk is high; use compression for redundant/intermediate outputs |
| Subagent design | Limit subagents to answering questions, not making decisions, to avoid context clash |
| Tool management | Apply RAG to tool descriptions when tool count exceeds ~30 |
| Long-term memory | Use narrow, always-loaded files (CLAUDE.md pattern) for procedural/episodic memory; use embeddings for larger semantic memory stores |
| Summarization | Treat summarization as its own dedicated stage with its own eval data, not an afterthought |

## See Also

- [Common Strategies for Context Management](./strategies.md)
- [Key Challenges in Context Management](./challenges.md)
- [Manus Context Engineering](./manus.md)
- [Anthropic Multi-Agent Research System](./anthropic.md)
- [Cognition / Devin: Don't Build Multi-Agents](./devin.md)
- [Agent Memory Management](../AgentMemory/README.md)

## References

- [Context Engineering for Agents — Lance Martin](https://rlancemartin.github.io/2025/06/23/context_engineering/) — primary blog post
- [Context Engineering Meetup Talk — Lance Martin, LangChain](https://docs.google.com/presentation/d/16aaXLu40GugY-kOpqDU4e-S0hD1FmHcNyF0rRRnb1OU/) — companion slide deck
- [open-deep-research — LangChain](https://github.com/langchain-ai/open_deep_research) — reference implementation
- [open-deep-research blog post — LangChain](https://blog.langchain.com/open-deep-research/)
- [how_to_fix_your_context — LangChain GitHub](https://github.com/langchain-ai/how_to_fix_your_context) — code examples
