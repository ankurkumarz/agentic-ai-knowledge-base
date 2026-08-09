---
type: Standard
title: "Agent Plugins Specification"
description: "Agent Plugins is an open, vendor-neutral specification (v1.0.0, August 2026) that packages Agent Skills and MCP servers into a single portable plugin directory readable by any conformant agent client."
tags: [standards, plugins, skills, mcp, interoperability, agentic-ai]
timestamp: 2026-08-09T00:00:00Z
---

# Agent Plugins Specification

## Overview

**Agent Plugins** is an open, vendor-neutral specification for packaging reusable components that extend AI agents into distributable plugins. Version **1.0.0** was published in August 2026 by a Technical Steering Committee of Core Maintainers from **Amazon, Cursor, Microsoft, OpenAI, and Vercel**, with **Google** announcing its participation as a Core Maintainer on the Google Developers Blog.

The problem it addresses is fragmentation at the *packaging* layer rather than the protocol layer. [Agent Skills](./skills.md) standardized how procedural knowledge is written (`SKILL.md` with frontmatter), and [MCP](./mcp.md) standardized how tools and data are exposed to a model. Neither defined how a vendor ships *both together* as one installable unit — so each client (Claude Code, Cursor, VS Code, Codex, Kiro) invented its own plugin manifest, and a Railway or Supabase integration had to be repackaged per host. Agent Plugins defines that container and nothing more:

> "A plugin is a directory rooted at a single filesystem location" with a manifest at `plugin.json`.

The design intent is minimalism. Components are discovered from **fixed filesystem locations**, not enumerated inline in configuration, and the manifest schema is **closed** — clients cannot extend the top level with proprietary keys.

## Package Structure

```text
my-plugin/
├── plugin.json              # REQUIRED — the manifest
├── skills/                  # Optional — portable Agent Skills
│   └── summarize/
│       ├── SKILL.md
│       ├── scripts/
│       │   └── analyze.sh
│       └── references/
│           └── checklist.md
├── mcp.json                 # Optional — MCP server declarations
├── com.example.client/      # Optional — client-specific namespace
│   └── hooks/
├── LICENSE
└── CHANGELOG.md
```

The smallest valid plugin is a directory containing only `plugin.json`. The smallest *useful* one adds a single skill:

```text
hello-plugin/
├── plugin.json
└── skills/
    └── greet/
        └── SKILL.md
```

**Discovery rules:**

| Component | Location | Depth |
|---|---|---|
| Agent Skills | `skills/*/SKILL.md` | One level deep only |
| MCP servers | `mcp.json` at plugin root | Root only |
| Client-specific extras | `<reverse.domain.namespace>/` directories | Client-owned and client-documented |

Missing component locations are **non-fatal** — a plugin with no `skills/` and no `mcp.json` still loads.

## The `plugin.json` Manifest

| Field | Required | Type | Meaning |
|---|---|---|---|
| `$schema` | Yes | string | Must be `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` |
| `name` | Yes | string | 1–64 chars, lowercase alphanumeric plus `-` and `.`, no consecutive separators (e.g. `my-plugin`, `acme.tools`, `lint3r`) |
| `version` | No | string | Semantic Versioning recommended; used for update detection and cache staleness |
| `description` | No | string | Brief statement of purpose |
| `author` | No | object | Optional `name`, `email`, `url` |
| `homepage` | No | string | Documentation URL |
| `repository` | No | string | Source repository URL |
| `license` | No | string | SPDX identifier recommended |
| `keywords` | No | string[] | Discovery and search tags |
| `extensions` | No | object | Client-specific data keyed by reverse-domain namespace |

**The schema is closed.** `hooks`, `agents`, `commands`, `mcpServers`, and `lspServers` must **not** appear at the top level. Client-owned capabilities belong either inside `extensions` (keyed by reverse-domain namespace) or in a reverse-domain namespace *directory* that the client owns and documents. Unknown top-level fields are reported and ignored; unimplemented `extensions` namespaces are ignored without validation.

Plugins **should** follow SemVer, but a plugin **must not** be rejected merely for a non-conforming version string.

## MCP Server Declaration (`mcp.json`)

MCP servers move out of the manifest into a dedicated root-level file with an explicit `type` on every entry:

```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
  "mcpServers": { }
}
```

Three transports are defined:

| Transport | Purpose | Fields |
|---|---|---|
| `stdio` | Local process execution | `command`, `args`, `env`, `cwd` |
| `streamable-http` | Remote HTTP endpoint | `url`, `headers` |
| `sse` | Deprecated HTTP+SSE, backward compatibility only | `url`, `headers` |

**stdio:**

```json
{
  "type": "stdio",
  "command": "./bin/server",
  "args": ["--flag", "value"],
  "env": { "KEY": "value" },
  "cwd": "${PLUGIN_ROOT}"
}
```

