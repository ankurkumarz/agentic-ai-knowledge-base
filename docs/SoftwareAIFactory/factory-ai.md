---
type: Platform
title: Factory AI
description: Factory AI is an agent-native software development platform whose Droids work across planning, implementation, testing, review, and engineering operations.
tags: [software-ai-factory, factory-ai, droids, sdlc, agentic-ai]
timestamp: 2026-10-20T00:00:00Z
---

# Factory AI

## Overview

Factory AI is an agent-native software development platform whose Droids work across planning, implementation, testing, review, and engineering operations. Its product documentation describes natural-language task delegation across terminal, IDE, browser, and Slack surfaces, with adjustable autonomy and support for multiple model providers ([Factory Droids](https://factory.com/product/droids)).

Factory announced general access to Droids on May 28, 2025, describing coding, incident investigation, codebase research, ticket management, product-spec creation, and PR review. Treat that announcement as historical scope rather than assuming its original packaging or pricing still applies ([GA announcement](https://factory.com/news/factory-is-ga)).

## Capabilities and Execution Model

| Capability | Documented behavior | Factory relevance |
|---|---|---|
| Task-to-PR workflow | Droids plan, implement, test, and create pull requests from a task description ([product page](https://factory.com/product/droids)). | Connects coding to a reviewable delivery artifact. |
| Shared project context | CLI work uses project files, repository instructions, and connected knowledge ([CLI overview](https://docs.factory.ai/cli/getting-started/overview)). | Connects execution to team conventions and external context. |
| Multi-agent Missions | `/missions` and `droid exec --mission` launch multi-agent Missions ([CLI overview](https://docs.factory.ai/cli/getting-started/overview)). | Supports workflows larger than a single interactive task. |
| Custom Droids and skills | `/droids` delegates scoped tasks; skills package reusable procedures ([CLI overview](https://docs.factory.ai/cli/getting-started/overview)). | Separates specialist work from reusable team knowledge. |
| MCP, hooks, and plugins | MCP connects tools and data; hooks run shell commands around lifecycle events; plugins bundle extensions ([CLI overview](https://docs.factory.ai/cli/getting-started/overview)). | Integration and customization points for a team workflow. |
| Headless execution | `droid exec` runs in scripts and CI/CD with structured input/output ([CLI overview](https://docs.factory.ai/cli/getting-started/overview)). | Moves a stable local procedure into repeatable automation. |
| Model choice and autonomy | Factory describes model selection across Claude, GPT, and Gemini and configurable boundaries for edits, execution, and approval ([product page](https://factory.com/product/droids)). | Requires evaluation of task quality and permissions, not just model preference. |

## Lifecycle Coverage

Factory's GA announcement explicitly covers product specs, research, implementation, PR review, and on-call investigation, while the CLI documentation adds a path to headless automation. These are documented capabilities, not a guarantee that every stage is autonomously completed or that production authorization is handled for a particular organization ([GA announcement](https://factory.com/news/factory-is-ga), [CLI overview](https://docs.factory.ai/cli/getting-started/overview)).

The distinction from the Anthropic playbook is product versus process: Factory supplies a runtime and workflow surfaces, while the playbook defines an artifact chain and review controls. Applying the playbook's operating model to Factory is an architectural option, not a documented native `intent.md`/`spec.md`/`plan.md` integration ([Factory CLI](https://docs.factory.ai/cli/getting-started/overview), [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)).

## Adoption Guidance and Limitations

The following is evaluation guidance, not a report of implementation results. It builds on the CLI's approval, context, and headless-execution surfaces ([Factory documentation](https://docs.factory.ai/cli/getting-started/overview)).

| Area | Recommendation | Verification required |
|---|---|---|
| Initial workflow | Start with a bounded bug fix or PR review and explicit test expectations. | Confirm the diff and tool output support the claimed outcome. |
| Customization | Version team instructions, skills, hooks, and plugin configuration. | Confirm which configuration is actually loaded by each execution surface. |
| Automation | Move a successful interactive workflow to `droid exec`. | Verify CI identity, credentials, allowed tools, timeout, and failure handling. |
| Deployment | Treat production release as a separately authorized action. | Check enforcement outside the agent's prose instructions. |

No current price, deployment-residency guarantee, or benchmark rank is asserted here. The fetched product and CLI sources do not establish all commercial and security terms needed for an enterprise procurement decision; the older GA announcement is not used as a current pricing reference.

## See Also

- [Warp Factories](warp-factories.md): another documented standing-factory platform; no feature parity implied.
- [Building Your Own Software Factory](building-your-own-software-factory.md): related operating-model workshop.
- [Software AI Factory](README.md)
- [Anthropic AI-Native SDLC](ai-native-sdlc.md)
- [Devin](devin.md)
- [OpenHands](openhands.md)
- [AI Coding Agents](../AICodingAgents/ai-coding-agents.md)
- [Loop Engineering](../AgentHarness/loop-engineering.md)
- [Production Deployment](../ProductionBestPractices/deployment.md)
- [Agent Security](../ProductionBestPractices/security.md)

## References

- [Warp Factories overview](https://docs.warp.dev/factories/): related platform reference, not evidence of Factory AI features.
- [Building your own software factory](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz): related Cursor workshop, not evidence of this platform's product features.
- [Factory Droids](https://factory.com/product/droids): product surfaces, task-to-PR workflow, model choice, and autonomy.
- [Factory is GA: Droids for the Entire SDLC](https://factory.com/news/factory-is-ga): May 28, 2025 announcement and historical lifecycle scope.
- [Droid CLI overview](https://docs.factory.ai/cli/getting-started/overview): Missions, Custom Droids, skills, MCP, hooks, plugins, and Exec Mode.
- [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): process reference used for the product-versus-operating-model distinction.
