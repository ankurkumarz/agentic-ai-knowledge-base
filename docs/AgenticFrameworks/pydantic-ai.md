# PydanticAI

## Overview

[PydanticAI](https://ai.pydantic.dev/) is built by the Pydantic team to bring that FastAPI feeling to GenAI app development. It integrates with [Pydantic Logfire](https://pydantic.dev/logfire) for GenAI application observability along with support for multiple LLMs and ecosystem support.

## High-level Architecture

![PydanticAI Components](../assets/images/frameworks-pydantic-ai-architecture.png)

*PydanticAI Components*

## Key Features

- **Pydantic approach**: Familiar, type-safe development experience aligned with the Pydantic ecosystem
- **Model agnostic implementation**: Supports multiple LLMs without vendor lock-in
- **Real-time observability**: Integration with Pydantic Logfire for monitoring and tracing
- **Type-safety**: Strong typing throughout the framework for safer development
- **Graph support**: Graph-based workflows via [Pydantic Graph](https://ai.pydantic.dev/graph/)
- **Dependency injection**: Built-in DI for clean, testable agent code
- **Simplicity**: Minimal abstractions, easy to learn and use

## Suitable for (Pros)

- **Applications leveraging Pydantic and FastAPI approach** and looking for a simple framework aligned with associated enterprise technology stack
- **Type-safe development**: Ideal for teams that prioritize strong typing and validation
- **Simple scenarios**: Well-suited as the framework is still evolving

## Where other frameworks flare better (Cons)

- **This framework is still in the early stages (beta)** and is expected to introduce many changes as it progresses
- **Limited production testing**: Not yet widely battle-tested in large enterprise deployments
- **Evolving ecosystem**: Smaller community and tooling compared to mature frameworks like LangChain

## Resources

- **Official Documentation**: [PydanticAI](https://ai.pydantic.dev/)
- **Pydantic Logfire**: [Observability platform](https://pydantic.dev/logfire)
- **Pydantic Graph**: [Graph support](https://ai.pydantic.dev/graph/)

## See Also
- [Agent Development Frameworks](README.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [LangChain](langchain.md)
