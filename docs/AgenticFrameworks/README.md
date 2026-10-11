---
type: Framework
title: Agentic Frameworks
description: "> Agentic AI will introduce a goal-driven digital workforce that autonomously makes plans and takes actions — an extension of the workforce that doesn't need vacations or other benefits"
tags: [frameworks, agentic-ai]
timestamp: 2026-07-17T00:00:00Z
---
# Agentic Frameworks

> Agentic AI will introduce a goal-driven digital workforce that autonomously makes plans and takes actions — an extension of the workforce that doesn't need vacations or other benefits.
> 
> -- Gartner

| Framework | Language(s) | License | Key features (short) | Suitable for (pros) | Main cons | GH stars / Deployment model |
|------------|--------------|----------|----------------------|---------------------|-------------|------------------------------|
| [**LangChain**](https://github.com/langchain-ai/langchain) | Python, TypeScript | MIT | De-facto standard, broad vendor & vector DB integrations, large ecosystem | Enterprise GenAI building blocks; wide community & vendor compatibility | Complex architecture, steep learning curve, maintenance overhead | ~98K / Self-hosted |
| [**LangGraph**](https://github.com/langchain-ai/langgraph) | Python, TypeScript | MIT | Graph-based stateful workflows, multi-agent, native LangChain integration, observability (LangSmith) | Enterprise multi-agent orchestration; LangChain ecosystem apps | Commercial features behind paid tier; dependency complexity | ~8K / SaaS & Self-hosted |
| [**CrewAI**](https://github.com/joaomdmoura/crewAI) | Python | MIT | Multi-agent workflows, wide LLM support, cloud integration, user-friendly UI | Fast time-to-market; lightweight agent creation for business use cases | Limited enterprise testing; vendor/dependency risks | ~25K / SaaS or Self-hosted |
| [**Autogen**](https://github.com/microsoft/autogen) | Python (multi-language) | MIT | Microsoft multi-agent conversational framework, async messaging, observability | Microsoft ecosystem alignment; prototyping with Autogen Studio | Experimental; limited production maturity | ~38K / Self-hosted |
| [**Semantic Kernel**](https://github.com/microsoft/semantic-kernel) | Python, C#, Java | MIT | Production-ready SDK, multi-language, built-in agent/process frameworks | Enterprise production agents; Azure integration; multi-language SDKs | Vendor dependency; evolving agent features | – / SDK (enterprise) |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Python, TypeScript | MIT | Data-centric indexing framework, connectors, document parsing, modular design | Data-intensive LLM apps, knowledge-heavy systems, rapid TTM | Less focus on agent decision-making; evolving agentic features | ~38K / SaaS & Self-hosted |
| [**AutoGPT**](https://github.com/Significant-Gravitas/AutoGPT) | Python | MIT | Low-code/no-code autonomous agents, multi-LLM support, continuous agents | Quick prototyping, simple autonomous workflows | Waitlists/cloud limits, community fragmentation | ~171K / SaaS & Self-hosted |
| [**PydanticAI**](https://github.com/pydantic/pydantic-ai) | Python | MIT | Type-safe FastAPI-style framework, strong typing, DI, observability | Type-safe FastAPI-aligned projects and quick prototypes | Early stage, limited production usage | – / Early-stage framework |
| [**Spring AI**](https://github.com/spring-projects/spring-ai) | Java / Spring | MIT | LangChain-inspired; native Spring integration, async processing, RAG & Advisors API | Java/Spring enterprise applications, system integration | Newer framework; limited complex-scenario testing | – / Self-hosted (Spring) |
| [**Haystack**](https://github.com/deepset-ai/haystack) | Python | MIT | Production-ready RAG/search pipelines, modular, Hugging Face & Elasticsearch integration | Cross-cloud RAG pipelines, production deployments, LLMOps | Limited multi-agent testing; complex setup | – / Self-hosted & deepsetCloud |
| [**Agno**](https://github.com/agno-agi/agno) | Python | MPL-2.0 | Full-stack multi-agent system: memory, knowledge, reasoning, UI; ~2μs agent creation, ~3.75 KiB per agent | Privacy-first and scalable; agent teams & composable workflows; high-performance high-volume operations | Newer ecosystem; limited production proof | ~34K / Self-hosted |
| [**Mastra**](https://mastra.ai) | TypeScript | Apache-2.0 | TypeScript-first multi-agent framework; graph-based state machines; integrates with existing REST APIs and web services | Web applications and TypeScript projects; workflow-centric hybrid architectures | Newer framework; TypeScript-only | – / Self-hosted |
| [**Microsoft Agent Framework**](https://github.com/microsoft/agent-framework) | .NET, Python | MIT | Unified SDK for orchestrating AI agents & workflows across .NET/Python | Enterprise production-ready; Microsoft ecosystem integration | Still early-stage; ecosystem tied to Microsoft stack | – / Self-hosted & Azure |
| [**Strands Agents**](https://strandsagents.com/latest/) | Python | Apache-2.0 | Lightweight agent SDK, model-driven, supports workflows & tools | Simple to use; good for orchestration & agent collaboration | Smaller community; limited advanced tooling | – / Self-hosted |
| [**Google ADK (Agent Development Kit)**](https://google.github.io/adk-docs/) | Python, Java | Open Source | Modular, model-agnostic agent framework optimized for multi-agent systems | Platform-agnostic; ideal for enterprise or academic adaptation | GCP-heavy; evolving documentation | – / Self-hosted & Cloud |
| [**OpenAI AgentKit**](https://openai.com/index/introducing-agentkit/) | Various (JS/Python via API) | Proprietary / Mixed | Visual builder, agent orchestration, evaluation, UI embedding | Rapid prototyping; integrated with OpenAI ecosystem | Vendor lock-in; limited low-level control | – / SaaS & Self-hosted |
| [**Flue**](https://flueframework.com/) | TypeScript | Apache-2.0 | Harness-first agent framework; built-in virtual sandbox (just-bash) + container sandbox (Daytona); sessions, skills, MCP, OpenTelemetry | Headless programmable agents; runtime-agnostic deploy (Node, Cloudflare, CI); harness-centric design | TypeScript-only; experimental; smaller ecosystem | ~3.8K / Self-hosted |
| [**Eve**](https://github.com/vercel/eve) | Filesystem-defined (markdown + tools) | Open Source | Filesystem-first agent framework; `instructions.md` defines the agent, tools auto-registered from `tools/`; built-in durable execution, sandboxed compute, approvals, channels, tracing, evals | Teams wanting file-based, diffable agent definitions; durable/resumable runs and HITL approvals out of the box | Public preview; API surface may change; strongest tooling fit is Vercel-hosted deployments | – / Public preview |
| [**FleetQ**](https://github.com/fleetq/fleetq) | TypeScript / Python | AGPLv3 | Visual DAG builder for multi-agent orchestration; 675+ MCP tools; supports "crews", workflows, and process types; human-in-the-loop approvals; full audit trail; mission-control UI | Teams wanting visual multi-agent mission control with MCP tool ecosystem and HITL approvals | AGPLv3 license (copyleft); newer ecosystem; community edition only | – / Self-hosted |
| [**Open Multi-Agent**](https://github.com/open-multi-agent/open-multi-agent) | TypeScript | MIT | Runtime DAG planning with approval gates, tracing, evaluation, checkpoints, and resume; requires Node 20+ | JS/TS shops wanting multi-agent orchestration in the same stack as their web apps; durability and resumability first-class | TypeScript-only; org semantics (teams, roles) are application-defined; smaller community | – / Self-hosted |
| [**Auto-Company**](https://github.com/auto-company/auto-company) | Python | MIT | Fully autonomous multi-agent "company" on a single PC; agents collaborate autonomously without human approval; built-in persistence | Experimental local dark-factory; lab setups and autonomous ops experiments | Experimental; minimal governance; not production-ready | – / Self-hosted (local) |
| [**SmythOS**](https://smythos.com/) | Python / TypeScript | MIT | Open agent OS: Runtime, CLI, SDK, and visual Studio are all OSS; cloud-native; orchestrates agents with tools, memory, workflows; open MCP | Teams wanting a general agent OS to embed under a custom control plane or product UI; extensible and brandable | Org/governance patterns are application-defined; cloud-native focus may add infra overhead for fully local deploys | – / Self-hosted & Cloud |
| [**Open Polsia**](https://github.com/PolsiaAI/Polsia) | Python (FastAPI) + TypeScript (Next.js 14) | OSS | Nine specialised agents (orchestrator/CEO, coding, marketing, sales outreach, support, finance, planning, competitor research, social) on staggered schedules; each agent calls Claude Code CLI (`claude -p ... --output-format json`) as a subprocess; PostgreSQL 16 (15 tables), Redis + Celery task queue, ChromaDB vector memory; SANDBOX_MODE for safe testing | Reference implementation of a fully autonomous multi-agent company; good for forking and experimentation; powered by Claude Code CLI in headless mode | Requires Claude Code CLI authenticated via OAuth; experimental; not designed as a production SaaS foundation; commercial hosted variant (Polsia SaaS) is separate | – / Self-hosted (Docker Compose) |



## LangChain

### High-level Architecture

![LangChain Stack](https://vedcraft.com/wp-content/uploads/2025/01/langchain_stack.png)

### Key Features
* De facto standard for building AI Apps with 1M+ builders and ~100K GitHub Stars
* Comprehensive vendor integration and cloud-vendor support
* Extensive third-party libraries integration
* Support for diverse vector databases
* Wide community knowledge and developer awareness

### Suitable for (Pros)
* Enterprise development with wider adoption as standard
* Building foundational blocks of enterprise GenAI applications
* Creating enterprise-specific frameworks
* Projects requiring third-party vendor compatibility
* Applications needing extensive community support

### Where other frameworks flare better (Cons)
* Complex architecture with steep learning curve
* Too many integrations leading to code complexity
* Continuous features/changes requiring frequent updates
* Possibility of breaking changes and incompatible libraries
* Maintenance overhead due to extensive ecosystem

## LangGraph

### High-level Architecture

![LangGraph Platform Architecture](https://vedcraft.com/wp-content/uploads/2025/01/lg_platform-1024x571.png)

*Source: [LangGraph Platform Architecture](https://langchain-ai.github.io)*

### Key Features
* Open-source framework from LangChain team
* Commercial solution for production deployment
* Stateful design with graph-based workflow
* Multi-agent capabilities
* Native integration with LangChain
* Enhanced observability with LangSmith
* IDE support and community backing

### Suitable for (Pros)
* Enterprise multi-agent framework development
* Projects requiring wide compatibility
* Integration with different solutions/products
* LangChain ecosystem applications
* Complex workflow orchestration

### Where other frameworks flare better (Cons)
* Enterprise features limited to commercial version
* Complex dependency management
* Framework complexity challenges
* Steep learning curve
* Limited features in open-source version

## CrewAI

### High-level Architecture

![Platform Architecture](https://vedcraft.com/wp-content/uploads/2025/01/crewAI-mindmap-1024x702.png)
Source: CrewAI Documentation

### Key Features
* Multi-agent framework capabilities
* Workflow-based applications
* Wide LLM support
* Cloud provider integration
* Structured workflow design
* User-friendly interface
* Strong community backing

### Suitable for (Pros)
* Fast-growing AI ecosystem
* Quick time-to-market needs
* Lightweight agent creation
* Marketing agent development
* Business-friendly implementations

### Where other frameworks flare better (Cons)
* Limited enterprise testing
* Complex scenario handling
* Vendor dependency concerns
* Potential acquisition risks
* Data integration challenges

## Autogen

### High-level Architecture

![Microsoft AutoGen Architecture](https://vedcraft.com/wp-content/uploads/2025/01/autogen.png)

*Source: [Microsoft Research Documentation](https://aka.ms/autogen)*

### Key Features
* Microsoft-developed programming framework
* Multi-agent conversation framework
* Asynchronous messaging capabilities
* Modular and extensible architecture
* Built-in observability and debugging
* Cross-language support
* Full-type support system

### Suitable for (Pros)
* Microsoft ecosystem alignment
* Open-source development projects
* Wide range of application domains
* Prototyping with Autogen studio UI
* Complex agent interactions research

### Where other frameworks flare better (Cons)
* Still in experimental phase
* Not fully production-ready
* Microsoft solution dependency
* Complex enterprise setup
* Limited production use cases

## Semantic Kernel

### High-level Architecture

![Semantic Kernel Architecture](https://vedcraft.com/wp-content/uploads/2025/01/sematic-kernel-v1-1024x482.png)

*Source: [Microsoft Documentation](https://learn.microsoft.com/semantic-kernel)*

### Key Features
* Production-ready SDK for LLM integration
* Multi-language support (C#, Python, Java)
* Built-in Agent and Process Frameworks
* Strong enterprise integration capabilities
* AI agent creation platform
* Business process optimization tools

### Suitable for (Pros)
* Production environment AI agents
* Multi-language SDK requirements
* Microsoft Azure environment integration
* Enterprise-level support needs
* Structured development approaches

### Where other frameworks flare better (Cons)
* Limited to SDK functionality
* Evolving agent framework
* Microsoft vendor dependency
* Java agent limitations
* Complex setup requirements

## LlamaIndex

### High-level Architecture

![Architecture](https://vedcraft.com/wp-content/uploads/2025/01/LlamaIndex-Arch.png)

Source: LlamaIndex Framework

### Key Features
* Advanced data framework capabilities
* AI agents and document parsing
* Workflow and connector-based integration
* Modular and extensible architecture
* LlamaCloud SaaS offering
* LlamaParse for data transformation
* Centralized LlamaHub for resources

### Suitable for (Pros)
* Data-intensive LLM applications
* Complex document parsing needs
* Quick time-to-market requirements
* Knowledge-intensive AI systems
* Chatbots and QA systems

### Where other frameworks flare better (Cons)
* Limited complex agent behaviors
* Focus mainly on data indexing
* Less decision-making capabilities
* Evolving agentic features
* Limited enterprise integration

## AutoGPT

### High-level Architecture

![Architecture](https://vedcraft.com/wp-content/uploads/2025/01/autogpt.drawio.png)

*AutoGPT Platform Components*

### Key Features
* Multiple LLM support (OpenAI, Anthropic, Groq, Llama)
* Seamless integration capabilities
* Low-code workflows
* Autonomous operation
* Continuous agents
* Intelligent automation
* Reliable performance metrics

### Suitable for (Pros)
* No-code/low-code development
* Cloud-based agent building
* Automated workflow creation
* Quick prototype development
* Simple agent deployments

### Where other frameworks flare better (Cons)
* Vendor lock-in concerns
* Complex licensing structure
* Limited LLM support
* Waitlist-based cloud hosting
* Community support challenges

## PydanticAI

### High-level Architecture

![Architecture](https://vedcraft.com/wp-content/uploads/2025/01/pydantic.drawio.png)

*PydanticAI Components*

### Key Features
* FastAPI-style development
* Pydantic Logfire integration
* Multiple LLM support
* Real-time observability
* Type-safety features
* Graph support
* Dependency injection

### Suitable for (Pros)
* Pydantic/FastAPI aligned projects
* Simple framework requirements
* Type-safe development needs
* Basic scenario implementation
* Quick prototyping

### Where other frameworks flare better (Cons)
* Beta stage development
* Frequent framework changes
* Limited production testing
* Early stage ecosystem
* Complex integration challenges

## Spring AI

### High-level Architecture

![Architecture](https://vedcraft.com/wp-content/uploads/2025/01/spring-ai-agentic-systems-1024x677.jpg)

Source: Spring AI Documentation

### Key Features
* LangChain-inspired architecture
* Spring ecosystem integration
* Multiple LLM support
* Built-in observability
* Model evaluation tools
* Advisors API for patterns
* RAG capabilities
* Chat conversation support

### Suitable for (Pros)
* Spring ecosystem projects
* Java-based enterprise applications
* Seamless Spring integration
* System integration needs
* Asynchronous processing requirements
* Data connectivity projects

### Where other frameworks flare better (Cons)
* Relatively new framework
* Limited complex scenario testing
* Early stage development
* Feature comparison gaps
* Limited community resources

## Haystack

### High-level Architecture

![Haystack Architecture](https://vedcraft.com/wp-content/uploads/2025/01/haystack-768x462.png)

*Source: [Haystack Documentation](https://haystack.ai)*

### Key Features
* Production-ready LLM framework
* RAG pipeline support
* Complex search capabilities
* Modular architecture
* OpenAI/Chroma integration
* Hugging Face compatibility
* Elasticsearch support
* deepsetCloud platform

### Suitable for (Pros)
* Cross-cloud LLM applications
* Custom RAG pipelines
* Jinja template integration
* Free development environment
* LLMOps capabilities
* Production deployments

### Where other frameworks flare better (Cons)
* Limited multi-agent testing
* Unclear roadmap visibility
* Battle-testing needed
* Complex setup requirements
* Integration challenges

## Other Frameworks/Platforms

* **[Strands](https://strandsagents.com/)**: An open-source agent framework & SDK launched by **AWS** on [July 25](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) promoting model-driven approach to building and running AI agents .
* **[Google ADK](https://google.github.io/adk-docs/)**: Launched by **Google** on [Apr 25](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/) (with a focus on multi-agent apps) as a modular framework for developing and deploying AI agents, particularly optimized for Gemini and the Google ecosystem.
* **[OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents)**: The OpenAI Agents SDK to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, Swarm.
* **[Dapr Agents](https://www.cncf.io/blog/2025/03/12/announcing-dapr-ai-agents/)**
* **OpenAI Swarm**: Educational framework for lightweight multi-agent orchestration
* **MetaGPT**: Research-based multi-agent framework promoting meta-programming
* **Flowise**: Open-source drag-and-drop UI for agent building
* **Langflow**: DataStax-acquired framework for interactive GenAI apps
* **[OpenAGI](https://openagi.aiplanet.com/)**: Simple framework, built by AI Planet, for building human-like agents
* **[Camel-AI.org](http://camel-ai.org/)**: Research-inspired customizable multi-agent framework inspired by the [CAMEL research paper](https://arxiv.org/abs/2303.17760)
* **PraisonAI**: a production-ready Multi AI Agents framework, designed to create AI Agents to automate and solve problems ranging from simple tasks to complex tasks.
* **[BroadAI](https://broad-ai.github.io)**: A Multi-Agent Framework for building powerful & intelligent AI Systems
* **[Vellum](https://www.vellum.ai/)**: A platform with products for Orchestration, Evaluation, Prompting, Retrieval, and Deployment - as a GUI tool for building and testing complex workflows.
* **[Rivet](https://rivet.ironcladapp.com/)**: a drag and drop GUI LLM workflow builder
* **Solace Agent Mesh**: Event-driven multi-agent framework built on the Solace messaging platform
* **Akka Agent Platform**: Distributed agent platform built on the Akka actor model
* **[Swarms AI](https://www.swarms.ai/)**: Choose from multiple swarm architectures to build sophisticated Enterprise AI systems
* **[IBM Granite BeeAI](https://iambee.ai/)**: Build production-ready AI agents in both Python and Typescript
* **[MetaGPT](https://github.com/geekan/MetaGPT)**: The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming
* **[FreePHDLabor](freephdlabor.md)**: Open-source, customizable multiagent framework (built on smolagents) that automates the scientific research lifecycle — hypothesis generation, experimentation, and LaTeX manuscript writing — via a ManagerAgent orchestrating specialized IdeationAgent, ExperimentationAgent, WriteupAgent, ReviewerAgent, and ProofreadingAgent roles

## Agent Company Platforms & Autonomous Systems

Frameworks and reference implementations specifically designed to model a multi-agent system as a company or autonomous organisation. For managed SaaS counterparts, see [Agent Workforce SaaS Platforms](../AgentPlatforms/agent-workforce-saas.md) and the full [Agent Company Platforms Comparison](../AgentPlatforms/agent-company-platforms.md).

* **[FleetQ](https://github.com/fleetq/fleetq)** (AGPLv3): Visual DAG builder for multi-agent orchestration with 675+ MCP tools, human-in-the-loop approvals, full audit trail, and a mission-control UI. Closest to Paperclip-style mission control but with visual DAGs and a richer MCP tool ecosystem. Community Edition is fully open source.
* **[Open Multi-Agent](https://github.com/open-multi-agent/open-multi-agent)** (MIT, TypeScript, Node 20+): Plans task DAGs at runtime with approval gates, tracing, evaluation, checkpoints, and resume. Focused on durability and composability in TypeScript stacks; org semantics (teams, roles) are application-defined.
* **[Auto-Company](https://github.com/auto-company/auto-company)** (MIT): Experimental open-source project that runs a fully autonomous multi-agent company on a single PC. Agents collaborate autonomously to operate like a company. Useful as a reference for dark-factory patterns; not production-ready.
* **[SmythOS Runtime](https://smythos.com/)** (MIT): Open agent OS — Runtime, CLI, SDK, and visual Studio are all open source. Cloud-native; orchestrates agents with tools, memory, and workflows. Positioned as a general agent OS that teams can embed under their own control plane or product UI.
* **[Open Polsia](https://github.com/PolsiaAI/Polsia)** (OSS): Open-source reference implementation of an autonomous multi-agent company. Nine specialised agents (orchestrator/CEO, coding, marketing, sales outreach, support, finance, planning, competitor research, social) run on staggered schedules via Celery Beat. Each agent calls Claude Code CLI (`claude -p "..." --output-format json`) as a subprocess. Stack: FastAPI + Next.js 14, PostgreSQL 16 (15 tables), Redis + Celery task queue, ChromaDB vector memory, nginx reverse proxy. SANDBOX_MODE=true prevents real posts/emails/charges during testing. CI mocks the CLI with `CLAUDE_CLI_MOCK=true`. The commercial hosted variant (Polsia SaaS) is a separate product.

## Additional Resources

### Large Foundation Models for Enterprises
* **[Liquid AI](https://www.liquid.ai/)**: LFMs (Liquid Foundation Models) for Enterprises

## Comparative Analysis

| Key Attributes | LangChain | LangGraph | Autogen | Semantic Kernel | LlamaIndex | AutoGPT | CrewAI |
|---------------|-----------|-----------|---------|-----------------|------------|----------|---------|
| License | MIT | MIT | MIT | MIT | MIT | MIT | MIT |
| Open-source | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Developed by | LangChain | LangChain | Microsoft | Microsoft | LlamaIndex | Significant Gravitas | CrewAI |
| GitHub Stars (Jan '25) | 98K | 8K | 38K | - | 38K | 171K | 25K |
| Used By (GH Public Repos) | 170K | 10K | 3K | - | 16K | N/A | 7K |
| Language | Python, TypeScript | Python, TypeScript | Python, C# | Python, C#, Java | Python, TypeScript | Python | Python |
| Enterprise Support | Yes | Yes | Yes | - | Yes | Yes | Yes |
| Deployment Model | Self-hosted | SaaS & Self-hosted | Self-hosted | - | SaaS & Self-hosted | SaaS & Self-hosted | SaaS & Self-hosted |


## See Also

- [Agent Company Platforms — Comparison Guide](../AgentPlatforms/agent-company-platforms.md)
- [Agent Workforce SaaS Platforms](../AgentPlatforms/agent-workforce-saas.md)
- [Paperclip](../AgentPlatforms/paperclip.md)
- [Multi-Agent System Architecture](../Architecture/multi-agent-system.md)
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md)
- [Popular AI Agents](../AgentPlatforms/README.md)
