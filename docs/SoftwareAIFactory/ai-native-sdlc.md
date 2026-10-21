---
type: Playbook
title: AI-Native SDLC
description: Anthropic's six-stage playbook for rebuilding the software development lifecycle around agentic AI, from intent capture to autonomous loop closure.
tags: [software-ai-factory, agentops, sdlc, agentic-ai, anthropic]
timestamp: 2026-10-20T00:00:00Z
---
# AI-Native SDLC

## Overview

Anthropic's AI-native SDLC playbook reimagines the software development lifecycle (SDLC) as a **loop rather than a linear phase sequence**, with agentic AI embedded at every stage. The playbook's premise is that code generation is no longer the bottleneck — agents can produce diffs in hours where humans took months — so the bottleneck has migrated to the human-speed stages around build (plan, review/test, deploy) and to governance controls (security review, compliance sign-off, change boards) that were sized for human output. The playbook rebuilds process and governance around that new reality while keeping humans accountable for every judgment call.

The source is [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) by Louis Claxton (Anthropic, Aug 21, 2026), reflecting Applied AI team best practices from customer work. This page represents Anthropic's recommendations, not universal practice; the sigma bands, suggested eval-suite size, and expected speed improvements are illustrative configuration, not measured outcomes.

## The Core Idea: The Artifact Chain

The unifying mechanism is the **committed artifact**. Each stage ends by committing one to version control; the next stage begins by reading it:

| Stage | Traditional | AI-Native | Artifact |
|---|---|---|---|
| Plan | Requirements by committee, workshops, sign-offs | Claude synthesizes intent directly from sources | `intent.md` |
| Design | Spec written by analysts, parsed by designers | Requirements + design in one working session with the agent | `spec.md` |
| Build | Tests/code handwritten, docs after | Agent-driven plan, code, tests; institutional knowledge as files | `plan.md`, diff, `CLAUDE.md`, skills |
| Test | QA gates at stage boundaries | Continuous evals woven through implementation | Eval suite, feedback loop |
| Deploy | Humans review every line; governance in review cycles | Agentic review layers, human review for critical code, hooks as approval gates | PR, review findings |
| Maintain | Humans watch production | Agents monitor; breaches write back to intent | `intent.md` (loop re-entry), incident record |

For the early stages, `.md` files dominate because both a product owner and an agent can read and act on the same file. From Build onward the artifact is code and its records. The chain of commits is also the audit trail: who asked for what, what the agent produced, and who approved it.

Humans remain accountable for every decision that requires judgment. Human attention shifts along with the artifacts to be reviewed — from generating them to reviewing what the agent flagged.

## Six Stages and Plays

Each play lists what changes, prerequisites, concrete implementation steps, governance considerations, and leading/lagging measures. Plays are non-linear and have a dependency graph; each ends with an artifact that triggers the next stage.

### Stage 1 — Plan: Capture as `intent.md`

An idea (person, ticket, or incident alert) becomes a version-controlled `intent.md` in the originator's own terms: what is wanted, why, and under which constraints. The originator brainstorms with Claude, writes the proto-spec, corrects misunderstandings, and commits the file to a shared, version-controlled home (often an `intent/` folder in the product repo). A connector to the VCS lets non-engineers commit markdown through claude.ai or Cowork without direct git use.

### Stage 2 — Design: Requirements and design as one session

Claude takes the accepted `intent.md` and produces a requirements + design spec, guided by the organization's skills for brand, security, compliance, and UX. The product owner reviews but doesn't write the spec. Front-end work flows through Claude Design (beta): mock the design from `intent.md`, iterate, export to Claude Code. Flagged concerns are worked through with the policy owner before engineering sees the spec.

### Stage 3 — Build

Several plays compose:

