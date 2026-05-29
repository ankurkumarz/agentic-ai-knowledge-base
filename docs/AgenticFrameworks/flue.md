# Flue

## Overview

Flue is a TypeScript agent harness framework for building autonomous AI agents that are fully headless and programmable. Its core equation — **Agent = Model + Harness** — positions the harness layer as the primary design concern. Where most frameworks focus on model orchestration, Flue centers on giving agents a secure, durable execution environment: sessions, tools, filesystem access, a built-in sandbox, and structured deployment targets. The framework was created by the Astro team (withastro) and is Apache-2.0 licensed with ~3.8K GitHub stars as of mid-2026.

Flue is comparable to Astro or Next.js, but for agents — write once, build, and deploy agents anywhere.

## Key Features

- **Harness-first architecture**: Sessions, tools, skills, sandbox, and filesystem access are first-class primitives, not afterthoughts
- **Virtual sandbox** (default): Powered by `just-bash` — faster, cheaper, and more scalable than full containers; suited for high-traffic agents
- **Container sandbox** (via Daytona connector): Full isolated Linux environments with git, Node.js, Python, and a cloned repo for complex coding agents
- **Skills system**: Reusable agent capabilities defined in Markdown (`.md` files with YAML frontmatter); auto-discovered from `.agents/skills/<name>/SKILL.md` at runtime
- **Session persistence**: Message history and sandbox state persist across requests; multi-thread support via `harness.session(threadName)`
- **Tasks**: Focused one-shot child agents with isolated message history via `session.task()`
- **MCP integration**: Connect remote Model Context Protocol servers at runtime via `connectMcpServer()`; secrets stay in env rather than prompts
- **Runtime-agnostic**: Deploy to Node.js, Cloudflare Workers, GitHub Actions, or GitLab CI/CD with a single build command
- **Observability**: Integrates with OpenTelemetry, Braintrust tracing, and Sentry error reporting
- **Built-in tools**: Filesystem read/write, shell, grep, glob out of the box

## Architecture

Flue's harness is composed of two core packages:

| Package | Role |
|---|---|
| `@flue/runtime` | Core harness: sessions, tools, sandbox, filesystem capabilities |
| `@flue/cli` | Build system and CLI tooling (`flue dev`, `flue build`, `flue run`) |

**Agent files** live in `agents/<name>.ts` and define the agent's harness configuration — model defaults, tools, sandbox type, and filesystem access. **Skills** are Markdown-based reusable behaviors assigned at the agent, session, or per-call level for fine-grained orchestration.

**Sandbox tiers:**

| Tier | Technology | Use case |
|---|---|---|
| Virtual (default) | `just-bash` in-memory FS + Bash | Fast, cost-effective, high-traffic agents |
| Container (via connector) | Daytona isolated Linux VM | Full coding agents, git workflows, browser access |

**State persistence targets:**

| Deploy target | State mechanism |
|---|---|
| Cloudflare Workers | Durable Objects |
| Node.js | Pluggable custom storage |

## Deployment

Flue supports three invocation patterns:

- **CLI**: `flue run <workflow>` for one-shot invocations
- **HTTP server**: Agents exposed at `/agents/<name>/<id>`; supports REST calls
- **WebSocket**: Long-lived connections for message-driven agents (with custom auth middleware)

Build and deployment commands:

```
flue dev --target node          # Watch-mode dev server on port 3583
flue build --target node        # Single bundled file for Node.js
flue build --target cloudflare  # Deploy to Cloudflare Workers
```

## Integrations

| Integration | Description |
|---|---|
| Daytona | Remote container sandbox connector — full Linux environment per session |
| MCP servers | Any remote MCP server connectable at runtime via `connectMcpServer()` |
| OpenTelemetry | Distributed tracing export |
| Braintrust | LLM evaluation and tracing |
| Sentry | Error monitoring |
| Slack / Teams / Discord / GitHub | Communication platform connectors |

Connectors are Markdown installation instructions applied by an AI coding agent, not npm packages.

## Comparison with Other Frameworks

| Dimension | Flue | LangChain / LangGraph | CrewAI | Mastra |
|---|---|---|---|---|
| Primary language | TypeScript | Python / TypeScript | Python | TypeScript |
| Core abstraction | Agent harness | Chain / graph | Crew / role | Workflow |
| Sandbox built-in | Yes (virtual + container) | No | No | No |
| Session persistence | First-class | Via LangGraph store | Limited | Partial |
| MCP support | Native | Plugin | Plugin | Plugin |
| Deploy targets | Node, Cloudflare, CI | Self-hosted | SaaS / self-hosted | Self-hosted |
| License | Apache-2.0 | MIT | MIT | Apache-2.0 |
| Maturity | Experimental (~3.8K stars) | Production (~98K stars) | Production (~25K stars) | Early-stage |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Secret management | Secrets in prompts or filesystem context create injection risks | Store secrets in `.env`; pass to MCP servers via `connectMcpServer()`, never inline |
| Sandbox selection | Full containers add latency and cost | Default to virtual `just-bash` sandbox; use Daytona only for workflows needing git, npm, or a browser |
| Session sprawl | Unbounded sessions consume memory and storage | Use `session.task()` for one-shot child agents; name threads explicitly |
| Skills organization | Ad-hoc prompts scattered across agents | Centralize reusable behaviors as Skills in `.agents/skills/`; assign at session level |
| Observability | Silent agent failures are hard to debug | Wire OpenTelemetry from the start; export spans to Braintrust or a compatible backend |
| Build targets | Deploying to the wrong runtime silently breaks agents | Test with `flue dev --target <env>` locally before `flue build` |

## Limitations

- **Experimental status**: Active development; breaking changes are possible
- **TypeScript-only**: No Python or other language SDK (a Python-inspired port, PyFlue, is community-maintained separately)
- **Ecosystem size**: Smaller community and connector library compared to LangChain or CrewAI
- **Sandbox depth**: The default virtual sandbox covers most shell operations but not browser automation or full GUI workflows without the Daytona connector

## See Also

- [Agent Harness](../AgentHarness/agent-harness.md) — foundational harness concepts and the Agent = Model + Harness equation
- [Harness Engineering](../AgentHarness/harness-engineering.md) — engineering practices for building and optimizing harnesses
- [LLM Harness Survey](../AgentHarness/llm-harness-survey.md) — ETCLOVG taxonomy and empirical benchmarks across 23+ harness systems
- [Mastra](./mastra.md) — TypeScript-first multi-agent framework; complementary to Flue for workflow-centric patterns
- [Standards: MCP](../Standards/mcp.md) — Model Context Protocol that Flue integrates natively
- [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md) — sandbox security models including the technologies Flue uses
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [Agentic Frameworks Overview](./README.md)

## References

- [Flue — The Agent Harness Framework](https://flueframework.com/) — official project site
- [GitHub: withastro/flue](https://github.com/withastro/flue) — source repository, Apache-2.0, ~3.8K stars (mid-2026)
- [Introducing Flue (X / Fred K. Schott)](https://x.com/FredKSchott/status/2050274923852210397) — launch announcement by the Astro co-founder
