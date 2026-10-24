---
type: Framework
title: OpenEnv
description: "OpenEnv is a BSD-3-Clause framework for packaging agent execution environments as isolated, Gymnasium-style services used for agentic reinforcement learning and evaluation"
tags: [evaluation, reinforcement-learning, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# OpenEnv

## Overview

OpenEnv describes itself as "an end-to-end framework for creating, deploying and using isolated execution environments for agentic RL, with a simple Gymnasium-style API." It addresses a practical gap in agentic reinforcement learning: a training loop needs an environment that an agent can act in, get rewards from, and reset, and that environment has to run isolated from the trainer. OpenEnv packages each environment as a deployable service with a client library, so the same environment can be used for training rollouts, for evaluation, and for ad hoc agent testing.

The framework sits between agent harnesses and training stacks. It is closer to a benchmark-and-rollout substrate than to an agent-building framework.

## Key Concepts / Architecture

- **Environments as images.** Each environment is packaged as a Docker image and can run locally, on a cloud sandbox, or as a Hugging Face Space. The catalog lists 40+ environments, covering games, coding sandboxes, browsers, finance, and simulators.
- **Gymnasium-style API.** Environments expose `reset()`, `step()`, and `state()`, in synchronous form or asynchronous form over a WebSocket.
- **Clients.** Users install an environment client package and connect to a running instance through a `base_url`, using an async context manager or a `.sync()` wrapper. The README does not describe the server-side internals in detail.
- **MCP exposure.** MCP-based environments expose their tools to agents at `/mcp` in production mode, while training continues to use `step()` and rewards. This lets one environment serve both tool-using agents and RL trainers.
- **Rewards and evaluation.** Rewards can be composed from rubrics, and evaluation is supported through Inspect AI.
- **Tooling.** A CLI scaffolds, validates, and deploys environments (`openenv init`, `openenv validate`, `openenv push`). `openenv import` wraps existing ORS/OpenReward or Verifiers environments.

## Training Integrations

The README lists integrations with ART, Lightning AI, Miles, Oumi, SkyRL, torchforge, TorchTitan-RL, TRL, and Unsloth. It states that TRL's `GRPOTrainer` accepts an `environment_factory`. It also describes a Harbor integration that runs coding-agent harnesses, such as Claude Code and Codex, and captures model tokens for RL training.

## Maturity and Governance

- **License:** BSD 3-Clause.
- **Stage:** The README says "OpenEnv is in early development, so APIs may still change."
- **Governance:** A technical committee oversees the project. Its members include Meta-PyTorch, Hugging Face, NVIDIA, and Microsoft, among others.
- **Community:** At capture, the repository showed about 2.8k stars, 494 forks, 2,314 commits, 68 open issues, and 71 open pull requests.
- **Repository location:** The repository is at `github.com/openenv/OpenEnv`, but some badges and links in the README point to `github.com/huggingface/OpenEnv`. Confirm the canonical location before pinning a dependency.

## Considerations

- Environments are only as useful as their reward design. Rubric composition helps, but reward hacking and reward leakage are still the main risks for RL on agent tasks.
- The Docker-image packaging makes environments reproducible but adds per-environment operational overhead at scale.
- Because the API is early, pin versions when using it for benchmarks you intend to repeat.

## See Also

- [Agent Evaluation Benchmarks](../Benchmarks/agent-benchmarks.md) — benchmark suites that OpenEnv-style environments can host or wrap
- [Designing Evaluations for AI Agents](agent-evals-design.md) — grader types and evaluation design that apply to environment-based rewards
- [AI as a Judge](ai-as-judge.md) — model-based grading, a common complement to rubric rewards
- [Evaluation Frameworks Overview](Readme.md) — other evaluation references
- [Fine-tuning](../Architecture/finetuning.md) — training methods that consume environment rollouts
- [Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md) — isolation requirements for executing untrusted agent actions during rollouts

## References

- [OpenEnv — GitHub repository](https://github.com/openenv/OpenEnv) — README, license, and integration list
- [OpenEnv documentation (Hugging Face)](https://huggingface.co/docs/openenv/index) — documentation set
- [OpenEnv environment catalog](https://huggingface.co/docs/openenv/environments) — available environments
- [OpenEnv Hub](https://huggingface.co/openenv) — published environments
