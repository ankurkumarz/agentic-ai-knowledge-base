# AI Governance

## Overview

AI Governance is the set of policies, processes, standards, and oversight mechanisms that ensure agentic AI systems are developed and operated responsibly, safely, and in compliance with applicable regulations and organizational values. As autonomous agents gain the ability to take real-world actions — browsing the web, executing code, calling APIs, and making consequential decisions — governance becomes a first-class engineering concern rather than an afterthought.

Effective AI governance for agentic systems spans three interacting layers: **strategy** (how the organization frames accountability and risk appetite), **best practices** (the repeatable processes and controls teams apply), and **solutions** (the tooling and platforms that operationalize governance at scale).

## Scope

This section covers governance topics specific to agentic AI systems, including:

- Regulatory compliance (EU AI Act, NIST AI RMF, ISO/IEC 42001)
- Organizational governance structures and accountability models
- Risk classification, tiering, and human-in-the-loop controls
- Auditability, explainability, and transparency requirements
- Bias monitoring, fairness evaluation, and incident response
- Commercial and open-source governance platforms

## Key Topics

| Page | What It Covers |
|---|---|
| [Governance Strategy](governance-strategy.md) | Regulatory landscape, risk frameworks, organizational structures, and policy design |
| [Governance Best Practices](governance-best-practices.md) | Concrete controls, HITL patterns, audit trails, bias monitoring, and data governance |
| [Governance Solutions](governance-solutions.md) | Commercial platforms, open-source tooling, and vendor-native governance offerings |

## Why Governance Matters for Agentic AI

Unlike traditional software, agents operate with a degree of autonomy that makes their behavior harder to predict and audit. Several properties create unique governance challenges:

- **Multi-step action chains**: a single user prompt can trigger dozens of downstream tool calls, each with side effects
- **Non-determinism**: LLM-based decision-making is probabilistic, making reproducibility and auditability difficult
- **Emergent behavior in multi-agent systems**: agents orchestrating other agents can produce outcomes no single component was designed to produce
- **Sensitive data exposure**: retrieval-augmented agents routinely access confidential documents, personal data, and production systems

Governance frameworks address these challenges by imposing structure, checkpoints, and accountability at the policy, process, and platform levels.

## See Also

- [Security Frameworks](../SecurityFrameworks/README.md)
- [ProductionBestPractices — Security](../ProductionBestPractices/security.md)
- [Agent Maturity Models](../MaturityModels/README.md)
- [Evaluation Frameworks](../EvaluationFrameworks/README.md)
- [Standards](../Standards/README.md)

## References

- [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — foundational US federal AI risk framework
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — risk-based regulatory framework for AI systems in the EU
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) — international standard for AI management systems
