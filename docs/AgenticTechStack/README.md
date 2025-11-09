
## Agent Frameworks

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
| [**Agno**](https://github.com/agno-agi/agno) | Python | MPL-2.0 | Full-stack multi-agent system: memory, knowledge, reasoning, UI | Privacy-first and scalable; agent teams & composable workflows | Newer ecosystem; limited production proof | ~34K / Self-hosted |
| [**Microsoft Agent Framework**](https://github.com/microsoft/agent-framework) | .NET, Python | MIT | Unified SDK for orchestrating AI agents & workflows across .NET/Python | Enterprise production-ready; Microsoft ecosystem integration | Still early-stage; ecosystem tied to Microsoft stack | – / Self-hosted & Azure |
| [**Strands Agents**](https://strandsagents.com/latest/) | Python | Apache-2.0 | Lightweight agent SDK, model-driven, supports workflows & tools | Simple to use; good for orchestration & agent collaboration | Smaller community; limited advanced tooling | – / Self-hosted |
| [**Google ADK (Agent Development Kit)**](https://google.github.io/adk-docs/) | Python, Java | Open Source | Modular, model-agnostic agent framework optimized for multi-agent systems | Platform-agnostic; ideal for enterprise or academic adaptation | GCP-heavy; evolving documentation | – / Self-hosted & Cloud |
| [**OpenAI AgentKit**](https://openai.com/index/introducing-agentkit/) | Various (JS/Python via API) | Proprietary / Mixed | Visual builder, agent orchestration, evaluation, UI embedding | Rapid prototyping; integrated with OpenAI ecosystem | Vendor lock-in; limited low-level control | – / SaaS & Self-hosted |


## AI Agents Landscape

![AI Agents Tech Landscape](https://i.postimg.cc/yYDbhVHq/ai-agent-stack-2024.png)
Ref: https://www.letta.com/blog/ai-agents-stack
