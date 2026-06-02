# Search as Code (SaC)

## Overview

Search as Code (SaC) is a retrieval architecture paradigm introduced by Perplexity AI (September 2025) in which language models generate executable code to assemble task-specific retrieval pipelines on demand, rather than routing through fixed, pre-designed pipelines. The core insight is that traditional search — which answers queries — is insufficient for agents that complete tasks, because tasks take countless shapes and require task-specific retrieval strategies that cannot be anticipated at pipeline design time.

In SaC, the model acts as a control plane: it reads the user's directive, decomposes it into sub-tasks, and writes code that composes search primitives from an SDK into a custom retrieval pipeline. That pipeline then runs inside a secure compute sandbox. This shifts the definition of "search infrastructure" from a rigid backend to a programmable surface exposed as an SDK.

## Architecture

SaC has three functional layers:

### 1. Models as Control Plane

The language model reasons about the user's directive, decomposes it into discrete tasks, decides which retrieval and processing pipelines each task needs, and generates Python code to implement those pipelines. The model does not execute search directly — it defines the execution plan as code and delegates deterministic operations to the sandbox.

### 2. Compute Sandboxes

A secure code execution runtime provides the model's generated code with a deterministic compute environment. The sandbox is the canvas for:
- Control flow (conditionals, loops, branching)
- Batching and parallelism across retrieval operations
- Retries and error handling
- Filtering, joining, and aggregating results
- Any deterministic post-processing step

The sandbox ensures that up to thousands of operations can be orchestrated within a single inference turn without exposing the host environment to arbitrary code risks.

### 3. Agentic Search SDK

The SDK exposes Perplexity's search stack as composable primitives ranging from low-level retrieval operations (raw document fetching, snippet ranking) to high-level semantic operations (entity extraction, semantic parsing, cross-document synthesis). The SDK is embedded in the sandbox's execution runtime, making it directly callable from model-generated code.

This composability means the model can mix retrieval primitives as needed: for a CVE audit task, it might fetch vendor advisories directly, run structured queries against CVE databases, cross-reference fix versions, and aggregate findings — all within a single generated script.

## Key Concepts

- **Task-specific pipelines**: Unlike RAG, where the pipeline is fixed and the query varies, SaC produces a new pipeline for each task. The pipeline topology (which primitives to invoke, in what order, with what parameters) is itself a model output.
- **Deterministic compute offload**: Filtering, joining, sorting, and aggregation are delegated to the sandbox rather than to the model's inference, improving accuracy and reducing token usage.
- **Model-agnostic platform**: The Perplexity SaC stack is designed to work with any language model as the control plane, not only Perplexity-hosted models.
- **Agentic, not just retrieval-augmented**: SaC is positioned as search infrastructure for agents that complete long-horizon tasks, not as a document retrieval layer for single-turn QA.

## Performance and Evaluation

### WANDR Benchmark

WANDR (Wide And Nuanced Deep Research) evaluates agents on "wide research" tasks requiring careful orchestration of search, compute, and model reasoning. It is designed around the kind of knowledge-intensive professional tasks that Perplexity Computer handles for users. WANDR iterates on WideSearch and similar benchmarks with an emphasis on more complex task structures.

SaC achieves a **2.5× advantage** over the next-best system on WANDR, with particularly pronounced gains on tasks that require multi-source synthesis and structured output constraints.

Across five benchmarks total, SaC **outperforms all other systems on four** and is essentially tied on the remaining one (HLE).

### CVE Audit Case Study

A real-world evaluation tasked the system with identifying and characterizing more than 200 high-severity CVEs from 2023–2025, with each record required to cite the affected vendor's security advisory and show correct fix versions. Results versus a non-SaC baseline:

| Metric | Non-SaC Baseline | SaC |
|---|---|---|
| Accuracy | Below 100% | 100% |
| Total token usage | Baseline | −85.1% |

The token reduction comes from the sandbox handling structured filtering and aggregation that would otherwise require model-in-the-loop iteration.

## Comparison with Traditional RAG

| Dimension | Traditional RAG | Search as Code |
|---|---|---|
| Pipeline structure | Fixed at design time | Generated per task by the model |
| Query handling | Single query → retrieve → answer | Multi-step program with branching |
| Aggregation | Post-retrieval by model (in-context) | In sandbox (deterministic, cheaper) |
| Retrieval granularity | Chunk-level similarity | Composable SDK primitives |
| Error handling | Manual or absent | Programmatic retries in sandbox |
| Token efficiency | Scales with retrieved content | Deterministic ops offloaded to sandbox |
| Suitable for | Document QA, knowledge lookup | Long-horizon agent tasks, structured research |

## Python SDK

Perplexity exposes SaC capabilities through the `perplexityai` Python package:

```python
pip install perplexityai
```

The SDK provides native support for three APIs:
- **Search API**: Core retrieval with fine-grained snippet ranking
- **Agent API**: Managed runtime for agentic workflows with integrated search, tool execution, and multi-model orchestration
- **Sonar API**: Grounded LLM completions with integrated search

The **Agent API** provides a managed runtime that allows developers to build agentic workflows without managing the sandbox infrastructure themselves.

## Perplexity Computer

Perplexity Computer is a multi-model agent orchestration platform that coordinates 19 different AI models to complete complex, long-running workflows. It reflects the thesis that AI models are specializing rather than converging toward general-purpose commodities — and serves as the primary production consumer of the SaC architecture. It is priced at $200/month as of the time of publication.

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| Task decomposition quality | SaC quality depends on the model's ability to decompose a directive into sub-tasks | Invest in system-prompt guidance for decomposition; evaluate decomposition quality as a separate metric |
| Sandbox resource limits | Generated code may produce unbounded loops or memory-intensive joins at scale | Set per-execution CPU/memory quotas; enforce maximum operation counts in the SDK |
| Primitive selection | Using high-level primitives when low-level ones suffice increases latency | Profile primitive usage per task type; prefer lower-level primitives for well-understood task patterns |
| Retrieval grounding | Model-generated code may reference non-existent SDK methods | Use strict SDK versioning; include API surface in the model's system prompt or tool schema |
| Evaluation | Traditional RAG metrics (recall, MRR) do not capture SaC-specific quality | Evaluate at task-completion level (e.g., accuracy, citation correctness) rather than retrieval level alone; use WANDR-style benchmarks |

## See Also

- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [RAG Implementation](../RAG/Readme.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Production Context Engineering](../ProductionBestPractices/context-engineering.md)
- [Agent Evaluation Benchmarks](../Benchmarks/agent-benchmarks.md)
- [Architecture Components Selection](../Architecture/components-selection.md)

## References

- [Rethinking Search as Code Generation](https://research.perplexity.ai/articles/rethinking-search-as-code-generation) — Perplexity AI Research, September 2025. Introduces the SaC architecture, three-layer model, and WANDR benchmark results.
- [Architecting and Evaluating an AI-First Search API](https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api) — Perplexity AI Research. Companion article on Search API design and evaluation methodology.
- [Agent API: A Managed Runtime for Agentic Workflows](https://www.perplexity.ai/hub/blog/agent-api-a-managed-runtime-for-agentic-workflows) — Perplexity AI. Details on the Agent API managed runtime.
- [Perplexity Search API Launch](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api) — Perplexity AI. Initial launch announcement with retrieval infrastructure overview.
