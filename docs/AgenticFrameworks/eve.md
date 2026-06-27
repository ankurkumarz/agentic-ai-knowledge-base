# Eve

## Overview

Eve is an open-source, filesystem-first agent framework released by Vercel (public preview, 2026). Where many frameworks define agents primarily through code, Eve defines an agent through a single `instructions.md` file at the root of an agent's directory — the agent's behavior, tone, and operating procedure live in plain markdown, while supporting capabilities (tools, sub-agents, evals) are discovered from the surrounding filesystem structure rather than registered imperatively. The project is hosted at [github.com/vercel/eve](https://github.com/vercel/eve).

## Key Concepts / Architecture / Features

- **Filesystem-first agent definition**: an agent is a directory; `instructions.md` is its system prompt and operating contract. There is no required code entry point to describe agent behavior.
- **Auto-registered tools**: any tool placed in the agent's `tools/` directory is automatically discovered and exposed to the agent at runtime — no manual tool registration step.
- **Durable execution**: agent runs are checkpointed so long-running or multi-step tasks can resume after interruption rather than restarting from scratch.
- **Sandboxed compute**: tool execution runs in an isolated compute environment by default, separating agent-driven code execution from the host process.
- **Approvals**: a built-in human-in-the-loop gate for sensitive or irreversible tool calls, configurable per tool.
- **Channels**: a connector layer for exposing an agent over different surfaces (e.g., chat, API) without changing the agent's core definition.
- **Tracing and evals**: first-class, built into the framework rather than bolted on via a third-party SDK — every run produces a trace, and evals can be defined alongside the agent to regression-test behavior changes.

## Suitable for (Pros)

- Teams that prefer an infrastructure-as-code-adjacent, file-based way to define and version agent behavior (the `instructions.md` + directory convention is easy to diff and review in pull requests)
- Workflows needing durable, resumable execution without standing up a separate orchestration layer
- Use cases requiring sandboxed tool execution and human approval gates out of the box, rather than as external add-ons

## Limitations (Cons)

- **Public preview**: the project is new and the API surface may change before a stable release
- **Vercel ecosystem affinity**: tooling and deployment conventions are most polished for Vercel-hosted deployments, though the framework itself is open source and self-hostable
- **Filesystem convention lock-in**: the markdown-and-directory convention is a strong opinion; teams wanting code-first agent definition (as in LangGraph or CrewAI) will find it a different mental model

## Comparison with Other Frameworks

| Dimension | Eve | Flue | LangChain / LangGraph | CrewAI |
|---|---|---|---|---|
| Agent definition | `instructions.md` + filesystem | TypeScript agent files | Python / TypeScript code | Python code (roles/crews) |
| Tool registration | Auto-discovered from `tools/` | Explicit harness config | Explicit binding | Explicit binding |
| Durable execution | Built-in checkpointing | Via Cloudflare Durable Objects / custom storage | Via LangGraph store | Limited |
| Sandboxed compute | Built-in | Virtual (`just-bash`) + container (Daytona) | No | No |
| Approvals (HITL) | Built-in | Not first-class | Plugin/custom | Not first-class |
| Maturity | Public preview | Experimental (~3.8K stars) | Production | Production |
| License | Open source | Apache-2.0 | MIT | MIT |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Instruction sprawl | A single large `instructions.md` becomes hard to maintain as agent scope grows | Keep instructions focused; split distinct responsibilities into sub-agents rather than one monolithic instruction file |
| Tool discovery surprises | Auto-registration means any file dropped in `tools/` becomes callable | Review the `tools/` directory in code review the same way you would review explicit tool registration elsewhere |
| Approval fatigue | Gating too many tool calls behind approvals slows iteration | Reserve approvals for genuinely irreversible or sensitive actions; let read-only or reversible tools run unattended |
| Evals as an afterthought | Teams skip writing evals since the framework doesn't force it | Treat eval definitions as part of the agent's directory from day one, alongside `instructions.md` |

## See Also

- [Flue](./flue.md) — comparable harness-first TypeScript framework with built-in sandbox tiers and session persistence
- [Agent Harness](../AgentHarness/agent-harness.md) — foundational harness concepts (system prompts, tools, sandbox, orchestration)
- [Agent Skills / SKILLS.md](../Standards/skills.md) — the broader markdown-based, filesystem-discovered workflow convention Eve's `instructions.md` model parallels
- [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md) — sandbox isolation models, including the sandboxed compute approach Eve uses by default
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [Agentic Frameworks Overview](./README.md)

## References

- [GitHub: vercel/eve](https://github.com/vercel/eve) — source repository, public preview
