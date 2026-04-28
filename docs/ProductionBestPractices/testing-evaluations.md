# Agent Testing & Evaluations

Evaluating agentic AI systems is fundamentally different from traditional software testing. Outputs are non-deterministic, tasks are multi-step, and quality is often subjective. A robust evaluation strategy combines automated metrics, human review, and continuous regression detection.

## Overview

Evaluation operates at multiple levels:

| Level | What It Tests | When |
|---|---|---|
| Unit | Individual LLM calls, tool outputs, prompt templates | During development |
| Integration | Agent + tool chains, memory reads/writes, handoffs | Pre-deployment |
| End-to-end | Full task completion from user input to final output | Staging and canary |
| Production | Real user interactions, sampled and scored | Continuously |

## Best Practices

| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
| Non-deterministic outputs | Same input produces different outputs, making assertion-based tests brittle | Tried exact string matching; tests were flaky and unmaintainable | Use LLM-as-judge evaluation with rubric-based scoring; assert on score thresholds not exact strings |
| No ground truth for open-ended tasks | Many agent tasks have no single correct answer | Tried human labeling for all outputs; didn't scale | Build golden datasets for representative tasks; use automated scoring for coverage, human review for edge cases |
| Evaluation coverage gaps | Unit tests pass but end-to-end quality degrades | Tested components in isolation; missed emergent failures in full pipelines | Maintain end-to-end eval suites that run on every deployment; track pass rate as a deployment gate |
| Prompt regression | Prompt changes silently degrade quality on edge cases | Deployed prompt updates without re-running evals; caught regressions in prod | Run full eval suite on every prompt change; block deployment if score drops below baseline |
| Tool call evaluation | Hard to evaluate whether the agent chose the right tool with the right parameters | Only evaluated final output; missed incorrect tool selection | Evaluate tool call traces separately — check tool selection accuracy and parameter correctness |
| Multi-agent evaluation | Difficult to attribute quality issues to a specific agent in a pipeline | Evaluated only the final output of the pipeline | Instrument each agent's output independently; evaluate at each handoff boundary |
| Benchmark gaming | Agents optimized for benchmarks perform poorly on real tasks | Relied solely on public benchmarks (GAIA, SWE-Bench); missed domain-specific failures | Supplement public benchmarks with internal domain-specific eval sets built from real user interactions |
| Evaluation cost | Running LLM-as-judge on every output is expensive | Evaluated 100% of outputs; costs were unsustainable | Sample strategically — evaluate 100% of failures, 10–20% of successes, and all edge case categories |

## Evaluation Frameworks

| Framework | Type | Best For |
|---|---|---|
| [DeepEval](https://docs.confident-ai.com/) | Open source | 14+ metrics for RAG and fine-tuning evaluation |
| [RAGAS](https://www.ragas.io/) | Open source | RAG-specific metrics (faithfulness, relevance, context recall) |
| [MLFlow LLM Evaluate](https://mlflow.org/docs/latest/llms/llm-evaluate/) | Open source | Integration into existing ML pipelines |
| [LangChain OpenEvals](https://github.com/langchain-ai/openevals) | Open source | LLM-as-judge with pre-built rubrics |

## Evaluation Platforms

| Platform | Key Capability |
|---|---|
| [Galileo](https://galileo.ai/) | Custom metrics, CLHF (Continuous Learning with Human Feedback), Autotune |
| [Google Stax](https://stax.withgoogle.com/) | Managed test datasets, pre-built and custom evaluators, visual tracking |
| [LastMile AI](https://lastmileai.dev/) | Enterprise-grade testing and benchmarking in production |
| [Braintrust](https://www.braintrust.dev/) | Regression detection using real user data |

## Agent Benchmarks Reference

| Benchmark | Focus |
|---|---|
| [METR](https://metr.org/) | Autonomous task completion without human input |
| [GAIA](https://huggingface.co/gaia-benchmark) | General-purpose agent capabilities across diverse tasks |
| [SWE-Bench](https://www.swebench.com/) | Code generation and GitHub issue resolution |
| [Terminal Bench](https://www.tbench.ai/) | Agents operating in terminal/CLI environments |
| [VisualWebArena](https://github.com/web-arena-x/visualwebarena) | Multimodal agents interacting with web interfaces |
| [OSWorld](https://os-world.github.io/) | Agents interacting with real operating system environments |

## Evaluation as a Quality Gate (Google AgentOps Model)

Traditional software tests are insufficient for agents because they evaluate only functional correctness. An agent requires assessment of **behavioral quality** — the full trajectory of reasoning and actions taken to complete a task.

Key principle from Google: evaluating an agent is distinct from evaluating an LLM. An agent can pass 100 unit tests for its tools but still fail spectacularly by choosing the wrong tool or hallucinating a response.

**Golden Dataset**: A curated, representative set of test cases designed to assess an agent's intended behavior and guardrail compliance. This is the foundation of evaluation-gated deployment. Production failures are continuously fed back to augment this dataset.

**Two implementation approaches for the evaluation gate:**
1. **Manual Pre-PR**: AI/Prompt Engineer runs eval locally; attaches performance report to PR; reviewer (ML Governor) assesses behavioral changes and guardrail violations
2. **Automated In-Pipeline**: Evaluation harness blocks deployments automatically when metrics like tool-call success rate or helpfulness fall below predefined thresholds

**What to evaluate in agent trajectories:**
- Tool selection accuracy (did it choose the right tool?)
- Parameter correctness (did it pass the right arguments?)
- Guardrail compliance (did it respect security/safety policies?)
- Task completion (did it actually solve the problem?)
- Behavioral regression vs. the production baseline

**Responsible AI (RAI) Testing:**
- **NPOV (Neutral Point of View) evaluations**: Test for neutrality and balance
- **Parity evaluations**: Test for consistent behavior across demographic groups
- **Persona-based simulation**: AI-driven simulation that proactively tries to break safety systems through creative scenarios

## See Also
- [Observability](./observability.md)
- [Deployment](./deployment.md)
- [Context Engineering](./context-engineering.md)
