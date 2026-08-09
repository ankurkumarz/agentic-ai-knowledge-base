---
type: Framework
title: LlamaIndex
description: LlamaIndex is a data framework for connecting custom data sources to large language models
tags: [frameworks, agentic-ai]
timestamp: 2026-07-17T00:00:00Z
---
# LlamaIndex

## Overview

LlamaIndex is a data framework for connecting custom data sources to large language models. LlamaIndex started with data framework capabilities for LLM applications and has evolved to cover AI agents, document parsing & indexing, workflow, connectors-based integration, modularity & extensibility, and many more capabilities.

## High-level Architecture

![LlamaIndex Framework](../assets/images/frameworks-llamaindex-overview.png)

*Source: [LlamaIndex Framework](https://www.llamaindex.ai/framework)*

## Key Features

- **Data framework capabilities**: Started with data framework capabilities for LLM applications and has evolved to cover AI agents, document parsing & indexing, workflow, connectors-based integration, modularity & extensibility
- **LlamaCloud**: Offers a SaaS capability as LlamaCloud as a knowledge management hub for AI Agents
- **LlamaParse**: A differentiated offering for transforming instructed data into LLM-optimized formats
- **LlamaHub**: A centralized place to explore Agents, LLMs, Vector Stores, Data Loaders, etc.
- **Document processing**: Efficient parsing and indexing of complex documents
- **Knowledge management**: Comprehensive knowledge management capabilities for AI systems
- **Multi-modal support**: Supports various data types and formats

## Parse Gateway — Smart Page-Level Parser Routing

LlamaIndex's **Parse Gateway** (announced 2026) addresses a specific inefficiency in document-parsing pipelines: most pipelines send every page of a PDF through the same parser, forcing a single cost/speed/accuracy tradeoff across a document even though pages vary widely in difficulty (a clean text page vs. a scanned cover, a dense table, or a figure-heavy diagram).

- **Mechanism**: Parse Gateway uses [LiteParse's](https://github.com/run-llama/liteparse) `is_complex` function to estimate each page's complexity individually — flagging *why* a page is hard (scanned, sparse text, garbled encoding, vector text, embedded images) and *how severely* — then routes that page to the cheapest parsing tier capable of handling it.
- **Effect**: simple pages are parsed for free, in-process, via LiteParse; genuinely difficult pages are routed up to more capable (and more expensive) LlamaParse tiers. This avoids paying premium per-page prices for pages that never needed it, without sacrificing accuracy on the pages that do.
- **Availability**: the gateway logic is open-source (shipped inside LiteParse) and also exposed as an MCP server, so agents can estimate page complexity and choose a parsing tier themselves rather than calling a fixed API.

This sits alongside LlamaParse in LlamaIndex's document-processing stack: LiteParse/Parse Gateway is the free, local, complexity-aware front door; LlamaParse (LlamaCloud) remains the escalation target for pages that need heavier-weight parsing.

## Suitable for (Pros)

- **As an alternative to LangChain**: LlamaIndex has evolved as a compelling alternative, particularly for data-intensive LLM applications
- **The ability to parse and index complex documents efficiently** with LlamaCloud makes it a compelling option for enterprises seeking quicker time-to-market
- **Building knowledge-intensive AI systems** like chatbots and question-answering systems
- **Data-centric applications**: Excellent for applications that require sophisticated data processing and retrieval
- **Enterprise knowledge management**: Strong capabilities for enterprise-scale knowledge management systems

## Where other frameworks flare better (Cons)

- **Primarily focused on data indexing and retrieval**, with less emphasis on complex agent behaviors and decision-making. However, the evolution of the framework towards building Agentic apps provides promising capabilities
- **Limited agent orchestration**: Less sophisticated agent coordination compared to specialized multi-agent frameworks
- **Learning curve**: Requires understanding of data indexing and retrieval concepts

## Resources

- **Official Website**: [LlamaIndex](https://www.llamaindex.ai/)
- **LlamaCloud**: [Knowledge management hub](https://cloud.llamaindex.ai/)
- **LlamaParse**: [Document parsing service](https://www.llamaindex.ai/llamaparse)
- **LlamaHub**: [Centralized resource hub](https://llamahub.ai/)
- **GitHub Repository**: [LlamaIndex GitHub](https://github.com/run-llama/llama_index)
- **LiteParse**: [Open-source local document parser](https://github.com/run-llama/liteparse) — powers Parse Gateway's page-complexity estimation
- **Parse Gateway announcement**: [Smart page-level document parser routing](https://www.llamaindex.ai/blog/parse-gateway-smart-page-level-document-parser-routing)

## See Also
- [Agent Development Frameworks](README.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Context Engineering](../ContextEngineering/README.md)
- [Memory Solutions & Technology Radar](../AgentMemory/solutions.md) — LlamaIndex Memory module vs. dedicated memory vendors