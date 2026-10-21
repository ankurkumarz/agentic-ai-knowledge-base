---
type: Reference
title: Software AI Factory
description: Software AI Factory organizes lifecycle playbooks and platforms for repeatable, governed agent-driven software delivery.
tags: [software-ai-factory, sdlc, software-engineering, agentic-ai]
timestamp: 2026-10-20T00:00:00Z
---

# Software AI Factory

## Overview

Software AI Factory organizes lifecycle playbooks and platforms for repeatable, governed agent-driven software delivery. This is a wiki classification, not a certification or a claim that every listed product implements the same architecture; it groups the artifact-driven lifecycle described by [Anthropic](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) with the execution platforms documented by [Factory](https://docs.factory.ai/cli/getting-started/overview), [Cognition](https://docs.devin.ai/get-started/devin-intro), and [OpenHands](https://docs.openhands.dev/overview/introduction).

The organizing distinction is between assistance on an individual coding task and an operating model that connects work intake, context, execution, verification, review, and feedback. Anthropic describes committed artifacts linking six lifecycle stages, while OpenHands describes a signal-to-plan-to-execute-to-validate-to-ship-to-monitor workflow; these are related approaches, not evidence of identical implementation ([Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), [OpenHands platform](https://www.openhands.dev/)).

## Playbooks and Platforms

| Entry | Documented scope | Role in this category |
|---|---|---|
| [Anthropic AI-Native SDLC](ai-native-sdlc.md) | Plan, design, build, test, deploy, maintain; versioned artifacts, skills, hooks, and human gates ([playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)). | Process and governance reference, not a standalone software product. |
| [Building Your Own Software Factory](building-your-own-software-factory.md) | Cursor workshop on runnable environments, isolated agents, verification artifacts, and feedback loops ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)). | Practical operating-model experience report, including limitations and Q&A. |
| [OpenAI's Agentic Software Factory](openai-software-factory.md) | Interview-based account of Codex-driven CI/review, supervised rollout, Perf Factory, and Sevbot ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). | Internal-practice case study; partial-access ingest, not a public product specification. |
| [Factory AI](factory-ai.md) | Droids across terminal/editor workflows; Missions, Custom Droids, skills, MCP, hooks, plugins, and headless Exec Mode ([Droid CLI documentation](https://docs.factory.ai/cli/getting-started/overview)). | Packaged agent-native engineering platform. |
| [Warp Factories](warp-factories.md) | Foreman-led cloud-agent teams, source-preserving work items, definitions as code, reviewed PR handoff, and measured improvement ([documentation](https://docs.warp.dev/factories/)). | Standing factory orchestration with separately configured execution, inference, and repository controls. |
| [Devin](devin.md) | Delegated tickets, features, migrations, tests, reviews, and documentation using an observable shell, IDE, and browser ([Devin introduction](https://docs.devin.ai/get-started/devin-intro)). | Delegated engineering execution; cloud and local CLI have different capabilities ([CLI documentation](https://docs.devin.ai/cli)). |
| [OpenHands](openhands.md) | Agent Canvas, Software Agent SDK, Agent Server, automation lifecycle, and managed or enterprise deployment options ([component map](https://docs.openhands.dev/overview/introduction)). | Composable execution and automation foundation. |

## Working Model

The following is an editorial synthesis for evaluating a software factory, not a description of a single vendor's internals. It draws on [Anthropic's artifact chain](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), [Factory's CLI execution model](https://docs.factory.ai/cli/getting-started/overview), and [OpenHands' SDLC integration guide](https://docs.openhands.dev/openhands/usage/essential-guidelines/sdlc-integration).

| Layer | Evaluation question | Evidence to request |
|---|---|---|
| Intake and intent | Can an issue, conversation, incident, or schedule become scoped work? | Original request, owner, acceptance criteria, and source record. |
| Context and planning | Can the agent access the right repository instructions, policies, and system context? | Approved plan and the versions of instructions used. |
| Execution | Where does work run, with which tools and credentials? | Workspace identity, permitted actions, execution logs, and isolation boundary. |
| Verification | Does the proposed change meet observable acceptance criteria? | Test/build output, behavior checks, and regression results. |
| Review and release | Which actions require an independent reviewer or release approver? | PR findings, required checks, approval record, and rollback readiness. |
| Feedback | Do incidents and recurring failures improve the next iteration? | Follow-up intent, incident regression cases, and tracked outcomes. |

## Selection and Adoption Guidance

These recommendations are wiki synthesis rather than vendor performance rankings. Start with one bounded workflow, establish acceptance checks, and add autonomy only after the workflow produces reviewable evidence; this follows the emphasis on feedback and approval gates in [Anthropic's playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) and scoped, verifiable work in [Devin's documentation](https://docs.devin.ai/get-started/devin-intro).

| Area | Recommendation | Tradeoff to assess |
|---|---|---|
| Buy versus compose | Evaluate Factory or Devin for packaged execution, and OpenHands for a composable foundation. | Product fit versus the engineering effort needed to integrate and operate components. |
| Deployment boundary | Validate the exact product surface, runtime, network access, and data path. | A local interface or a self-hosted component does not by itself establish end-to-end data residency. |
| Permissions | Keep production release approval separate from agent authorship. | More autonomy can reduce handoffs while increasing the importance of deterministic controls. |
| Validation | Compare on your own representative tasks and regression suite. | Marketing claims and unrelated benchmark runs do not establish local success rates. |

## Related Coverage

This category is the home for lifecycle operating models and software-factory platforms. Individual editor and terminal-agent comparisons remain in [AI Coding Agents](../AICodingAgents/ai-coding-agents.md), while operational guidance for running agents remains in [AgentOps](../AgentOps/README.md); the categories are linked rather than duplicated.

Approval models differ between the playbooks: the Cursor workshop describes delegated approval of some low-risk PRs, whereas Anthropic retains a human code-owner approval gate. Select the applicable model deliberately rather than treating either as a universal product default ([Cursor video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)).

## See Also

- [Warp Factories](warp-factories.md)
- [OpenAI's Agentic Software Factory](openai-software-factory.md)
- [Building Your Own Software Factory](building-your-own-software-factory.md)
- [Anthropic AI-Native SDLC](ai-native-sdlc.md)
- [Factory AI](factory-ai.md)
- [Devin](devin.md)
- [OpenHands](openhands.md)
- [AI Coding Agents](../AICodingAgents/ai-coding-agents.md)
- [Claude Code](../AICodingAgents/claude-code.md)
- [AgentOps](../AgentOps/README.md)
- [Loop Engineering](../AgentHarness/loop-engineering.md)
- [Production Deployment](../ProductionBestPractices/deployment.md)
- [Testing and Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Agent Security](../ProductionBestPractices/security.md)
- [AWS AI-DLC Workflows](../Standards/aidlc.md)
- [OpenSpec](../Standards/openspec.md)

## References

- [Warp Factories overview](https://docs.warp.dev/factories/): standing multi-agent delivery platform and factory operating model.
- [Inside OpenAI's agentic software factory](https://newsletter.pragmaticengineer.com/p/openai-software-factory): accessible reporting through the start of section 4; subscriber-only remainder not ingested.
- [Building your own software factory](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz): Eric Zakariasson's Cursor workshop, full transcript including Q&A.
- [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): Anthropic's lifecycle and governance playbook.
- [Factory Droid CLI](https://docs.factory.ai/cli/getting-started/overview): execution, customization, and automation surfaces.
- [Introducing Devin](https://docs.devin.ai/get-started/devin-intro): delegated engineering workflows and verification guidance.
- [Devin CLI](https://docs.devin.ai/cli): distinction between local CLI and cloud Devin.
- [OpenHands introduction](https://docs.openhands.dev/overview/introduction): component responsibilities and deployment options.
- [OpenHands platform](https://www.openhands.dev/): event-driven lifecycle and control-plane positioning.
- [OpenHands in Your SDLC](https://docs.openhands.dev/openhands/usage/essential-guidelines/sdlc-integration): integration and governance examples.
