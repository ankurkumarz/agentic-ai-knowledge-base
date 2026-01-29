# Semantic Kernel

## Overview

Semantic Kernel (by Microsoft) is designed for creating stable, enterprise-ready applications with strong integration capabilities. As per Microsoft, Semantic Kernel is a production-ready SDK that integrates large language models (LLMs) and data stores into applications, enabling the creation of product-scale GenAI solutions.

## High-level Architecture

![Semantic Kernel Architecture](../assets/images/frameworks-semantic-kernel-architecture.png)

*Source: [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel)*

## Key Features

- **Production-ready SDK**: Integrates large language models (LLMs) and data stores into applications, enabling the creation of product-scale GenAI solutions
- **Multi-language support**: Supports multiple programming languages: C#, Python, and Java
- **Agent and Process Frameworks**: Has Agent and Process Frameworks in preview, enabling customers to build single-agent and multi-agent solutions
- **Semantic Kernel Agent Framework**: Provides a platform within the Semantic Kernel ecosystem that allows for the creation of AI agents and the ability to incorporate agentic patterns into any application
- **Semantic Kernel Process Framework**: Provides an approach to optimize AI integration with your business processes
- **Enterprise integration**: Strong integration capabilities with existing enterprise systems
- **Stable and reliable**: Designed for production environments with enterprise-level support

## Suitable for (Pros)

- **If you need to build a reliable AI agent** for a production environment with strong enterprise-level support and integration with existing systems
- **When SDKs are needed in multiple languages** as Semantic Kernel supports Python, C#, .NET, and Java
- **Developer training support** with enterprise support is available, particularly in the Microsoft Azure environment
- **Production-ready applications**: Ideal for stable, enterprise-ready applications
- **Strong integration requirements**: Excellent for applications requiring deep integration with existing enterprise systems

## Where other frameworks flare better (Cons)

- **Semantic Kernel falls into the category of SDK** whereas the competitive frameworks provide higher-level abstractions and user interfaces for simpler agents
- **Agent framework is still evolving** (Agents are currently not available for Java)
- **When vendor dependency on Microsoft needs to be avoided**, other options can be considered as per the context
- **Lower-level abstraction**: May require more development effort compared to higher-level frameworks

## Resources

- **Official Documentation**: [Microsoft Learn - Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- **Training Course**: [Develop AI agents with Azure OpenAI and Semantic Kernel SDK](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure-open-ai-semantic-kernel-sdk/)
- **GitHub Repository**: [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel)

## See Also
- [Microsoft Agent Framework](microsoft-framework.md)
- [AutoGen](autogen.md)
- [Agent Development Frameworks](README.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)