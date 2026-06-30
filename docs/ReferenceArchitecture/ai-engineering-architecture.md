# AI Engineering Architecture

## Overview

This page describes the production architecture for foundation model applications, synthesized from Chip Huyen's *AI Engineering* (O'Reilly, 2025, Chapter 10). The architecture follows a progressive approach: start with the simplest possible system and add components incrementally as production needs justify them, rather than over-engineering from the start.

Despite the diversity of AI applications, they share a common set of components. This five-step architecture has been validated across multiple production deployments.

## The Simplest Architecture

The minimal viable architecture receives a query and sends it directly to a model API, which returns the response to the user. No context augmentation, no guardrails, no optimization.

```
[User Query] → [Model API] → [Response]
```

The Model API box covers both third-party APIs (OpenAI, Anthropic, Google) and self-hosted models (requiring an inference server, discussed under Inference Optimization).

Starting here keeps early development fast. Complexity is added only when evidence from users or production metrics demands it.

## Step 1: Enhance Context

The first expansion adds mechanisms for dynamic context construction — giving the model relevant information it doesn't have in its weights.

Context can be constructed via:

- **Text retrieval** (RAG): Search a vector database or keyword index to retrieve relevant document chunks
- **Image/multimodal retrieval**: Retrieve relevant images, tables, or structured data
- **Tabular data retrieval**: SQL query execution to retrieve structured records
- **API-based augmentation**: Real-time data via web search, weather, news, or internal API calls

Context construction is analogous to feature engineering in traditional ML: it provides the model with the data it needs to produce an accurate output.

**Key consideration**: Different model API providers differ in context construction support — upload limits, chunk sizes, retrieval algorithms, tool execution modes (sequential vs. parallel). When the generic API is insufficient, a specialized RAG solution may allow unlimited document upload bounded only by vector database capacity.

## Step 2: Put in Guardrails

Guardrails protect the system and its users from risks. They apply to both inputs and outputs.

### Input Guardrails

Two primary risks:
1. **Leaking private information to external APIs**: Employees or applications may inadvertently include sensitive data (PII, trade secrets, internal policies) in prompts sent to third-party APIs.
2. **Prompt injection and jailbreaking**: Attackers craft inputs that override system instructions or extract information the system should not reveal.

Mitigation:
- **PII/sensitive data detection**: Automated tools scan prompts for PII (ID numbers, bank accounts, faces), IP keywords, or privileged phrases. If detected, the prompt can be blocked, redacted, or routed to a local model.
- **Injection detection**: Pattern-based and model-based classifiers detect injection attempts.

### Output Guardrails

Three primary output risks:
1. **Empty or malformed responses**: Model fails or returns invalid structure
2. **Hallucinations**: Factually incorrect content presented as fact
3. **Unsafe content**: Toxic, harmful, or policy-violating outputs

Output guardrails can include:
- **Model-based scorers**: Small models evaluate output quality (relevance, faithfulness, toxicity) and trigger remediation (regenerate, escalate to human, return fallback)
- **Format validators**: Ensure structured outputs (JSON, XML) conform to expected schemas
- **Content classifiers**: Flag unsafe, off-topic, or legally risky content

**Tradeoff**: Output guardrails require additional model calls per response, adding latency and cost.

## Step 3: Add Model Router and Gateway

As applications grow, managing multiple models and entry points requires additional infrastructure.

### Router

A router uses an intent classifier or next-action predictor to route each query to the optimal solution:

- **Model routing**: Route simple queries to cheap/fast models; complex queries to frontier models
- **Action routing**: For agents, predict the next action (code interpreter, web search, human escalation)
- **Memory routing**: Determine which memory tier (in-context, semantic cache, vector store, database) to pull from

Routers are typically small, fast models (fine-tuned BERT, Llama-7B, or even rule-based classifiers) that add minimal latency while enabling significant cost savings.

**Routing order**: Routing often happens before retrieval (determine if the query is in scope, if retrieval is needed). Post-retrieval routing is also used (route to human when retrieval confidence is low).

### Gateway

A model gateway provides a unified interface to multiple models, abstracting away provider-specific APIs:

- **Unified interface**: One API call regardless of underlying model (OpenAI, Google, Anthropic, self-hosted)
- **Access control**: Centralized management of API keys and per-team/user access permissions
- **Cost monitoring**: Track and limit API consumption per user, project, or model
- **Fallback policies**: Automatic failover when primary model is rate-limited or unavailable
- **Versioning**: Pin specific model versions to prevent unexpected behavior changes from provider updates

## Step 4: Reduce Latency with Caches

Caching prevents redundant computation and dramatically reduces both latency and cost for repeated or similar queries.

### Exact Caching

Cache results keyed by exact query or embedding hash:

