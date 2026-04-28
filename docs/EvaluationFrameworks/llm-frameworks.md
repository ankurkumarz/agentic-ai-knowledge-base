# LLM Evaluation Frameworks

## Overview

LLM evaluation frameworks provide programmatic tools for measuring the quality, accuracy, and safety of LLM outputs. They enable automated evaluation pipelines that can run continuously in CI/CD workflows, replacing or augmenting expensive human evaluation.

## Open Source Frameworks

### DeepEval
**Resource**: [Confident AI DeepEval](https://docs.confident-ai.com/)

The most widely adopted open-source LLM evaluation framework. Provides 14+ evaluation metrics covering both RAG and fine-tuning use cases. Integrates with pytest for familiar developer workflows.

**Key Metrics**:
- **Faithfulness**: Measures whether the response is grounded in the provided context
- **Answer Relevancy**: Evaluates whether the response addresses the question
- **Contextual Precision/Recall**: Assesses retrieval quality in RAG systems
- **Hallucination**: Detects factually incorrect statements
- **Toxicity**: Identifies harmful or inappropriate content
- **Bias**: Detects biased language or reasoning
- **G-Eval**: Custom metric definition using LLM-as-judge

**Use Cases**: RAG evaluation, fine-tuning validation, regression testing, CI/CD integration

### MLFlow LLM Evaluate
**Resource**: [MLFlow LLM Evaluate](https://mlflow.org/docs/latest/llms/llm-evaluate/)

A modular evaluation package integrated into the MLFlow ecosystem. Enables running evaluations within existing ML pipelines with minimal setup. Supports RAG evaluation, QA evaluation, and custom metric definitions.

**Key Features**:
- Seamless integration with MLFlow experiment tracking
- Built-in metrics for QA and RAG scenarios
- Support for custom LLM judges
- Comparison across model versions and configurations
- Works with any LLM provider via MLFlow's model abstraction

### RAGAS
**Resource**: [RAGAS](https://www.ragas.io/)

Specialized evaluation framework for RAG systems and agentic workflows. Provides 8+ metrics for RAG evaluation and 3 metrics specifically for agent evaluation.

**RAG Metrics**:
- **Context Precision**: Proportion of retrieved context that is relevant
- **Context Recall**: Proportion of relevant information that was retrieved
- **Faithfulness**: Whether the answer is supported by the context
- **Answer Relevancy**: Whether the answer addresses the question
- **Context Entity Recall**: Coverage of key entities from ground truth

**Agent Metrics**:
- **Tool Call Accuracy**: Correctness of tool selection and parameter passing
- **Agent Goal Accuracy**: Whether the agent achieved the intended goal
- **Topic Adherence**: Whether the agent stayed on topic

### LangChain OpenEvals
**Resource**: [LangChain OpenEvals](https://github.com/langchain-ai/openevals)

Based on the LLM-as-judge methodology with pre-built prompts for common evaluation scenarios. Provides evaluators for conciseness, fairness, hallucination detection, and custom criteria.

**Key Features**:
- Pre-built evaluators for common quality dimensions
- Easy integration with LangSmith for tracking
- Extensible with custom evaluation criteria
- Supports both reference-based and reference-free evaluation

## Evaluation Methodologies

### LLM-as-Judge
Using a capable LLM (e.g., GPT-4, Claude) to evaluate the outputs of another LLM. The judge model scores responses based on criteria defined in a prompt.

**Advantages**: Flexible, can evaluate subjective qualities, scales easily
**Limitations**: Expensive, judge model biases, inconsistency across runs

**Best Practices**:
- Use a more capable model as judge than the model being evaluated
- Define clear, specific evaluation criteria
- Use structured output (scores + reasoning) for consistency
- Validate judge reliability with human correlation studies

### Reference-Based Evaluation
Compare model outputs against ground truth answers using automated metrics.

**Metrics**:
- **BLEU/ROUGE**: N-gram overlap (primarily for summarization/translation)
- **BERTScore**: Semantic similarity using BERT embeddings
- **Exact Match**: Binary correctness for factual questions
- **F1 Score**: Token-level overlap for extractive QA

### Human Evaluation
Gold standard for quality assessment, but expensive and slow. Best used for:
- Validating automated metrics
- Evaluating subjective qualities (creativity, tone, helpfulness)
- Final production readiness assessment

## Evaluation Pipeline Design

### Continuous Evaluation
Integrate evaluation into CI/CD pipelines to catch regressions:

```python
# Example with DeepEval
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="What is the capital of France?",
    actual_output=agent_response,
    retrieval_context=retrieved_docs
)

evaluate([test_case], [AnswerRelevancyMetric(), FaithfulnessMetric()])
```

### Evaluation Dataset Management
- Maintain curated golden datasets for regression testing
- Regularly update datasets to reflect new use cases
- Version datasets alongside model versions
- Include edge cases and adversarial examples

## Selection Guide

| Use Case | Recommended Framework |
|----------|----------------------|
| RAG system evaluation | RAGAS, DeepEval |
| General LLM quality | DeepEval, LangChain OpenEvals |
| MLFlow integration | MLFlow LLM Evaluate |
| Agent evaluation | RAGAS (agent metrics), DeepEval |
| Custom metrics | DeepEval (G-Eval), LangChain OpenEvals |

## See Also

- [Agent Evaluation Platforms](platforms.md)
- [Benchmarks](../Benchmarks/Readme.md)
- [Observability](../Observability/Readme.md)
