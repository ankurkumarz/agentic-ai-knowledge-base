# Mastra

## Overview

Mastra is a TypeScript-first multi-agent framework designed to bring multi-agent systems to web developers. It provides LLM-powered agents with tools, workflows, and synced data, integrating directly with existing REST APIs and web services without requiring a separate AI infrastructure.

## Key Features

- **TypeScript-first design**: Native TypeScript integration; agents run alongside existing web applications
- **Graph-based state machines**: Orchestrates complex sequences of AI operations through graph-based workflows
- **Existing API integration**: Agents call existing functions, third-party APIs, and knowledge bases without data synchronization overhead
- **Workflow-centric architecture**: Business logic takes precedence over pure agent autonomy
- **No separate AI infrastructure**: Runs within existing web application stacks

## Architecture

Mastra is optimized for **workflow-centric hybrid architectures** where business logic matters more than pure agent autonomy. The framework provides graph-based state machines that orchestrate complex sequences of AI operations while maintaining tight integration with web services and APIs already in use.

### Example: E-Commerce Platform

A typical Mastra deployment for an e-commerce platform:
- **Product agent**: queries existing inventory API
- **Recommendation agent**: calls existing ML models
- **Order agent**: integrates with existing checkout system

All agents run in TypeScript alongside the existing web application, eliminating the need to manage separate AI infrastructure or worry about data synchronization between systems.

## Suitable For (Pros)

- Web applications and TypeScript projects
- Teams with existing REST API infrastructure
- Workflow-centric hybrid architectures
- Organizations that want to avoid separate AI infrastructure
- Projects where business logic and existing integrations are the primary concern

## Limitations (Cons)

- TypeScript-only — not suitable for Python-first teams
- Newer framework with limited production proof points compared to LangGraph or CrewAI
- Less suited for pure agent autonomy use cases

## Comparison with Similar Frameworks

| Dimension | Mastra | LangGraph | CrewAI |
|---|---|---|---|
| Language | TypeScript | Python/TypeScript | Python |
| Primary pattern | Workflow-centric hybrid | Graph-based state management | Role-based centralized |
| Integration style | Existing REST APIs | Custom state transitions | Predefined agent personas |
| Best for | Web apps with existing APIs | Complex stateful workflows | Role-based collaboration |

## See Also

- [Agentic Frameworks Overview](./README.md)
- [LangGraph](./langgraph.md)
- [CrewAI](./crewai.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)

## References

- [Mastra Documentation](https://mastra.ai) — Official framework documentation
- [Mastering Multi-Agent Systems eBook](https://galileo.ai) — Galileo, 2026. Chapter 3 covers Mastra's role in multi-agent architecture selection.
