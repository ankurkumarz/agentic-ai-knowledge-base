# AWS Strands Agents

## Overview

AWS Strands Agents is an open-source multi-agent framework for building AI Agents. AWS launched Strands Agents as a model-driven, autonomous agent framework that leverages foundation models for planning, reasoning, tool selection, and execution.

## High-level Architecture

![Strands Agentic Loop](../assets/images/frameworks-strands-agentic-loop.png)

*Source: [Strands Agents](https://strandsagents.com/)*

## Key Features

- **Model-driven, autonomous agent loop**: Leverages a foundation model for planning, reasoning, tool selection, and execution
- **Lightweight, code-first SDK**: With simple Python/TypeScript APIs for agent creation and execution
- **Model and provider agnostic**: Supports Amazon Bedrock, OpenAI, Anthropic, Llama, and other providers via flexible interfaces
- **Native AWS ecosystem integration**: (e.g., AWS Lambda, Step Functions, EC2/EKS) for seamless workflows and deployment
- **Tooling support via Model Context Protocol (MCP)**: Enabling standardized connection to external tools and resources
- **Multi-agent coordination primitives**: Including agents-as-tools, swarms, graphs, and meta-agents for complex workflows
- **Production-ready observability**: With OpenTelemetry support for tracing, logging, and metrics
- **Flexible deployment targets**: From local development to cloud production environments

## Suitable for (Pros)

- **Ideal for AWS-centric development teams** seeking deep integration with cloud services and infrastructure
- **Excellent choice for enterprise use cases** requiring security, compliance, and controlled deployment patterns
- **Strong option for autonomous agent workflows** that need flexible model selection across providers
- **Simplifies production readiness** with observability and telemetry built into the SDK
- **Supports multi-modal interactions** and collaboration between agents for complex problem solving
- **Offers scalable deployment paths** (Lambda, Fargate, EC2/EKS, containerized environments)

## Where other frameworks flare better (Cons)

- **AWS ecosystem focus** can feel restrictive if you want a truly cloud-agnostic or hybrid environment; other frameworks like LangGraph or AutoGen may be more neutral
- **Model-first autonomous loop** may introduce non-determinism that complicates debugging and reproducibility compared to frameworks with explicit orchestration logic
- **Newer ecosystem** with a smaller community and tooling ecosystem compared to mature open frameworks like LangChain or CrewAI
- **Potential for higher development costs and complexity** early on due to model-driven reasoning and reliance on LLM loops

## Resources

- **Official Website**: [strandsagents.com](https://strandsagents.com)
- **AWS Blog**: [Introducing Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/)
- **GitHub Samples**: [Strands Agents Samples](https://github.com/strands-agents/samples/)
- **Code Samples and Labs**: [Personal Finance Assistant Lab](https://github.com/strands-agents/samples/blob/main/02-samples/11-personal-finance-assistant/lab1-foundations.ipynb)

## See Also
- [Agent Development Frameworks](README.md)
- [AWS AgentCore](../AgentPlatforms/aws-agentcore.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)