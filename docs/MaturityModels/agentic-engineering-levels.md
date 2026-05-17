# The 8 Levels of Agentic Engineering

## Overview

The 8 Levels of Agentic Engineering is a practitioner progression framework mapping the journey from basic AI-assisted coding to fully autonomous multi-agent teams. Proposed by Bassim Eledath (March 2026), the framework describes how engineering teams can incrementally adopt agentic AI, with each level building on the capabilities established below it.

The framework has a critical architectural insight: **Levels 3–5 are prerequisites for Levels 6–8.** If context is noisy, prompts are under-specified, or tools are poorly described, higher levels of automation only amplify the mess rather than solve problems.

## The Eight Levels

### Level 1: Tab Complete

The entry point for AI-assisted coding, exemplified by GitHub Copilot. The AI autocompletes code inline based on context. Passive and suggestion-based — the developer initiates every interaction.

### Level 2: Agent IDE

AI-specific integrated development environments such as Cursor introduce chat functionality integrated directly with the codebase. This enables cross-file editing and richer agentic interactions while remaining synchronous and developer-directed.

### Level 3: Context Engineering

The shift from using AI to *designing for AI*. The guiding principle: every token must fight for its place in the prompt.

Context engineering in practice covers:
- **System prompts**: Instructions that shape agent behavior at session start
- **Rule files**: CLAUDE.md, `.cursorrules`, AGENTS.md — conventions baked into every future session
- **Tool descriptions**: Metadata that guides model selection among available tools
- **Conversation history management**: Controlling what stays in context and what is evicted

Practitioners at this level become hyper-aware of the context being fed to their LLM. When a model makes a mistake, the instinct is to ask "what context is missing?" before blaming model competence.

### Level 4: Compounding Engineering

The goal is to make each feature easier to build than the last — inverting the traditional pattern where technical debt makes each new feature harder.

The mechanism is a four-step loop:

1. **Plan** — define the task and expected outcomes
2. **Delegate** — hand the task to an agent
3. **Assess** — evaluate what the agent did; identify errors and missing context
4. **Codify** — update rule files (CLAUDE.md, hooks, slash commands) so the lesson applies to all future sessions

Because LLMs are stateless, lessons learned must be explicitly recorded. The codify step is what makes the process compound — without it, the agent makes the same mistakes repeatedly across sessions. A well-maintained CLAUDE.md essentially accumulates organizational memory that is automatically injected into every future session.

### Level 5: MCP and Skills

[Model Context Protocol (MCP)](../Standards/mcp.md) and reusable skills allow teams to share agent capabilities across contexts and contributors. A PR review skill, for example, can fan out into specialized subagents — each checking a different quality dimension (security, style, performance, correctness) — triggered conditionally based on the nature of the changeset.

A growing practitioner trend at this level: preferring CLI tools over MCP servers for token efficiency. CLIs allow agents to run targeted commands and inject only the relevant output into the context window, whereas MCP server registrations inject full tool definitions on every invocation.

### Level 6: Harness Engineering and Automated Feedback Loops

This level operationalizes everything built in Levels 3–5. Good context, compounding rules, capable tools, and automated feedback loops now run without direct human supervision, triggered from existing infrastructure.

Concrete examples:
- A **docs bot** that regenerates documentation on every merge and raises a PR to update CLAUDE.md with any new conventions discovered
- A **security reviewer** that scans PRs and opens fix PRs autonomously
- A **dependency bot** that upgrades packages and runs the full test suite before requesting human sign-off

The agent harness at this level includes feedforward guides (what the agent should do) and feedback sensors (whether it did it right). See [Harness Engineering](../AgentHarness/harness-engineering.md) for the full engineering pattern.

### Level 7: Background Agents

The orchestrator LLM dispatches work to worker LLMs in a hub-and-spoke pattern. Agents work overnight, navigate ambiguity independently, and present completed work each morning — "agents raising PRs while you sleep."

