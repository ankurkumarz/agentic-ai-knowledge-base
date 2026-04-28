# Cost Management for Agentic AI

Cost management is a first-class production concern for agentic AI systems. Unlike traditional software, agent costs scale with token consumption, tool call frequency, model selection, and memory retrieval patterns — all of which can compound unexpectedly at scale.

## Overview

Effective cost management spans the full agent stack:

- **Inference costs**: LLM API calls (input/output tokens, model tier)
- **Infrastructure costs**: Compute, memory, storage, and networking
- **Observability overhead**: Tracing, logging, and monitoring storage
- **Memory and retrieval costs**: Vector DB queries, knowledge graph traversals, cache storage

## Token Cost Optimization

### Model Routing

Match task complexity to model capability. Not every agent step requires a frontier model.

| Task Type | Recommended Approach |
|---|---|
| Simple classification / routing | Small/fast model (e.g., GPT-4o-mini, Haiku) |
| Tool call generation | Mid-tier model |
| Complex reasoning / synthesis | Frontier model (e.g., GPT-4o, Claude Sonnet/Opus) |
| Embedding generation | Dedicated embedding model |

**Implementation**: Use a lightweight classifier or rule-based router to select the appropriate model per request before invoking the agent.

### Prompt Optimization

- **Minimize system prompt size**: Audit system prompts regularly; remove redundant instructions
- **Tool description pruning**: Only include tools relevant to the current task context
- **Context compaction**: Summarize conversation history rather than passing full transcripts (see [Context Engineering](../ContextEngineering/README.md))
- **Structured outputs**: Request JSON/structured responses to reduce verbose prose in outputs

### Caching Strategies

**Prompt caching** (supported by Anthropic Claude, Google Gemini):
- Cache static prefixes: system prompts, tool definitions, large document contexts
- Cached tokens are billed at a significant discount (typically 80-90% reduction)
- Particularly effective for agents with large, stable system instructions

**Semantic caching**:
- Cache responses to semantically similar queries using embedding similarity
- Tools: [GPTCache](https://github.com/zilliztech/GPTCache), Redis with vector search, or platform-native caching
- Best for high-volume, repetitive query patterns (e.g., FAQ agents, classification pipelines)

**Tool result caching**:
- Cache deterministic tool outputs (API responses, database queries) with appropriate TTLs
- Prevents redundant external API calls within and across agent sessions

## Budget Controls and Alerting

### Per-Request Budgets

Set hard token limits per agent invocation to prevent runaway loops:

```python
# Example: LangChain callback for token budget enforcement
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    result = agent.invoke(input)
    if cb.total_tokens > TOKEN_BUDGET:
        raise BudgetExceededError(f"Token budget exceeded: {cb.total_tokens}")
```

### Cost Monitoring Tooling

| Tool | Capability |
|---|---|
| [Langfuse](https://langfuse.com/) | Per-trace cost tracking, cost dashboards, budget alerts |
| [Openlit](https://openlit.io/) | OpenTelemetry-native cost metrics, GPU monitoring |
| [LangSmith](https://www.langchain.com/langsmith) | Cost analytics per run, project-level cost aggregation |
| [Braintrust](https://www.braintrust.dev/) | Cost tracking with regression detection against baselines |
| [AgentOps](https://www.agentops.ai) | Agent-specific cost optimization insights |

### Alert Thresholds

Recommended alert tiers:

- **Warning**: 70% of daily/monthly budget consumed
- **Critical**: 90% of budget consumed — trigger throttling or fallback to cheaper models
- **Hard stop**: Budget exhausted — queue requests or return graceful degradation response

## Infrastructure Cost Optimization

### Right-Sizing

- Profile agent memory and CPU usage under realistic load before choosing instance types
- Use spot/preemptible instances for batch agent workloads (evaluation runs, data processing)
- Implement auto-scaling with scale-to-zero for low-traffic agents

### Storage Optimization

- **Vector DB**: Choose storage tier based on query frequency — hot storage for active sessions, cold/archived for historical embeddings
- **Conversation history**: Implement retention policies; archive or delete sessions beyond a defined age
- **Observability data**: Use sampling in production (10-20% trace capture) rather than 100% tracing

### Multi-Region and Edge Considerations

- Route requests to the lowest-latency region to reduce time-to-first-token (which also reduces perceived cost of slow responses)
- Consider edge inference for latency-sensitive, high-volume use cases where smaller models suffice

## Cost Attribution and Chargeback

For multi-tenant or multi-team deployments:

- Tag all LLM API calls with `project_id`, `team_id`, `agent_id`, and `environment` metadata
- Use observability platforms (Langfuse, LangSmith) to aggregate costs by tag
- Implement chargeback reporting for internal cost allocation
- Track cost-per-task-completion as a business metric alongside raw token spend

## Cost vs. Quality Trade-offs

Cost optimization should never silently degrade agent quality. Establish baselines:

1. **Benchmark quality** at your current model/prompt configuration
2. **Apply optimization** (model downgrade, prompt reduction, caching)
3. **Re-evaluate quality** against the same benchmark
4. **Accept only if quality delta is within tolerance**

Use evaluation frameworks (see [Agent Testing & Evaluations](../EvaluationFrameworks/Readme.md)) to automate this regression check as part of your CI/CD pipeline.

## Vendor-Specific Cost Guidance

### Anthropic
- Use prompt caching for large system prompts and document contexts
- Haiku for routing/classification, Sonnet for most tasks, Opus for complex reasoning
- [Anthropic pricing](https://www.anthropic.com/pricing)

### OpenAI
- GPT-4o-mini for high-volume, lower-complexity tasks
- Batch API for non-real-time workloads (50% cost reduction)
- [OpenAI pricing](https://openai.com/api/pricing/)

### Google (Vertex AI / Gemini)
- Context caching for long, stable contexts
- Gemini Flash for cost-efficient high-volume use cases
- [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)

### AWS (Bedrock)
- On-demand vs. provisioned throughput trade-offs for predictable workloads
- Cross-region inference for availability and cost balancing
- [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)

## Balancing Speed, Reliability, and Cost

Scaling an agent always involves three competing goals. Optimizing for one affects the others:

| Goal | Strategy |
|---|---|
| **Speed (Latency)** | Design for parallel tool execution; aggressively cache results; use smaller, efficient models for routine subtasks |
| **Reliability** | Handle transient failures with automatic retry + exponential backoff; design "safe-to-retry" (idempotent) tools to prevent duplicate side effects (e.g., duplicate charges); use circuit breakers to stop retry storms |
| **Cost** | Shorten prompts; use cheaper models for simpler tasks; send requests in groups (batching); use asynchronous processing for non-real-time work |

**Idempotent tools**: A non-obvious cost control. If a tool call fails and is retried, idempotent design ensures the second call doesn't double-charge or create duplicate records — preventing costly cleanup work downstream.

**Batching**: For non-real-time agent workloads, batch multiple requests into a single API call. OpenAI Batch API offers 50% cost reduction; Vertex AI provides similar batch inference options.

## See Also

- **[Observability](../Observability/Readme.md)**: Cost monitoring as part of observability
- **[Context Engineering](../ContextEngineering/README.md)**: Context compaction to reduce token usage
- **[Deployment](../AgentOps/README.md)**: Infrastructure cost management in AgentOps
- **[Agent Testing & Evaluations](../EvaluationFrameworks/Readme.md)**: Validating quality after cost optimizations
