# Cloud Security Alliance (CSA)

## Overview

The **Cloud Security Alliance (CSA)** is a not-for-profit organization focused on defining and promoting best practices for secure cloud and, increasingly, AI computing. Within the agentic AI space, CSA's **AI Organizational Responsibilities Working Group** publishes research artifacts that establish testing, governance, and threat-modeling standards for Agentic AI systems — positioning CSA as one of the industry standards bodies shaping safe agentic deployment alongside NIST and Google SAIF.

## Key Artifacts

### Agentic AI Red Teaming Guide
Published August 2025, this guide defines a 12-category threat taxonomy and a four-phase (Preparation → Execution → Analysis → Reporting) testing methodology specifically for autonomous, multi-step, tool-using AI agents — extending traditional LLM red teaming to cover the full agentic action chain. See the full breakdown: [Agentic AI Red Teaming Guide (CSA)](../SecurityFrameworks/agentic-ai-red-teaming-guide.md).

### MAESTRO
**MAESTRO** (Multi-Agent Environment, Security, Threat, Risk, and Outcome) is CSA's multi-layered **threat-modeling** framework for Agentic AI — distinct from and complementary to the Red Teaming Guide's testing focus. MAESTRO addresses:

- **Evaluation and Observability** — detecting anomalies, poisoned datasets, evasion techniques
- **Deployment and Infrastructure** — compromised container images, orchestration attacks
- **Agent Frameworks** — backdoor attacks, input validation exploits, supply chain vulnerabilities
- **Data Operations** — data poisoning, exfiltration, tampering, compromised RAG pipelines

### AI Organizational Responsibilities: Governance, Risk Management, Compliance, and Cultural Aspects
A companion artifact from the same working group addressing organizational-level AI governance structures, risk management processes, and compliance practices.

## Relationship to Other Standards

CSA's agentic AI artifacts complement rather than replace other security frameworks referenced in this wiki:

| Body | Focus | Relationship to CSA |
|---|---|---|
| [NIST AI RMF](../SecurityFrameworks/nist-ai-rmf.md) | Risk-based governance across the AI lifecycle | CSA's Red Teaming Guide calls out alignment with NIST AI RMF as a future-outlook priority |
| [Google SAIF](../SecurityFrameworks/google-saif.md) | Secure AI development/deployment foundation | Both share the three-layer (policy/guardrails/monitoring) defense philosophy |
| [Agentic AI Foundation (AAIF)](./agentic-ai-foundation.md) | Open standards (MCP, AGENTS.md) under the Linux Foundation | CSA artifacts are testing/governance guidance rather than protocol standards |

## See Also
- [Agentic AI Red Teaming Guide (CSA)](../SecurityFrameworks/agentic-ai-red-teaming-guide.md)
- [Agentic AI Security Overview](../SecurityFrameworks/Readme.md)
- [Agent Security Best Practices](../ProductionBestPractices/security.md)
- [Agentic AI Foundation (AAIF)](./agentic-ai-foundation.md)

## References
- [Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide) — Cloud Security Alliance (Aug 2025)
- [Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) — Cloud Security Alliance
- [AI Organizational Responsibilities: Governance, Risk Management, Compliance, and Cultural Aspects](https://cloudsecurityalliance.org/artifacts/ai-organizational-responsibilities-governance-risk-management-compliance-and-cultural-aspects) — Cloud Security Alliance
- [AI Organizational Responsibilities Working Group](https://cloudsecurityalliance.org/research/working-groups/ai-organizational-responsibilities) — Cloud Security Alliance
