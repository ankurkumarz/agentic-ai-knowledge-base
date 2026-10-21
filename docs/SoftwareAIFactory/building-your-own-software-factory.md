---
type: Playbook
title: Building Your Own Software Factory
description: Eric Zakariasson's Cursor workshop explains how runnable environments, verification, isolated agents, and feedback loops support delegated software delivery.
tags: [software-ai-factory, cursor, harness-engineering, sdlc, agentic-ai]
timestamp: 2026-10-20T00:00:00Z
---

# Building Your Own Software Factory

## Overview

Eric Zakariasson's Cursor workshop explains how runnable environments, verification, isolated agents, and feedback loops support delegated software delivery. The source is the AI Engineer video [Building your own software factory](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), supported by its [official talk page](https://ai.engineer/talks/rnDm57Py54A-building-your-own-software-factory); this ingest uses the full timestamped transcript, including the Q&A, rather than the description alone.

The speaker explicitly says that Cursor is not yet a fully autonomous software factory, although some parts operate with substantial autonomy. Treat the demos and internal practices as an experience report, not a general guarantee of throughput, product availability, or safe autonomous production changes ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), opening 00:16–01:05).

## Foundation: Runnable, Accessible, Verifiable

The workshop's readiness checklist is whether the system is runnable, whether agents can access the context they need, and whether they can verify their own work. It groups preparation into codebase primitives, guardrails, and enablers rather than treating additional agents as the starting point ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 04:59–10:42).

| Foundation | Guidance from the workshop | Evidence to check |
|---|---|---|
| Discoverable structure | Co-locate related code and provide patterns the agent can follow. | Can a new run find the relevant module and a comparable implementation? ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Runnable environment | Expose reliable startup and test commands; hide complex service startup behind a dependable interface. | A fresh run can start the application and dependencies without human repair. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Accessible context | Connect relevant repository instructions, specs, issues, logs, and external tools. | The run can retrieve the actual task context rather than receiving copied fragments. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Guardrails | Restrict sensitive changes with hooks and checks; use rules to address observed gaps. | Protected areas and failure routes are explicit. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Enablers | Provide reusable skills and tool access, including feature-flag workflows. | Required capabilities are available within the approved boundary. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Verifiable outcomes | Provide unit, integration, and end-to-end checks; use browser interaction where necessary. | Behavior is demonstrated, not merely described in the final response. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |

The table synthesizes the speaker's checklist and startup example; the evidence questions are editorial operationalizations, not reported measurements ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 04:59–10:42 and 50:42–52:20).

## Running and Scaling the Factory

### Plan Synchronously, Execute Asynchronously

The speaker recommends front-loading intent, context, and a plan before dispatching longer-running work. Scope tasks before multiplying agents, avoid parallel tasks that change the same code, and preserve human understanding of data flows and critical systems ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 16:52–20:33 and 58:13–1:02:24).

The human role shifts toward specifying, coordinating, reviewing evidence, and improving the environment. More agents also create more review and coordination work; the speaker's personal concurrency examples are not a recommended capacity target or a benchmark ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 16:52–20:33 and 1:00:24–1:02:24).

### A Worktree Is Not Full Runtime Isolation

A separate checkout does not isolate databases, caches, user state, or shared services. The speaker prefers separate VMs for independent long-running work, while acknowledging the additional setup effort and expense; the operational requirement is isolated state, not a universal requirement to use one specific virtualization product ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 20:33–22:07).

In the Q&A, the speaker demonstrates a worker approach for running the harness on infrastructure the team controls, while noting that frontier-model calls still occur and computer-use parity is not universally available at the time of the talk. These are talk-time product observations, not a current installation guide or proof of fully local inference/data residency ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 1:11:20–1:18:07).

### Evidence Before Claims of Completion

The workshop demonstrates agents running the application and returning recordings or screenshots that a person can inspect. It separately distinguishes functional behavior checks from visual acceptance: a working login does not establish that every screen looks correct, and a recording does not replace architecture or security review ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 14:35–16:52, 33:39–35:53, and 46:01–50:42).

## Feedback Loops and Automations

The speaker describes the following internal or personal examples, not an audited universal operating model. Each uses retained context or an external signal to reduce repeated manual handoffs ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 22:20–31:05 and 1:08:19–1:11:09).

| Loop | Input | Result described |
|---|---|---|
| Daily review | Slack and GitHub activity. | Scheduled summary of recent work. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Review-learning loop | Human comments on merged PRs. | Preserve high-signal corrections for later runs. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Risk-aware ownership | PR diff, assessed risk, and prior authorship. | Delegate some low-risk approvals; bring relevant people into higher-risk review. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Transcript-to-rule loop | Repeated corrections in agent conversations. | Extract memories or rules so the correction need not be repeated. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Feature-flag cleanup | System signal that a flag has been fully rolled out. | Create a Linear issue, trigger a cloud agent, and return a change for review. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Issue triage | Slack messages and issue events. | Detect duplicates, investigate, or start a bounded fix. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |

