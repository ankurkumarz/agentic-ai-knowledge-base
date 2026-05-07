# Governance Strategy

## Overview

A governance strategy defines *how* an organization frames accountability, risk appetite, and policy for its agentic AI systems before those systems reach production. Without a deliberate strategy, governance efforts fragment across teams and comply with regulations only reactively. A strong strategy aligns business objectives, regulatory obligations, and technical controls into a coherent operating model.

## Regulatory Landscape

### EU AI Act (2024)

The EU AI Act is the first comprehensive binding regulation for AI systems. It applies a **risk-based classification** that directly impacts agentic AI deployments:

| Risk Tier | Definition | Examples | Obligations |
|---|---|---|---|
| Unacceptable Risk | AI practices posing a clear threat to fundamental rights | Social scoring, real-time biometric surveillance | Prohibited outright |
| High Risk | AI in regulated sectors or affecting safety/rights | Autonomous agents in healthcare, finance, HR, law enforcement | Conformity assessments, logging, human oversight, documentation |
| Limited Risk | AI with specific transparency obligations | Chatbots, deepfake generators | Disclose AI nature to users |
| Minimal Risk | All other AI | Spam filters, recommendation systems | No mandatory requirements |

Agentic systems that operate in high-risk domains (credit scoring, employee monitoring, medical triage) must implement mandatory human oversight mechanisms, maintain logs for post-market surveillance, and undergo conformity assessments before deployment.

### NIST AI Risk Management Framework (AI RMF 1.0)

The NIST AI RMF provides a voluntary but widely adopted structure for managing AI risk across four core functions:

- **Govern**: Establish organizational policies, roles, responsibilities, and culture for AI risk management
- **Map**: Identify and classify AI risks in context (mission, stakeholders, data, system capabilities)
- **Measure**: Quantify and assess identified risks using qualitative and quantitative methods
- **Manage**: Prioritize and implement risk responses; track and communicate residual risk

For agentic AI, the *Map* and *Measure* phases are especially important because autonomous action chains amplify the blast radius of a misconfigured or misused agent.

### ISO/IEC 42001:2023

ISO 42001 is the international standard for **AI Management Systems (AIMS)**. It specifies requirements for establishing, implementing, maintaining, and continuously improving an organization's approach to responsible AI development. Key requirements include:

- Defining the scope and context of AI use
- Leadership commitment and accountability assignment
- Risk and impact assessment processes
- Operational controls and monitoring procedures
- Internal audit and management review cycles

### Other Relevant Regulations

| Regulation / Standard | Jurisdiction | Relevance to Agentic AI |
|---|---|---|
| GDPR / CCPA | EU / California | Data minimization, right to explanation, consent for automated decisions |
| SOC 2 Type II | US (voluntary) | Security, availability, and confidentiality controls for AI services |
| HIPAA | US | PHI handling by agents operating in healthcare pipelines |
| FINRA / SEC rules | US | Explainability and audit trails for agents in financial services |
| DORA | EU | Operational resilience for AI in financial entities |

## Organizational Governance Structures

### Centralized AI Governance Office

A dedicated function (AI Governance Office or AI Risk Committee) sets enterprise-wide policy, approves high-risk AI deployments, maintains the AI system inventory, and tracks regulatory changes. Suitable for large enterprises or organizations in regulated industries.

### Federated Governance

Each business unit owns governance for the agents it deploys, guided by central policy guardrails. A central function sets the minimum bar (risk classification criteria, mandatory controls, reporting templates) while teams have autonomy in implementation. Works well in multi-product technology companies.

### Embedded Governance (DevSecAI)

Governance controls are embedded directly into the CI/CD pipeline — automated policy checks, pre-deployment risk assessments, and mandatory review gates — rather than managed by a separate team. This model scales best for organizations with high deployment velocity.

## Risk Classification for Agentic Systems

Before deploying an agent, classify it across two dimensions:

**Impact scope** (what happens if the agent fails or is misused):
- **Low**: output is advisory only; no automated action taken
- **Medium**: agent triggers reversible actions (send email, create document)
- **High**: agent triggers irreversible or high-value actions (financial transactions, access provisioning, data deletion)

**Autonomy level** (how much human oversight exists):
- **Supervised**: every action requires explicit human approval
- **Semi-autonomous**: human approves categories of action; individual actions proceed automatically
- **Fully autonomous**: agent acts without per-action human review

The intersection of impact scope and autonomy level determines the required governance tier (and, under the EU AI Act, the risk classification).

## Policy Design Principles

| Principle | Description |
|---|---|
| Least privilege | Agents are granted only the permissions required for their specific task; no standing access to sensitive systems |
| Human-in-the-loop thresholds | Define explicit criteria for when an agent must pause and request human approval before proceeding |
| Audit by default | All agent actions and decisions are logged in a tamper-evident, queryable store from day one |
| Explainability requirement | High-risk agents must produce a human-readable rationale for consequential decisions |
| Incident response plan | Every production agent deployment has a documented escalation path and rollback procedure |
| Time-bounded autonomy | Autonomous operation is scoped to defined windows; agents do not run indefinitely without oversight checks |

## See Also

- [Governance Best Practices](governance-best-practices.md)
- [Governance Solutions](governance-solutions.md)
- [Security Frameworks](../SecurityFrameworks/README.md)
- [ProductionBestPractices — Security](../ProductionBestPractices/security.md)
- [Agent Maturity Models](../MaturityModels/README.md)

## References

- [NIST AI Risk Management Framework 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — voluntary US federal AI risk framework
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — EU regulation with risk-based classification
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) — international AI management systems standard