- `command` — a bare name or a `./`-prefixed plugin-relative path; resolved as a **single executable token, never through a shell**
- `args` / `env` / `cwd` — support `${PLUGIN_ROOT}` and `${PLUGIN_DATA}` expansion
- `env` may not define `PLUGIN_ROOT` or `PLUGIN_DATA` keys
- `cwd` defaults to the plugin root

**streamable-http:**

```json
{
  "type": "streamable-http",
  "url": "https://deploy.example.com/mcp",
  "headers": { "X-Tenant": "public-tenant" }
}
```

- `url` must be absolute HTTPS (plain HTTP permitted only for localhost), with no user info, no fragment, and no placeholder expansion
- `headers` are string values with case-insensitive names and no expansion

**sse** carries the same URL and header requirements; clients SHOULD prefer `streamable-http`.

If `mcp.json` declares a `$schema`, its version MUST match the one in `plugin.json`. A mismatch disables MCP loading but is **non-fatal** to the rest of the plugin.

## Environment Variables and Placeholder Expansion

Clients launching plugin subprocesses must provide exactly two reserved variables:

| Variable | Meaning |
|---|---|
| `PLUGIN_ROOT` | Absolute path to the plugin directory |
| `PLUGIN_DATA` | Client-managed writable directory for plugin state |

Expansion is deliberately narrow: **only** `${PLUGIN_ROOT}` and `${PLUGIN_DATA}`, **only** in `args`, `env`, and `cwd`, **non-recursive and literal**. No shell interpolation, no arbitrary environment lookups. Client `env` overlays are applied *before* the reserved variables are set, so a plugin cannot shadow them.

## Security Model

The spec's central security invariant is path containment:

> "When a client discovers, reads, or executes a file … the filesystem-resolved path MUST remain within the filesystem-resolved plugin root."

| Rule | Detail |
|---|---|
| Symlink handling | Symlinks and junctions may resolve *within* the plugin root; anything escaping it is rejected |
| Plugin-relative paths | Must begin with `./` |
| Non-path fields | Command arguments and env values are opaque — not subject to containment checks |
| `cwd` validation | Validated *after* expansion: `./path` and `${PLUGIN_ROOT}` forms must stay inside the plugin; `${PLUGIN_DATA}` forms must stay inside the data directory |
| No shell | `command` is a single executable token, not a shell string |

**Failure boundaries** are graduated — the narrowest applicable boundary applies, so one bad component never takes down the whole plugin:

| Failure | Consequence |
|---|---|
| Invalid `plugin.json` | Reject the entire plugin |
| Invalid component location | Treat that component *type* as invalid, continue loading others |
| Invalid discovered `SKILL.md` | Skip that skill, continue |
| Invalid MCP server entry | Skip that server, continue |
| Other path escapes | Deny access to the offending file |

Note that the spec governs *packaging*, not trust. It does not define signing, provenance, sandboxing, or a permission model — those remain the client's responsibility. Skill content inside a plugin is still untrusted instruction text and carries the same prompt-injection and exfiltration exposure as any other installed skill (see [Skill Security Scanners](../SecurityFrameworks/skill-scanners.md)).

## Client Conformance

A conformant client MUST:

- Load a plugin from a directory path and validate `plugin.json` against the `$schema`-selected schema
- Parse the closed schema, reporting and ignoring unknown top-level fields (except a non-object `extensions`)
- Ignore `extensions` namespaces it does not implement, without validating them
- Discover each supported component type from its fixed location (`skills/`, `mcp.json`)
- Treat missing locations and invalid component types as non-fatal
- Support **at least one** component type (skills or MCP servers)
- If it supports MCP, implement **at least one** of `stdio` or `streamable-http`
- Provide `PLUGIN_ROOT` and `PLUGIN_DATA` to subprocesses and expand only those two placeholders
- Continue loading remaining components when an individual component fails

How a client *exposes* loaded skills to users is explicitly outside the standard.

## Scope and Non-Goals

| In scope | Out of scope |
|---|---|
| Directory layout and manifest schema | Marketplaces and registries |
| Skills packaging (delegating format to the Agent Skills spec) | Install mechanisms and distribution protocols |
| MCP server declaration and transports | Permission and consent models |
| Path containment and failure boundaries | Signing, provenance, and sandboxing |
| Client conformance requirements | UI/UX for surfacing skills |

This restraint is the specification's main design decision: it standardizes the *artifact*, leaving competition and differentiation in discovery, curation, and trust to individual clients. It is a narrower bet than [MCP](./mcp.md) (a wire protocol) or [A2A](./agent2agent.md) (an agent interoperability protocol) — closer in spirit to [AGENTS.md](./agents-md.md) and [OKF](./open-knowledge-format.md), which likewise standardize on-disk conventions rather than runtime behavior.

