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

## Context Management API Primitives (Cookbook)

Source: [Tool Use Context Engineering Cookbook — Anthropic](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)

This cookbook provides a detailed, empirical walkthrough of three first-party API primitives for managing context in long-running agents. The test case is a biology research agent that reads a corpus of eight ~40K-token documents (~328K tokens total) across two sessions — a workload that naturally hits all three context problems.

### The Three Primitives

| Primitive | API Identifier | Beta Header | Triggered By | Solves |
|---|---|---|---|---|
| Compaction | `compact_20260112` | `compact-2026-01-12` | Token threshold (min 50K, default 150K) | All in-session context growth |
| Tool-result clearing | `clear_tool_uses_20250919` | `context-management-2025-06-27` | Token threshold (default 100K) | Tool-result bloat specifically |
| Memory tool | `memory_20250818` | none (standalone) | Model-driven tool calls | Cross-session persistence |

The three primitives address different slices of the context problem and compose rather than compete. Clearing and compaction manage what is inside the current window; memory moves information out of the window so it survives across sessions.

### Baseline: What Happens Without Context Management

Without any context management, the research agent's context climbs to 335,279 tokens across 5 turns. The breakdown at the end of the run:

- File-read results: ~322,946 tokens (96.3% of total)
- Tool-call records: ~6,287 tokens (1.9%)
- Agent reasoning text: ~5,660 tokens (1.7%)
- User/task prompts: ~357 tokens (0.1%)

On a 200K-token model, the same run hits a hard stop mid-task. On a 1M-token model, the run completes but context rot degrades recall of early documents — the first file read is technically present but buried under hundreds of thousands of tokens of subsequent content.

### Compaction

Compaction takes a conversation nearing the context window limit, summarizes its contents, and reinitiates with that summary. It is a whole-transcript operation: user messages, assistant messages, tool calls, tool results, and prior compaction blocks are all flattened into the summary.

In the cookbook's research agent run (trigger at 180K), compaction fired once at turn 4, replacing prior turns with a ~2,783-token summary. Peak context dropped from 335,279 (baseline) to 169,164.

What survives compaction vs. what is lost:
- High-level facts central to the task (lifespan figures, organism identities, major comparisons): typically preserved
- Obscure specifics (appendix table cells, heterogeneity statistics, exact phrasing): typically lost

This is a meaningful difference from clearing: clearing drops tool results wholesale so content is gone until re-fetched, while compaction keeps the substance in compressed form but loses verbatim detail.

**Implementing compaction effectively**: The `instructions` parameter completely replaces the default summarization prompt (it does not supplement it). The default prompt is:

> "You have written a partial transcript for the initial task above. Please write a summary of the transcript. The purpose of this summary is to provide continuity so you can continue to make progress towards solving the task in a future context... You must wrap your summary in a `<summary></summary>` block."

For a research agent, a custom instruction might be: "Summarize this research agent transcript. Preserve every quantitative lifespan figure and effect size with its source organism, and note which documents have been read and which remain."

**When to skip compaction**: If sessions stay well under the context limit naturally, compaction adds lossiness without benefit. If context bloat is mostly re-fetchable tool output, clearing is cheaper and lossless.

### Tool-Result Clearing

Clearing is a sub-transcript operation: it walks the message list and surgically replaces `tool_result` content blocks with a short placeholder, leaving everything else (user messages, assistant reasoning, the `tool_use` record) untouched. The model retains a record that it made the call and with what input, but the bulky response body is gone.

In the cookbook's run (trigger at 30K, keep=4), clearing fired 4 times, freeing ~163K tokens per event. Peak context: 173,137 vs. 335,279 baseline. No inference cost — purely a mechanical edit to the message list.

What clearing costs: every file read except the most recent `keep` is gone from context. If the agent needs that content again, it must call the tool again. How much this costs depends on the tool: re-reading a local file is nearly free; re-calling a rate-limited or slow API is not.

