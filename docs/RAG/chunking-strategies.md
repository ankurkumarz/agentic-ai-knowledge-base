---
type: Reference
title: Chunking Strategies for RAG
description: "Eight chunking strategies for splitting documents before embedding in a RAG pipeline: fixed-size, recursive, document-based, semantic, LLM-based, agentic, late chunking, and hierarchical."
tags: [rag, chunking, retrieval, agentic-ai]
timestamp: 2026-10-18T00:00:00Z
---
# Chunking Strategies for RAG

## Overview

Chunking is the step in a RAG pipeline that splits source documents into pieces before they are embedded and indexed. The chunk is the unit the retriever ranks and the generator receives, so the splitting rule determines what context the model can see. Chunk size, overlap, and boundary placement all affect retrieval recall and context length (see [RAG Overview](Readme.md)).

The eight strategies below differ mainly in where they place boundaries and in how much compute they spend deciding where those boundaries go.

![Eight chunking strategies for RAG](https://substack-post-media.s3.amazonaws.com/public/images/88462ca4-b0a1-4441-9537-59dae9d5ef65_2484x3002.png)

*8 Chunking Strategies for RAG (ByteByteGo, EP229) — overview of the eight approaches compared on this page.*

## The Eight Strategies

| Strategy | How It Works | Notes |
|---|---|---|
| **Fixed-Size** | Cuts text every fixed number of tokens, with a small overlap between adjacent chunks | Simplest approach; boundaries ignore the document's structure |
| **Recursive** | Splits on paragraphs first, falls back to lines, then words and characters, and only goes finer when a piece is still too big | Keeps natural text boundaries where possible while staying within a size limit |
| **Document-Based** | Splits wherever the document already marks a break: a heading, chapter, or HTML tag. A markdown file becomes one chunk per section | Depends on the document having reliable markup |
| **Semantic** | Embeds each sentence, compares its similarity to the previous sentence, and starts a new chunk when similarity drops | Finds real topic shifts instead of guessing by length; needs an embedding pass over sentences |
| **LLM-Based** | Asks an LLM to rewrite the text as standalone propositions, one idea per line, and turns each proposition into a chunk | High quality, but expensive across a large corpus |
| **Agentic** | An AI agent reads each document, decides what it is (code, contract, table), and selects the chunking method for that file | Chooses a method per file rather than applying one rule to everything |
| **Late Chunking** | Runs the full document through an embedding model first, then applies normal split boundaries and mean-pools token embeddings within each boundary | Chunk embeddings are computed after the whole document has been encoded; boundaries are still applied, but to the embeddings rather than the raw text |
| **Hierarchical** | Breaks the document into layers: sections, then paragraphs, then sentences | Represents one document at several granularities |

## Selection Guidance

The source describes each strategy but does not rank them. The points below follow from those descriptions:

- **Documents with reliable structure** (markdown, HTML, chapters): document-based splitting gives one chunk per section without extra computation.
- **Long prose with topic drift**: semantic chunking places boundaries at topic shifts instead of at fixed lengths.
- **Large corpora where cost matters**: LLM-based chunking is described as expensive across a large corpus, so it is usually reserved for high-value material.
- **Mixed file types**: agentic chunking chooses a method per file, which suits corpora that combine code, contracts, and tables.
- **Baseline pipelines**: fixed-size chunks with overlap, or recursive splitting, are the simplest starting points.

## Relation to Other Wiki Pages

- Chunking sits in the indexing path of the [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md), which lists "Text Chunking" under the Knowledge Processing Layer.
- Retrieved chunks feed the context window, so chunk size and boundary choices interact with [context engineering](../ContextEngineering/strategies.md) and retrieval-noise controls such as metadata filtering and re-ranking ([Context Engineering Best Practices](../ProductionBestPractices/context-engineering.md)).
- Chunking choices are measured through retrieval evaluation; see [RAG Evaluation Benchmarks](../Benchmarks/rag-benchmarks.md).

## See Also

- [RAG Overview](Readme.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Search as Code](search-as-code.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Context Engineering Best Practices](../ProductionBestPractices/context-engineering.md)
- [RAG Evaluation Benchmarks](../Benchmarks/rag-benchmarks.md)

## References

- [8 Chunking Strategies for RAG — ByteByteGo (EP229)](https://blog.bytebytego.com/p/ep229-8-chunking-strategies-for-rag) — source for the eight strategies and the overview image