## Migration from Client-Specific Plugin Formats

Existing Claude Code–style plugins that carry `hooks`, `agents`, `commands`, `lspServers`, and `mcpServers` at the top level of their manifest require restructuring:

| Legacy location | Agent Plugins v1 location |
|---|---|
| `mcpServers` in `plugin.json` | `mcp.json`, with an explicit `type` per entry |
| Loose skill files | `skills/<skill-name>/SKILL.md` |
| `hooks`, `agents`, `commands`, `lspServers` in `plugin.json` | Client-owned reverse-domain directory, e.g. `com.vendor.client/hooks/` |
| Arbitrary client keys in `plugin.json` | `extensions` object, keyed by reverse-domain namespace |

The reference migration guide recommends an **additive** approach — "add and validate the root `plugin.json` without deleting working platform files" — so a plugin can be validated against the new spec and tested in parallel before legacy configuration is removed.

## Governance

| Aspect | Detail |
|---|---|
| Model | Community-governed open specification: Contributors → Maintainers → Core Maintainers → Lead Core Maintainer |
| Technical Steering Committee | All Core Maintainers plus the Lead Core Maintainer; holds technical oversight |
| Vendor neutrality | "No single vendor may control a majority of Core Maintainer seats"; all governance roles are held by individuals, not organizations |
| Decisions | Consensus-seeking; standard decisions need 50% quorum and majority of those present; electronic votes need a majority of all TSC members; Lead Core Maintainer breaks ties |
| Charter amendments | Two-thirds vote of the entire TSC |
| Spec evolution | TSC approves changes, extensions, and deprecations |
| License | Specification text and documentation under **CC-BY-4.0**; code under **Apache 2.0** |

Core Maintainers listed in the project's `MAINTAINERS` file: Clare Liguori (Amazon), Roshan Sadanani (Cursor), Harald Kirschner (Microsoft), Gav Verma (OpenAI), and Jonathan Hefner (Vercel, Lead Core Maintainer). Google announced its participation as a Core Maintainer in its August 2026 Developers Blog post; membership is tracked in that file rather than in the charter.

## Adoption

Clients reported as supporting or committing to the format at launch include **VS Code**, **Cursor**, **GitHub Copilot**, **ChatGPT**, **OpenAI Codex**, and **Amazon Kiro**. Vercel published its own launch announcement alongside the specification.

The practical target is the vendor-integration long tail: a platform vendor (Railway, Supabase, Vercel) ships one plugin bundling the *knowledge* of how to work with the platform (skills) and *live account access* to it (an MCP server), and every conformant client can consume it without a vendor-specific repackaging step.

*(Adoption claims and the Google Core Maintainer role are as reported in launch coverage of August 2026; the `agent-plugins.org` site and the Google Developers Blog were not directly reachable from this environment — see Sourcing note in the ingest log.)*

## See Also

- [Agent Skills / SKILLS.md](./skills.md) — the skill format that Agent Plugins packages
- [Model Context Protocol (MCP)](./mcp.md) — the tool/data protocol declared in `mcp.json`
- [AGENTS.md Standard](./agents-md.md) — sibling filesystem convention for always-on agent instructions
- [Open Knowledge Format (OKF)](./open-knowledge-format.md) — comparable markdown-plus-frontmatter packaging convention for knowledge bundles
- [Agent2Agent (A2A) Protocol](./agent2agent.md) — complementary agent-to-agent interoperability standard
- [Agentic AI Foundation (AAIF)](./agentic-ai-foundation.md) — the other major vendor-neutral governance body in the agentic standards space
- [Claude Code](../AICodingAgents/claude-code.md) — plugin and skills ecosystem affected by the migration path
- [AI Coding Agents](../AICodingAgents/ai-coding-agents.md) — the client landscape adopting the format
- [AI Agent Skill Security Scanners](../SecurityFrameworks/skill-scanners.md) — trust concerns the spec explicitly leaves to clients
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md) — how harnesses load and expose plugin components

## References

- [Agent Plugins package your skills, tools, and more](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/) — Google Developers Blog announcement of Google joining Agent Plugins as a Core Maintainer *(direct fetch returned EGRESS_BLOCKED; content corroborated via the specification repository and launch coverage)*
- [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) — canonical specification repository
- [Agent Plugins Specification v1.0.0](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md) — the authoritative spec text
- [agentplugins/agent-plugins-example](https://github.com/agentplugins/agent-plugins-example) — canonical example plugin and v1 migration guide
- [agent-plugins.org](https://agent-plugins.org/) — specification site hosting the JSON Schemas, plugin-author and client-implementer guides, governance charter, and future-considerations document
- [Introducing Agent Plugins](https://vercel.com/blog/introducing-agent-plugins) — Vercel launch post
- [Agent plugins in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins) — VS Code client documentation
