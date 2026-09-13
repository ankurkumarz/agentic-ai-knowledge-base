---
type: Playbook
title: OpenTelemetry GenAI Semantic Conventions
description: "The OpenTelemetry GenAI Semantic Conventions define vendor-neutral spans, metrics, and events for instrumented GenAI clients, MCP servers, and provider-specific integrations."
tags: [observability, opentelemetry, standards, tracing, genai, mcp, agentic-ai]
timestamp: 2026-09-13T00:00:00Z
---

# OpenTelemetry GenAI Semantic Conventions

## Overview

The **OpenTelemetry GenAI Semantic Conventions** (`open-telemetry/semantic-conventions-genai`) extend the OpenTelemetry Semantic Conventions with definitions specific to Generative AI workloads. They provide a vendor-neutral, community-governed specification for how spans, metrics, and events should be named, structured, and attributed when instrumenting GenAI clients, Model Context Protocol (MCP) servers, and provider-specific integrations (OpenAI, Anthropic, etc.).

This repository is managed using OpenTelemetry's **Weaver** toolchain, which treats YAML definition files as the normative source and generates human-readable Markdown documentation from them. Reference implementations and compliance matrices are maintained under `reference/`.

Without shared semantic conventions, every observability platform invents its own span names and attribute keys — making it impossible to write portable dashboards, alerts, or queries across tools. The GenAI conventions close this gap for LLM and agent observability.

## Scope

The conventions cover three tiers of instrumentation:

| Tier | Scope | Examples |
|---|---|---|
| **GenAI client spans** | Spans emitted by client libraries making calls to LLM providers | `gen_ai.client.operation.duration`, model name, token counts, finish reason |
| **MCP instrumentation** | Spans and events for Model Context Protocol tool calls and resource access | Tool invocation spans, resource fetch events, server-side processing |
| **Provider-specific conventions** | Attribute extensions for individual providers | OpenAI-specific span attributes, streaming event shapes |

## Repository Structure

```
semantic-conventions-genai/
├── docs/          # Human-readable Markdown (generated from YAML)
├── model/         # YAML definitions — normative source of truth
└── reference/     # Reference implementations and compliance matrices
    ├── README.md  # Per-signal support reports and Python compliance matrix
    └── CONTRIBUTING.md
```

All normative definitions live in `model/`. The `docs/` folder is generated output — do not edit it directly.

## Key Semantic Conventions

### Span Attributes for LLM Calls

Standard attributes allow observability tools to provide consistent trace views across providers:

| Attribute | Type | Description |
|---|---|---|
| `gen_ai.system` | string | The GenAI provider (e.g., `openai`, `anthropic`, `aws.bedrock`) |
| `gen_ai.operation.name` | string | Operation type: `chat`, `text_completion`, `embeddings` |
| `gen_ai.request.model` | string | Requested model identifier |
| `gen_ai.response.model` | string | Actual model used (may differ from request) |
| `gen_ai.usage.input_tokens` | int | Number of prompt tokens consumed |
| `gen_ai.usage.output_tokens` | int | Number of completion tokens generated |
| `gen_ai.response.finish_reasons` | string[] | Reasons the generation stopped (e.g., `stop`, `max_tokens`, `tool_calls`) |

### Span Attributes for MCP

MCP instrumentation enables tracing through tool call chains:

| Attribute | Type | Description |
|---|---|---|
| `mcp.method` | string | MCP method invoked (e.g., `tools/call`, `resources/read`) |
| `mcp.tool.name` | string | Name of the tool being called |
| `gen_ai.system` | string | Reused — identifies the orchestrating LLM provider |

### Events

The conventions define structured events (as opposed to free-form log lines) for key GenAI operations:

- `gen_ai.system.message` — system prompt content event
- `gen_ai.user.message` — user turn content event
- `gen_ai.assistant.message` — model response event
- `gen_ai.tool.message` — tool result injected into conversation

Events carry the full content of messages and tool results, enabling prompt-level debugging within traces.

## Relationship to the Broader OTel Ecosystem

The GenAI conventions slot into the standard OTel pipeline:

```
Agent / LLM Client
       │  (instrumented with GenAI semantic conventions)
       ▼
OTel SDK (spans, metrics, events)
       │
       ▼
OTel Collector (export pipeline)
       │
  ┌────┴────┐
  │         │
Jaeger   Prometheus   (or any backend: Grafana Tempo, Datadog, New Relic, etc.)
```

Platforms built natively on OTel (Openlit, Langfuse v3) emit spans that conform to these conventions, enabling interoperability with general-purpose observability tooling that predates GenAI.

## Why This Matters for Agent Observability

Multi-agent systems involve long chains of LLM calls, tool invocations, and handoffs. Without standardized span attributes:

- You cannot correlate a trace across an orchestrator agent and its sub-agents if they use different instrumentation libraries
- Cost attribution (per model, per provider) requires parsing inconsistent span names
- MCP tool call latency is invisible unless explicitly instrumented
- Switching observability backends requires re-instrumenting your code

With the GenAI conventions in place, a single trace propagation header and a conformant SDK are sufficient to reconstruct the full execution graph in any OTel-compatible backend.

## Tooling Integration

| Tool | OTel GenAI Convention Support |
|---|---|
| **Openlit** | Built on OTel; emits GenAI-convention-compliant spans |
| **Langfuse v3** | OTel-native SDK; aligns with GenAI span attributes |
| **AWS Distro for OpenTelemetry (ADOT)** | Supports GenAI spans via CloudWatch integration |
| **Datadog** | LLM observability add-on maps to GenAI convention attributes |
| **New Relic** | AI monitoring ingests OTel GenAI spans |

## Best Practices

| Challenge | Recommendation |
|---|---|
| Consistent span naming | Adopt `gen_ai.*` attribute names exactly as specified — do not abbreviate or prefix them differently |
| Token cost tracking | Record both `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` on every LLM span; multiply by per-token price downstream for cost attribution |
| MCP tool latency | Wrap every MCP `tools/call` in a child span with `mcp.tool.name`; trace propagation headers must be forwarded to the MCP server |
| Provider diversity | Use `gen_ai.system` to segment dashboards and alerts by provider — enables provider-level cost and latency comparison |
| Event sampling | Full message content events (`gen_ai.user.message`, etc.) are verbose; sample at 10–20% in production or redact PII before recording |
| Keep up with spec | The conventions are under active development; pin the Weaver version used to generate your docs and review the CHANGELOG on releases |

## See Also

- [Observability Solutions](./solutions.md)
- [Observability Goals](./goals.md)
- [Production Observability Best Practices](../ProductionBestPractices/observability.md)
- [Model Context Protocol (MCP)](../Standards/mcp.md)
- [Agent Client Protocol (ACP)](../Standards/agent-client-protocol.md)
- [AgentOps Overview](../AgentOps/README.md)

## References

- [open-telemetry/semantic-conventions-genai on GitHub](https://github.com/open-telemetry/semantic-conventions-genai) — canonical spec repository with YAML definitions, generated docs, and reference implementations
