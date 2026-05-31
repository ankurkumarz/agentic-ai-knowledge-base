# Agent Skills / SKILLS.md

## Overview

**Agent Skills** (also referred to by the emerging convention **SKILLS.md**) are reusable, shareable workflow definitions that allow Claude Code agents — and by extension any compatible agentic harness — to execute repeatable engineering procedures on demand via slash commands. Introduced by Anthropic in 2025, Skills act as first-class, version-controlled task modules: teams encode their best practices once and any agent in the project can invoke them consistently.

Where `CLAUDE.md` / `AGENTS.md` govern *always-on* agent behavior, Skills govern *on-demand* task execution. The two conventions are complementary: CLAUDE.md sets persistent instructions and constraints; SKILLS.md packages specific, triggerable workflows.

## Key Concepts

### What a Skill Is

A Skill is a markdown document (or a named section within one) that contains:
- A **name** — the slash command trigger (`/skill-name`)
- A **description** — one-line summary surfaced in `/help` output
- **Instructions** — the ordered steps Claude must follow when the skill is invoked

Skills are stateless by default. Each invocation starts fresh, reading the current state of files, tests, and context rather than assuming prior state.

### Invocation Model

Users trigger skills with a slash command:

```
/skill-name [optional arguments]
```

Claude Code discovers the matching skill definition at session start, loads it into context, and executes the declared steps when the user types the trigger. Arguments are passed as free-text and referenced in the instructions as `$args` or described contextually.

### Scoping

| Scope | Location | Visibility |
|---|---|---|
| Project | `.claude/skills/<name>.md` | All team members via version control |
| User global | `~/.claude/skills/<name>.md` | Single user, all projects |
| Inline (CLAUDE.md) | Defined within `CLAUDE.md` or `SKILLS.md` at repo root | Project-wide, single file |

Project-scoped skills are the recommended approach for teams: skills live next to the code they operate on, are reviewed in pull requests, and evolve alongside the codebase.

## Skill File Format

A skill is a markdown file (or named section) following this structure:

```markdown
# <Skill Name>

<One-line description of what this skill does.>

## Instructions

When the user invokes /<skill-name> [describe argument handling]:

1. <First step>
2. <Second step — reference $args or specific files as needed>
3. <Continue…>

Report results to the user after each major step.
```

**Rules for well-formed skill files:**
- The H1 heading becomes the slash command name (lowercased, spaces replaced with hyphens).
- Instructions must be unambiguous enough for the agent to execute without clarifying questions.
- Skills should reference specific tools, paths, or commands rather than general guidance.
- Avoid instructions that depend on session memory — skills must be self-contained.

### Example: Code Review Skill

```markdown
# review

Run a structured code review of the current diff.

## Instructions

When the user invokes /review [optional focus area]:

1. Run `git diff main...HEAD` to gather the full diff.
2. If $args specifies a focus (e.g. "security", "performance"), weight findings accordingly.
3. Check for correctness bugs, missing error handling at system boundaries, and obvious security issues (injection, XSS, unvalidated input).
4. Report findings as a numbered list ordered by severity. For each finding include: file, line range, issue, and a one-line fix suggestion.
5. End with a summary: total findings by severity, and an overall recommendation (approve / approve with minor changes / request changes).
```

### Example: Deploy Skill

```markdown
# deploy

Run pre-deploy checks and deploy to staging.

## Instructions

When the user invokes /deploy [environment]:

1. Run the full test suite. Stop and report if any tests fail.
2. Run `npm run build` (or equivalent). Stop and report build errors.
3. Check that all required environment variables are set for $args environment (default: staging).
4. Execute the deploy command for $args: `./scripts/deploy.sh $args`.
5. Tail the deploy log for 60 seconds and surface any ERROR lines.
6. Report final status: deployed / failed, with the URL if successful.
```

## Architecture and Discovery

### How Claude Discovers Skills

At session start, the agent harness scans the configured skill directories and injects a skill manifest into the system context. This manifest lists available slash commands and their descriptions, enabling `/help` to enumerate them without loading full instruction bodies.

When a user types a slash command, the harness:
1. Matches the command against the manifest.
2. Loads the full skill instruction body into the current context window.
3. Passes control to Claude with the user's arguments.
4. Claude executes the steps, using available tools (Bash, Read, Edit, etc.) as directed.

### Relationship to CLAUDE.md and AGENTS.md

| File | Purpose | Trigger |
|---|---|---|
| `CLAUDE.md` / `AGENTS.md` | Persistent agent instructions, constraints, coding style | Always active |
| `SKILLS.md` / `.claude/skills/*.md` | Triggerable task workflows | On-demand, slash command |
| `HOOKS` (settings.json) | Event-driven automation (pre/post tool calls) | Event-driven |

