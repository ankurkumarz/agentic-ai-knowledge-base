# Agentic AI Knowledge Base


![Agentic AI](./assets/images/agentic-header.png)

A comprehensive, structured knowledge repository consolidating cutting-edge research, patterns, frameworks, and best practices for building, deploying, and operating agentic AI systems at scale.

<p align="center">
<a href="https://agentic-ai.readthedocs.io"><img src="https://img.shields.io/badge/agentic-@readthedocs.io-blue"></a>
</p>

<p align="center">
<a href="https://opensource.org/licenses/Apache"><img src="https://img.shields.io/badge/license-Apache--2.0-green"></a>
</p>

## Executive Overview

The **Agentic AI Knowledge Base** serves as a consolidated knowledge hub designed to support the full lifecycle of agentic AI development—from foundational concepts and architectural patterns to production deployment, security, and operational excellence. This repository brings together curated knowledge articles, architecture patterns, white papers, research insights, and industry best practices spanning the entire agentic AI ecosystem.

Our comprehensive knowledge base structure provides systematic coverage of all aspects of agentic AI, enabling architects, engineers, researchers, and platform teams to design robust, secure, and production-ready agentic AI solutions. The knowledge base spans core topics including agent architectures and frameworks, technology stacks, industry standards, evaluation methodologies, security frameworks, and operational best practices.

## Knowledge Base Structure

### **1. Introduction**
- **Overview**: Welcome and foundational information about the knowledge base
- **Disclaimer and Usage Guidelines**: Important usage information and disclaimers
- **Target Audience**: Architects, engineers, researchers, and platform teams working with agentic AI

### **2. Agent Harness**
- **Agent Harness**: What a harness is and its core components (system prompts, tools, sandbox, orchestration, hooks); the Model–Harness Co-Evolution Loop
- **Harness Engineering**: Feedforward/feedback control, computational vs. inferential sensors, regulation categories (maintainability, architecture fitness, behaviour), harnessability factors
- **Code as Agent Harness**: 197-paper survey (Ning et al., 2026) establishing code as the executable, inspectable, and stateful substrate for agent systems; three-layer taxonomy: harness interface (reasoning/acting/environment modeling), harness mechanisms (planning/memory/tool use/iterative debugging), and harness scaling (multi-agent coordination over shared code artifacts); application domains spanning code assistants, GUI/OS agents, scientific discovery, embodied robotics, DevOps, and enterprise workflows
- **Harness Optimization**: Automated search over harness code using an agentic proposer with filesystem access to prior execution traces (Meta-Harness, Lee et al., 2026); +7.7 points on text classification (4x fewer tokens), +4.7 points on IMO math reasoning across 5 held-out models, surpasses hand-engineered baselines on TerminalBench-2
- **Loop Engineering**: Designing scheduled, self-feeding systems that prompt the agent instead of being prompted by a human — six primitives (automations, worktrees, skills, connectors, sub-agents, externalized state), mapped across the Codex app and Claude Code; verification, comprehension rot, and cognitive surrender remain unresolved as the loop improves
- **LLM Harness Survey & Taxonomy**: ETCLOVG seven-layer taxonomy (Execution, Tooling, Context, Lifecycle, Observability, Verification, Governance); formal H=(E,T,C,S,L,V) model; harness completeness matrix across 23+ systems; nine empirically-grounded technical challenges; covers 110+ papers and timeline from 1997–2026

### **3. Concepts**
- **Agent Definition**: Fundamental definitions and terminology for agentic AI systems; Chat-Engine vs. Do-Engine framing (You.com, 2026)
- **Agent Types**: Classification and comparison of different agent architectures
- **References**: Key research papers and foundational materials
- **2026 AI Predictions (You.com)**: 35 predictions by Richard Socher and Bryan McCann covering workforce transformation, reward engineering, 10-person unicorns, software development, vertical AI agents, space computing, biotech, and consumer media

### **4. Architecture and Design Patterns**
- **Agentic Architecture Components**: Selection criteria for system components
- **Design Pattern Selection**: Proven patterns including OpenAI's agentic patterns, the Arsanjani & Bustos pattern catalog (Agent Router, Supervisor, Swarm, Blackboard, FCoT, Instruction Fidelity Auditing, Adaptive Retry, Canary Agent Testing, and 20+ others), and Confluent's event-driven realizations of Orchestrator-Worker, Hierarchical, Blackboard, and Market-Based patterns over Kafka/Flink
- **Multi-agent Systems**: Four architectures (centralized, decentralized, hierarchical, hybrid); Supervisor vs. Swarm comparison; Agent Router pattern; seven benefits; failure modes and decision framework; framework comparison for architecture selection; event-driven (Kafka consumer-group) realizations of Orchestrator-Worker, Hierarchical, Blackboard, and Market-Based coordination
- **12-Factor Agents**: Principles for building reliable LLM applications
- **Gartner LLM Patterns**: Industry-recognized design patterns

