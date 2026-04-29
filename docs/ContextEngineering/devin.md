# Cognition / Devin: Context Engineering Principles

## Overview

Walden Yan (Cognition, builders of Devin) published "Don't Build Multi-Agents" as a challenge to the prevailing trend of multi-agent architectures. The post argues that context engineering — not agent count — is the primary determinant of agent reliability, and that naive multi-agent designs systematically violate the two principles that make agents reliable.

> "Context engineering… is effectively the #1 job of engineers building AI agents." — Cognition

## Two Core Principles

### Principle 1: Share Context — Full Agent Traces, Not Just Individual Messages

When subagents receive only a summary or a single message describing their subtask, they lack the full context of decisions made upstream. This leads to misinterpretation of the task and outputs that don't fit the broader work.

**Example**: An agent tasked with "build a Flappy Bird clone" decomposes into two subagents. Subagent 1 builds a Super Mario Bros-style background (misinterpreting the subtask). Subagent 2 builds a bird that doesn't look like a game asset. The orchestrator is left combining two miscommunications.

Simply copying the original task to subagents doesn't solve this — in a real multi-turn production system, the agent has made tool calls, accumulated context, and made implicit decisions that all affect how the subtask should be interpreted.

### Principle 2: Actions Carry Implicit Decisions — Conflicting Decisions Carry Bad Results

When subagents work in parallel without seeing each other's work, their actions reflect incompatible assumptions. Even if each subagent individually produces reasonable output, the combined result is inconsistent.

**Example**: Two subagents building different parts of a UI independently choose different visual styles, component libraries, and interaction patterns. Neither is wrong in isolation; together they're unusable.

Yan argues these two principles are so critical that any architecture violating them should be ruled out by default.

## Recommended Architectures

### Single-Threaded Linear Agent (Default)

The simplest approach: one agent, continuous context, sequential execution. Context is never split, so there are no coordination problems. This gets further than most teams expect.

Limitation: for very large tasks, context windows overflow.

### Compression-Based Extension

For truly long-duration tasks, introduce a dedicated compression model whose purpose is to distill a history of actions and decisions into key details, events, and decisions. This is hard to get right — Cognition fine-tuned a smaller model specifically for this task.

The benefit: an agent that handles longer contexts without the coordination problems of multi-agent systems. The limit: you will still eventually hit a context ceiling, and the compression quality directly determines reliability.

## Analysis of Real-World Agent Designs

### Claude Code Subagents

As of June 2025, Claude Code spawns subtasks but never runs them in parallel with the main agent. Subagents are tasked only with answering questions, not writing code. Why? The subagent lacks the main agent's full context — it can answer a well-defined question, but can't safely make decisions that affect the broader codebase. The benefit of subagents here is that their investigative work doesn't accumulate in the main agent's history, extending the effective context before overflow.

### Edit Apply Models (Historical)

In 2024, many coding agents used a two-model pattern: a large model outputs a markdown description of desired code changes, and a small model rewrites the file accordingly. This was an attempt to isolate decision-making from execution. It was fragile — the small model frequently misinterpreted the large model's instructions due to subtle ambiguities. Today, decision-making and applying are more often done by a single model in one action.

### Multi-Agent Collaboration (Current State)

Yan is skeptical of multi-agent collaboration in 2025: "running multiple agents in collaboration only results in fragile systems. The decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough between the agents."

The cross-agent context-passing problem has not been solved. Yan expects it will eventually come as single-threaded agents get better at communicating with humans — at which point the same communication efficiency will unlock reliable multi-agent coordination.

## Relationship to Other Approaches

Cognition's position is more conservative than Anthropic's multi-agent research system, which uses parallel subagents successfully for breadth-first research tasks. The key distinction:

- **Research tasks** (Anthropic's use case): subagents explore independent directions with minimal interdependencies. Context clash is manageable because subagents don't need to coordinate on shared decisions.
- **Coding/construction tasks** (Cognition's use case): subagents must make decisions that affect shared artifacts. Context clash is catastrophic because inconsistent decisions produce unusable outputs.

Lance Martin (LangChain) captures this in open-deep-research's design: subagents are limited to information gathering, not decision-making, specifically to avoid the coordination problems Cognition describes.

## See Also

- [Common Strategies for Context Management](./strategies.md)
- [Key Challenges in Context Management](./challenges.md)
- [Anthropic Multi-Agent Research System](./anthropic.md)
- [LangGraph Context Engineering](./langgraph.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)

## References

- [Don't Build Multi-Agents — Cognition / Walden Yan](https://cognition.ai/blog/dont-build-multi-agents) — primary source
- [Context Engineering for Agents — Lance Martin (references Cognition)](https://rlancemartin.github.io/2025/06/23/context_engineering/)
