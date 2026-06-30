# AI Engineering

## Overview

AI engineering is the process of building applications on top of readily available foundation models. Coined and formalized in Chip Huyen's *AI Engineering* (O'Reilly, 2025), it describes a distinct discipline that differs from traditional ML engineering: instead of developing models from scratch, AI engineers adapt existing foundation models — via prompt engineering, RAG, finetuning, and agentic patterns — to solve specific real-world problems.

The discipline emerged from three converging forces: dramatically more capable general-purpose models, surging investment in AI applications, and a drastically lowered barrier to entry (model-as-a-service APIs allow anyone to build AI applications without ML expertise or model infrastructure).

## The Rise of AI Engineering

Foundation models evolved through three stages:

- **Language models → Large Language Models**: Self-supervised training on internet-scale data enabled models to grow to billions of parameters without requiring labeled data. Self-supervision is the key: each sentence in a corpus provides its own training labels (the next token), eliminating the annotation bottleneck.
- **LLMs → Foundation Models**: Models capable of multi-modal inputs (text, images, audio, code) and a wide range of tasks — translation, summarization, coding, reasoning, data extraction — from a single model.
- **Foundation Models → AI Engineering**: The availability of these models via API created a new engineering discipline focused on adaptation and application, not model construction.

Key adoption signals:
- Within 2 years of launch, four open-source AI engineering tools (AutoGPT, Stable Diffusion WebUI, LangChain, Ollama) accumulated more GitHub stars than Bitcoin.
- LinkedIn showed 75% monthly growth in professionals adding "Generative AI", "ChatGPT", and "Prompt Engineering" to their profiles.
- 1 in 3 S&P 500 companies mentioned AI in their Q2 2023 earnings calls — 3× more than the year before.

## Foundation Model Use Cases

Huyen analyzed 205 open-source AI applications (≥500 GitHub stars) and conducted 50 enterprise interviews, categorizing applications into eight groups:

| Category | Consumer Examples | Enterprise Examples |
|---|---|---|
| Coding | Code completion, test generation | Automated code review, migration tools |
| Image and video production | Profile photo generation, design | Ad generation, marketing content |
| Writing | Email improvement, blog posts | Copywriting, SEO, performance reports |
| Education | Tutoring, essay feedback | Employee onboarding, upskill training |
| Conversational bots | General chatbot, AI companion | Customer support, product copilots |
| Information aggregation | Summarization, talk-to-your-docs | Market research, competitive intelligence |
| Data organization | Image search, memex | Knowledge management, document processing |
| Workflow automation | Travel planning, event planning | Data extraction, lead generation |

**Enterprise adoption pattern**: Companies deploy internal-facing applications (knowledge management, productivity tools) before external-facing ones (customer chatbots), trading slower rollout for lower compliance and data-privacy risk.

**Occupational exposure** (Eloundou et al., 2023): Tasks where AI can reduce time-to-completion by ≥50% are "exposed." Mathematicians, tax preparers, financial analysts, writers, and web designers show 100% exposure. Cooks, stonemasons, and athletes show near-zero exposure.

## The AI Engineering Stack

Huyen defines three layers:

1. **Infrastructure layer**: Hardware accelerators (GPUs/TPUs), cloud compute, storage, and networking. Provided by hyperscalers and specialist vendors.
2. **Model layer**: Foundation models themselves — proprietary (GPT-4, Claude, Gemini) and open-weight (Llama, Mistral, Qwen). Teams either access these via API or self-host.
3. **Application layer**: Where AI engineering happens — prompt engineering, RAG systems, agentic workflows, finetuning, evaluation pipelines, and deployment infrastructure.

The AI engineering stack includes three interconnected disciplines:

- **Prompt engineering**: Crafting instructions, few-shot examples, and context that guide model behavior without changing model weights.
- **RAG (Retrieval-Augmented Generation)**: Supplementing model context with dynamically retrieved information from external knowledge bases.
- **Finetuning**: Adapting model weights to improve performance on a specific task or domain, at far lower cost than pretraining.
- **Agents**: Systems that use a model to plan and execute sequences of actions, using tools and memory to accomplish complex tasks.

## AI Engineering vs. ML Engineering

| Dimension | Traditional ML Engineering | AI Engineering |
|---|---|---|
| Core activity | Build and train models | Adapt and deploy existing models |
| Data requirement | Large labeled datasets | Small prompt examples; synthetic data for finetuning |
| Primary skill | Statistics, model architecture, training optimization | Prompt design, context engineering, evaluation |
| Iteration speed | Weeks to months | Hours to days |
| Model ownership | Team owns the model | Model provided as a service |
| Evaluation | Offline metrics (accuracy, F1, AUC) | LLM-as-judge, functional correctness, human eval |
| Dominant technique | Feature engineering, hyperparameter tuning | Context engineering, prompt engineering, RAG |

Traditional ML models remain relevant — production systems often combine both traditional ML models and foundation models. AI engineers who understand both have a significant advantage.

## Planning AI Applications

Huyen's framework for deciding whether to build an AI application:

1. **Use case evaluation**: Does this task benefit from AI? Is the task exposed to AI? Is there sufficient data to evaluate quality?
2. **Setting expectations**: What constitutes success? What are the acceptable failure modes? What is the minimum viable quality?
3. **Milestone planning**: Prototype (demonstrate feasibility) → Production (deployed to real users) → Iteration (continuous improvement based on feedback).
4. **Maintenance**: AI applications require ongoing maintenance — model deprecations, capability drift, data drift, and changing user expectations all require active management.

The hardest part of building an AI application is often not the AI itself but the evaluation infrastructure: defining what "good" means, collecting labeled examples, and building automated pipelines to detect regressions.

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| Starting complexity | Teams over-engineer from the start | Begin with the simplest possible architecture; add components only when justified by evidence |
| Evaluation gap | No systematic way to measure quality | Build evaluation infrastructure before scaling; treat it as a first-class engineering concern |
| Model selection | Too many options with unclear trade-offs | Establish a selection workflow: baseline → accuracy → cost/latency; benchmark on your own data |
| Hallucinations | Models generate plausible but incorrect content | Use RAG for knowledge-intensive tasks; implement output verification; calibrate user expectations |
| Cost and latency | Frontier model costs scale poorly at volume | Route simpler queries to smaller models; implement caching; profile actual token usage |
| Prompt fragility | Prompts that work today break after model updates | Version prompts; include regression tests; test on multiple model versions |

## See Also

- [Agent Definition](agent-definition.md)
- [Agent Types](agent-types.md)
- [Prompt Engineering](../PromptEngineering/README.md)
- [RAG Architecture](../RAG/Readme.md)
- [AI Engineering Architecture (Reference)](../ReferenceArchitecture/ai-engineering-architecture.md)
- [Evaluation Frameworks](../EvaluationFrameworks/llm-frameworks.md)
- [Inference Optimization](../ProductionBestPractices/cost-management.md)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166304/) — Chip Huyen, O'Reilly Media, December 2024. ISBN 978-1-098-16630-4.
- [Eloundou et al. (2023) — GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130)
