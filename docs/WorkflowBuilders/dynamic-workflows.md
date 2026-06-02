# Dynamic Workflows (Claude Code)

## Overview

Dynamic workflows are an orchestration primitive in Claude Code (v2.1.154+) in which Claude writes a JavaScript script that a background runtime executes to coordinate subagents at scale. The key architectural shift: the **orchestration plan moves into code** — Claude no longer decides turn-by-turn what to spawn next; the script holds the loop, branching, and intermediate results, while Claude's context window receives only the final answer.

Dynamic workflows are suited to tasks that need more agents than a single conversation can coordinate, or where the orchestration itself should be repeatable: codebase-wide bug sweeps, large-scale file migrations, multi-source research questions with cross-checking, and plan drafting from several independent angles.

Available on Pro, Max, Team, and Enterprise plans; requires Anthropic API, Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry access.

## Orchestration Primitives Compared

Claude Code offers four coordination options. Dynamic workflows occupy the high-scale, script-driven end of the spectrum.

| | Subagents | Skills | Agent Teams | Workflows |
|---|---|---|---|---|
| **What it is** | A worker Claude spawns | Instructions Claude follows | Lead agent supervising peer sessions | A script the runtime executes |
| **Who decides next step** | Claude, turn by turn | Claude, following the prompt | Lead agent, turn by turn | The script |
| **Intermediate results** | Claude's context window | Claude's context window | Shared task list | Script variables |
| **What's repeatable** | Worker definition | Instructions | Team definition | Orchestration itself |
| **Scale** | Few tasks per turn | Same as subagents | Handful of long-running peers | Dozens to hundreds of agents per run |
| **Interruption behaviour** | Restarts the turn | Restarts the turn | Teammates keep running | Resumable within same session |

The distinction between workflows and the other primitives is the **plan-in-code** property: with subagents and agent teams, Claude is the orchestrator, reconstructing intent from context on every turn. A workflow script codifies that intent once; the runtime drives execution from there.

## Architecture and Runtime

### Script Generation

Claude generates a JavaScript workflow script for the task when:
- The user includes `ultracode` in the prompt, or phrases the request as "use a workflow"
- `/effort ultracode` is active (Claude plans a workflow for every substantive task in the session)
- A saved workflow command (e.g., `/deep-research`) is invoked

Every run writes its script to a file under `~/.claude/projects/<session>/`. The script can be read, diffed against prior runs, or edited and relaunched.

### Execution Environment

The runtime executes the script in isolation, separate from the conversation:
- Intermediate results live in script variables, not the context window
- Up to **16 concurrent agents** per run (fewer on machines with limited CPU cores)
- Up to **1,000 agents total** per run (guards against runaway loops)
- Subagents always run in `acceptEdits` mode and inherit the session's tool allowlist
- File edits are auto-approved; shell commands and web fetches not in the allowlist may prompt mid-run

### Resumability

If a run is paused or stopped, it can be resumed within the same session: agents that completed return cached results, and the rest run live. Exiting Claude Code mid-run requires a fresh start in the next session.

### Background Execution

Runs execute in the background; the session stays responsive. Progress is visible via `/workflows` or the task panel below the input box. The `/workflows` view supports drilling into individual phases and agents, pausing/resuming, stopping individual agents, and saving the script as a reusable command.

## Bundled and Saved Workflows

Claude Code ships with one bundled workflow:

| Command | What it does |
|---|---|
| `/deep-research <question>` | Fans out web searches across multiple angles, fetches and cross-checks sources, votes on each claim, returns a cited report with uncorroborated claims filtered out |

Users can save any run's script as a project-level command (`.claude/workflows/`) shared with the repo, or a personal command (`~/.claude/workflows/`) available in every project. Saved workflows appear in `/` autocomplete alongside bundled ones and accept structured input via an `args` global.

## The Plan-in-Code Pattern

