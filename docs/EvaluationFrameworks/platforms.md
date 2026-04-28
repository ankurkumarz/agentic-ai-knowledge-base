# Agent Evaluation Platforms

## Overview

Agent evaluation platforms provide end-to-end infrastructure for testing, measuring, and improving AI agent performance in production. They go beyond simple metric computation to offer dataset management, experiment tracking, human review workflows, and continuous monitoring.

## Enterprise Evaluation Platforms

### Galileo
**Resource**: [Galileo](https://galileo.ai/)

A custom-built evaluation platform featuring pre-built evaluation metrics, custom metrics, and Autotune capabilities. Galileo's CLHF (Continuous Learning with Human Feedback) improves evaluators over time based on human corrections.

**Key Features**:
- Pre-built metrics for hallucination, toxicity, PII, and relevance
- Custom metric creation without code
- Autotune: automatically improves evaluators using human feedback
- Production monitoring with real-time alerts
- Integration with major LLM providers and frameworks
- [Agent Leaderboard](https://huggingface.co/spaces/galileo-ai/agent-leaderboard) for benchmarking

**Best For**: Enterprise teams needing production-grade evaluation with human feedback loops

### Google Stax
**Resource**: [Google Stax](https://stax.withgoogle.com/)

A SaaS evaluation solution by Google for LLM evaluation. Provides managed test datasets, pre-built and custom evaluators, and visual tracking of aggregated AI performance.

**Key Features**:
- Managed test dataset creation and versioning
- Pre-built evaluators for common quality dimensions
- Custom evaluator creation
- Visual performance tracking and trend analysis
- Integration with Google Cloud and Vertex AI

**Best For**: Teams using Google Cloud infrastructure and Vertex AI

### LastMile AI
**Resource**: [LastMile AI](https://lastmileai.dev/)

An enterprise-grade evaluation platform providing essential tools for developers to test, evaluate, and benchmark AI applications in production environments.

**Key Features**:
- Comprehensive testing and benchmarking tools
- Production monitoring and alerting
- Collaboration features for team-based evaluation
- Integration with popular LLM frameworks

**Best For**: Enterprise teams needing comprehensive production evaluation

## Open Source and Developer Platforms

### LangSmith
**Resource**: [LangSmith](https://www.langchain.com/langsmith)

LangChain's integrated development and evaluation platform. Combines tracing, dataset management, and evaluation in a single platform tightly integrated with the LangChain ecosystem.

**Key Features**:
- Trace capture and visualization for LangChain/LangGraph applications
- Dataset creation from production traces
- Automated evaluation with custom evaluators
- Prompt versioning and A/B testing
- Human annotation workflows
- CI/CD integration for regression testing

**Best For**: Teams using LangChain/LangGraph who want integrated tracing and evaluation

### Braintrust
**Resource**: [Braintrust](https://www.braintrust.dev/)

Evaluation platform focused on measuring and improving AI in production. Specializes in regression detection using real user data and continuous improvement workflows.

**Key Features**:
- Experiment tracking with side-by-side comparison
- Regression detection against production baselines
- Human review and annotation interface
- Prompt playground with evaluation integration
- SDK for programmatic evaluation

**Best For**: Teams that need to iterate quickly on production AI systems

### Langfuse
**Resource**: [Langfuse](https://langfuse.com/)

Open-source LLM observability and evaluation platform. Combines tracing with evaluation capabilities in a self-hostable package.

**Key Features**:
- Full trace capture with evaluation scoring
- Dataset management and annotation
- LLM-as-judge evaluation pipelines
- Open-source with enterprise cloud option
- Native SDKs for Python and TypeScript

**Best For**: Teams wanting open-source evaluation with self-hosting option

## Research Evaluation Frameworks

### Meta MLGym
**Resource**: [Meta MLGym](https://arxiv.org/abs/2502.14499)

A framework and benchmark for advancing AI research agents. Provides standardized environments for evaluating agents on machine learning research tasks. [GitHub Repository](https://github.com/facebookresearch/MLGym) provides implementation details.

**Key Features**:
- Standardized ML research task environments
- Evaluation of agents on real ML problems (dataset analysis, model training, hyperparameter tuning)
- Reproducible benchmarking methodology

## Evaluation Platform Comparison

| Platform | Open Source | Self-Hosted | Human Review | CI/CD Integration | Agent-Specific |
|----------|-------------|-------------|--------------|-------------------|----------------|
| Galileo | ❌ | ❌ | ✅ | ✅ | ✅ |
| Google Stax | ❌ | ❌ | ✅ | ✅ | ✅ |
| LastMile AI | ❌ | ❌ | ✅ | ✅ | ✅ |
| LangSmith | ❌ | Limited | ✅ | ✅ | ✅ |
| Braintrust | ❌ | ❌ | ✅ | ✅ | ✅ |
| Langfuse | ✅ | ✅ | ✅ | ✅ | ✅ |

## Getting Started

### For Developers
1. Start with **LangSmith** (if using LangChain) or **Langfuse** (open-source, framework-agnostic)
2. Capture traces from production to build evaluation datasets
3. Define evaluation criteria and implement automated metrics
4. Set up regression tests in CI/CD pipeline

### For Enterprise Teams
1. Evaluate **Galileo** or **LastMile AI** for comprehensive enterprise features
2. Integrate with existing observability infrastructure
3. Establish human review workflows for high-stakes decisions
4. Implement continuous evaluation with production data

### For Research Teams
1. Use **Meta MLGym** for research agent evaluation
2. Combine with **Langfuse** for detailed trace analysis
3. Publish evaluation results using standardized benchmarks

## Best Practices

- **Separate evaluation from training data**: Never use evaluation datasets for training
- **Combine automated and human evaluation**: Automated metrics for scale, human review for quality
- **Track evaluation over time**: Monitor for performance regressions as models and prompts change
- **Use production data**: Build evaluation datasets from real user interactions
- **Define success criteria upfront**: Establish what "good" looks like before building

## See Also

- [LLM Evaluation Frameworks](llm-frameworks.md)
- [Benchmarks](../Benchmarks/Readme.md)
- [Observability Solutions](../Observability/solutions.md)
