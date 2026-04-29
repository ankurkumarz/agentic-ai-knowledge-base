# Anthropic Context Engineering

## Overview

Anthropic has published two major pieces on context engineering: a detailed post on their multi-agent research system, and a broader guide on effective context engineering for AI agents. Together they cover both the architectural patterns for managing context in production and the underlying principles for why context must be treated as a finite, precious resource.

## Effective Context Engineering for AI Agents

Source: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### Context as a Finite Attention Budget

Anthropic frames context engineering as the natural progression of prompt engineering. As agents move from one-shot tasks to multi-turn, long-horizon work, the challenge shifts from "how to write a good prompt" to "what configuration of context is most likely to generate the desired behavior at each step."

The core constraint: LLMs have a finite attention budget. The transformer architecture creates n² pairwise relationships for n tokens. As context grows, the model's ability to capture these relationships gets stretched thin. This creates a performance gradient — not a hard cliff — where models remain capable at longer contexts but show reduced precision for information retrieval and long-range reasoning.

**Guiding principle**: Find the smallest possible set of high-signal tokens that maximize the likelihood of the desired outcome.

### System Prompt Design

- Aim for the "Goldilocks zone" between brittle hardcoded logic and vague high-level guidance.
- Organize prompts into distinct sections using XML tags or Markdown headers (`<background_information>`, `<instructions>`, `## Tool guidance`, etc.).
- Start with a minimal prompt on the best available model, then add instructions based on observed failure modes — not preemptively.
- Examples (few-shot) are worth more than long lists of edge-case rules. Curate a diverse, canonical set rather than exhaustively enumerating every case.

### Tool Design

- Tools should be self-contained, robust to error, and unambiguous in their intended use.
- One of the most common failure modes: bloated tool sets with overlapping functionality. If a human engineer can't definitively say which tool to use in a given situation, an AI agent can't be expected to do better.
- Curating a minimal viable tool set also simplifies context pruning over long interactions.

### Just-in-Time Context Retrieval

Rather than pre-loading all relevant data, agents maintain lightweight identifiers (file paths, URLs, stored queries) and use tools to dynamically load data at runtime. Claude Code exemplifies this: CLAUDE.md files are loaded up front, while `glob` and `grep` allow just-in-time file retrieval.

Benefits of just-in-time loading:
- Avoids stale indexing
- Enables progressive disclosure — agents discover relevant context through exploration
- Metadata (file names, folder structure, timestamps) provides implicit signals about relevance and purpose

### Long-Horizon Context Techniques

**Compaction**: When a conversation approaches the context window limit, summarize its contents and reinitiate with the summary. Claude Code implements this by passing message history to the model to summarize, preserving architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs. The agent continues with the compressed context plus the five most recently accessed files.

Tuning compaction: start by maximizing recall (capture everything relevant), then iterate to improve precision (eliminate superfluous content). Tool result clearing — removing raw tool outputs once processed — is the lightest-touch form of compaction and is now available as a feature on the Claude Developer Platform.

**Structured note-taking**: Agents regularly write notes to memory outside the context window, retrieved at later turns. Claude Code's todo list pattern is one example. The Pokémon-playing Claude agent maintained precise tallies across thousands of game steps using this pattern — tracking objectives, explored regions, and combat strategies across context resets.

**Sub-agent architectures**: Specialized subagents handle focused tasks with clean context windows. Each subagent may use tens of thousands of tokens but returns only a condensed summary (typically 1,000–2,000 tokens) to the lead agent. This achieves separation of concerns: detailed search context stays isolated within subagents while the lead agent focuses on synthesis.

## How Anthropic Built Their Multi-Agent Research System

Source: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/multi-agent-research-system)

### Architecture

The Research feature uses an orchestrator-worker pattern:
- A **LeadResearcher** agent analyzes the query, develops a strategy, and spawns subagents.
- **Subagents** operate in parallel with isolated context windows, each exploring a different aspect of the query.
- A **CitationAgent** post-processes findings to identify and attribute sources.

The LeadResearcher begins by saving its plan to Memory (external storage), since context exceeding 200K tokens will be truncated and the plan must survive.

### Why Multi-Agent Works for Research

Token usage explains 80% of performance variance on the BrowseComp evaluation. Multi-agent architectures effectively scale token usage for tasks that exceed single-agent limits. A multi-agent system with Claude Opus 4 as lead and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by **90.2%** on their internal research eval.

Tradeoff: multi-agent systems use ~15x more tokens than chat interactions. This pattern is economically viable only for high-value tasks.

### Context Management in the Research System

- **Subagent output to filesystem**: Subagents write outputs to external systems and pass lightweight references back to the coordinator. This prevents information loss during multi-stage processing and reduces token overhead from copying large outputs through conversation history.
- **Long-horizon conversation management**: When context limits approach, agents spawn fresh subagents with clean contexts while maintaining continuity through careful handoffs. Agents retrieve stored context (e.g., the research plan) from memory rather than losing it at the context limit.
- **Extended thinking as scratchpad**: The lead agent uses extended thinking to plan its approach — assessing tools, determining query complexity, defining subagent roles. Subagents use interleaved thinking after tool results to evaluate quality and refine next queries.

### Prompt Engineering Lessons

| Principle | Detail |
|---|---|
| Think like your agents | Build simulations using Console with exact prompts and tools; watch agents work step-by-step to reveal failure modes |
| Teach the orchestrator to delegate | Each subagent needs: objective, output format, tool/source guidance, clear task boundaries |
| Scale effort to query complexity | Embed scaling rules: 1 agent + 3–10 tool calls for simple facts; 10+ subagents for complex research |
| Tool design is critical | Bad tool descriptions send agents down wrong paths; each tool needs a distinct purpose and clear description |
| Let agents improve themselves | Claude 4 models can diagnose prompt failures and suggest improvements; a tool-testing agent rewrote MCP tool descriptions, yielding 40% reduction in task completion time |
| Start wide, then narrow | Prompt agents to start with short, broad queries, then progressively narrow focus |
| Parallel tool calling | Introducing parallel subagents and parallel tool calls cut research time by up to 90% for complex queries |

### Production Engineering

- **Rainbow deployments**: Gradually shift traffic from old to new versions while keeping both running, to avoid disrupting in-flight agents.
- **Durable execution**: Agents maintain state across many tool calls; errors must be recoverable without restarting from scratch. Retry logic and regular checkpoints are combined with model-level graceful degradation.
- **Observability**: Full production tracing to diagnose why agents failed. High-level monitoring of agent decision patterns without monitoring individual conversation contents.

## See Also

- [Common Strategies for Context Management](./strategies.md)
- [Key Challenges in Context Management](./challenges.md)
- [Manus Context Engineering](./manus.md)
- [LangGraph Context Engineering](./langgraph.md)
- [Cognition / Devin: Don't Build Multi-Agents](./devin.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Agent Memory Management](../AgentMemory/README.md)
- [Production Best Practices: Context Engineering](../ProductionBestPractices/context-engineering.md)

## References

- [Effective Context Engineering for AI Agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [How we built our multi-agent research system — Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Tool use context engineering cookbook — Anthropic](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)
