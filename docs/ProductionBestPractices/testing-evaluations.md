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
| Single-model critical decisions | Relying on one non-deterministic LLM for a high-stakes decision (credit scoring, compliance) | Trusted a single model call; hallucinations or biased outputs went undetected | **Parallel Execution Consensus**: run two or more independent agents on the same task using different models or prompts; orchestrator validates result when outputs agree within a tolerance; escalates to a resolver or human when they disagree significantly |
| Silent agent version regressions | Deploying a new agent version to all users risks widespread quality degradation | Rolled out new versions 100% immediately; regressions only detected after users complained | **Canary Agent Testing**: route a small traffic fraction (e.g., 5%) to the new agent version; compare performance metrics against the stable version; block full rollout if regression rate exceeds threshold |

## Evaluation Frameworks

| Framework | Type | Best For |
|---|---|---|
| [DeepEval](https://docs.confident-ai.com/) | Open source | 14+ metrics for RAG and fine-tuning evaluation |
| [RAGAS](https://www.ragas.io/) | Open source | RAG-specific metrics (faithfulness, relevance, context recall) |
| [MLFlow LLM Evaluate](https://mlflow.org/docs/latest/llms/llm-evaluate/) | Open source | Integration into existing ML pipelines |
| [LangChain OpenEvals](https://github.com/langchain-ai/openevals) | Open source | LLM-as-judge with pre-built rubrics |
| [AIDLC Evaluator](../Standards/aidlc.md) | Open source (AWS Labs) | Golden test cases, semantic evaluation, code analysis (linting, security), NFR testing (tokens, execution time), CI/CD integration — bundled with AIDLC Workflows framework |
| [AgentPex](https://github.com/microsoft/agentpex) | Open source (Microsoft) | Trace-based agent evaluation: imports execution traces (JSON, Langfuse, Langtrace/OTEL), extracts specs from system prompts and tool schemas, applies 8 evaluation techniques including groundedness and argument checking; pushes scores to Langfuse/Langtrace |

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
| [DeepResearch Bench](https://deepresearch-bench.github.io/) | Deep research agents — report quality (RACE) and citation accuracy/grounding (FACT) across 100 PhD-level tasks |

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

## Harness-Level Eval Categories

Evaluate the harness, not only the model. Model accuracy is necessary but not sufficient — a model that scores well on benchmarks can still fail catastrophically through harness-level weaknesses.

| Eval Category | What It Measures |
|---|---|
| Task success | Did the agent complete the goal? |
| Tool selection precision | Did it choose the right tool, avoid unnecessary calls? |
| Permission correctness | Were permission checks triggered at the right times? |
| Approval correctness | Were approval requests issued at the right risk level? |
| Prompt injection resistance | Does the agent treat retrieved content as data, not instruction? |
| Context compaction retention | Did compaction preserve the active objective and approvals? |
| Retrieval relevance | Did retrieval return useful, in-scope content? |
| Output format adherence | Did tool results and final answers match expected schemas? |
| Failure recovery | Did the agent handle tool failures gracefully (structured error, not silent skip)? |
| Cost and latency | Were budgets respected? |
| Human intervention rate | How often did the agent require unexpected escalation? |

## Adversarial Test Cases

Required adversarial scenarios for any production-bound harness:

- Retrieved document contains "ignore previous instructions"
- Email body contains a request to exfiltrate data
- User asks for an external send without approval
- Tool returns malformed or oversized data
- Connector auth expires mid-run
- Model calls an unknown tool
- Model supplies invalid tool arguments
- Context reaches limit and compaction triggers mid-task
- Two loaded instructions conflict
- Goal is vague or impossible to measure
- Sensitive data (PII, secrets) appears in retrieved content
- Subagent returns an unsupported or unverifiable conclusion

Each failed adversarial test should become a permanent regression eval.

## Agentic AI Red Teaming (CSA)

The [Cloud Security Alliance's Agentic AI Red Teaming Guide](../SecurityFrameworks/agentic-ai-red-teaming-guide.md) (Aug 2025) extends the adversarial test cases above into a structured, 12-category red teaming program purpose-built for autonomous agents:

| Category | Example Test Focus |
|---|---|
| Agent Authorization and Control Hijacking | Permission escalation, role inheritance exploitation, least-privilege enforcement |
| Checker-Out-of-the-Loop | Threshold-breach simulation, human/checker engagement latency |
| Agent Critical System Interaction | Physical/IoT command injection, safety interlock bypass |
| Agent Goal and Instruction Manipulation | Goal interpretation attacks, instruction-set poisoning |
| Agent Hallucination Exploitation | Induced hallucination, cascading hallucination across agent chains |
| Agent Impact Chain and Blast Radius | Cross-system exploitation via a compromised agent, containment validation |
| Agent Knowledge Base Poisoning | Training data poisoning, RAG knowledge base corruption |
| Agent Memory and Context Manipulation | Cross-session data leakage, memory poisoning |
| Agent Orchestration and Multi-Agent Exploitation | Inter-agent trust abuse, orchestrator state poisoning |
| Agent Resource and Service Exhaustion | Computational/API quota depletion |
| Agent Supply Chain and Dependency Attacks | Development-chain and deployment-pipeline compromise |
| Agent Untraceability | Trace evasion, forensic obfuscation, accountability chain verification |

CSA's recommended four-phase methodology — **Preparation → Execution → Analysis → Reporting** — maps cleanly onto a launch-gate process: define scenarios and isolated test environments, execute and log step-by-step, analyze and prioritize findings by severity, then report mitigation strategies to stakeholders. See [Agentic AI Red Teaming Guide (CSA)](../SecurityFrameworks/agentic-ai-red-teaming-guide.md) for the full taxonomy, actionable test steps, and a survey of red teaming tools (AgentDojo, Agent-SafetyBench, SplxAI Agentic Radar, Azure AI Red Teaming Agent, FuzzAI, and others).

## Launch Gates

The following must be true before production rollout:

- Tool registry is narrow — only the minimum set for the MVP job
- Schema validation runs locally before every tool execution
- Permission matrix is enforced in harness code (not only in prompts)
- Approval UX exists for every risky action class
- Prompt injection tests pass on realistic retrieval content
- Compaction tests confirm the active objective survives compaction
- Connector auth and revocation flows are tested end-to-end
- Trace logging is enabled and includes all required fields
- Cost budgets are enforced and wired to stop conditions
- Rollback or incident response path is documented
- Evals run on both realistic and adversarial task sets

## See Also
- [Observability](./observability.md)
- [Deployment](./deployment.md)
- [Context Engineering](./context-engineering.md)
- [Agentic AI Red Teaming Guide (CSA)](../SecurityFrameworks/agentic-ai-red-teaming-guide.md) — 12-category threat taxonomy and four-phase testing methodology
- [Agent Security](./security.md) — guardrails, approval workflows, and audit trails

## References
- [agents-best-practices — DenisSergeevitch (2025)](https://github.com/DenisSergeevitch/agents-best-practices) — source for harness-level eval categories, adversarial test scenarios, and launch gates checklist
- [Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide) — Cloud Security Alliance (Aug 2025)
