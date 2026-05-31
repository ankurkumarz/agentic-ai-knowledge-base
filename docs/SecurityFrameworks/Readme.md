# Agentic AI Security

This section provides comprehensive coverage of security frameworks, standards, and best practices for building secure agentic AI systems. From industry standards like NIST AI RMF to vendor-specific security approaches from Google and AWS, this collection offers the essential security guidance needed to deploy AI agents safely in production environments.

## Overview

Securing agentic AI systems requires specialized approaches that address unique risks such as rogue actions, sensitive data disclosure, and autonomous decision-making. This section covers:

- **Security Standards**: Industry-standard frameworks and guidelines
- **Vendor Perspectives**: Security approaches from major cloud providers
- **Risk Management**: Frameworks for identifying and mitigating AI-specific risks
- **Implementation Guidance**: Practical approaches to securing AI agents

## Security Standards

### NIST AI RMF (Risk Management Framework)

The **[NIST AI Risk Management Framework (AI RMF)](https://doi.org/10.6028/NIST.AI.100-1)** provides a comprehensive approach to managing risks associated with artificial intelligence systems.

**Key Resources:**
- **Framework Document**: [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1)
- **Implementation Guide**: [NIST Playbook](https://airc.nist.gov/airmf-resources/playbook/)

![NIST AI Risk Management Framework overview showing the comprehensive approach to AI risk management](../assets/images/security-nist-ai-rmf-overview.png)

The NIST AI RMF provides a structured approach to AI risk management through four core functions:

![NIST AI RMF circular process diagram illustrating the four core functions: Govern, Map, Measure, and Manage](../assets/images/security-nist-ai-rmf-circular-diagram.png)

**Framework Components:**

![NIST AI RMF framework components diagram showing the detailed structure and relationships](../assets/images/security-nist-ai-rmf-framework-diagram.png)

**Key Features:**
- **Risk-based approach** to AI system governance
- **Lifecycle integration** from design to deployment
- **Stakeholder engagement** across organizational levels
- **Continuous monitoring** and improvement processes
- **Flexible implementation** adaptable to various organizational contexts

**Implementation Benefits:**
- Systematic identification of AI-related risks
- Structured approach to risk mitigation
- Compliance with regulatory requirements
- Enhanced stakeholder confidence
- Improved AI system reliability and safety

## Google Perspective

### Agentic Security Operations Center (SOC)

Google's **[Agentic SOC](https://cloud.google.com/solutions/security/agentic-soc?hl=en)** represents a modernized security operations model that moves beyond traditional automation to a system powered by autonomous AI agents. These agents can reason, make decisions, and execute complex security tasks independently while keeping human analysts in control.

### Google's Secure AI Framework (SAIF)

**[Google's Secure AI Framework (SAIF)](https://safety.google/safety/saif/)** provides comprehensive security guidance for AI systems.

**Additional Resources:**
- **[Google's Approach for Secure AI Agents](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/)**

### AI Agent Security Risks and Principles

![Google AI agent security risks and principles diagram outlining key security considerations](../assets/images/security-google-agent-risks-principles.png)

**Key Risks Identified:**
- **Risk 1: Rogue actions** - Agents taking unauthorized or harmful actions
- **Risk 2: Sensitive data disclosure** - Unintended exposure of confidential information

**Security Principles:**
- **Principle 1**: Agents must have well-defined human controllers
- **Principle 2**: Agent powers must have limitations
- **Principle 3**: Agent actions and planning must be observable

### Three Layers of Defense

![Google three layers of defense for AI agents showing policy definition, guardrails, and human oversight](../assets/images/security-google-three-layers-defense.png)

Google's security approach implements three complementary layers:

#### 1. Policy Definition and System Instructions (The Agent's Constitution)
The process begins by defining policies for desired and undesired agent behavior. These are engineered into System Instructions (SIs) that act as the agent's core constitution.

#### 2. Guardrails, Safeguards, and Filtering (The Enforcement Layer)
This layer acts as the hard-stop enforcement mechanism:

- **Input Filtering**: Use classifiers and services like the Perspective API to analyze prompts and block malicious inputs before they reach the agent
- **Output Filtering**: Vertex AI's built-in safety filters provide a final check for harmful content, PII, or policy violations
- **Human-in-the-Loop (HITL) Escalation**: For high-risk or ambiguous actions, the system must pause and escalate to human oversight

#### 3. Monitoring and Response
Continuous monitoring of agent behavior with automated response capabilities for detected anomalies.

### SAIF Framework Implementation

**Google's Secure AI Framework**: [https://saif.google/](https://saif.google/)

**Interactive Implementation Map**: [https://saif.google/secure-ai-framework/saif-map](https://saif.google/secure-ai-framework/saif-map)

![Google Secure AI Framework (SAIF) diagram showing the comprehensive security approach](../assets/images/security-google-saif-framework.png)

**SAIF Framework Components:**
- **Secure Foundation**: Establishing secure infrastructure and development practices
- **Secure Development**: Implementing security throughout the AI development lifecycle
- **Secure Deployment**: Ensuring secure deployment and operational practices
- **Secure Operations**: Maintaining security through ongoing operations and monitoring

## AWS Perspective

### Generative AI Security Scoping Matrix

AWS launched the **[Generative AI Security Scoping Matrix](https://aws.amazon.com/ai/security/generative-ai-scoping-matrix/)** to help organizations understand and address the unique security challenges of foundation model (FM)-based applications.

The **AI Security Scoping Matrix** is a comprehensive framework designed to help organizations assess and implement security controls throughout the AI lifecycle. It breaks down security considerations into specific categories, enabling a focused approach to securing AI applications.

![AWS Agentic AI Security Scoping Matrix showing comprehensive security controls throughout the AI lifecycle](../assets/images/security-aws-scoping-matrix.png)

**Key Features:**
- **Lifecycle Coverage**: Security considerations from development to deployment
- **Risk Categorization**: Structured approach to identifying and addressing risks
- **Control Mapping**: Specific security controls for different AI application types
- **Compliance Alignment**: Framework alignment with regulatory requirements

**Implementation Areas:**
- **Data Security**: Protection of training data and model inputs/outputs
- **Model Security**: Securing the AI models themselves
- **Infrastructure Security**: Securing the underlying compute and storage infrastructure
- **Application Security**: Securing the applications that use AI models
- **Operational Security**: Ongoing security monitoring and incident response

## Implementation Best Practices

### For Development Teams
1. **Implement Defense in Depth**: Use multiple security layers as demonstrated in Google's approach
2. **Follow NIST AI RMF**: Adopt structured risk management practices
3. **Use Vendor Frameworks**: Leverage cloud provider security tools and frameworks
4. **Continuous Monitoring**: Implement ongoing security monitoring and alerting

### For Enterprise Organizations
1. **Adopt Comprehensive Frameworks**: Implement NIST AI RMF or similar comprehensive frameworks
2. **Vendor-Specific Security**: Utilize cloud provider security services (Google SAIF, AWS Security Matrix)
3. **Human Oversight**: Maintain human-in-the-loop controls for critical decisions
4. **Regular Assessments**: Conduct regular security assessments and penetration testing

### For Compliance and Governance
1. **Risk Documentation**: Maintain comprehensive risk registers and mitigation plans
2. **Policy Development**: Develop clear AI governance policies and procedures
3. **Stakeholder Engagement**: Ensure cross-functional involvement in AI security
4. **Regulatory Alignment**: Align security practices with relevant regulatory requirements

## Security Considerations by Use Case

### High-Risk Applications
- Financial services and trading systems
- Healthcare and medical diagnosis
- Critical infrastructure control
- Autonomous vehicle systems

**Additional Controls:**
- Enhanced human oversight requirements
- Stricter access controls and authentication
- Real-time monitoring and alerting
- Comprehensive audit trails

### Medium-Risk Applications
- Customer service and support
- Content generation and marketing
- Business process automation
- Data analysis and reporting

**Standard Controls:**
- Regular security assessments
- Standard access controls
- Monitoring and logging
- Incident response procedures

### Lower-Risk Applications
- Internal productivity tools
- Research and development
- Non-critical automation
- Educational applications

**Basic Controls:**
- Basic access controls
- Standard monitoring
- Regular updates and patches
- User training and awareness

## Emerging Security Challenges

### AI-Specific Threats
- **Prompt Injection**: Malicious inputs designed to manipulate AI behavior
- **Model Poisoning**: Attacks on training data or model parameters
- **Data Extraction**: Attempts to extract sensitive training data
- **Adversarial Examples**: Inputs designed to cause misclassification

### Mitigation Strategies
- **Input Validation**: Comprehensive validation of all inputs to AI systems
- **Output Filtering**: Filtering and validation of AI-generated outputs
- **Model Monitoring**: Continuous monitoring of model behavior and performance
- **Secure Training**: Secure practices for model training and data handling

This security framework provides the foundation for building trustworthy, secure, and compliant agentic AI systems that can operate safely in production environments while maintaining the flexibility and capabilities that make AI agents valuable.

## Microsoft Perspective

### Agent Governance Toolkit

Microsoft's **[Agent Governance Toolkit (AGT)](./agent-governance-toolkit.md)** takes a middleware-layer approach to runtime governance — deterministic policy enforcement, zero-trust identity, and execution sandboxing applied to every agent action before it executes. Key characteristics:

- **Policy engine**: YAML / OPA Rego / Cedar rules with 0.012 ms p50 latency; fail-closed design achieves 0.00% policy violation pass-through
- **Zero-trust identity**: Ed25519 + quantum-safe ML-DSA-65 credentials; behavioral trust scores (0–1000) with decay on anomalous behavior; SPIFFE/SVID compatible
- **Execution rings**: Four hardware-inspired privilege levels; Saga orchestration with automatic compensation; fleet-wide kill switch
- **MCP Security Gateway**: Tool poisoning detection, description drift monitoring, typosquatting checks for Model Context Protocol tools
- **Agent SRE**: SLOs, error budgets, circuit breakers, replay debugging, OpenTelemetry-native governance events
- **Compliance**: Merkle-chained audit logs, Decision BOM, automated EU AI Act / SOC 2 / HIPAA / GDPR evidence
- **OWASP coverage**: All 10 OWASP Agentic Top 10 risks addressed; 13,000+ tests across 10 formal specifications
- **Adapters**: 20+ frameworks (LangChain, AutoGen, CrewAI, Semantic Kernel, Google ADK, OpenAI Agents SDK, etc.); Python, TypeScript, .NET, Rust, Go SDKs

See [Agent Governance Toolkit](./agent-governance-toolkit.md) for full detail.

## Anthropic Perspective

### Anthropic Sandbox Runtime

Anthropic's **[Sandbox Runtime (`srt`)](./anthropic-sandbox-runtime.md)** is a lightweight OS-level sandboxing tool that enforces filesystem and network restrictions on arbitrary processes without containers. Its primary use case is wrapping **MCP servers** in a least-privilege execution envelope:

- **Filesystem isolation**: deny-then-allow policy scoped to explicit path allowlists
- **Network isolation**: allow-only model via HTTP/SOCKS5 proxies; blocks all unlisted domains
- **OS-native primitives**: macOS Seatbelt (`sandbox-exec`) and Linux `bubblewrap` — lower overhead than Docker
- **Violation monitoring**: real-time breach alerts for forensics and observability integration

Install: `npm install -g @anthropic-ai/sandbox-runtime` (Apache-2.0, ~4.1k stars)

See [Anthropic Sandbox Runtime](./anthropic-sandbox-runtime.md) for full detail.

## Agent Sandboxing — Cross-Vendor Overview

For a full comparison of cloud-hosted and local sandbox solutions (E2B, Daytona, Modal, Firecracker, gVisor, Kata Containers, nsjail, and more), see the [Agent Sandboxing](./agent-sandboxing.md) reference page.

## AI Agent Skill Security Scanners

As agent skills (SKILLS.md / `.claude/commands/*.md`) become a primary distribution unit for agentic workflows, scanning them for embedded threats has become a distinct security discipline. Research shows 26.1% of skills contain vulnerabilities and 5.2% show likely malicious intent.

Two open-source tools address skill supply-chain security:

| Tool | Vendor | Key Strengths |
|---|---|---|
| [Skill Scanner](./skill-scanners.md) | Cisco AI Defense | Multi-engine consensus (YARA + AST + LLM + VirusTotal); interactive HTML reports; SARIF/GitHub Actions integration |
| [SkillSpector](./skill-scanners.md) | NVIDIA | 64 patterns across 16 categories; live OSV.dev CVE lookup; MCP-specific risk detection; LangGraph pipeline |

See [AI Agent Skill Security Scanners](./skill-scanners.md) for full detail, CLI usage, and a threat-model comparison.

## See Also

- **[Agent Development Frameworks](../AgenticFrameworks/README.md)**: Security considerations for frameworks
- **[Agent Platforms](../AgentPlatforms/README.md)**: Platform security features
- **[Standards](../Standards/README.md)**: Security standards and protocols
- **[Best Practices](../ProductionBestPractices/README.md)**: Security best practices
- **[Agent Governance Toolkit](./agent-governance-toolkit.md)**: Microsoft runtime governance for agents
- **[Anthropic Sandbox Runtime](./anthropic-sandbox-runtime.md)**: OS-level process sandboxing for MCP servers
- **[Agent Sandboxing](./agent-sandboxing.md)**: Cross-vendor comparison of sandbox solutions
- **[AI Agent Skill Security Scanners](./skill-scanners.md)**: Cisco Skill Scanner and NVIDIA SkillSpector — scanning agent skills for prompt injection, data exfiltration, and malicious patterns
- **[MCP Standard](../Standards/mcp.md)**: Model Context Protocol (MCP Security Gateway target)
- **[AI Governance Solutions](../AIGovernance/governance-solutions.md)**: Governance platforms and tooling