**Implementing clearing effectively**: Unlike compaction and memory, clearing has no prompt to tune. Key knobs:
- `trigger`: token threshold at which clearing fires
- `keep`: number of most-recent tool results to retain (default 3)
- `clear_at_least`: minimum tokens to clear per firing (important for cache invalidation economics — clearing invalidates cached prompt prefixes, so clear enough to make the cache write cost worthwhile)
- `exclude_tools`: list of tool names to exempt from clearing (critical when combining with the memory tool — see below)

**When to skip clearing**: If the agent genuinely needs to see past tool results in full (e.g., cross-document comparison where passages must be visible side by side), clearing forces redundant re-reads.

### Memory Tool

The memory tool enables the model to store and retrieve information across conversations through a persistent file directory. The model decides what and when to save as part of its tool-use loop. An auto-injected system prompt establishes a check-memory-first protocol: "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE... Your context window might be reset at any moment."

The tool is client-side: the API provides the protocol and tool schema; the application implements the file backend. The tool supports six operations: `view`, `create`, `str_replace`, `insert`, `delete`, `rename`.

In the cookbook's two-session comparison:
- Session 2 without memory: 8 file reads, peak context 333,977 tokens (had to rediscover everything from scratch)
- Session 2 with memory: 4 file reads, peak context 172,623 tokens (read Session 1's saved notes, skipped re-reading 4 documents)

**Implementing memory effectively**:
- Topical guidance: add a system-prompt instruction like "Only write down information relevant to `<topic>` in your memory system" to steer what gets saved.
- Organization: add "when editing your memory folder, always try to keep its content up-to-date, coherent and organized... Do not create new files unless necessary" to prevent accumulating half-overlapping notes.
- Initializer sessions: for multi-session work, run a dedicated first session that sets up memory artifacts (progress log, feature checklist, references) before substantive work begins.
- Storage hygiene: track file sizes to prevent unbounded growth; validate against path traversal (`../../etc/passwd`); consider clearing files not accessed in extended periods.

**When to skip memory**: If each session should start fresh (e.g., a user-facing chatbot where every conversation is independent), memory carries state you don't want.

### Combining All Three

Claude Code uses multiple of these strategies in production: compaction for long conversations, and two complementary memory systems — CLAUDE.md files (user-written, checked into source control) and auto memory (model-written learnings and patterns).

When combining clearing with the memory tool, use `exclude_tools: ["memory"]` to prevent the agent's memory reads and writes from being cleared. Without this, the agent could lose track of what it just saved.

In the cookbook's all-three run (triggers set above the first batch so all three activate in one session):
- Peak context: 169,938 tokens (vs. 335,279 baseline)
- Final context: 13,749 tokens (vs. 335,279 baseline)
- Clearing fired 9 times; compaction fired once; memory wrote 3 files

### Workload-to-Primitive Mapping

| If your workload has... | Worth trying first | Watch for |
|---|---|---|
| Sessions spanning days or weeks | Memory tool | Tool-call overhead; stale memory if facts change |
| Agent that should learn user preferences across sessions | Memory tool | PII/sensitive data policy; stale preferences |
| Large, re-fetchable tool results | Clearing | Agent re-reading what was just cleared; tune `keep` and `trigger` |
| Dialogue as the primary context | Compaction | Specific figures getting summarized away |
| Tool results that aren't easily re-fetchable (ephemeral APIs, uploads) | Compaction over clearing | Summary fidelity on those specific results |
| Every session should start fresh | Skip memory | Cross-session state you don't want |
| Sessions stay well under the window | Skip compaction | Lossiness you don't need |

### On Larger Context Windows

With Claude Sonnet 4.6 and Opus 4.6 providing 1M-token context, the hard limit is far away — but context rot and prefill latency scale with how much is in the window, not with the window's limit. The baseline's context breakdown showed 96.3% of tokens were stale file-read results. Keeping the working set lean is still worth doing even when the hard wall is far away.

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
- [Tool Use Context Engineering Cookbook — Anthropic](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)