- **Response cache**: If the same query (or the same product summary request) was answered before, return the cached result directly
- **Embedding cache**: If a query was already embedded and vector-searched, return cached retrieval results
- **Tool result cache**: Cache deterministic tool outputs (API responses, SQL results) with appropriate TTLs

**Implementation**: Redis (for fast in-memory lookup), PostgreSQL or tiered storage for larger caches. Eviction policies: LRU, LFU, or FIFO. Train a classifier to predict which queries are worth caching (avoid user-specific or time-sensitive queries).

**Security risk**: Improper caching can cause data leaks. User-specific responses must never be cached and returned to a different user.

### Semantic Caching

Return cached results for semantically similar (not just identical) queries using embedding similarity:
- Embed the incoming query and search a cache of past query embeddings
- Return the cached response if cosine similarity exceeds a threshold

Particularly effective for FAQ agents, classification pipelines, and any high-volume use case with predictable query patterns.

## Step 5: Add Agent Patterns

Simple sequential query-response flows can be upgraded to agentic patterns for complex tasks:

- **Loops**: Generated output is fed back into the model when the task is not yet complete (e.g., a search agent that determines its first retrieval was insufficient)
- **Parallel execution**: Multiple retrieval or tool calls dispatched concurrently
- **Conditional branching**: Different execution paths based on intermediate model outputs
- **Write actions**: Model outputs trigger real-world changes (compose email, place order, update database, initiate transfer)

**Critical caution on write actions**: Write actions dramatically expand what a system can accomplish, but they also introduce irreversible consequences. Write action capabilities should be granted only when necessary, with explicit human-in-the-loop checkpoints for high-impact operations, strict idempotency guarantees to prevent duplicate side effects, and audit logging for all write events.

## Monitoring and Observability

Observability should be designed into the application, not added after. The more complex the system, the more critical this is.

Key distinctions:
- **Monitoring**: Tracking external outputs of a system to detect when something goes wrong
- **Observability**: Instrumenting the system so its internal state can be inferred from external outputs — enabling root cause diagnosis without deploying new code

Three DevOps-derived metrics for evaluating observability quality:

| Metric | Definition | Goal |
|---|---|---|
| MTTD (Mean Time to Detection) | How long to detect a failure | Minimize |
| MTTR (Mean Time to Response) | How long to resolve after detection | Minimize |
| CFR (Change Failure Rate) | % of deployments causing failures requiring rollback | Track and reduce |

**What to instrument** specifically for foundation model apps:
- **Response quality metrics**: Sampled AI-as-judge scores for relevance, faithfulness, toxicity
- **User feedback signals**: Thumbs up/down, explicit ratings, follow-up questions (implicit dissatisfaction signal)
- **Latency breakdowns**: Time in retrieval, model inference, guardrails, caching
- **Cost per request**: Token counts, model tier used, cache hit rate
- **Failure modes**: Guardrail rejections, empty responses, tool call errors, routing misclassifications

Evaluation and monitoring pipelines must stay synchronized: a model that performs well in offline evaluation should also perform well in production. Issues detected in monitoring should feed back into the evaluation pipeline.

## AI Pipeline Orchestration

For complex multi-step pipelines, an orchestration layer chains all components together:

- **Sequential chaining**: Retrieval → generation → scoring → output
- **Parallel fan-out**: Multiple retrievals or tool calls dispatched simultaneously, results merged
- **Retry logic**: Re-invoke failed steps with exponential backoff
- **State management**: Track partial execution state for long-running agentic workflows (durable execution)

Popular orchestration frameworks: LangChain/LangGraph, AWS Strands, Google ADK, Temporal (for durable execution), and custom orchestration for simple pipelines.

## Architecture Evolution Summary

| Step | Component Added | Problem Solved |
|---|---|---|
| Base | Model API | Basic query-response |
| Step 1 | Context construction (RAG, tools) | Model lacks knowledge of private/recent data |
| Step 2 | Input/output guardrails | Security risks, quality control |
| Step 3 | Router + Gateway | Multi-model management, cost control |
| Step 4 | Exact + semantic caching | Latency and cost at scale |
| Step 5 | Agent patterns + write actions | Complex multi-step tasks |
| + | Monitoring & observability | Production reliability |
| + | Orchestration layer | Chaining all components |

## See Also

- [AI Engineering (Concepts)](../Concepts/ai-engineering.md)
- [RAG Architecture](../RAG/Readme.md)
- [Agent Definition and Planning](../Concepts/agent-definition.md)
- [Prompt Engineering](../PromptEngineering/README.md)
- [AI as a Judge](../EvaluationFrameworks/ai-as-judge.md)
- [Observability Solutions](../Observability/solutions.md)
- [Cost Management](../ProductionBestPractices/cost-management.md)
- [Context Engineering](../ContextEngineering/strategies.md)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166304/) — Chip Huyen, O'Reilly, 2024. Chapter 10.
