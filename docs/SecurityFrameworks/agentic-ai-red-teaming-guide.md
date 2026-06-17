# Agentic AI Red Teaming Guide (CSA)

## Overview

Red teaming is the practice of simulating real-world adversarial attacks against a system to uncover exploitable weaknesses before malicious actors do. The concept originated in military wargaming, where a designated "red team" plays the adversary against a "blue team" defending a position, and has since been adopted across cybersecurity and, more recently, AI systems — where it now also covers probing models and agents for harmful, biased, or unsafe outputs in addition to traditional exploit-based testing *(background per [IBM: What is red teaming?](https://www.ibm.com/think/topics/red-teaming))*.

The [Cloud Security Alliance (CSA) Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide) (published by the AI Organizational Responsibilities Working Group, August 2025) extends this practice specifically to **Agentic AI systems**. Traditional LLM red teaming focuses on single-turn prompt/response safety. Agentic systems plan, reason, act autonomously across multiple steps, invoke tools, retain memory, and coordinate with other agents — which means a red teaming methodology must test the full action chain, not just model outputs. The guide explicitly excludes threat *modeling* (covered separately by CSA's [MAESTRO framework](#maestro-and-tooling-landscape)) and focuses purely on **testing procedures**.

## Why Red Teaming Agentic AI Is Important

Agentic AI introduces unique challenges beyond single-turn LLM interactions:

- **Autonomous action** — agents execute multi-step plans and invoke tools without per-step human confirmation, so a single manipulated decision can cascade into real-world consequences.
- **Reuse of existing knowledge and resources** — agents draw on external knowledge bases, memory stores, and other agents' outputs, widening the attack surface beyond the model itself.
- **Emergent, compounding risk** — errors, hallucinations, or injected instructions can propagate through a chain of tool calls or agent handoffs before a human ever reviews the outcome.

## The 12 Threat Categories

The guide organizes its detailed testing guidance into 12 threat categories. Each category defines **Test Requirements**, breaks down into numbered sub-tests, and provides concrete **Actionable Steps** red teamers can execute.

| # | Category | What It Tests |
|---|---|---|
| 4.1 | **Agent Authorization and Control Hijacking** | Direct control hijacking, permission escalation, role inheritance exploitation, activity monitoring/detection gaps, separation of control vs. execution, audit trail completeness, least-privilege enforcement |
| 4.2 | **Checker-Out-of-the-Loop** | Threshold-breach simulation, checker/human engagement testing, anomaly detection and response, context-aware decision analysis, continuous monitoring and feedback loops |
| 4.3 | **Agent Critical System Interaction** | Physical system manipulation, IoT/OT command injection, critical infrastructure access, safety interlock bypass, real-time anomaly monitoring, command/action validation |
| 4.4 | **Agent Goal and Instruction Manipulation** | Goal interpretation attacks, instruction-set poisoning, semantic manipulation, recursive/hierarchical goal subversion, adaptive manipulation, data exfiltration via goal drift, goal extraction attempts |
| 4.5 | **Agent Hallucination Exploitation** | Induced hallucination testing, cascading hallucination across agents, decision manipulation via fabricated outputs, output verification/validation, anomaly detection, protective failsafes, domain-specific hallucination triggers |
| 4.6 | **Agent Impact Chain and Blast Radius** | Cross-system exploitation via compromised agents, trust-relationship abuse, blast-radius limitation, containment mechanisms, security barrier validation |
| 4.7 | **Agent Knowledge Base Poisoning** | Training data poisoning, external knowledge manipulation, knowledge base corruption, guided-learning exploitation, update mechanism vulnerabilities, cross-agent knowledge sharing, recovery/monitoring |
| 4.8 | **Agent Memory and Context Manipulation** | Context amnesia exploitation, cross-session/cross-application data leakage, memory poisoning, memory overflow/context loss, secure session management |
| 4.9 | **Agent Orchestration and Multi-Agent Exploitation** | Inter-agent communication exploitation, trust-relationship abuse, coordination protocol manipulation, feedback-loop resource exhaustion, orchestration/boundary control, adversarial collusion/spoofing between agents, orchestrator state poisoning via managed-agent responses |
| 4.10 | **Agent Resource and Service Exhaustion** | Computational resource depletion, memory exhaustion, API/service quota depletion, learning-process exploitation, anomaly monitoring, defensive architecture testing |
| 4.11 | **Agent Supply Chain and Dependency Attacks** | Development-chain compromise, dependency injection, service-chain compromise, deployment-pipeline security, monitoring/detection capability |
| 4.12 | **Agent Untraceability** | Trace evasion simulation, downstream tool activation analysis, forensic analysis obfuscation, accountability chain verification, anonymization stress tests with PII/PCI/PHI |

### Representative Actionable Steps

A sample of the guide's testing procedures, illustrating the level of specificity:

- Use API testing tools (Postman, Burp Suite) to inject malicious commands into an agent's control plane and observe whether unauthorized actions are accepted (4.1).
- Simulate breaches of predefined operational thresholds (e.g., aviation operational limits) and measure how quickly the agent detects and reports checker/human-in-the-loop unavailability (4.2).
- Use simulation tools to mimic unsafe physical conditions (e.g., overriding temperature controls) and evaluate whether the agent logs and reports anomalies before acting (4.3).
- Provide intentionally ambiguous or conflicting goal instructions and document how the agent resolves the ambiguity (4.4).
- Seed follow-up tasks with deliberately fabricated outputs from an earlier step and trace whether the error cascades through downstream agents (4.5, 4.9).
- Attempt to access interconnected systems using the credentials of a deliberately compromised agent to measure blast radius (4.6).
- Stress-test agents with use cases involving PII/PCI/PHI to confirm logs remain comprehensible without leaking sensitive data (4.12).

## Testing Methodology

The guide proposes a four-phase structured approach to red teaming Agentic AI systems:

| Phase | Activities |
|---|---|
| **Preparation** | Define specific test scenarios; set up protected/isolated testing environments; prepare tools and scripts |
| **Execution** | Conduct step-by-step tests; document real-time observations; capture logs and metrics |
| **Analysis** | Evaluate test results; identify vulnerabilities and their potential impact; prioritize findings by severity |
| **Reporting** | Create detailed reports per test; develop actionable mitigation strategies; document a summary of findings for stakeholders |

**Suggested effectiveness metrics** (human-in-the-loop and automated):
- Response time to detect and block unauthorized access attempts
- Percentage of successful exploits vs. total attempts
- Time to containment for identified vulnerabilities
- Number of undetected malicious actions during testing

## MAESTRO and Tooling Landscape

The guide names **MAESTRO** (CSA's separate multi-layered *threat-modeling* framework for Agentic AI — covering evaluation/observability, deployment/infrastructure, agent frameworks, and data operations) as the complementary modeling layer to this testing guide, plus a set of emerging red-teaming tools and benchmarks:

| Tool / Framework | Provider | Focus |
|---|---|---|
| [MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) | Cloud Security Alliance | Multi-layered threat *modeling* (not testing) for Agentic AI: anomaly/poisoned-dataset detection, deployment/infra risks, agent framework backdoors, data operation poisoning |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | ETH Zurich (SPY Lab) | Dynamic evaluation of prompt injection attacks/defenses via 97 realistic tasks and 629 security test cases; measures utility preservation vs. attack success rate |
| Agent-SafetyBench | Academic | 349 interactive environments, 2,000 test cases across 8 risk categories; automated scoring model (91.5% accuracy); evaluates 16+ LLM agents |
| [AgentFence](https://github.com/) | Open source | Automated probing for prompt injection and secret leakage; prebuilt role-confusion/instruction-leakage attacks; SDK support for LangChain and OpenAI agents |
| [SplxAI Agentic Radar](https://github.com/splx-ai/agentic-radar) | SplxAI | Security scanner for LLM agentic workflows: workflow visualization, tool identification (MCP, email, JIRA, etc.), vulnerability mapping report |
| Agent Security Bench (ASB) | ICLR 2025 | Evaluates 27 attack/defense methods across 10 scenarios; benchmarks 13 LLMs (84.3% max attack success rate); introduces a utility-security balance metric |
| [Promptfoo LLM Security DB](https://www.promptfoo.dev/lm-security-db/) | Promptfoo | Structured repository of security vulnerabilities for LLMs and Agentic AI |
| Pentest Copilot | Bugbase | AI-driven red teaming automation: contextualized attack orchestration, continuous learning from threat intel, dynamic adversary campaign generation |
| [AI Red Teaming Agent](https://devblogs.microsoft.com/foundry/ai-red-teaming-agent-preview/) | Microsoft (Azure AI Foundry) | Automated content-safety risk scans; Attack Success Rate (ASR) metrics; deployment-readiness reporting |
| FuzzAI Framework | Salesforce | Automated, scalable AI security fuzzing: context-specific input generation (Mutator module), many-shot jailbreaking support, feature-specific attack strategy selection |

## Future Outlook

The guide identifies priority areas for the evolution of Agentic AI red teaming:

- **Autonomous red teaming agents** — adaptive, automated vulnerability discovery and adversarial simulation in real time
- **Downstream action red teaming** — automated, multi-domain testing of agentic action chains (beyond manual static/log-based mapping)
- **Secure multi-agent orchestration research** — trust boundaries, privilege separation, and inter-agent communication security at scale
- **Standardized metrics and benchmarks** — Mean Time to Detection (MTTD), exploit success rates, containment time, comparable across environments
- **Alignment with regulatory frameworks** — EU AI Act, [NIST AI RMF](./nist-ai-rmf.md), and similar emerging requirements around accountability and explainability
- **Open-source security tooling and research** — community-driven simulation frameworks and attack scenario generators

## See Also
- [Agentic AI Security Overview](./Readme.md) — NIST AI RMF, Google SAIF, AWS, Microsoft, Anthropic perspectives
- [Agent Security Best Practices](../ProductionBestPractices/security.md) — prompt injection, least privilege, audit trails
- [Agent Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md) — adversarial test cases, launch gates
- [Cloud Security Alliance (Industry Standards)](../Standards/csa.md)
- [Agent Sandboxing](./agent-sandboxing.md)

## References
- [Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide) — Cloud Security Alliance, AI Organizational Responsibilities Working Group (Aug 2025) — primary source for this page
- [HarmBench](https://github.com/centerforaisafety/HarmBench/tree/main) — standardized evaluation framework for automated red teaming and robust refusal
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) — dynamic environment to evaluate prompt injection attacks and defenses for LLM agents
- [NIST: Strengthening AI Agent Hijacking Evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)
- [AI Organizational Responsibilities: Governance, Risk Management, Compliance, and Cultural Aspects](https://cloudsecurityalliance.org/artifacts/ai-organizational-responsibilities-governance-risk-management-compliance-and-cultural-aspects) — CSA
- [Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) — CSA
- [Promptfoo LLM Security DB](https://www.promptfoo.dev/lm-security-db/)
- [Introducing AI Red Teaming Agent — Azure AI Foundry](https://devblogs.microsoft.com/foundry/ai-red-teaming-agent-preview/) — Microsoft
- [SplxAI Agentic Radar](https://github.com/splx-ai/agentic-radar)
- [AI Red Teaming Reasoning LLMs](https://adversa.ai/blog/ai-red-teaming-reasoning-llm-jailbreak-china-deepseek-qwen-kimi/) — Adversa AI
- [What is red teaming?](https://www.ibm.com/think/topics/red-teaming) — IBM, background on red teaming origins and general practice