- **Claude Code plan mode as the default starting point.** The engineer starts in plan mode, gives Claude the `spec.md`, and lets it interview them until the plan is implementable by an engineer who never saw the conversation. The approved plan is committed as `plan.md` and the eventual diff is checked against it in PR review. When implementation departs from the plan, update `plan.md` in the same commit; a hook can enforce synchronization.
- **Claude Code on auto mode.** Once the guardrails mature (tuned `CLAUDE.md`, skills encoding policy, hooks blocking unsafe actions, a test suite Claude can run), auto-accept becomes the default for routine work: tight `spec.md`, small blast radius, tested code. Auto mode also enables parallelism via worktrees and is fundamental to running the SDLC autonomously.
- **`CLAUDE.md`** gives Claude the context a new joiner would need: conventions, commands, architecture, and recurring mistakes. Rules of thumb: run `/init` to generate a starting version, cut it down to what a new joiner needs on day one, check it into git, and when Claude makes a mistake twice, put the correction in `CLAUDE.md`. Keep it under a page.
- **Skills as institutional knowledge.** A skill is a folder with `SKILL.md` whose frontmatter says when it triggers. Skills are version-controlled, applied broadly, updated centrally when policy changes. Write a skill for knowledge that must be applied consistently. A skill is advisory; a policy that must always hold needs a deterministic control behind it (a hook).
- **Hooks as build-time guardrails.** Hooks block edits to protected paths, run formatter/linter after file edits, keep credentials out of the diff. Build-phase hooks should be fast and scoped to the changed file; heavier checks belong at commit or PR.
- **Parallel sessions and subagents.** A parallel session is a separate Claude Code instance in its own git worktree on a separate task; a subagent is a scoped helper inside one session with its own context window and tool limits (defined in `.claude/agents/*.md`). Anthropic suggests two to three parallel sessions as a sensible starting point; the ceiling is how many streams one person can review.

### Stage 4 — Test

- **Give Claude a feedback loop.** The session must be able to check its own work before an engineer sees it: tests, build, screenshot diff. For bug fixes, write the failing test first (reproduce → confirm → commit → make pass without editing the test). A hook can block the agent from editing test files during a fix so the agent cannot weaken its own check.
- **Continuous evals in CI.** Evals are the AI-native equivalent of stage-gate QA. Anthropic recommends a suite of 20–50 real tasks that runs whenever the agent's configuration (`CLAUDE.md`, skills, hooks) changes — configuration steers the agent and deserves the regression testing code gets. Gate merges on pass rate. Each production incident becomes an eval.

### Stage 5 — Deploy

- **AI in the PR review loop.** Claude reviews incoming PRs against `REVIEW.md` (bugs, security, compliance vs. `spec.md`/`plan.md`, design principles) and addresses review comments on its own PRs via `@claude` mentions. Findings don't approve or block on their own; branch protection still requires approval from a human code owner (the writing agent has no route to approve its own code). Human review is risk-tiered — reserved for regulated and critical code — but the code-owner approval remains the gate.
- **Hooks as approval gates.** A hook can allow, ask, or block — the "ask" path is the release gate: production deploys require a named release authorization. Team hooks live in `.claude/settings.json` in git; non-negotiable hooks live in managed settings owned by the platform admin. A block message should explain itself and route to approval.
- **Managed settings for a regulated enterprise** lock down the agent's tool surface (Anthropic presents this as a tailored example, not a universal security guarantee — every deny trades against capability and the right balance depends on the data classification of the repo): `permissions.deny` blocks secrets and arbitrary network egress; `sandbox` closes the gap that tool-level permissions cannot — a tool-level deny on WebFetch does not stop a shell command from reaching the network, so the OS-level sandbox domain allowlist blocks egress outright, denies reads on credential files (`~/.ssh`, `~/.aws/credentials`), and strips named secrets from every sandboxed command's environment; `failIfUnavailable` and `allowUnsandboxedCommands` make the sandbox a hard gate; `disableBypassPermissionsMode` and `allowManagedPermissionRulesOnly` prevent any engineer, project file, or CLI flag from widening rules; `allowManagedHooksOnly`, `disableSideloadFlags`, and `strictKnownMarketplaces` mean every skill/hook/MCP server arrived through the organization's approved plugin marketplace; `requiredMinimumVersion` refuses to start on an unassessed build.
- **CI/CD integration and deployment.** Claude Code runs non-interactively inside the pipeline (`claude -p`) for judgment steps — triage failed builds, summarize flaky tests, draft changelogs. Execution is sandboxed with short-lived scoped tokens and no standing production credentials. Deployment is exposed through MCP as tools scoped per environment. Autonomy is tiered by environment: dev = free, staging = middle, production = agent prepares, release manager authorizes, a hook enforces. Rollback is the most rehearsed path in the pipeline.

### Stage 6 — Maintain: Closing the loop

