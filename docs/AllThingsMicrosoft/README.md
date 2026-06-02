# Microsoft — Agentic AI Overview

## Overview

Microsoft's agentic AI strategy centres on Azure AI services, the open-source Semantic Kernel SDK, and the AutoGen multi-agent framework. Integration with Microsoft 365, GitHub Copilot, and the broader Azure ecosystem makes Microsoft a strong choice for enterprise agent deployment.

## Key Offerings

| Product / Area | One-liner | Wiki Reference |
|---|---|---|
| Microsoft Agent Framework | Microsoft's opinionated framework for building production-grade agents on Azure | [AgenticFrameworks/microsoft-framework.md](../AgenticFrameworks/microsoft-framework.md) |
| Semantic Kernel | Open-source SDK for integrating LLMs into .NET, Python, and Java applications | [AgenticFrameworks/semantic-kernel.md](../AgenticFrameworks/semantic-kernel.md) |
| AutoGen | Microsoft Research framework for multi-agent conversation and orchestration | [AgenticFrameworks/autogen.md](../AgenticFrameworks/autogen.md) |
| Azure AI Agent Service | Managed Azure platform for deploying, running, and monitoring agents | [AgentPlatforms/microsoft-azure.md](../AgentPlatforms/microsoft-azure.md) |
| Azure AI Foundry Agent Service | Developer-grade managed runtime with Entra identity, private networking, multi-framework SDK (LangGraph, Claude, OpenAI), scale-to-zero | [AgentPlatforms/enterprise-platforms-2026.md](../AgentPlatforms/enterprise-platforms-2026.md) |
| Microsoft Copilot Studio | Low-code agent builder for M365/Teams; 160,000 organizations, 400,000+ custom agents (May 2026) | [AgentPlatforms/enterprise-platforms-2026.md](../AgentPlatforms/enterprise-platforms-2026.md) |
| Agent Governance Toolkit | MIT-licensed runtime governance: deterministic policy enforcement (YAML/Rego/Cedar), zero-trust identity (Ed25519 + ML-DSA-65), execution rings, MCP security gateway; covers all 10 OWASP Agentic risks | [SecurityFrameworks/agent-governance-toolkit.md](../SecurityFrameworks/agent-governance-toolkit.md) |
| Azure Skills Repository | Official GitHub repository of ready-made skills targeting Azure AI Agent Service and Semantic Kernel toolchains | [Standards/skills.md#provider-skills-repositories](../Standards/skills.md) |
| SkillOpt | Text-space optimizer that trains reusable natural-language skill documents for frozen LLM agents; 52/52 benchmark wins without weight updates | [PromptEngineering/skillopt.md](../PromptEngineering/skillopt.md) |
| AgentPex | Open-source (MIT) agent evaluation tool that imports execution traces, extracts specs from system prompts and tool schemas, and scores behavior using 8 LLM-based evaluation techniques; integrates with Langfuse and Langtrace | [EvaluationFrameworks/llm-frameworks.md](../EvaluationFrameworks/llm-frameworks.md) |

## See Also

- [Agent Platforms Overview](../AgentPlatforms/README.md)
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)
- [Multi-agent System Architecture](../Architecture/multi-agent-system.md)
