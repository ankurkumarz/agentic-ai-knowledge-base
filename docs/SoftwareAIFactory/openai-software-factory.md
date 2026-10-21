---
type: Reference
title: OpenAI's Agentic Software Factory
description: OpenAI's internal Codex-based software factory is described in Gergely Orosz's September 2026 reporting on engineering practices at the company.
tags: [software-ai-factory, openai, codex, sdlc, agentic-ai]
timestamp: 2026-10-20T00:00:00Z
---

# OpenAI's Agentic Software Factory

## Overview

OpenAI's internal Codex-based software factory is described in Gergely Orosz's September 2026 reporting on engineering practices at the company. The case study connects human-defined outcomes, repository and organizational context, implementation, CI repair, specialist reviews, supervised rollout, performance feedback, and incident assistance ([The Pragmatic Engineer, September 15, 2026](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).

This is an interview-based account of internal practice, not OpenAI product documentation, an independently audited benchmark, or a publicly installable architecture. The author explicitly notes that internal Codex is more extensively connected to company systems than the external product ([article](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).

## Access and Provenance

This ingest covers the accessible introduction, sections 1–3, and the opening of section 4. Both cleaned text and the rendered HTML show a paid-subscriber gate at that point; the rest of sections 4–7 was not available and is not represented as read.

The opening table of contents names additional topics, including infrastructure scaling, API reliability, and changing engineering roles, but a topic listing is not evidence for the unavailable details. No claims about those later sections are inferred from their headings ([article and subscriber boundary](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).

## Reported Factory Pipeline

| Stage | Practice reported in the accessible article | Boundary or implication |
|---|---|---|
| Intent and context | A person defines the outcome; Codex accesses source-adjacent documentation, repositories, collaboration systems, internal telemetry/data, and skills. | Internal integrations are central to the example, not evidence that the public product has the same access ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |
| Implementation and CI | The agent changes code, builds/tests it, opens a PR, and continues fixing CI failures until checks pass. | Persistent follow-through extends beyond generating the initial diff ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |
| Performance verification | A performance harness can route problematic PRs to a Synthetics A/B framework. | Behavioral correctness checks and performance checks are separate concerns ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |
| Review and risk routing | Multiple domain-configured reviewers assess changes; higher-risk work may receive more reviews or require human review, while opted-in areas may auto-approve low-risk PRs. | This is a reported local approval policy, not a universal Codex default ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |
| Supervised rollout | After human production approval, a change-specific agent follows the rollout or feature flag and may construct a dashboard for its signals. | Release authorization remains distinct from PR approval; fully autonomous per-change SRE operation is a longer-term goal ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |
| Performance feedback | Perf Factory filters and deduplicates production signals, investigates latency regressions, and proposes fixes. | The feedback loop continues after deployment; a proposed fix is not evidence of unconstrained production changes ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |
| Incident assistance | Sevbot gathers incident context, suggests mitigations, and answers questions in the incident channel; an engineer can direct a specific mitigation. | Autonomous mitigation is described as an aspiration, not the current default; on-call responsibility remains ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)). |

## What Makes the Example Distinctive

- **Context-rich specialist review**: The author's explanation is that reviewers need domain-relevant code, documentation, and a focused context window. Merely labeling a generic agent a specialist is not established as equivalent to expert review ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).
- **Per-change observation**: Agents create or select signals at the granularity of an individual rollout, rather than relying only on a service's standing dashboards. This is reported practice, not proof that generated monitoring is complete or trustworthy without validation ([article, section 3](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).
- **Downstream bottlenecks**: Interviewees report roughly tenfold load growth on some build/test/deploy systems over about six months. That is an attributed infrastructure-load observation, not a tenfold measured productivity improvement ([article, section 2](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).
- **Native release constraints**: Faster code production still encounters mobile-store review and distribution delays. The reporting discusses feature flags and release design, not bypassing store policies ([article, section 2](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).
- **Adoption is organizational**: Role-specific plugins, longer-running goals, team learning, and embedded domain experts are described as adoption enablers. OpenAI's unusually broad internal access and token budgets limit straightforward extrapolation to other organizations ([article, section 1](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).

## Governance Across the Factory Sources

The reported OpenAI workflow permits low-risk PR auto-approval only in areas that opt in, but still describes human authorization before production rollout and human-directed incident mitigation. Keep these three decisions separate: accepting a code change, authorizing release, and authorizing an incident action ([Pragmatic Engineer case study](https://newsletter.pragmaticengineer.com/p/openai-software-factory)).

The [Cursor workshop](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz) also describes risk-aware low-risk approval, while [Anthropic's playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) retains human code-owner approval. These source-specific models should be compared explicitly rather than combined into a claim that a software factory removes human authorization.

## Adoption Questions

These are wiki recommendations derived from the case study, not controls that the reporting proves OpenAI has implemented in a particular way.

| Area | Evaluation question |
|---|---|
| Context | Which systems and documentation must a run access, and under whose identity? |
| Review | What specialized evidence does each reviewer receive, and how is its usefulness assessed? |
| Capacity | Can source control, CI, test infrastructure, and release processes absorb more concurrent changes? |
| Rollout | Who authorizes production changes, and which signals and stop conditions govern follow-through? |
| Feedback | How does a regression become a scoped, reviewable repair rather than an uncontrolled action loop? |
| Incidents | Which actions remain recommendation-only, which require an operator, and who retains accountability? |

## See Also

- [Software AI Factory](README.md)
- [Anthropic AI-Native SDLC](ai-native-sdlc.md)
- [Building Your Own Software Factory](building-your-own-software-factory.md)
- [AI Coding Agents](../AICodingAgents/ai-coding-agents.md)
- [Harness Engineering](../AgentHarness/harness-engineering.md)
- [Loop Engineering](../AgentHarness/loop-engineering.md)
- [OpenAI Vendor Hub](../AllThingsOpenAI/README.md)
- [Production Deployment](../ProductionBestPractices/deployment.md)
- [Testing and Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Production Observability](../ProductionBestPractices/observability.md)
- [Agent Security](../ProductionBestPractices/security.md)
- [Production Context Engineering](../ProductionBestPractices/context-engineering.md)

## References

- [Inside OpenAI's agentic software factory](https://newsletter.pragmaticengineer.com/p/openai-software-factory): Gergely Orosz, The Pragmatic Engineer, September 15, 2026. Canonical user-provided source; partial-access ingest through the opening of section 4.
- [Building your own software factory](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz): Cursor workshop, used only to compare governance approaches.
- [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): Anthropic's distinct human code-owner review model.
