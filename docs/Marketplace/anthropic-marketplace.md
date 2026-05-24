# Anthropic Agents Marketplace Presence

## Overview

Anthropic does not operate a standalone agent marketplace. Instead, Claude models and Anthropic-built tooling reach enterprise buyers through three distribution channels: major cloud provider marketplaces (AWS Bedrock, Google Cloud Vertex AI, Azure AI Foundry), the Claude.ai Enterprise platform with its growing partner integrations, and the open Model Context Protocol (MCP) ecosystem that enables third-party tool and agent builders to connect to Claude.

## Distribution Channels

### Cloud Provider Marketplaces

Claude models are available as managed foundation models on the major hyperscaler platforms, giving enterprise buyers access within their existing procurement and compliance frameworks:

| Platform | Offering | Notes |
|---|---|---|
| **AWS Bedrock** | Claude 3.x and Claude 4.x model family | Integrated with Amazon Bedrock Agents; supports cross-region inference |
| **Google Cloud Vertex AI** | Claude models via Model Garden | Deployable alongside Gemini; supports Vertex AI Agent Builder |
| **Azure AI Foundry** | Claude via Azure AI model catalog | Supports Azure AI Agent Service and Semantic Kernel integrations |

### Claude.ai Enterprise

The Claude.ai Enterprise plan provides:
- **Projects** — persistent context workspaces for team-level agent deployments
- **Integrations** — connectors to enterprise tools (Google Drive, GitHub, Jira, Confluence, Slack, and others)
- **Admin controls** — SSO, audit logs, usage policies, and data residency options
- **Claude.ai Apps** — lightweight partner-built agents and workflows accessible within the Claude.ai interface

### MCP Ecosystem (Open Marketplace Equivalent)

Anthropic's Model Context Protocol (MCP) functions as a de-facto open marketplace for agent tools and connectors. Any MCP server published by a vendor or open-source developer can be attached to Claude, extending its capabilities:

- **MCP Registry** — community-maintained index of available MCP servers
- **Partner MCP servers** — enterprise vendors (Atlassian, GitHub, Salesforce, Stripe, and others) publish official MCP servers
- **Claude Code MCP** — Claude Code can act as an MCP client or server, enabling IDE-level agent composition

Because MCP is an open standard, the ecosystem is not controlled by Anthropic but grows through community and vendor contributions.

## Finance Agents Example

Anthropic has highlighted finance-specific agent use cases as an early enterprise vertical, with partners building agents for tasks such as financial analysis, regulatory document processing, and automated reporting. These agents typically run via Claude's API (or through Bedrock/Vertex AI) rather than through a dedicated Anthropic-hosted marketplace storefront.

*(Note: a specific Anthropic finance agents announcement URL was referenced in the ingest request but could not be confirmed — details will be updated once the source is verified.)*

## Partner and Integration Ecosystem

Key enterprise partners building agents on Claude:

- **Consulting/SI firms** — Accenture, Deloitte, and other system integrators deploy Claude within client environments via Bedrock or direct API
- **Productivity platforms** — Salesforce, ServiceNow, Atlassian, and GitHub have Claude-powered features or official MCP integrations
- **Developer platforms** — Cursor, Windsurf, and other AI-assisted coding tools embed Claude models
- **Vertical SaaS** — Harvey (legal), Notion (productivity), Intercom (support), and others use Claude as the underlying model for agent features

## Comparison with Platform Marketplaces

| Dimension | Anthropic | AWS Marketplace | Google Agent Gallery |
|---|---|---|---|
| **Marketplace type** | Cloud re-seller + open MCP ecosystem | Centralized storefront | Embedded in Gemini Enterprise app |
| **Agent discovery** | Via cloud portals or MCP Registry | AWS Marketplace console | Gemini Enterprise Agent Gallery |
| **Certification program** | None (model availability via cloud SLAs) | AWS Partner Network validation | "Google Cloud Ready — Gemini Enterprise" 4-step evaluation |
| **Governance** | Cloud-provider IAM + enterprise admin controls | AWS IAM + Marketplace controls | Two-step IT approval + cryptographic identity |
| **Open standard** | MCP (open, Anthropic-originated) | Proprietary (Bedrock Agents API) | A2A (open) |

## See Also

- [Model Context Protocol (MCP)](../Standards/mcp.md)
- [Claude Managed Agents](../AgentPlatforms/claude-managed-agents.md)
- [AWS AI Agents Marketplace](../Marketplace/aws-marketplace.md)
- [Google Cloud Agents Marketplace](../Marketplace/google-cloud-marketplace.md)
- [Agents Marketplace Overview](../Marketplace/Readme.md)
- [AllThings Anthropic](../AllThingsAnthropic/README.md)

## References

- [Anthropic Claude on AWS Bedrock](https://aws.amazon.com/bedrock/claude/) — AWS product page
- [Claude Models on Google Cloud Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) — Google Cloud docs
- [Claude on Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) — Azure product page
- [Model Context Protocol](https://modelcontextprotocol.io/) — MCP open standard