Architectural pattern: pairing **local background agents** for short-running tasks with **cloud-hosted sandboxed agents** for longer-running, more autonomous work. Ramp's Inspect tool is a reference implementation: each agent session spins up in a cloud-hosted sandboxed VM with the full development environment pre-loaded.

This is where most engineering teams should focus today. The leverage is high and the tooling is sufficiently mature.

### Level 8: Autonomous Agent Teams

Level 8 removes the single-orchestrator bottleneck of Level 7. Agents coordinate directly: claiming tasks, sharing findings, flagging dependencies, and resolving conflicts without routing everything through a central orchestrator.

Claude Code's experimental Agent Teams feature is an early implementation: multiple Claude Code instances work in parallel on a shared codebase, with each instance operating in its own context window and communicating directly with peers.

**Current limitation**: The author assesses that most models are not ready for this level of autonomy for typical day-to-day work. Even where models are capable enough, they remain too slow and too token-hungry for the pattern to be economical outside high-value moonshot projects — compiler development, browser builds, or large-scale refactors where parallelism provides significant leverage.

## Progression Summary

| Level | Name | Mode | Key Capability |
|---|---|---|---|
| 1 | Tab Complete | Passive | Inline code suggestions |
| 2 | Agent IDE | Interactive | Cross-file chat editing |
| 3 | Context Engineering | Design | Prompt and rule optimization |
| 4 | Compounding Engineering | Systematic | Plan-delegate-assess-codify loop |
| 5 | MCP and Skills | Shared | Reusable, composable agent capabilities |
| 6 | Harness Engineering | Automated | Feedback loops without supervision |
| 7 | Background Agents | Autonomous | Overnight work, hub-and-spoke orchestration |
| 8 | Autonomous Agent Teams | Experimental | Direct agent-to-agent coordination |

## Key Insights

- **Levels 3–5 are foundational.** LLMs are unpredictably good at some things and bad at others. Teams must develop intuition for those edges before stacking more automation on top.
- **The codify step is the flywheel.** Without explicitly recording lessons in rule files, compounding cannot occur — the agent resets to zero every session.
- **Context quality scales up.** Problems introduced at Level 3 are amplified, not solved, by Levels 6–8. Noisy context at scale wastes tokens and produces unreliable output.
- **Level 7 is the current sweet spot.** The tooling is mature, the patterns are proven, and the leverage is high for most engineering teams.
- **Level 8 is a research frontier.** Coordination protocols, conflict resolution, and shared state management across autonomous agents remain open problems.

## Best Practices

| Area | Challenge | Recommendation |
|---|---|---|
| Level 3 | Generic system prompts | Be specific: encode codebase conventions, error handling patterns, and naming standards in rule files |
| Level 4 | Codify step omitted | After every agent session, update CLAUDE.md with lessons learned before closing |
| Level 4 | Agents repeat the same mistakes | When errors recur, identify the missing context — don't assume model incompetence |
| Level 5 | MCP token overhead | Prefer CLI tools for token-sensitive tasks; MCP is better for stateful or structured integrations |
| Level 6 | Jumping to automation too early | Validate Levels 3–5 thoroughly before building automated feedback loops |
| Level 7 | Single local agent bottleneck | Pair local agents with cloud-sandboxed agents for long-running tasks |
| Level 8 | Adopting prematurely | Keep Level 8 for moonshot projects; Level 7 provides better economics for typical engineering work |

## See Also

- [Agent Harness](../AgentHarness/agent-harness.md)
- [Harness Engineering](../AgentHarness/harness-engineering.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Context Engineering Challenges](../ContextEngineering/challenges.md)
- [Model Context Protocol (MCP)](../Standards/mcp.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Agent Types](../Concepts/agent-types.md)

## References

- [The 8 Levels of Agentic Engineering — Bassim Eledath (March 2026)](https://www.bassimeledath.com/blog/levels-of-agentic-engineering) — the original framework defining the eight-level progression
- [Compounding Engineering Pattern — nibzard/awesome-agentic-patterns](https://github.com/nibzard/awesome-agentic-patterns/blob/main/patterns/compounding-engineering-pattern.md) — community documentation of the plan-delegate-assess-codify loop
