---
type: Standard
title: Open Responses
description: "Open Responses is an open-source specification, built on the OpenAI Responses API, that aims to give model providers and clients one interoperable schema for calling LLMs, streaming results, and running agent workflows"
tags: [standards, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# Open Responses

## Overview

Open Responses is an open-source specification and ecosystem for multi-provider, interoperable LLM interfaces. Its stated purpose is a shared schema and tooling layer for calling models, streaming their results, and building agent workflows, so that an application does not have to be rewritten for each model provider. It is derived from the OpenAI Responses API rather than the Chat Completions API. Secondary coverage describes it as vendor-neutral and notes that it is a community specification, not an official OpenAI product.

Simon Willison's January 2026 write-up gives the reason for choosing this base API: Responses already includes features such as reasoning traces.

## Key Concepts / Architecture

- **Base API.** The specification is built on the OpenAI Responses API surface, so existing Responses-style clients have a migration path.
- **Shared schema.** A common request, response, and streaming format is intended to let one client talk to several providers.
- **Agent workflows.** The specification targets tool calls and multi-step agent interactions, not only single completions.
- **Launch partners.** Coverage names OpenRouter, Hugging Face, LM Studio, vLLM, Ollama, and Vercel as early implementers.

## Status and Gaps

- **Conformance testing.** One review says a client-side compliance suite is currently missing. Willison has called for a comprehensive, language-independent conformance test site. Until one exists, interoperability claims rest on implementers' own tests.
- **Event detail.** Exact event types and field-level semantics were not verified for this page. Check the specification text before implementing against it.

## Relationship to Other Standards

Open Responses addresses the **model-call interface**. It is complementary to, not a replacement for, the protocols that govern tools and agent-to-agent communication:

| Layer | Standard | Scope |
|---|---|---|
| Model call and streaming | Open Responses | Request, response, and streaming schema across providers |
| Tool and context exposure | [Model Context Protocol](mcp.md) | Tools, resources, and prompts exposed to a model |
| Agent-to-agent | [Agent2Agent](agent2agent.md) | Discovery and task exchange between agents |
| Editor-agent | [Agent Client Protocol](agent-client-protocol.md) | Session and permission interface between an editor and a coding agent |

## Considerations

- **Vendor neutrality is a claim to verify.** The specification originates from a design that is OpenAI-shaped. Confirm that the schema is not tied to one provider's extensions before treating it as neutral.
- **Early ecosystem.** Launch-partner adoption is encouraging, but the wiki has no independent measurement of conformance across implementations.

## See Also

- [AllThingsOpenAI](../AllThingsOpenAI/README.md) — OpenAI's agentic offerings, including the Responses API that this specification builds on
- [Model Context Protocol (MCP)](mcp.md) — tool and context exposure, the layer above the model call
- [Agent2Agent (A2A) Protocol](agent2agent.md) — agent-to-agent interoperability
- [Agent Client Protocol (ACP)](agent-client-protocol.md) — editor-agent interoperability
- [Agentic AI Industry Standards](README.md) — standards overview

## References

- [Open Responses](https://www.openresponses.org/) — official site; the authoritative specification source (not retrievable while preparing this page, so details here come from secondary sources)
- [Simon Willison — Open Responses (Jan 15, 2026)](https://simonwillison.net/2026/Jan/15/open-responses/) — rationale for building on the Responses API and the conformance-testing gap
