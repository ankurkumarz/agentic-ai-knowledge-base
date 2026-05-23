# Anthropic — Agentic AI Overview

## Overview

Anthropic builds the Claude model family with a focus on safety, interpretability, and reliable long-horizon task performance. Their public engineering writing and Model Context Protocol (MCP) specification are widely referenced reference points for context engineering and agent tool use across the industry.

## Key Offerings

| Product / Area | One-liner | Wiki Reference |
|---|---|---|
| Claude Code | Anthropic's agentic coding CLI/IDE — swarm orchestration, KAIROS daemon, 44 feature flags; architecture partially revealed via 2026 source leak | [AgenticFrameworks/ai-coding-agents.md](../AgenticFrameworks/ai-coding-agents.md) |
| Claude Managed Agents | Hosted agent execution platform with persistent memory, dreaming (scheduled memory consolidation), outcomes (self-grading loop), and multiagent orchestration — Harvey reported 6× task completion improvement | [AgentPlatforms/claude-managed-agents.md](../AgentPlatforms/claude-managed-agents.md) |
| Claude Managed Agents — Dreaming | Scheduled between-session memory curation inspired by hippocampal sleep consolidation; merges patterns, removes outdated facts, surfaces team-wide learnings; research preview | [AgentPlatforms/claude-managed-agents.md](../AgentPlatforms/claude-managed-agents.md) |
| Claude Managed Agents — Outcomes | Self-grading loop: developer writes plain-language rubric, isolated grader agent scores output, agent iterates; up to +10 pp task success over baseline prompting | [AgentPlatforms/claude-managed-agents.md](../AgentPlatforms/claude-managed-agents.md) |
| Claude Managed Agents — Multiagent Orchestration | Lead agent delegates to parallel specialist agents, each with own model/prompt/tools, on a shared filesystem with durable event log | [AgentPlatforms/claude-managed-agents.md](../AgentPlatforms/claude-managed-agents.md) |
| Context Engineering Guidance | Anthropic's practical guidance on managing context windows for long-running agents | [ContextEngineering/anthropic.md](../ContextEngineering/anthropic.md) |
| Context Management API Primitives | First-party API primitives for compaction, tool-result clearing, and cross-session memory — empirically benchmarked on a 328K-token research corpus | [ContextEngineering/anthropic.md#context-management-api-primitives-cookbook](../ContextEngineering/anthropic.md) |
| Model Context Protocol (MCP) | Open standard for tool and resource exposure to LLMs; co-developed by Anthropic | [Standards/mcp.md](../Standards/mcp.md) |
| Building Effective Agents | Anthropic's canonical reference on agent design principles and patterns | [ProductionBestPractices/README.md](../ProductionBestPractices/README.md) |
| Claude Models (Production) | Best practices for using Claude in production agentic workloads | [ProductionBestPractices/security.md](../ProductionBestPractices/security.md) |
| Agent Skills / SKILLS.md | Reusable, slash-command-triggered workflow definitions for Claude Code agents; SKILLS.md convention packages repeatable engineering procedures as version-controlled, shareable task modules | [Standards/skills-md.md](../Standards/skills-md.md) |

## See Also

- [Claude Managed Agents](../AgentPlatforms/claude-managed-agents.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Production Best Practices — Context Engineering](../ProductionBestPractices/context-engineering.md)
- [Agentic AI Industry Standards](../Standards/mcp.md)
- [Agent Memory Management](../AgentMemory/README.md)
- [Self-Learning Agents Reference Architecture](../ReferenceArchitecture/self-learning-agents.md)