### **5. Agent Development Frameworks**
Comprehensive coverage of major development frameworks:
- **LangChain & LangGraph**: Industry-standard frameworks with 1M+ builders; LangGraph excels at complex stateful multi-agent workflows
- **Google ADK**: Model-agnostic framework optimized for Google Cloud; hierarchical agent composition with built-in evaluation
- **AWS Strands Agents**: Model-driven autonomous agent framework with native MCP and A2A support
- **Microsoft Agent Framework**: Unified .NET and Python framework
- **AutoGen**: Multi-agent conversation framework by Microsoft
- **Semantic Kernel**: Production-ready SDK for enterprise applications
- **LlamaIndex**: Data-intensive LLM applications and knowledge management
- **AutoGPT**: Continuous AI agents for workflow automation
- **CrewAI**: Role-based multi-agent collaboration framework; minimal configuration
- **Agno**: High-performance multi-agent framework (~2μs agent creation, ~3.75 KiB per agent)
- **Mastra**: TypeScript-first framework for web applications integrating with existing REST APIs
- **PydanticAI**: Type-safe GenAI development
- **Spring AI**: Java ecosystem integration
- **Haystack**: Production-ready LLM applications and RAG pipelines

### **6. Agent Technology Stack**
- **Tech Stack References**: Comprehensive technology landscape overview
- **Agentic AI Platforms**: Google Gemini Enterprise Agent Platform, AWS AgentCore, Microsoft Azure AI; **Enterprise Platform Comparison (2026)** covering Salesforce Agentforce, Microsoft Copilot Studio, ServiceNow, Kore.ai, UiPath Maestro, Azure AI Foundry Agent Service, IBM watsonx Orchestrate, LangGraph, and CrewAI Enterprise with pricing, adoption data, and honest constraints
- **Workflow Engines**: Open source, self-hosted, and SaaS solutions; **Temporal** for durable execution — fault-tolerant, long-running AI agent workflows with Event History replay, Signals for human-in-the-loop, and Child Workflows for multi-agent fan-out; **Confluent** (Apache Kafka & Flink) as the event-streaming backbone for high fan-out multi-agent coordination, agentic RAG ingestion, and real-time stream processing
- **Popular AI Agents**: Coding agents, research agents, and super agents

### **7. Agentic AI Industry Standards**
- **Agentic AI Foundation**: Linux Foundation initiative for open standards
- **Model Context Protocol (MCP)**: Anthropic's standardization for LLM context
- **Agent2Agent (A2A) Protocol**: Google's agent interoperability standard
- **AGENTS.md**: Industry standard for AI agent instructions
- **OpenSpec & AG-UI**: Emerging standards for development and interfaces
- **AIDLC Workflows (AWS)**: Methodology-first AI-driven development lifecycle with structured Inception → Construction phases, approval gates, and a built-in evaluator for CI/CD quality gates
- **Open Knowledge Format (OKF)**: Google Cloud's open specification (v0.1, June 2026) for portable, agent- and human-readable knowledge bundles — markdown files with YAML frontmatter, no SDK or runtime required; formalizes Karpathy's "LLM-wiki" pattern
- **Cloud Security Alliance (CSA)**: Industry standards body for Agentic AI testing and governance — Agentic AI Red Teaming Guide (12-category threat taxonomy) and the MAESTRO threat-modeling framework

### **8. Agentic AI Reference Architecture**
- **AI Automation**: LangManus framework and automation patterns
- **Self-learning Agents**: Agent0 series and self-evolving systems
- **AI Assistant Architecture**: Reference implementations and blueprints
- **RAG Architecture**: Retrieval-augmented generation patterns
- **Search as Code (SaC)**: Perplexity's paradigm where models generate code to assemble task-specific retrieval pipelines; three layers — Models as Control Plane, Compute Sandboxes, Agentic Search SDK; 2.5× advantage on WANDR benchmark; 85.1% token reduction in CVE audit case study
- **NVIDIA AI Blueprints**: Video search and summarization agents

### **9. Agentic AI Maturity Models**
- **Gartner's Perspective**: Industry maturity assessment frameworks
- **AWS Perspective**: Generative AI maturity models and progression paths
- **Google's Perspective**: Cloud-native maturity considerations
- **IDC's Perspective**: Market evolution and adoption patterns
- **Arsanjani GenAI Maturity Model**: 7-level framework (data foundation → RAG → tuning → grounding → single-agent → multi-agent) with agent anatomy, the new agentic stack (Function Calling, MCP, A2A), and maturity-to-pattern mapping

