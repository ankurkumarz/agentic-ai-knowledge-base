## RAG Architecture (Huyen, 2025)

A RAG system has two core components:

- **Retriever**: Processes external memory sources via two functions — *indexing* (preparing data for fast retrieval) and *querying* (ranking documents by relevance to a given query)
- **Generator**: A foundation model that produces a response based on the query plus the retrieved context

In modern RAG systems these components are typically trained separately. Finetuning the whole RAG system end-to-end (retriever + generator jointly) can improve performance significantly but is less common.

### Retrieval Algorithms

Retrieval is the backbone of RAG. The choice of algorithm determines quality, cost, and latency:

| Algorithm Type | How It Works | Best For |
|---|---|---|
| **Keyword (BM25/TF-IDF)** | Scores documents by term frequency and inverse document frequency | Exact match; technical terms; legal/compliance text |
| **Dense retrieval (vector search)** | Embeds query and documents; retrieves by cosine/dot-product similarity | Semantic similarity; paraphrases; concept search |
| **Hybrid** | Combines keyword + dense scores (typically via RRF or weighted sum) | General-purpose; balances exact and semantic match |
| **Sparse + dense (SPLADE, ColBERT)** | Learned sparse representations; dense interaction at query time | High recall with interpretability |
| **Re-ranking** | A second-pass cross-encoder scores the top-k retrieved chunks for final ranking | Improving precision after first-pass retrieval |

### Retrieval Optimization

Key strategies for improving retrieval quality:

- **Chunking strategy**: Splitting documents into workable chunks is a core design decision. Chunk size and overlap affect both recall and context length. Common approaches: fixed-size chunks, sentence-level chunks, semantic chunking (split at topic boundaries).
- **Query expansion**: Rewrite or augment the user query to improve recall (hypothetical document embeddings, multi-query retrieval)
- **Metadata filtering**: Attach and filter by document metadata (date, source, category) to reduce irrelevant retrievals
- **Contextual compression**: After retrieval, extract only the passages most relevant to the specific query rather than including whole chunks
- **Embedding model selection**: The embedding model is as important as the retriever algorithm. Domain-specific finetuned embeddings outperform general models on specialized corpora.

### RAG vs. Full-Context Prompting vs. Finetuning

| Approach | When to Use |
|---|---|
| RAG | External knowledge not in model weights; needs to stay current; large/proprietary document sets |
| Full-context prompting | Knowledge fits in context window; latency tolerant; no need to maintain an index |
| Finetuning | Style/format adaptation; domain specialization; recurring task patterns |

RAG and finetuning are complementary: RAG provides current knowledge retrieval; finetuning adapts the model's behavior and style. Both can (and often should) be used together.

## Search as Code (SaC)

An emerging paradigm where language models generate code to assemble task-specific retrieval pipelines on demand, rather than routing through fixed pipelines. See [Search as Code](search-as-code.md) for Perplexity's full architecture — Models as Control Plane, Compute Sandboxes, and Agentic Search SDK — including the WANDR benchmark and CVE case study showing 85.1% token reduction.

## RAG Engines

- [Contextual AI RAG Agents](https://contextual.ai): enterprise solution for building and deploying specialized RAG agents with Reranker
- [Gigaspaces eRAG](https://www.gigaspaces.com/technology/erag-solution)

## Retrieval Approaches

[Traditional retrieval, hybrid retrieval, semantic retrieval, knowledge-based retrieval, and agentic contextual retrieval](https://arxiv.org/abs/2502.16866)

![retrieval strategies](https://arxiv.org/html/2502.16866v1/x1.png)

Comparison of Key Retrieval Strategies:

![retrieval strategies](https://arxiv.org/html/2502.16866v1/x2.png)

Agentic contextual retrieval:

![contextual retrieval](https://arxiv.org/html/2502.16866v1/x4.png)

## Fine-tuning Models for RAG

- [Databricks - Improving Retrieval and RAG with Embedding Model Finetuning](https://www.databricks.com/blog/improving-retrieval-and-rag-embedding-model-finetuning)
- [Fine-tuning Embedding Model Reference ](https://github.com/apatti/AIEBootcamp/blob/main/09_Finetuning_Embeddings/Fine_tuning_Embedding_Models_for_RAG_using_RAGAS.ipynb)

## See Also

- [AI Engineering Architecture](../ReferenceArchitecture/ai-engineering-architecture.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Search as Code](search-as-code.md)
- [Semantic Data Layer Technology Radar](../AgenticTechStack/semantic-data-layer-radar.md)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166304/) — Chip Huyen, O'Reilly, 2024. Chapter 6.