- **Trigger → agent → intent.md.** A deterministic script (no model in the detection path) watches production for control-band breaches using mean/standard deviation with Western Electric-style rules. Response tiers are version-controlled config (`bands.yaml`) — Anthropic's illustrative example is 1σ = log, 2σ = diagnose read-only, 3σ = act via PR or pre-approved runbook. Claude runs stateless, writes its diagnosis as `intent.md` in the Stage 1 format, and the finding flows through the pipeline like anything else. Stage 6 places an **independent confidence gate between stages** — a deterministic check or an adversarial reviewing agent decides whether the previous stage's output continues or is escalated to a human. Dismissals tune the bands to reduce noise.
- **Recurring codebase scans.** A security scan is a point-in-time statement about a codebase under a particular model — both halves go stale. The AI-native answer: run on schedule without a human in the invocation path. Claude Security (hosted, public beta) scans connected GitHub repos on Anthropic infrastructure, validates findings before reporting, attaches confidence ratings. Bounded fixes go through the PR gate; anything wider becomes an `intent.md`.
- **Claude on call with Claude Tag** (public beta, Slack). Claude Tag makes Claude a member of incident channels under its own identity. Incidents arriving via Slack get a first responder; the channel history is the audit trail. Claude can verify the metric is back to baseline, write the post-mortem to a version-controlled lessons file, and open a PR for bounded fixes or write an `intent.md` for larger work.

## Cross-cutting Themes

### Bottleneck migration

When build collapses to hours, the bottleneck moves left and right of build. Plan, review/test, and deploy still run at human speed; governance costs increase because exceptions still route through committees that meet weekly. The playbook's response is to make the surrounding stages agentic too, while keeping human judgment at the gates.

### Source of truth for legacy systems

