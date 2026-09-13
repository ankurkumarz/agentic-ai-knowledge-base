---
type: Standard
title: "DESIGN.md — Visual Identity Format for Coding Agents"
description: "DESIGN.md is a file format specification that gives coding agents a persistent, structured understanding of a product's visual identity by combining machine-readable design tokens with human-readable design rationale."
tags: [standards, design-system, coding-agents, agentic-ai, google]
timestamp: 2026-09-13T00:00:00Z
---

# DESIGN.md — Visual Identity Format for Coding Agents

## Overview

**DESIGN.md** is an open format specification developed by Google Labs (`google-labs-code`) that provides coding agents with a persistent, structured understanding of a product's visual identity. It is the design-system analogue to `AGENTS.md` or `README.md` — a well-known file that agents read to understand the conventions of a project, in this case focused on UI/UX consistency.

The format solves a common problem in AI-assisted frontend development: without a canonical source of design truth, coding agents generate UIs that are inconsistent with a product's color palette, typography, spacing, and component conventions. DESIGN.md gives agents exact token values and the rationale for how to apply them.

## File Structure

A DESIGN.md file has two distinct layers:

| Layer | Format | Purpose |
|---|---|---|
| **YAML front matter** | Delimited by `---` fences at the top of the file | Machine-readable design tokens with exact values |
| **Markdown body** | Organized into `##` sections | Human-readable design rationale explaining *why* values exist and *how* to apply them |

The tokens are the normative values. The prose provides context that prevents agents from applying tokens mechanically in the wrong situations.

## Token Schema

```yaml
version: <string>           # optional, current: "alpha"
name: <string>
description: <string>       # optional
omitted: <string[]>         # optional — sections intentionally omitted
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <token-name>: <string | token reference>
```

### Token Types

| Type | Format | Example |
|---|---|---|
| Color | Any CSS color (hex, rgb(), oklch(), named) | `"#1A1C1E"`, `"oklch(62% 0.18 250)"` |
| Dimension | number + unit (px, em, rem) | `48px`, `-0.02em` |
| Token Reference | `{path.to.token}` | `{colors.primary}` |
| Typography | Object with `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` | See example below |

### Minimal Example

```yaml
---
name: Heritage
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 8px
  md: 16px
---

## Overview

Architectural Minimalism meets Journalistic Gravitas. The UI evokes a
premium matte finish — a high-end broadsheet or contemporary gallery.

## Colors

- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Tertiary (#B8422E):** "Boston Clay" — the sole driver for interaction.
```

## Tooling

The spec ships with a CLI validator:

```bash
npx @google/design.md lint DESIGN.md
```

This validates the file against the spec, checks for broken token references, evaluates WCAG contrast ratios, and returns structured JSON findings that agents can act on programmatically.

A diff command detects regressions between design system versions:

```bash
npx @google/design.md diff DESIGN.md DESIGN-v2.md
```

The diff output reports token-level additions, removals, and modifications — and whether any change constitutes a regression in accessibility findings.

## Relationship to Coding Agent Workflows

DESIGN.md is most effective when placed at the repository root alongside other agent-instruction files. Coding agents (Claude Code, Kiro, Cursor, Copilot, etc.) that read DESIGN.md at session start produce UI code that matches the product's design system without requiring repeated inline instructions.

This positions DESIGN.md as part of a broader family of **agent steering files**:

| File | Purpose |
|---|---|
| `README.md` | Project overview for humans and agents |
| `AGENTS.md` / `CLAUDE.md` | Agent behavioral instructions and tool permissions |
| `DESIGN.md` | Visual identity and design token specification |
| `.kiro/steering/*.md` | IDE-level context steering for Kiro |

## Maturity and Status

As of mid-2026, the DESIGN.md spec is at **alpha** maturity. The format is functional and tooled (lint + diff CLI), but token schema and section conventions may evolve. The repository is hosted at `github.com/google-labs-code/design.md`.

## Best Practices

| Challenge | Recommendation |
|---|---|
| Token drift | Use `design.md diff` in CI to catch unintended token changes before merge |
| Accessibility | Run `design.md lint` to surface WCAG contrast failures before agents propagate them across components |
| Prose quality | Write rationale sections (Colors, Typography) that explain *intent* — agents use prose to resolve ambiguity in token application |
| Adoption | Place DESIGN.md at the repo root so all coding agents pick it up automatically without explicit instruction |
| Version pinning | Pin the `@google/design.md` CLI version in CI to avoid spec drift breaking validation pipelines |

## See Also

- [AGENTS.md Standard](./agents-md.md)
- [Agent Skills / SKILLS.md](./skills.md)
- [AI Coding Agents Overview](../AICodingAgents/ai-coding-agents.md)
- [Claude Code](../AICodingAgents/claude-code.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [AllThingsGoogle](../AllThingsGoogle/README.md)

## References

- [google-labs-code/design.md on GitHub](https://github.com/google-labs-code/design.md) — format specification, token schema, and CLI tooling
