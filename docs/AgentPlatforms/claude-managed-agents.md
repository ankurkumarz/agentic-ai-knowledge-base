# Claude Managed Agents

## Overview

Claude Managed Agents is Anthropic's hosted agent execution platform, providing a first-party runtime where agents persist state, manage memory, and coordinate across sessions without developers building their own infrastructure. Announced through 2025–2026, the platform has progressively added memory, dreaming, outcomes, and multiagent orchestration — moving Claude from a stateless completion API toward a durable, self-improving agent system.

## Key Features

### Memory (Public Beta — April 2026)

Claude Managed Agents lets Claude manage its own memory as a file system: the agent reads and writes folders and text files using familiar tools like bash and grep. Claude itself decides how many files to use, how to structure them, and what information is worth retaining.

- Memory is human-readable and inspectable — stored as plain markdown/text files
- The model autonomously determines memory structure and granularity
- Memory persists across sessions and is available on the Claude Managed Agents API

### Dreaming (Research Preview — May 2026)

Dreaming is a scheduled memory-curation process that runs **between** agent sessions, analogous to hippocampal memory consolidation during sleep. Rather than storing raw session logs indefinitely, dreaming reviews prior sessions and memory stores to improve future performance.

**What dreaming does:**
- Merges new signal into existing topic files rather than creating near-duplicates
- Removes outdated or contradicted facts
- Converts relative date references to absolute dates for temporal durability
- Highlights recurring patterns: repeated mistakes, workflows agents converge on, team-wide preferences
- Reorganizes memory into clean, indexed topic files; keeps the final index under 200 lines

**Developer control**: Dreaming can update memory automatically or surface proposed changes for human review before they land. Developers choose the level of control.

**Availability**: Research preview; requires requesting access. Only available on the Claude Managed Agents API.

**Biological analogy**: Anthropic compares it explicitly to hippocampal replay — the brain's process of replaying the day's events during sleep to consolidate long-term learning.

### Outcomes (Public Beta — May 2026)

Outcomes is a self-grading loop that allows developers to define success criteria in plain language, then automatically evaluate whether the agent met them.

**How it works:**
1. Developer writes a rubric describing what a successful output looks like (plain text)
2. Agent completes its task
3. A separate **grader** (an evaluator agent running in its own context window, isolated from the agent's reasoning) scores the output against the rubric
4. When the output falls short, the grader identifies what needs to change and the agent takes another pass

**Why the grader runs in a separate context**: This prevents the agent's own reasoning from contaminating the evaluation — the same principle used in LLM-as-judge evaluation frameworks.

**Benchmarks**:
- Anthropic's internal benchmarks show up to +10 percentage points task success improvement over a standard prompting loop
- Largest gains occur on the hardest tasks
- Harvey (legal AI startup, pilot customer) reported approximately **6× jump in task completion rates**

### Multiagent Orchestration (Public Beta — May 2026)

Multiagent orchestration lets a lead agent break a job into pieces and delegate each piece to a **specialist agent** with its own model, prompt, and tools.

**Architecture:**
- Specialists work in **parallel** on a shared filesystem
- Each specialist contributes to the lead agent's overall context
- The lead agent can check back in mid-workflow because events are persistent
- Every agent retains memory of what it has done (durable event log)

This enables compound workflows where parallelism and specialization improve both speed and quality — e.g., a research lead agent delegating to a data-fetching specialist, a reasoning specialist, and a writing specialist simultaneously.

## Memory Architecture

Claude Managed Agents implements a filesystem-based memory model distinct from most third-party memory solutions:

| Aspect | Approach |
|---|---|
| Storage format | Plain text / markdown files in a virtual filesystem |
| Structure | Agent-determined — model decides file layout and granularity |
| Access | bash, grep, and standard file tools |
| Cross-session persistence | Yes |
| Human inspectability | High — files are directly readable |
| Consolidation | Via dreaming (scheduled, between sessions) |

## Self-Improvement Loop

The combination of Memory + Dreaming + Outcomes creates a compound self-improvement loop:

1. **Session**: Agent executes a task, writes to memory as it goes
2. **Outcomes evaluation**: Grader scores the result; agent iterates if needed
3. **Dreaming**: Between sessions, patterns are extracted from episodic memory, outdated facts removed, and procedural improvements consolidated
4. **Next session**: Agent starts with richer, more accurate memory and inherited behavioral improvements

This is Anthropic's production implementation of the reflection/consolidation strategy described in the CoALA memory taxonomy.

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| Rubric design for Outcomes | Vague rubrics produce inconsistent grading | Write rubrics as observable, measurable criteria — "The response cites at least 2 sources" rather than "The response is good" |
| Dreaming data quality | Poorly structured memory leads to poor consolidation | Structure initial memory files by topic; avoid mixing unrelated facts in a single file |
| Multiagent context budget | Parallel specialists can inflate total token cost significantly | Set per-specialist token budgets; use the lead agent's context only for synthesis, not raw data |
| Memory staleness before dreaming | Rapidly changing facts can be stale between dreaming cycles | For volatile facts, prefer explicit in-session overwrites rather than relying on dreaming to clean up |
| Grader context isolation | Grader seeing agent reasoning defeats the purpose | Do not pass agent scratchpad or chain-of-thought to the grader context |

## Availability

| Feature | Status |
|---|---|
| Memory | Public beta |
| Outcomes | Public beta |
| Multiagent Orchestration | Public beta |
| Dreaming | Research preview (request required) |

## See Also

- [Agent Memory Management](../AgentMemory/README.md)
- [Long-Term Memory Strategies](../AgentMemory/ltm-strategies.md)
- [Self-Learning Agents Reference Architecture](../ReferenceArchitecture/self-learning-agents.md)
- [Production Best Practices — State & Memory](../ProductionBestPractices/state-memory.md)
- [Anthropic Overview](../AllThingsAnthropic/README.md)
- [Evaluation Frameworks](../EvaluationFrameworks/README.md)

## References

- [New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](https://claude.com/blog/new-in-claude-managed-agents) — Anthropic official announcement, May 2026
- [Memory and dreaming for self-learning agents](https://youtu.be/RtywqDFBYnQ) — YouTube video, Anthropic, 2026
- [Dreams — Claude API Docs](https://platform.claude.com/docs/en/managed-agents/dreams) — Official API documentation
- [Anthropic adds self-improving 'dreaming' system to Claude Managed Agents](https://yourstory.com/ai-story/anthropic-claude-dreaming-self-improving-agents) — YourStory, May 2026
- [Anthropic introduces "dreaming," a system that lets AI agents learn from their own mistakes](https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes) — VentureBeat, May 2026
