# Microsoft Agent Framework

## Overview

Microsoft Agent Framework is an open-source development kit for building AI agents and multi-agent workflows for .NET and Python. It brings together and extends ideas from Semantic Kernel and AutoGen projects, combining their strengths while adding new capabilities. Built by the same teams, it is the unified foundation for building AI agents going forward.

## High-level Architecture

![Microsoft Agent Framework](../assets/images/frameworks-microsoft-agent-framework.png)

*Source: [Microsoft Agent Framework](https://aka.ms/AgentFrameWork)*

## Key Features

- **Unified open-source framework**: For building, orchestrating, and deploying AI agents and multi-agent workflows in **.NET and Python** environments
- **Combines strengths of Semantic Kernel and AutoGen**: Offering enterprise grade features (thread-based state management, type safety, telemetry, model/embedding support) with intuitive multi-agent patterns
- **AI agents**: That process user inputs with LLMs, call tools and MCP servers, and generate responses; supports providers such as Azure OpenAI and OpenAI
- **Graph-based workflow orchestration**: Enabling complex, multi-step processes with nesting, conditional routing, parallel execution, and human-in-the-loop integration
- **Foundational building blocks**: Such as model clients, context providers (memory), middleware, and agent threads for state and action management
- **Strong developer infrastructure**: With tooling, samples, migration guides (from AutoGen / Semantic Kernel), and community contributions
- **Preview status**: With open feedback and GitHub ecosystem participation for ongoing improvements

## Suitable for (Pros)

- **Teams building enterprise-grade AI agent systems** that need robust state management, telemetry, and type safety
- **Organizations standardizing on .NET or Python** stacks with seamless integration into Azure and Microsoft developer tooling
- **Projects requiring explicit workflow orchestration** with clear execution control and coordinator components
- **Use cases where modularity, reuse, and composability** matter—thanks to graph-based workflows, strong typing, and nested execution
- **Scenarios involving long-running processes or human-in-the-loop interactions**, supported by checkpoints and flexible flow management
- **Developers who want a single unified framework** instead of piecing together multiple agent libraries

## Where other frameworks flare better (Cons)

- **Less cloud-agnostic**: Tighter coupling with Microsoft ecosystems may be suboptimal compared to more neutral or multi-cloud frameworks (e.g., LangGraph, CrewAI) for heterogeneous deployments
- **Still in preview**: Production-critical applications may prefer more mature frameworks with wider community adoption and stability
- **Complexity for simple tasks**: High-level orchestration and strong typing may be overkill for lightweight or quick proof-of-concept agents compared to simpler SDKs
- **Smaller ecosystem**: Emerging community and tooling base relative to long-standing open frameworks like LangChain or standalone agent SDKs with larger contributor networks
- **Azure influence**: While supporting multiple providers, developers seeking full control over model and runtime choices outside Azure/Azure AI may find constraints or extra integration work

## Resources

- **Official Documentation**: [Microsoft Learn - Agent Framework](https://learn.microsoft.com/en-us/agent-framework/)
- **GitHub Repository**: [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- **Overview Video**: [Microsoft Agent Framework Introduction](https://www.youtube.com/watch?v=JlzteydCK_Q)

## See Also
- [Semantic Kernel](semantic-kernel.md)
- [AutoGen](autogen.md)
- [Agent Development Frameworks](README.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)