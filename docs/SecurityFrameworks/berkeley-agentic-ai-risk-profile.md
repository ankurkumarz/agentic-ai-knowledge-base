---
type: Playbook
title: UC Berkeley Agentic AI Risk-Management Standards Profile
description: The UC Berkeley Agentic AI Profile extends general-purpose AI risk management with system-level guidance for autonomous single-agent and multi-agent systems.
tags: [security, governance, risk-management, nist-ai-rmf, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---

# UC Berkeley Agentic AI Risk-Management Standards Profile

## Overview

The UC Berkeley Agentic AI Profile extends general-purpose AI risk management with system-level guidance for autonomous single-agent and multi-agent systems. Published by the AI Security Initiative at UC Berkeley's Center for Long-Term Cybersecurity (CLTC), Version 1.0 (February 2026) complements the NIST AI Risk Management Framework and extends Berkeley's General-Purpose AI (GPAI) Risk-Management Standards Profile. It is guidance, not a separate certification or a substitute for the underlying GPAI Profile.

Authors: Nada Madkour, Jessica Newman, Deepika Raman, Krystal Jackson, Evan R. Murphy, and Charlotte Yuan. This synthesis uses the supplied 67-page PDF, Agentic-AI-Risk-Management-Standards-Profile-1.pdf. Page references below use the document's printed page numbers.

## From Model Risk to System Risk

The central shift is to assess the deployed system, not just its foundation model. Autonomy, delegated authority, tools, memory, environment access, and interactions can introduce risks absent from isolated model testing. Assess agents individually and collectively: safe-looking components do not establish that a multi-agent workflow is safe (pp. 6–15).

Governance should scale with degrees of agency, rather than treat autonomy as binary. Map 5.1 considers autonomy, authority, causal impact, environment type and complexity, and agent efficacy. Its illustrative L0–L5 autonomy scale is adapted from cited research; the Profile also acknowledges that terminology and autonomy taxonomies lack consensus (pp. 13–15, 36–38).

## Four Risk-Management Functions

| Function | Agentic emphasis | Source sections |
|---|---|---|
| Govern | Human accountability; bounded delegated authority; agent-specific policies; supply-chain provenance; change-triggered review | Govern 1, 2, 4, 5, 6; pp. 16–23 |
| Map | Intended and prohibited uses; harm pathways; permissions and integrations; cumulative impact; risk tolerances; human oversight | Map 1, 2, 3, 5; pp. 24–38 |
| Measure | Capability screening; deeper adversarial testing; system-level evaluation; explicit measurement gaps; continuous risk tracking | Measure 1, 2, 3; pp. 39–44 |
| Manage | Deployment decisions; prioritized mitigations; containment; emergency intervention; recovery; post-deployment monitoring | Manage 1, 2, 4; pp. 45–52 |

## High-Priority Subcategories

The Profile carries forward 13 high-priority subcategories from the GPAI Profile. The following are concise paraphrases, not replacements for the source text (pp. 12–13).

| Subcategory | Priority |
|---|---|
| Govern 2.1 | Document roles, responsibilities, and communication lines |
| Govern 4.2 | Document and communicate risks and impacts |
| Govern 5.1 | Collect, prioritize, and integrate external feedback |
| Map 1.1 | Establish intended uses, deployment context, impacts, assumptions, and evaluation metrics |
| Map 1.5 | Document organizational risk tolerances |
| Map 5.1 | Assess likelihood and magnitude of beneficial and harmful impacts |
| Measure 1.1 | Prioritize risk measurement and document what cannot or will not be measured |
| Measure 3.2 | Track risks even where measurement techniques or metrics are immature |
| Manage 1.1 | Decide whether development or deployment should proceed |
| Manage 1.3 | Document mitigation, transfer, avoidance, or acceptance of prioritized risks |
| Manage 2.3 | Respond to and recover from newly identified risks |
| Manage 2.4 | Assign and implement authority to supersede, disengage, or deactivate unsafe systems |
| Manage 4.1 | Maintain monitoring, feedback, override, incident response, recovery, and change management |

## Risk Domains

Map 1.1 and Manage 1.3 organize agentic risks and responses across eight domains (pp. 7, 24–31, 45–49):

- Discrimination and toxicity: repeated actions and feedback loops can amplify disparities.
- Privacy and security: persistent memory, third-party integrations, sensitive logs, and cascading compromises expand exposure.
- Misinformation: erroneous outputs can propagate between agents and downstream systems.
- Malicious actors and misuse: autonomous orchestration can lower barriers to harmful workflows.
- Human–computer interaction: reduced oversight, anthropomorphic behavior, and overreliance complicate effective control.
- Loss of control: action velocity and oversight subversion can outpace intervention.
- Socioeconomic and environmental harms: unequal access, concentrated authority, disruption, and runaway resource use can produce broader impacts.
- AI system safety, failures, and limitations: misalignment, reward hacking, collusion, self-modification, replication, and long-horizon goal pursuit require tailored assessment.

These are risk categories and research concerns, not claims that every deployed agent exhibits every capability.

## Engineering and Operational Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Delegated authority | Agents can perform multi-step actions beyond intended scope | Document authorized actions, forbidden uses, human decision rights, and escalation triggers; enforce least privilege (Govern 2.1; Map 1.3, 3.5) |
| Governance modification | AI-readable policies are not equivalent to AI-writable policies | Make governance interpretable and verifiable; subject any agent write access to robust independent human oversight (Govern 1.4) |
| Risk thresholds | Many individually modest actions can create unacceptable cumulative harm | Set conservative context-specific risk tiers below intolerable thresholds; account for uncertainty and interacting systems (Map 1.5) |
| Oversight triggers | Periodic manual review may miss fast or long-running activity | Use quantitative triggers such as API-call counts and unsupervised duration, plus qualitative triggers such as out-of-scope access attempts (Map 3.5) |
| Evaluation blind spots | Benchmarks alone do not establish safe deployment | Use capability screening to trigger deeper red teaming; evaluate privilege escalation, memory manipulation, orchestration, and collusion; document residual uncertainty (Measure 1.1) |
| Correlated evaluators | An AI evaluator can share flaws with the evaluated model | Verify automated red-teaming findings and combine deterministic checks with model-based defenses (Measure 1.1) |
| Supervisory-agent collusion | Monitoring agents may cooperate with monitored agents | The Profile advises against supervisory AI in high-stakes contexts until collusion is better understood and substantially mitigated (Manage 1.3) |
| Multi-agent compromise | A compromised agent can affect connected peers and tools | Authenticate inter-agent communication; use agent identity controls, continuous monitoring, and containment (Manage 1.3) |
| Logging versus privacy | Comprehensive traces can expose sensitive information or enable surveillance | Log only necessary information; encrypt logs; establish need- and regulation-based retention; filter identifying information (Map 1.1; Manage 1.3) |
| Shutdown and recovery | Agents may have dependencies or capabilities that undermine simple shutdown | Support automatic and manual intervention; protect shutdown mechanisms; isolate integrations; investigate before reactivation (Govern 1.7; Manage 2.4) |
| Business continuity | Agent shutdown may interrupt mission-critical workflows | Maintain independent critical data, deterministic non-AI fallback systems, and tested recovery procedures (Govern 1.7) |
| Changing risk | New tools, privileges, autonomy, context, or supply-chain changes invalidate assumptions | Trigger reassessment after significant changes, alongside continuous monitoring and periodic review (Govern 1.5) |
| Constrained resources | Effective oversight may exceed available budget or staffing | If adequate controls or reasonable alternatives are unavailable, reduce autonomy, authority, or access to a manageable scope (Map 5.1) |

## Implementation Artifacts

The following artifact set is a repository synthesis of the guidance, not a Berkeley-prescribed template or a compliance certification:

1. System inventory and agent card: purpose, models, memory, integrations, permissions, limitations, and evaluation coverage.
2. Authority and oversight matrix: accountable humans, permitted actions, approval points, and escalation conditions.
3. Risk register: harm pathways, affected stakeholders, likelihood, severity, uncertainty, thresholds, treatments, and residual risk.
4. Evaluation record: screening results, adversarial scenarios, independent review, measurement gaps, and deployment decision.
5. Runtime oversight plan: agent identifiers, action and tool traces, privacy controls, alerts, feedback, incident and near-miss reporting.
6. Intervention and continuity runbook: authority reduction, isolation, shutdown, dependency handling, fallback testing, recovery, and reactivation review.

## Limitations

The Profile is a living framework, not a static checklist. Agent definitions, alignment research, emergent-behavior evaluation, and long-term harm measurement remain incomplete. Passing evaluations cannot eliminate uncertainty; the authors emphasize defense-in-depth, containment, conservative assumptions, and continuous reassessment. The guidance covers generalist and specialist agents, open and closed models, and single- and multi-agent systems, but does not provide sector-specific implementation guidance (pp. 8, 11–15).

## See Also

- [NIST AI Risk Management Framework](nist-ai-rmf.md)
- [Agentic AI Red Teaming Guide (CSA)](agentic-ai-red-teaming-guide.md)
- [Agent Sandboxing](agent-sandboxing.md)
- [Agent Identity](agent-identity.md)
- [Governance Best Practices](../AIGovernance/governance-best-practices.md)
- [Production Agent Security](../ProductionBestPractices/security.md)
- [Production Testing and Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Production Observability](../ProductionBestPractices/observability.md)
- [Production State and Memory](../ProductionBestPractices/state-memory.md)

## References

- Madkour, N., Newman, J., Raman, D., Jackson, K., Murphy, E. R., and Yuan, C. (February 2026). [Agentic AI Risk-Management Standards Profile](https://cltc.berkeley.edu/publication/agentic-ai-risk-management-standards-profile), Version 1.0. AI Security Initiative, Center for Long-Term Cybersecurity, UC Berkeley. Primary source; synthesis based on the supplied PDF.
- [General-Purpose AI Risk-Management Standards Profile, Version 1.2](https://cltc.berkeley.edu/publication/ai-risk-management-standards-profile-v1.2/). Foundational companion identified by the Agentic AI Profile; not separately ingested here.
