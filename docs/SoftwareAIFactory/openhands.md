---
type: Platform
title: OpenHands
description: OpenHands is a software-agent ecosystem combining an agent control center, SDK, execution APIs, automation components, and deployment options.
tags: [software-ai-factory, openhands, software-agents, sdlc, agentic-ai]
timestamp: 2026-10-20T00:00:00Z
---

# OpenHands

## Overview

OpenHands is a software-agent ecosystem combining an agent control center, SDK, execution APIs, automation components, and deployment options. Its documentation distinguishes Agent Canvas, Software Agent SDK, Agent Server, managed Cloud, Enterprise, and a community-supported Sandbox Server rather than presenting them as one interchangeable component ([OpenHands introduction](https://docs.openhands.dev/overview/introduction)).

The platform describes an event-driven workflow from signal through plan, execution, validation, shipping, and monitoring, while keeping engineers responsible for review, approval, and merge. That lifecycle scope makes it relevant to a software AI factory rather than only an interactive coding-agent catalog ([OpenHands platform](https://www.openhands.dev/)).

## Component Boundaries

| Component | Documented responsibility | Evaluation implication |
|---|---|---|
| Agent Canvas | Open-source browser control center for conversations and automations; connects to one or more execution backends ([introduction](https://docs.openhands.dev/overview/introduction)). | Distinguish UI hosting from where tools and agents actually execute. |
| Software Agent SDK | Python and REST APIs for coding agents, with shell, file-editing, browsing, and MCP tools ([SDK documentation](https://docs.openhands.dev/sdk)). | Foundation for custom software-engineering workflows. |
| Agent Server | Execution, conversations, tools, and workspaces over REST and WebSocket APIs ([introduction](https://docs.openhands.dev/overview/introduction)). | A runtime/API boundary, not just a browser session. |
| Automation Server | Scheduled and event-driven automation lifecycle, listed separately in the repository map ([introduction](https://docs.openhands.dev/overview/introduction)). | Check trigger delivery, run ownership, and operation history. |
| Sandbox Server | Community-supported control plane for sandbox environments hosting Agent Server ([introduction](https://docs.openhands.dev/overview/introduction)). | Separate sandbox provisioning from agent reasoning and UI concerns. |
| Cloud and Enterprise | Cloud provides managed execution, collaboration, access controls, usage reporting, and budgets; Enterprise provides commercial deployment and support options ([introduction](https://docs.openhands.dev/overview/introduction)). | Verify the exact offering and contract rather than assuming feature parity. |

## Lifecycle Integration

OpenHands documents planning, development, testing, review, and deployment preparation, plus SDK-based CI/CD integration for reviews, documentation, and operational analysis. The guide's example prompts and configuration snippets illustrate workflows; they are not a verified installation recipe for every current product surface ([OpenHands in Your SDLC](https://docs.openhands.dev/openhands/usage/essential-guidelines/sdlc-integration)).

The current platform page describes issue triage, CI-failure fixes, QA, incident investigation, documentation upkeep, and scheduled engineering chores, triggered through engineering systems and integrations. These are vendor-documented workflow capabilities, not independent outcome measurements ([OpenHands platform](https://www.openhands.dev/)).

## Deployment, Licensing, and Governance

The SDK documentation describes the SDK as MIT-licensed and model-agnostic, but the ecosystem introduction explicitly says each public repository has its own license. Do not extend one component's license to commercial Enterprise features or every repository ([SDK documentation](https://docs.openhands.dev/sdk), [component and repository map](https://docs.openhands.dev/overview/introduction)).

| Area | Recommendation | Basis |
|---|---|---|
| Runtime choice | Verify backend placement, credentials, model calls, and network policy separately from the browser client. | Wiki guidance based on distinct client, server, sandbox, and managed-service components ([introduction](https://docs.openhands.dev/overview/introduction)). |
| Human review | Define approval requirements, action scope, and audit logging before automating changes. | Governance guidance in the [SDLC integration guide](https://docs.openhands.dev/openhands/usage/essential-guidelines/sdlc-integration). |
| Agent configuration | Keep repository instructions current and validate representative tasks. | Repository guidance in the [SDLC integration guide](https://docs.openhands.dev/openhands/usage/essential-guidelines/sdlc-integration). |
| Surface selection | Prefer the current component map over older monolithic architecture assumptions. | The docs mark the former Local GUI deprecated and the CLI feature-complete and maintained primarily for stability ([introduction](https://docs.openhands.dev/overview/introduction)). |

Self-hosting a component does not prove that all data stays local: check the chosen model provider, integrations, execution backend, and telemetry. This is evaluation guidance, not an independently verified data-residency guarantee.

## See Also

- [Warp Factories](warp-factories.md): compare control/execution boundaries and reviewed delivery loops.
- [Building Your Own Software Factory](building-your-own-software-factory.md): related operating-model workshop.
- [Software AI Factory](README.md)
- [Factory AI](factory-ai.md)
- [Devin](devin.md)
- [Anthropic AI-Native SDLC](ai-native-sdlc.md)
- [AI Coding Agents](../AICodingAgents/ai-coding-agents.md)
- [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md)
- [Production Deployment](../ProductionBestPractices/deployment.md)

## References

- [Warp Factories overview](https://docs.warp.dev/factories/): related platform reference, not evidence of OpenHands features.
- [Building your own software factory](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz): related Cursor workshop, not evidence of this platform's product features.
- [OpenHands introduction](https://docs.openhands.dev/overview/introduction): component map, deployment surfaces, legacy status, and licensing boundary.
- [Software Agent SDK](https://docs.openhands.dev/sdk): coding-agent APIs, tools, model choice, and SDK licensing.
- [OpenHands in Your SDLC](https://docs.openhands.dev/openhands/usage/essential-guidelines/sdlc-integration): lifecycle integration and governance examples.
- [OpenHands platform](https://www.openhands.dev/): event-driven software lifecycle and automation use cases.
