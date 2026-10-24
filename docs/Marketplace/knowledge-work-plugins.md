---
type: Reference
title: Knowledge Work Plugins (Anthropic)
description: "knowledge-work-plugins is Anthropic's Apache-2.0 repository of file-based plugins that specialize Claude Cowork, and Claude Code, for roles such as sales, legal, finance, support, and product management"
tags: [marketplace, plugins, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# Knowledge Work Plugins (Anthropic)

## Overview

`anthropics/knowledge-work-plugins` is an open-source repository of plugins intended for knowledge workers using Claude Cowork. The README describes them as turning Claude "into a specialist for your role, team, and company." Each plugin bundles domain skills, slash commands, and connector configuration, so a team can change how Claude does a role's work without writing code. The plugins are also compatible with Claude Code.

The repository is best read as a **plugin catalog and reference format** rather than a runtime. Every component is a file: markdown for skills and commands, JSON for the manifest and connector configuration.

## Plugins

The README lists eleven open-sourced plugins:

| Plugin | What it does | Example connectors |
|---|---|---|
| productivity | Tasks, calendars, daily workflows, personal context | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| sales | Prospect research, call prep, pipeline review, outreach drafts, battlecards | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| customer-support | Ticket triage, response drafts, escalation packaging, knowledge-base articles | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| product-management | Specs, roadmaps, user-research synthesis, competitor tracking | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| marketing | Content drafts, campaign plans, brand-voice checks, performance reports | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| legal | Contract review, NDA triage, risk assessment, templated responses | Slack, Box, Egnyte, Jira, Microsoft 365 |
| finance | Journal-entry prep, account reconciliation, statements, variance analysis, audit support | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| data | SQL, statistical analysis, dashboards, validation | Snowflake, Databricks, BigQuery, Definite, Hex, Amplitude, Jira |
| enterprise-search | One query across email, chat, documents, and wikis | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| bio-research | Literature search, genomics analysis, target prioritization | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Synapse, Wiley, Owkin, Open Targets, Benchling |
| cowork-plugin-management | Create new plugins or customize existing ones | None |

The repository also contains folders the README does not describe: `partner-built`, `pdf-viewer`, `design`, `engineering`, `operations`, `human-resources`, and `small-business`. Check each folder's own files before relying on it.

## Plugin Structure

```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── .mcp.json                    # Tool connections
├── commands/                    # Slash commands invoked explicitly
└── skills/                      # Domain knowledge Claude draws on when relevant
```

- **Skills** encode domain expertise, best practices, and step-by-step workflows. Claude applies them automatically when relevant.
- **Commands** are explicit actions, such as `/finance:reconciliation` or `/product-management:write-spec`.
- **Connectors** are MCP server configurations in `.mcp.json` that link Claude to the external tools a role depends on.

The structure parallels the Agent Skills convention covered in [Agent Skills / SKILLS.md](../Standards/skills.md), with the addition of connectors and a manifest.

## Installation

- **Cowork:** install plugins from claude.com/plugins.
- **Claude Code:** add the marketplace, then install a plugin:

```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```

Once installed, skills activate when relevant, and commands are available in the session.

## Customization

The README recommends editing `.mcp.json` to match a team's tool stack, adding terminology, org structure, and processes to skill files, and adjusting skill instructions to match how the team works. New plugins can be built with `cowork-plugin-management` or by following the structure above. Contributions are accepted by pull request.

## Considerations

- **Connectors are the sensitive surface.** A plugin that reads email, chat, financial warehouses, or legal document stores grants Claude access to that data. Scope connectors to least privilege and review each plugin's `.mcp.json` before installing it.
- **Skills are guidance, not enforcement.** Skill files shape behavior but do not enforce controls. Approval gates for consequential actions need to be implemented elsewhere, for example with hooks or the platform's permission model.
- **Professional domains need expert review.** Legal, finance, and bio-research plugins produce drafts and analyses. The README does not claim they replace professional judgment, and outputs should be reviewed by a qualified person.
- **Repository snapshot.** At capture the repository showed about 32.3k stars, 3.6k forks, 87 open issues, and 50 open pull requests.

## See Also

- [Agent Skills / SKILLS.md](../Standards/skills.md) — the skill convention that the plugins' skill folders follow
- [Claude Code](../AICodingAgents/claude-code.md) — the coding agent that also loads these plugins
- [Anthropic Marketplace Presence](anthropic-marketplace.md) — Anthropic's distribution channels
- [Model Context Protocol (MCP)](../Standards/mcp.md) — the protocol behind the connector configuration
- [Loop Engineering](../AgentHarness/loop-engineering.md) — hooks and scheduled automation that can enforce controls skills cannot
- [AllThingsAnthropic](../AllThingsAnthropic/README.md) — Anthropic's agentic offerings

## References

- [anthropics/knowledge-work-plugins — GitHub repository](https://github.com/anthropics/knowledge-work-plugins) — README, plugin folders, and Apache-2.0 license