Existing SDLC tooling (Jira, ServiceNow, requirements tools with regulatory traceability) is hard to displace because auditors and other teams depend on it. The AI-native SDLC fits around it: name **one system as the source of truth** per artifact, with everything else holding a copy or a link. Options: repo as source of truth (cleanest for engineering-led orgs), legacy system as source of truth (markdown artifacts are working copies; Claude writes back through an MCP connector), or linkage as the minimum bar (both records carry each other's ID/commit SHA).

### Skills vs. hooks (advisory vs. deterministic)

A skill makes a violation rare; a hook makes it close to impossible. Skills are the policy-shaped input; hooks are the enforcement layer that runs on every matching action. Policies that must always hold get both.

### Separation of duties

The agent that wrote the code has no route to approve it. Approval always comes from a human through branch protection, informed by the agent's findings.

### Measures of effectiveness

Each play pairs a leading indicator (speed of the artifact move) with a lagging indicator (quality downstream). Examples:

| Play | Leading indicator | Lagging indicator |
|---|---|---|
| `intent.md` capture | Time from first conversation to committed `intent.md` | Survival rate (share accepted into Design) |
| Requirements + design | `intent.md` commit → `spec.md` commit elapsed time | `spec.md` commits after the first `plan.md` commit (rework) |
| Plan mode | Share of changes merging from first implementation pass | Rework cycles per change; diff still matching `plan.md` |
| `CLAUDE.md` | How often Claude repeats a mistake it should have caught | Time to first merged PR for a new team member |
| Skills | Policy approval → updated skill merging time | PR review findings citing the policy |
| Parallel sessions | Concurrent sessions per engineer (review quality held) | Changes merged per engineer per week, vs. rework rate |
| Feedback loop | First-pass CI success rate | Review time per PR; change failure rate |
| Continuous evals | Eval pass rate over time; incident → permanent eval elapsed time | Regressions caught in CI vs. production |
| PR review | Time to first review; share of review comments resolved without human branch touch | Defects caught pre-merge vs. escaping to production |
| Hooks as gates | Time spent waiting per gate | Gate violations reaching production |
| CI/CD | Share of pipeline failures triaged without paging a human | DORA measures |
| Closing the loop | Time from band breach to `intent.md` in triage queue | Share of findings that become merged fixes; repeat incidents |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Human-speed stages around build | Plan, review, deploy still run at human speed while build collapses | Make each surrounding stage agentic; concentrate human attention at gates reviewing what the agent flagged |
| Governance that doesn't keep pace | Security review queues sized for human output; code ships under-reviewed or queues build | Make checks deterministic (hooks, evals) and run them as the agent acts; tier autonomy by environment |
| Institutional knowledge lives in heads and wikis | Not reviewable, not versioned, not applied consistently | Move to `CLAUDE.md` (per-repo working knowledge) and skills (policies that must apply consistently); hook for hard guarantees |
| Review capacity at agent output volume | A human reading every line of every PR cannot keep up | Layer agentic review passes with severity-ranked findings; reserve human review for regulated/critical code |
| Maintaining an audit trail | Manual handoffs lose provenance; committees lack timestamped record | Chain of commits IS the audit trail; each stage commits an artifact the next reads |
| Legacy tooling is hard to displace | Jira/ServiceNow/regulatory traceability tools already accepted by auditors | Name one source of truth per artifact; use linkage as the minimum bar when transitioning |
| Skills drift from official policy | A skill's text can become stale relative to the policy owner's source | Policy owner signs off skill changes; PR review findings citing the policy should fall to zero if the skill is live |
| Detection of drift and silent regression | Monitoring often relies on human eyes or lagging dashboards | Deterministic script + Western Electric rules on a stable metric; response tiers in version-controlled `bands.yaml` |
| Security scan freshness | Point-in-time scans go stale as code and models both change | Recurring scheduled scans; each finding validated with confidence rating; fixes through the normal PR gate |

## See Also

- [OpenAI's Agentic Software Factory](openai-software-factory.md): separate PR, rollout, and incident-action approval boundaries.
- [Building Your Own Software Factory](building-your-own-software-factory.md): Cursor operating-model workshop, with a different low-risk PR approval example.
- [Software AI Factory](README.md): category scope and platform selection.
- [Factory AI](factory-ai.md): multi-surface Droid workflows and headless execution.
- [Devin](devin.md): delegated engineering tasks with verifiable outcomes.
- [OpenHands](openhands.md): agent control center, execution backends, and software-agent SDK.
- [Claude Code](../AICodingAgents/claude-code.md) — the primary agentic coding tool the playbook is built around
- [Claude Managed Agents](../AgentPlatforms/claude-managed-agents.md) — Anthropic's hosted agent execution platform; the playbook's Stage 6 uses a similar headless, non-interactive agent invocation pattern via CI runners or the Agent SDK
- [Agent Skills / SKILLS.md](../Standards/skills.md) — the skill convention this playbook leans on for institutional knowledge
- [Loop Engineering (Claude Code)](../AgentHarness/loop-engineering.md) — the same loop-closing pattern applied to Claude Code-specific automations
- [GenOps – Evolution of MLOps for GenAI](../AgentOps/genops.md) — the broader operational evolution this playbook extends to the SDLC
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)
- [Production Best Practices — Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Anthropic — Agentic AI Overview](../AllThingsAnthropic/README.md)
- [Agent Observability](../Observability/Readme.md) — SDLC observability patterns (verification evidence, per-gate timing, drift detection)
- [Production Best Practices — Observability](../ProductionBestPractices/observability.md)
- [Designing Evaluations for AI Agents](../EvaluationFrameworks/agent-evals-design.md) — the eval-design counterpart to the playbook's continuous evals
- [Anthropic Sandbox Runtime (`srt`)](../SecurityFrameworks/anthropic-sandbox-runtime.md) — a related OS-level isolation runtime for MCP-invoked processes

## References

- [Inside OpenAI's agentic software factory](https://newsletter.pragmaticengineer.com/p/openai-software-factory): related internal-practice case study; does not replace Anthropic's human code-owner requirement.
- [Building your own software factory](https://youtu.be/rnDm57Py54A?is=bkOS_zVfmSgXgxSz): related Cursor workshop; its delegated low-risk approval example is not the human code-owner gate described in this Anthropic playbook.
- [The AI-native SDLC playbook — Anthropic](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) — canonical source; Louis Claxton, Aug 21, 2026
- [Claude Code settings reference](https://code.claude.com/docs/en/settings) — managed settings, permissions, sandbox keys referenced by the playbook
- [Claude Code hooks guide](https://code.claude.com/docs/en/hooks-guide) — the approval-gate mechanism
- [Claude Code skills docs](https://code.claude.com/docs/en/skills) — skill authoring and distribution
- [Managed MCP](https://code.claude.com/docs/en/managed-mcp) — central control of the agent's tool surface