The speaker warns that triggering a cloud agent for every issue can be expensive and does not recommend it indiscriminately. He also distinguishes extracting rules from transcripts from learning by changing model weights; the plugin example does not demonstrate fine-tuning ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 42:40–44:08 and 1:08:19–1:11:09).

## Governance and Human Judgment

| Area | Workshop guidance | Boundary |
|---|---|---|
| Important decisions | Humans retain judgment over security, authentication, databases, payments, and other critical choices. | Passing mechanical checks does not settle architecture quality. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Critical code | Use carefully designed tests and targeted invariant checks; preserve human review of critical areas. | The talk's security-sentinel examples are internal practices, not a published turnkey control package. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Durable rules | Let rules emerge from repeated model-versus-intent gaps; review the factory's shared configuration as a team. | Do not install every generic rule or turn one-off preferences into permanent policy. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Prototype handoff | Hand over intended interactions and an understandable artifact. | Engineers need not preserve a prototype's accidental database or framework decisions. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Factory ownership | Keep workflow specifications and rules in the repository and agree as a team on what belongs there. | Product direction and cross-team coordination remain human responsibilities. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |

These points come from the main talk and Q&A, including the explicit admission that architecture quality and team agreement remain difficult problems ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 31:05–40:58, 44:08–45:46, 53:05–58:13, and 1:02:37–1:04:41).

### Difference from the Anthropic Playbook

The Cursor talk describes an agentic code-owner workflow that may approve low-risk PRs and route higher-risk work to relevant people. The Anthropic playbook instead states that the writing agent cannot approve its own work and that branch protection retains a human code-owner approval; these are different approval models, not interchangeable evidence for one universal gate ([Cursor video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), 27:38–29:28; [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), PR-review play).

Wiki recommendation: choose approval policy explicitly according to risk and applicable controls, keep authorship and approval identities distinguishable, and do not infer permission to auto-merge from the talk's internal example. This is governance synthesis rather than a claim about either product's default configuration.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| State collisions | Independent branches can still touch one database or cache. | Isolate runtime state, not just files. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Unreviewable output | A final message claiming success is weak evidence. | Return test output and behavior evidence that a reviewer can inspect. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Repeated corrections | Context disappears between sessions. | Promote recurring, reviewed lessons into durable instructions. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Excess rules | Generic rules can obscure actual intent. | Introduce rules for observed gaps; keep task-specific plans ephemeral. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Activity without progress | Long sessions may repeat failed tool calls or never change useful output. | Monitor duration, useful changes, and loops; investigate stuck runs. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |
| Prototype migration | Accidental technical choices can become expensive constraints. | Preserve intended interaction, and let engineers select production architecture. ([workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz)) |

These practices synthesize the workshop's examples and closing discussion; no numerical performance gain, savings estimate, or guaranteed success rate is claimed ([video](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz), especially 20:33–22:07, 29:28–31:05, 44:08–45:46, 53:05–58:13, and 1:21:00–1:23:19).

## See Also

- [Warp Factories](warp-factories.md): documented factory stages, boundaries, and measured improvement.
- [OpenAI's Agentic Software Factory](openai-software-factory.md): reported CI follow-through, risk-aware reviews, and production feedback.
- [Software AI Factory](README.md)
- [Anthropic AI-Native SDLC](ai-native-sdlc.md)
- [Factory AI](factory-ai.md)
- [Devin](devin.md)
- [OpenHands](openhands.md)
- [AI Coding Agents](../AICodingAgents/ai-coding-agents.md)
- [Harness Engineering](../AgentHarness/harness-engineering.md)
- [Loop Engineering](../AgentHarness/loop-engineering.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md)
- [Agent Observability](../Observability/Readme.md)
- [Production Deployment](../ProductionBestPractices/deployment.md)
- [Testing and Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Agent Security](../ProductionBestPractices/security.md)
- [State and Memory](../ProductionBestPractices/state-memory.md)
- [Production Context Engineering](../ProductionBestPractices/context-engineering.md)
- [Production Observability](../ProductionBestPractices/observability.md)
- [Cost Management](../ProductionBestPractices/cost-management.md)

## References

- [Warp Factories overview](https://docs.warp.dev/factories/): related product documentation, separate from the Cursor workshop.
- [Inside OpenAI's agentic software factory](https://newsletter.pragmaticengineer.com/p/openai-software-factory): related case study with separate release and mitigation approval boundaries.
- [Building your own software factory: Eric Zakariasson, Cursor](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz): user-provided canonical video, ingested from the full timestamped transcript including Q&A.
- [Official AI Engineer talk page](https://ai.engineer/talks/rnDm57Py54A-building-your-own-software-factory): publisher-hosted article, chapter guide, and corrected-transcript resource.
- [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): reference for the explicitly contrasted PR-approval model.
