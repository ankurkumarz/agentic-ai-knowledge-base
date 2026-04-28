# Production Best Practices & Guidelines

A consolidated reference for teams moving agentic AI systems from prototype to production. Each page covers a specific production concern with a structured best practices table: **Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied**.

## Pages in This Section

| Page | What It Covers |
|---|---|
| [Observability](./observability.md) | Tracing, metrics, logs, evaluations, cost visibility, tooling (Langfuse, LangSmith, Braintrust) |
| [State & Memory Management](./state-memory.md) | Memory tiers, LTM strategies, session persistence, memory solutions (Mem0, Zep, AgentFS) |
| [Deployment](./deployment.md) | GenOps, canary rollouts, prompt versioning, durable execution, multi-agent coordination |
| [Agent Testing & Evaluations](./testing-evaluations.md) | LLM-as-judge, eval frameworks (DeepEval, RAGAS), benchmarks (GAIA, SWE-Bench), platforms |
| [Context Engineering](./context-engineering.md) | Context rot, compaction, retrieval, isolation, caching — with references from Manus, Anthropic, LangGraph |
| [Agent Security](./security.md) | Prompt injection, least privilege, HITL, audit trails, NIST AI RMF, Google SAIF, AWS Scoping Matrix |
| [Cost Management](./cost-management.md) | Model routing, prompt caching, token budgets, cost monitoring, vendor-specific guidance |

## Vendor Best Practices

Industry guidance from the major AI providers on building production-ready agents:

| Vendor | Key Resources |
|---|---|
| Anthropic | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · [Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [Long-Running Agent Harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) |
| Google | [Introduction to Agents](https://www.kaggle.com/whitepaper-introduction-to-agents) · [Agent Tools & MCP Interoperability](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp) · [Context Engineering: Sessions & Memory](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory) · [Agent Quality](https://www.kaggle.com/whitepaper-agent-quality) · [Prototype to Production](https://www.kaggle.com/whitepaper-prototype-to-production) |
| Microsoft | [AI Agents for Beginners – 12 Lessons](https://github.com/microsoft/ai-agents-for-beginners) · [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) · [AutoGen Docs](https://microsoft.github.io/autogen/) · [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) |
| OpenAI | [A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) · [OpenAI Cookbook](https://github.com/openai/openai-cookbook) · [Safety Best Practices](https://platform.openai.com/docs/guides/safety-best-practices) |

## Universal Production Principles

| Principle | Rationale |
|---|---|
| Instrument before you deploy | Retrofitting observability is significantly harder than building it in from the start |
| Treat prompts as versioned artifacts | Prompt changes are as impactful as code changes — track, review, and roll back like code |
| Apply least privilege to tool access | Agents with broad permissions cause broader blast radius when they go wrong |
| Set cost alerts from day one | Token costs compound silently; catching overruns on the monthly bill is too late |
| Test continuously in production | One-time pre-deployment evaluation misses quality drift over time |
| Design for graceful degradation | Agents should fail safely — define fallback behaviors and HITL escalation paths |
| Enforce tenant isolation everywhere | Memory, caches, and tool configs must be strictly namespaced in multi-tenant deployments |
