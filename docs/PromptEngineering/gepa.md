# GEPA: Genetic-Pareto Prompt Optimization

## Overview

GEPA (Genetic-Pareto) is a reflective prompt-optimization framework that evolves text prompts using full natural-language execution traces — rather than the scalar reward signals consumed by reinforcement-learning-style optimizers such as GRPO. The core insight is that a single number (pass/fail, score) discards almost all of the diagnostic information available in an LLM rollout: what the model reasoned, which tool calls it made, where it went wrong. GEPA instead feeds the complete trace back into an LLM reflection step that proposes a textual mutation to the prompt, and tracks a **Pareto frontier** of candidate prompts rather than collapsing to a single best-so-far candidate. The project is maintained at [gepa-ai/gepa](https://gepa-ai.github.io/gepa/) and is integrated into [DSPy](https://github.com/stanfordnlp/dspy) as an optimizer.

## Key Concepts / Architecture / Features

- **Reflective mutation**: after each rollout, an LLM reads the full trace (reasoning, tool calls, intermediate outputs, final score) and proposes a specific textual edit to the prompt — analogous to a human engineer reading a failure log and patching the prompt, rather than a black-box gradient step.
- **Full traces over scalar rewards**: GEPA's optimizer sees the same rich diagnostic signal that human prompt engineers use, instead of a single reward number — this is the same design principle later generalized to harness *code* optimization by Meta-Harness (see [Harness Optimization](../AgentHarness/harness-optimization.md)).
- **Pareto-frontier candidate selection**: rather than greedily keeping only the single highest-scoring candidate, GEPA maintains a frontier of candidates that are each best on at least one evaluation instance or sub-metric. This avoids premature convergence to a locally-optimal prompt that overfits to the aggregate score.
- **Sample efficiency**: GEPA's reflective, trace-driven mutation requires far fewer rollouts than reward-only RL fine-tuning to reach a comparable or better prompt.

## Evaluation Results

- Outperforms GRPO (Group Relative Policy Optimization) by roughly **10–20%**, using up to **35x fewer rollouts**
- Outperforms MIPROv2 (a leading DSPy prompt optimizer) by **more than 10%**
- Demonstrated across multiple task domains as a DSPy-integrated optimizer

## Suitable for (Pros)

- Teams optimizing prompts for frozen, non-fine-tunable models where RL-style weight updates are not an option
- Settings with an expensive or slow rollout budget, where GEPA's sample efficiency over GRPO matters
- DSPy users who want a drop-in optimizer that uses richer feedback than module scores alone

## Limitations (Cons)

- Still a **text-space** optimizer — it mutates prompts, not the surrounding retrieval/tool/state-management code that a harness-level optimizer like Meta-Harness can edit
- Requires an LLM reflection step per rollout batch, adding inference cost beyond the rollouts themselves
- Pareto-frontier maintenance adds bookkeeping complexity relative to single-best-candidate optimizers like OPRO

## Relationship to Other Optimizers

GEPA sits between classic text-space prompt optimizers (OPRO, ProTeGi, TextGrad, MIPROv2 — which compress feedback into scalar scores or short textual gradients) and code-level harness optimizers (Meta-Harness — which edits arbitrary harness code using raw execution traces via a coding agent). GEPA was the first widely-adopted approach to bring *full-trace* reflection to prompt optimization specifically; Meta-Harness extends the same full-trace principle from prompt text to the entire harness codebase. See the comparison table in [Harness Optimization](../AgentHarness/harness-optimization.md#relationship-to-prior-optimization-work).

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Reflection model choice | A weak reflection model proposes low-quality mutations | Use a frontier-class model for the reflection step even if the target/optimized prompt runs on a smaller model |
| Frontier size growth | Tracking too many Pareto-optimal candidates increases evaluation cost | Cap frontier size or prune dominated candidates periodically during long optimization runs |
| Rollout batch size | Too few rollouts per mutation step produces noisy reflection signal | Batch enough rollouts per round that the reflection step sees a representative failure sample, not a single anecdote |
| Overfitting to training instances | A mutated prompt over-specializes to the training set's specific failure cases | Hold out a validation split distinct from the rollouts used for reflection; only accept mutations that improve validation score |

## See Also

- [Harness Optimization](../AgentHarness/harness-optimization.md) — Meta-Harness extends GEPA's full-trace reflection principle from prompt text to arbitrary harness code
- [SkillOpt](./skillopt.md) — Microsoft's text-space skill-document optimizer; benchmarked against GEPA (52/52 wins reported by SkillOpt's authors)
- [Prompt Engineering Overview](./README.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Agent Harness](../AgentHarness/agent-harness.md)

## References

- [GEPA Project Page](https://gepa-ai.github.io/gepa/) — official documentation and DSPy integration guide
- [gepa-ai/gepa GitHub Repository](https://github.com/gepa-ai/gepa) — open-source implementation