### **10. Agents Marketplace**
- **AWS AI Agents Marketplace**: Enterprise agent solutions and platforms
- **AgentOps Marketplace**: Operational tools and services
- **Miscellaneous Platforms**: Community and specialized marketplaces

### **11. AI Agents Best Practices**
- **Anthropic**: Building effective agents and safety considerations
- **Google**: Enterprise deployment and scaling best practices
- **Microsoft**: .NET and Azure integration patterns
- **OpenAI**: Practical guide to building agents and agentic patterns

---

## Production Best Practices & Guidelines

A dedicated section consolidating all production-readiness guidance — cross-cutting concerns for teams moving agents from prototype to production.

### **Observability**
- **Goals & Objectives**: Monitoring, debugging, and performance optimization
- **Observability Solutions**: LangSmith, Langfuse, Openlit, Braintrust, W&B Weave, Galileo (Graph/Trace/Timeline views, Insights Engine)
- **Best Practices**: Distributed tracing, alerting, dashboards, and predictive observability; three-level tracking (session/step/system); production benchmarks (Action Completion, Tool Selection Quality)

### **State & Memory Management**
- **Three Functional Tiers**: Short-term, episodic, and long-term memory systems
- **LTM Strategies**: Vector RAG, knowledge graphs, entity extraction, and reflection
- **Memory Solutions**: Mem0, MemMachine, Zep, AgentFS, and cloud-managed memory services

### **Deployment**
- **AgentOps & GenOps**: Evolution of MLOps for generative AI systems
- **Lifecycle Management**: Development, testing, deployment, and operations
- **Production Operations**: Container orchestration, auto-scaling, and multi-agent coordination

### **Agent Testing & Evaluations**
- **LLM Evaluation Frameworks**: DeepEval, MLFlow, RAGAS, and OpenEvals
- **Agent Benchmarks**: METR, Terminal Bench, VisualWebArena, GAIA, and DeepResearch Bench (RACE/FACT evaluation of deep research agents)
- **Evaluation Platforms**: Galileo, Google Stax, and LastMile AI

### **Context Engineering**
- **Key Challenges**: Context rot, poisoning, distraction, confusion, and clash — with empirical evidence from DeepMind, Gemini 2.5, Berkeley, Microsoft/Salesforce research
- **Memory vs. Context**: The 100:1 rule; what to keep in context vs. store in memory; four types of context
- **Management Strategies**: Offloading, reduction, retrieval, isolation, and caching; context size thresholds; phased implementation roadmap
- **Efficiency Frontier**: Deployment-aware cost-performance optimization; reuse-parameter (N) driven strategy selection; ~25% token savings; transition boundaries between retrieval and compression (Shen et al., 2026)
- **Implementation References**: Manus, Anthropic, LangGraph, and Devin approaches

### **Agent Security**
- **Security Standards**: NIST AI Risk Management Framework
- **Google Perspective**: SAIF Framework and secure AI agents approach
- **AWS Perspective**: Generative AI Security Scoping Matrix
- **Microsoft Perspective**: Agent Governance Toolkit — runtime governance with deterministic policy enforcement (YAML/OPA/Cedar), zero-trust identity, execution sandboxing, MCP Security Gateway; covers all 10 OWASP Agentic Top 10 risks
- **CSA Perspective**: Agentic AI Red Teaming Guide — 12-category adversarial testing taxonomy (authorization hijacking, checker-out-of-the-loop, hallucination exploitation, blast radius, knowledge base poisoning, multi-agent exploitation, and more) with a four-phase Preparation/Execution/Analysis/Reporting methodology
- **Risk Management**: Rogue actions, data disclosure, prompt injection, and mitigation strategies

### **Cost Management**
- **Token Optimization**: Model routing, prompt optimization, and caching strategies
- **Budget Controls**: Per-request budgets, alerting thresholds, and hard stops
- **Cost Monitoring**: Langfuse, Openlit, LangSmith, Braintrust cost tracking
- **Vendor Guidance**: Anthropic, OpenAI, Google, and AWS cost optimization approaches

## Target Audiences

### **Architects & Technical Leaders**
- System architects designing agentic AI solutions
- Technical leaders evaluating frameworks and platforms
- Enterprise architects planning AI transformation initiatives

### **Software Engineers & Developers**
- Developers building agentic applications and workflows
- Engineers integrating AI agents into existing systems
- Full-stack developers working with AI-powered applications

### **AI/ML Engineers & Researchers**
- ML engineers implementing agent-based systems
- AI researchers exploring multi-agent architectures
- Data scientists building intelligent automation solutions

### **Platform & DevOps Teams**
- Platform engineers deploying agent infrastructure
- DevOps teams managing AI agent lifecycles
- Site reliability engineers monitoring agent systems

