# Gemini Enterprise Agent Platform

## Overview

Gemini Enterprise Agent Platform is Google Cloud's comprehensive platform for building, scaling, governing, and optimizing AI agents in production. Announced in 2025, it is the evolution of Vertex AI — consolidating model selection, model building, and agent building capabilities from Vertex AI with new features for agent integration, DevOps, orchestration, and security. All Vertex AI services and roadmap evolutions are now delivered exclusively through Agent Platform.

The platform provides a single destination for technical teams to build agents that can transform products, services, and operations, with delivery to employees through the Gemini Enterprise app and tight integration with IT operations for control, governance, and security at scale.

## Key Components

![Gemini Enterprise Agent Platform](../assets/images/gemini_enterprise_agent_platform.jpg)
*Source: [Google Cloud - Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)*


### Build

| Component | Description |
|---|---|
| Agent Studio | Low-code, visual interface for building and deploying agents; supports export to ADK for full-code customization |
| Agent Development Kit (ADK) | Code-first framework for building single and multi-agent systems; processes over 6 trillion tokens monthly on Gemini models; now supports graph-based sub-agent networks |
| Agent Garden | Curated library of pre-built agent templates (code modernization, financial analysis, invoice processing, etc.) |
| Model Garden | Access to 200+ models including Gemini 3.1 Pro, Gemini 3.1 Flash Image, Lyria 3, Gemma 4, and third-party models (Anthropic Claude Opus/Sonnet/Haiku) |
| Workspaces | Hardened, sandboxed environments for agents to run bash commands and manage files in isolation |
| Multimodal Streaming | Real-time audio and video support for human-like interactions |

### Scale

| Component | Description |
|---|---|
| Agent Runtime | Re-engineered runtime with sub-second cold starts; supports long-running agents that maintain state for days |
| Memory Bank | Persistent, long-term context storage; Memory Profiles enable high-accuracy recall with low latency |
| Agent Sessions | Session history management with Custom Session IDs mappable to internal databases and CRM records |
| Agent Sandbox | Hardened environment for safely executing model-generated code and browser-based automation |
| Bidirectional Streaming | WebSocket-based protocol for real-time, low-latency audio and video agent interactions |
| Batch & Event-driven Agents | Asynchronous task execution integrated with BigQuery and Pub/Sub |

### Govern

| Component | Description |
|---|---|
| Agent Identity | Assigns every agent a unique cryptographic ID, creating an auditable trail mapped to authorization policies |
| Agent Registry | Central library of approved internal agents, tools, and skills; single source of truth for governed assets |
| Agent Gateway | Unified connectivity layer acting as air traffic control across agent ecosystems; enforces security policies and Model Armor protections against prompt injection and data leakage |
| Agent Anomaly Detection | Statistical models and LLM-as-a-judge framework to flag unusual agent reasoning in real time |
| Agent Threat Detection | Visibility into malicious activity such as reverse shells or connections to known bad IP addresses |
| Agent Security Dashboard | Powered by Security Command Center; maps agent-model relationships, automates asset discovery, and scans for OS and package vulnerabilities |

### Optimize

| Component | Description |
|---|---|
| Agent Simulation | Tests agents against synthetic user interactions and virtualized tools; auto-scores on task success and safety |
| Agent Evaluation | Continuously scores agents against live traffic using multi-turn autoraters that evaluate full conversation logic |
| Agent Observability | Visual tracing of complex agent reasoning for real-time debugging |
| Agent Optimizer | Automatically clusters real-world failures and suggests refined system instructions to improve accuracy |

## Architecture

Agent Platform follows a layered architecture:

- **Agent Runtime Layer** — execution engine, tool integration, state management, and memory systems
- **Platform Services Layer** — model services (Model Garden), data services (BigQuery/Pub/Sub), security services (Agent Identity/Gateway), and monitoring (Agent Observability)
- **Integration Layer** — Native Ecosystem Integrations for plug-and-play connectivity to internal data and tools; support for MCP and A2A protocols; Agent Payment Protocol (AP2) for trusted agent payments

The ADK now supports a graph-based framework for organizing agents into networks of sub-agents, enabling clear, reliable logic for complex multi-agent coordination with both generative and deterministic orchestration patterns.

## Use Cases

- **Customer service**: Multi-agent architectures for personalized troubleshooting and self-service (e.g., Comcast Xfinity Assistant)
- **Healthcare**: End-to-end care delivery with real-time eligibility and scheduling (e.g., Color Health Virtual Cancer Clinic)
- **Financial services**: Autonomous expense management with long-term memory (e.g., Payhawk Financial Controller Agent)
- **Enterprise knowledge**: Turning decades of project data into real-time actionable intelligence (e.g., Burns & McDonnell)
- **Commerce**: Trusted agent-based payment flows (e.g., PayPal AP2 integration)

## Relationship to Vertex AI

Gemini Enterprise Agent Platform is the direct successor to Vertex AI. Key transition points:

- All Vertex AI services are now delivered through Agent Platform — Vertex AI no longer exists as a standalone service
- Existing Vertex AI capabilities (model building, agent building, model selection) are preserved and extended
- The ADK, previously associated with Vertex AI, is now a first-class component of Agent Platform
- Documentation and console access have migrated to the Agent Platform destination in Google Cloud Console

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Agent governance at scale | Managing identity and access across many agents | Use Agent Identity (cryptographic IDs) + Agent Registry as single source of truth |
| Long-running workflows | Agents that need to persist state across days | Deploy via Agent Runtime with Memory Bank and Memory Profiles |
| Security hardening | Preventing prompt injection and data leakage | Route all agent traffic through Agent Gateway with Model Armor enabled |
| Production quality | Catching failures before and after deployment | Combine Agent Simulation (pre-ship) with Agent Evaluation + Agent Optimizer (post-ship) |
| Multi-agent coordination | Reliable orchestration of sub-agent networks | Use ADK's graph-based framework; apply deterministic paths for compliance-critical flows |
| Cost and model flexibility | Avoiding lock-in to a single model | Leverage Model Garden's 200+ models including third-party options |

## See Also

- [Google ADK](../AgenticFrameworks/google-adk.md)
- [Agent Platforms Overview](README.md)
- [AllThingsGoogle](../AllThingsGoogle/README.md)
- [AgentOps / GenOps](../AgentOps/genops.md)
- [Security Frameworks — Google SAIF](../SecurityFrameworks/google-saif.md)
- [Agent Memory — LTM Strategies](../AgentMemory/ltm-strategies.md)
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Production Best Practices — Observability](../ProductionBestPractices/observability.md)

## References

- [Introducing Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) — Google Cloud blog post announcing the platform, its components, and the transition from Vertex AI
