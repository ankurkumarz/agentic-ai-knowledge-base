# NIST AI Risk Management Framework (AI RMF)

## Overview

The [NIST AI Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1), published in January 2023, provides a voluntary, flexible, and structured approach to managing risks associated with artificial intelligence systems throughout their full lifecycle. Developed through broad stakeholder engagement, it is designed to be technology-agnostic and applicable across industries, sectors, and organizational sizes. For agentic AI systems — which take autonomous real-world actions — the framework's emphasis on governance, accountability, and continuous measurement is especially relevant.

![NIST AI Risk Management Framework overview](../assets/images/security-nist-ai-rmf-overview.png)

## Core Structure

The framework is organized around two primary sections: the **AI RMF Core** (four functions and their subcategories) and the **AI RMF Profiles** (customizable roadmaps tailored to an organization's risk tolerance and context).

### Four Core Functions

![NIST AI RMF circular process diagram](../assets/images/security-nist-ai-rmf-circular-diagram.png)

| Function | Purpose | Key Activities |
|---|---|---|
| **GOVERN** | Establish organizational policies, culture, and accountability for AI risk | Define roles and responsibilities; establish risk tolerance; create AI governance policies; build risk-aware culture |
| **MAP** | Identify and categorize AI risks in context | Characterize the AI system and its environment; identify stakeholders; catalog potential harms (technical, societal, individual) |
| **MEASURE** | Analyze and assess identified risks | Quantify risks using metrics and tools; conduct bias/fairness evaluations; track performance against benchmarks; apply red-teaming |
| **MANAGE** | Prioritize and address AI risks | Implement risk mitigations; allocate resources; respond to incidents; document and communicate residual risk |

These functions are not strictly sequential — GOVERN is foundational and continuous, while MAP→MEASURE→MANAGE form an iterative cycle applied throughout the AI lifecycle.

![NIST AI RMF framework components](../assets/images/security-nist-ai-rmf-framework-diagram.png)

### Trustworthy AI Characteristics

NIST defines trustworthy AI across seven properties. Risk management should address each:

| Property | Description |
|---|---|
| **Valid and Reliable** | The system performs its intended function consistently and accurately |
| **Safe** | Does not pose unreasonable risk of harm to people or the environment |
| **Secure and Resilient** | Resists adversarial attacks; recovers from disruptions |
| **Explainable and Interpretable** | Decisions and outputs can be understood by relevant stakeholders |
| **Privacy-Enhanced** | Protects individual privacy throughout the lifecycle |
| **Fair and Unbiased** | Does not produce unjustified differential outcomes across groups |
| **Accountable and Transparent** | Clear human responsibility; disclosed capabilities and limitations |

## Application to Agentic AI Systems

Agentic AI introduces compounding risks beyond standard ML systems. The AI RMF maps to agentic-specific concerns as follows:

| AI RMF Function | Agentic-Specific Risk | Recommended Action |
|---|---|---|
| GOVERN | Unclear human oversight boundaries for autonomous agents | Define explicit escalation policies; assign accountability per agent role in multi-agent systems |
| MAP | Agent can take novel action paths not anticipated at design time | Map all tools and their real-world impact (reversibility, scope, blast radius) |
| MEASURE | Emergent multi-agent behavior is hard to evaluate in isolation | Evaluate full agent chains end-to-end; include adversarial red-team inputs (prompt injection, goal hijacking) |
| MANAGE | Autonomous actions may be irreversible | Require human-in-the-loop (HITL) confirmation for high-risk actions; implement dry-run mode; maintain audit trails |

## AI RMF Playbook

The [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) accompanies the core framework and provides actionable sub-practices for each function/category. It serves as the implementation guide, translating abstract risk principles into concrete organizational actions. Key playbook sections relevant to agentic AI:

- **GOVERN 1.x** — Policies for AI risk tolerance and escalation
- **MAP 1.x** — Stakeholder identification and harm taxonomy
- **MEASURE 2.x** — Bias and fairness evaluation methods
- **MANAGE 1.x** — Incident response and containment procedures

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| Governance gaps in autonomous systems | Agents make decisions without per-step human approval | Define explicit risk tolerance thresholds in GOVERN; require HITL for actions above threshold |
| Incomplete risk mapping | Novel agent capabilities create unmapped risk surfaces | Enumerate all tools, integrations, and data flows in MAP before deployment |
| Measurement for generative outputs | Traditional ML metrics don't capture agent behavior quality | Use LLM-as-judge evals, red-team exercises, and behavioral monitoring against MAP-defined risk categories |
| Residual risk documentation | Stakeholders unaware of accepted risks | Document residual risks explicitly in MANAGE; include in system cards and deployment approvals |
| Cross-organization AI supply chain | Third-party models and APIs introduce external risk | Apply MAP and MEASURE to all upstream model dependencies; require vendor transparency on training data and safety evaluations |

## Relationship to Other Frameworks

| Framework | Relationship |
|---|---|
| [Google SAIF](./google-saif.md) | Operational/technical implementation guidance; complements NIST's governance-level structure |
| [AWS Generative AI Security Scoping Matrix](../AllThingsAWS/README.md) | Maps security controls to AI lifecycle stages; aligns with NIST's MAP function |
| [ISO/IEC 42001](https://www.iso.org/standard/81230.html) | International AI management system standard; harmonizes with AI RMF |
| [EU AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) | Regulatory compliance layer; NIST AI RMF adoption can support Act conformity |

## See Also

- [Google SAIF](./google-saif.md) — Technical security framework for AI systems
- [Agent Security (Production Best Practices)](../ProductionBestPractices/security.md) — Security controls, threat model, and response playbook
- [SecurityFrameworks Overview](./Readme.md) — All security frameworks and cross-vendor comparison
- [Observability](../ProductionBestPractices/observability.md) — Monitoring infrastructure that feeds MEASURE function evidence

## References

- [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) — Primary framework document
- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) — Implementation sub-practices for each core function
- [NIST AI Resource Center](https://airc.nist.gov/) — Portal for AI RMF resources, profiles, and community updates