### **Product & Business Teams**
- Product managers defining agent capabilities
- Business analysts evaluating AI agent ROI
- Innovation teams exploring agentic AI opportunities

## Learning Paths

### **Beginner Path: Foundations**
1. **Start Here**: Introduction → Concepts → Architecture Patterns
2. **Choose Framework**: Agent Development Frameworks (start with LangChain/LangGraph)
3. **Build First Agent**: Technology Stack → Reference Architecture
4. **Learn Standards**: Industry Standards → Best Practices

### **Intermediate Path: Implementation**
1. **Deep Dive Frameworks**: Compare multiple frameworks for your use case
2. **Architecture Design**: Reference Architecture → Context Engineering
3. **Memory & State**: State & Memory Management → Agent Testing & Evaluations
4. **Production Readiness**: Agent Security → Observability → Deployment

### **Advanced Path: Production & Scale**
1. **Enterprise Patterns**: Maturity Models → Agent Security → Cost Management
2. **Operational Excellence**: Deployment → Observability → Agent Testing & Evaluations
3. **Marketplace & Ecosystem**: Agents Marketplace → Industry Standards
4. **Innovation & Research**: Latest research papers and emerging patterns

### **Specialized Paths**

**Security-Focused Path**: Agent Security → Agent Testing & Evaluations → Standards → Observability

**Research-Oriented Path**: Concepts → Reference Architecture → Agent Testing & Evaluations → State & Memory Management

**Platform Engineering Path**: Technology Stack → Deployment → Observability → Cost Management → Marketplace

## Key Features

- **Comprehensive Coverage**: Structured sections covering the entire agentic AI landscape
- **Framework Comparison**: Detailed analysis of 14+ major development frameworks
- **Production Focus**: Dedicated Production Best Practices section covering security, observability, cost, deployment, and testing
- **Industry Standards**: Coverage of emerging standards like MCP, A2A, and AGENTS.md
- **Visual Documentation**: 60+ diagrams and architectural references with meaningful naming
- **Research Integration**: Latest academic research and industry white papers
- **Vendor Perspectives**: Multi-cloud and vendor-agnostic approach
- **Community Driven**: Open source with Apache 2.0 license

## Getting Started

### **Quick Start**
1. **Explore the Structure**: Browse the 16-section navigation to understand the scope
2. **Choose Your Path**: Select a learning path based on your role and experience
3. **Start with Concepts**: Begin with foundational concepts if new to agentic AI
4. **Pick a Framework**: Choose a development framework that fits your technology stack

### **For Developers**
- Start with **Agent Development Frameworks** to choose your development approach
- Review **Reference Architecture** for implementation patterns
- Explore **Technology Stack** for platform and tooling decisions

### **For Architects**
- Begin with **Architecture and Design Patterns** for system design
- Review **Production Best Practices & Guidelines** (Security, Observability, Cost Management) for production considerations
- Study **Maturity Models** for organizational readiness assessment

### **For Researchers**
- Dive into **Concepts** and **Reference Architecture** for theoretical foundations
- Explore **Evaluation** frameworks and benchmarks
- Review **Memory Management** and **Context Engineering** for advanced topics

## Contributing

We welcome contributions from the community! This knowledge base is designed to be a living resource that evolves with the rapidly advancing field of agentic AI.

### **How to Contribute**
- **Content Updates**: Submit pull requests for new research, frameworks, or best practices
- **Framework Reviews**: Add analysis of new or updated development frameworks
- **Case Studies**: Share real-world implementation experiences and lessons learned
- **Documentation**: Improve existing content clarity and accuracy

### **Contribution Guidelines**
- Follow the established 16-section structure
- Include proper citations and references
- Maintain vendor-neutral perspective where possible
- Add visual diagrams with meaningful file names

## Disclaimer

*This knowledge base includes images, diagrams, and visual references sourced or adapted from external articles, research papers, vendor documentation, and publicly available materials. All such visuals remain the property of their respective owners and are used for educational, reference, and illustrative purposes only. Where applicable, original sources are cited or referenced, and no claim of ownership is made over third-party content.*

## License

This project is licensed under the Apache License 2.0.

## Acknowledgments

This knowledge base builds upon the incredible work of the open source community, academic researchers, and industry practitioners who continue to advance the field of agentic AI. Special thanks to all contributors and the organizations that have shared their research and insights publicly.

---

**GitHub Repository**: [https://github.com/ankurkumarz/agentic-ai-knowledge-base/](https://github.com/ankurkumarz/agentic-ai-knowledge-base/)

**Documentation Site**: [https://agentic-ai.readthedocs.io](https://agentic-ai.readthedocs.io)