Dynamic workflows are a concrete implementation of the broader architectural insight that **moving the plan into code** enables qualitative gains, not just scale:

- **Adversarial cross-checking**: independent agents can review each other's findings before results are reported, producing more reliable output than a single-pass approach
- **Multi-angle planning**: several agents draft a plan from different starting assumptions; the script weighs them before committing to one
- **Scale without context cost**: hundreds of agent results accumulate in script variables, not the orchestrator's context window

This mirrors the "Code as Agent Harness" paradigm (Ning et al., 2026), where code provides executability, inspectability, and statefulness that pure natural-language orchestration cannot. See [Code as Agent Harness](../AgentHarness/code-as-agent-harness.md).

## Comparison with Perplexity Search as Code

Perplexity's **Search as Code (SaC)** paradigm and Claude Code's **dynamic workflows** are structurally analogous — both instantiate the same meta-pattern — but operate at different layers of the stack.

| Dimension | Perplexity Search as Code | Claude Code Dynamic Workflows |
|---|---|---|
| **What the model writes** | A Python retrieval pipeline | A JavaScript orchestration script |
| **What the code controls** | Search SDK primitives (fetch, rank, synthesize) | Subagent invocations |
| **Execution environment** | Secure compute sandbox | Isolated workflow runtime |
| **Scale** | Hundreds–thousands of retrieval ops per task | Up to 1,000 subagents per run |
| **Plan lives in** | Generated code (not model context) | Generated code (not model context) |
| **Reuse** | SDK-level (per task type) | Saveable as project or personal commands |
| **Primary domain** | Search and retrieval | General-purpose task orchestration |

Both shift control from *what the model decides turn-by-turn in context* to *what a generated script executes deterministically*. Perplexity SaC makes **retrieval primitives** programmable; Claude Code dynamic workflows make **agent coordination** programmable. They address adjacent layers of the agentic stack — SaC is the retrieval substrate a dynamic workflow might call into.

The shared architectural root is the **"code as orchestrator"** insight: tasks too large or complex to hold in a single context window are better expressed as executable scripts that the runtime drives, with the model acting as a code-generating control plane rather than a turn-by-turn decision-maker.

See [Search as Code (Perplexity)](../RAG/search-as-code.md) for the full treatment of the retrieval-layer version of this pattern.

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| Runaway cost | A single workflow can spawn hundreds of agents and consume significantly more tokens than conversational work | Run on a small slice first (one directory, one narrow question) to gauge spend before committing to a large task |
| Mid-run tool prompts | Agents that call shell commands or web fetches not in the allowlist can pause a long run | Add expected commands to the tool allowlist before starting a large run |
| Model selection | All agents default to the session model; high-capability models are expensive at scale | Ask Claude to route lower-complexity stages to a smaller model when describing the task |
| Repeatability | Ad-hoc workflows are lost when the session ends | Save runs that produce useful results as project or personal commands immediately after a successful run |
| Determinism across reruns | Script logic may produce different agent assignments on each run | Treat saved workflows as stable orchestration — avoid embedding run-specific IDs or timestamps in saved scripts |
| Quality vs. speed | Ultracode mode applies workflows to every task, increasing token use and latency | Reserve `/effort ultracode` for tasks where multi-agent cross-checking adds clear value; use `/effort high` for routine work |

## See Also

- [Search as Code (Perplexity)](../RAG/search-as-code.md)
- [Code as Agent Harness](../AgentHarness/code-as-agent-harness.md)
- [Workflow Orchestration](./orchestration.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Claude Managed Agents](../AgentPlatforms/claude-managed-agents.md)
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [Production Best Practices: Cost Management](../ProductionBestPractices/cost-management.md)

## References

- [Orchestrate subagents at scale with dynamic workflows — Claude Code Docs](https://code.claude.com/docs/en/workflows) — official documentation for Claude Code dynamic workflows; covers the orchestration model, runtime constraints, bundled workflows, ultracode mode, and reuse patterns.