Skills and persistent instructions do not conflict: CLAUDE.md establishes the agent's baseline behavior, while skills encode specific procedures on top of that baseline.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Idempotency | Skills may be invoked multiple times on the same state | Write instructions so re-running produces the same result; check for existing output before writing |
| Argument handling | Freeform arguments can be ambiguous | Document the expected argument format explicitly in the instructions; provide a default when $args is absent |
| Scope creep | Skills that try to do too much produce unpredictable results | One skill, one purpose; split complex workflows into composable sub-skills |
| Stale instructions | Skills written for an old repo structure silently fail | Version skills with the codebase; review skill files in the same PR as structural changes |
| Discoverability | Teams don't know what skills exist | Maintain a `skills/README.md` with a table of all available skills and their triggers |
| Testing skills | Hard to verify skill behavior without running them | Write a companion test skill (`/test-skill <name>`) that exercises the skill on a fixture branch |
| Secret handling | Skills that deploy or call APIs risk leaking credentials in logs | Never hard-code secrets in skill files; reference environment variables by name, not value |

## Use Cases

### Software Development
- `/review` — structured code review with configurable focus areas
- `/test` — generate or run tests for modified files
- `/docs` — update documentation to reflect recent code changes
- `/refactor` — apply a defined refactoring pattern to a specified module

### DevOps and Deployment
- `/deploy [env]` — pre-deploy checks + deploy to named environment
- `/rollback [version]` — revert to a specific release with validation
- `/migrate` — run database migrations with pre/post checks
- `/infra-check` — validate infrastructure configuration before apply

### Security and Quality
- `/security-review` — scan diff for OWASP top-10 and secrets
- `/lint-fix` — run linters and auto-apply safe fixes
- `/depcheck` — audit dependencies for known vulnerabilities

### Knowledge and Process
- `/standup` — generate a standup summary from recent commits and open PRs
- `/estimate` — produce a time/complexity estimate for a described task
- `/onboard` — walk a new team member through the project setup checklist

## Provider Skills Repositories

Leading AI and cloud providers maintain public repositories of ready-made skills that teams can import directly into compatible harnesses. The table below lists the canonical source repositories as of 2025–2026.

| Provider | Repository / Install Command | Notes |
|---|---|---|
| Anthropic | [github.com/anthropics/skills](https://github.com/anthropics/skills) | Reference collection for Claude Code; covers code review, deploy, security, and docs workflows |
| Google | [github.com/google/skills](https://github.com/google/skills) | Skills for Gemini CLI and Google ADK-based harnesses |
| Microsoft | [github.com/microsoft/azure-skills](https://github.com/microsoft/azure-skills) | Skills targeting Azure AI Agent Service and Semantic Kernel toolchains |
| OpenAI | [github.com/openai/skills](https://github.com/openai/skills) | Skills for OpenAI Codex and Responses API-based agents |
| AWS | `npx skills add aws/agent-toolkit-for-aws/skills` | Installed via the Skills CLI from the AWS Agent Toolkit registry; targets Strands Agents and Kiro |
| Cloudflare | [github.com/cloudflare/skills](https://github.com/cloudflare/skills) | Skills for Cloudflare Workers AI and edge-deployed agents |
| Vercel | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) | Skills targeting AI SDK and Vercel-hosted agent deployments |

### Installing skills from a provider repository

Most repositories follow the same pattern — clone or install via the Skills CLI, then reference the skill by name:

```bash
# GitHub-hosted (any provider)
git clone https://github.com/<org>/skills .claude/skills/<provider>

# AWS registry via npm-style CLI
npx skills add aws/agent-toolkit-for-aws/skills

# Selective install — copy a single skill file
cp .claude/skills/anthropics/review.md .claude/skills/review.md
```

Provider skills are community-maintained and evolve independently of the harness. Pin to a specific commit or tag in production to prevent unreviewed changes from loading into the agent context at session start.

## Integration with Agent Harnesses

Skills are a first-class concept in the Claude Code harness but are designed to be portable. Any harness that:
1. Reads a skill manifest at session start
2. Injects skill instructions into context on command match
3. Passes user arguments to the agent

…can implement the SKILLS.md convention. This makes skills a candidate for standardization alongside AGENTS.md and MCP as part of the emerging agentic AI interoperability layer.

## Relationship to MCP and Tool Use

Skills orchestrate *how* an agent uses its available tools — they do not add new tools. MCP servers extend the agent's tool set (new capabilities); Skills direct the agent's existing capabilities toward specific workflows. A deploy skill, for example, might call Bash tools, Read tools, and MCP-provided deployment API tools — the skill is the workflow, MCP provides the primitives.

## See Also

- [AGENTS.md Standard](./agents-md.md)
- [Model Context Protocol](./mcp.md)
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md)
- [Claude Managed Agents](../AgentPlatforms/claude-managed-agents.md)
- [Anthropic Overview](../AllThingsAnthropic/README.md)
- [Context Engineering — Anthropic](../ContextEngineering/anthropic.md)
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)
- [AI Agent Skill Security Scanners](../SecurityFrameworks/skill-scanners.md) — Scan skills for prompt injection, data exfiltration, and malicious patterns before installation

## References

- [Claude Skills — Announcement](https://claude.com/blog/skills) — Anthropic blog post introducing Agent Skills for Claude Code
- [Claude Skills Explained](https://claude.com/blog/skills-explained) — Deep-dive on the Skills architecture, invocation model, and scoping
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) — Comprehensive authoring guide covering format, best practices, and examples (Anthropic, 2025)
