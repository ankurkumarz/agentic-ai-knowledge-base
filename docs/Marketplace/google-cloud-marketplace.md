# Google Cloud Agents Marketplace (Agent Gallery)

## Overview

Google Cloud's Agent Gallery is the partner-built agents hub embedded directly in the Gemini Enterprise app. Launched in 2025, it provides a governed, enterprise-grade storefront where organizations discover, approve, and deploy specialized AI agents from 50+ certified partners — all running on the Gemini Enterprise Agent Platform with unified identity, security, and governance.

Unlike a traditional software marketplace, the Agent Gallery integrates agents into employees' daily workflows inside the Gemini app rather than routing users to external storefronts.

## Platform Architecture

### Access and Integration Model

| Layer | Detail |
|---|---|
| **Hub** | Agent Gallery tab within the Gemini Enterprise app |
| **Deployment runtime** | Gemini Enterprise Agent Platform (Google Cloud) |
| **Agent protocol** | A2A (Agent-to-Agent) — agents communicate via the open standard |
| **User discovery** | Employees browse gallery and submit access requests |
| **IT governance** | IT admins review, approve/deny with granular access controls |
| **Coexistence** | Custom internal agents and third-party agents share one unified infrastructure |

### Enterprise Security Features

- **Cryptographic identity**: Each agent has a secure identity enabling full audit trails
- **Agent Gateway**: Traffic screening for data exfiltration protection
- **Model Armor**: Prevents enterprise data from being used for model training
- **No API silos**: All agents operate on the same governed infrastructure

### Certification Standard

Partner agents earn the **"Google Cloud Ready — Gemini Enterprise"** designation by passing a four-step evaluation: basic functionality → output accuracy → autonomous execution → enterprise standards compliance.

## Partner Ecosystem (50+ Partners)

### Supply Chain & Operations
- **Accenture** — Supply Chain Inventory Intelligent Advisor (real-time optimization)
- **Pluto7** — Planning in a Box Pi Agent (50+ sub-agents for autonomous supply chain)
- **Manhattan** — Active Agents for warehouse, transportation, and order management
- **Devoteam** — Demand Sensing Agent (forecast accuracy, inventory optimization)

### Sales & Revenue
- **Salesforce** — Agentforce Sales (lead engagement, deal risk, pipeline management)
- **Backstory** — Revenue Answers Agent (account intelligence, deal risk identification)
- **Cotality** — Payoff Analysis Agent (mortgage lending insights)

### Marketing & Content
- **Adobe** — Marketing Agent (campaign performance, audience targeting)
- **Invideo** — Video production at scale across 50+ languages
- **Supermetrics** — Marketing Intelligence Agent (175+ data sources including Google Ads, GA4)
- **Typeface** — Brand asset and campaign orchestration

### Finance & Banking
- **AutoCIO** — Financial Forecasting Agent (portfolio optimization, 50,000+ securities)
- **Obin AI** — Financial analysis for private markets and commercial lending
- **Genpact** — Revenue Lens and PnL Agents

### IT & Infrastructure
- **ServiceNow** — Now Assist for IT Operations Management (alert/incident management)
- **HCLTech** — ITOps Agent (autonomous IT operations, ServiceNow integration)
- **Red Hat** — Lightspeed Agent (RHEL infrastructure management on Google Cloud)
- **Dynatrace** — Observability data integration with real-time insights

### Data & Analytics
- **Teradata** — Data Analyst AI Agent (natural-language analytics, governed SQL)
- **Neo4j** — GraphRAG-grounded agent (Cypher translation, knowledge graphs)
- **Alteryx** — AI Insights Agent (trusted datasets, analyst-curated insights)
- **Carto** — Site Selection Agent (spatial analytics, foot traffic, demographics)

### Security & Compliance
- **Palo Alto Networks** — Prisma AIRS Model Security (35+ model formats, poisoned-weight detection)
- **Acalvio** — ShadowPlex (honeytokens, agentic AI attack prevention)
- **Saviynt** — Identity Security for AI (agent inventory, access control, governance)
- **Skyflow** — Runtime Data Security Agent (fine-grained access controls)
- **XM Cyber** — PostureAI (Google Workspace security assessment)

### HR & People Operations
- **Sana/Workday** — Self-Service Agent (300+ HR/finance skills globally)
- **UKG** — Agentic People Assist (time, pay, HR workflow orchestration)
- **Ambiguous AI** — Recruiting Coworker (scheduling, pipeline tracking, Gmail/Calendar integration)

### Customer Service & Support
- **Amdocs** — Telco Customer Experience Agent (multi-channel issue resolution)
- **Tech Mahindra** — Order Assist (complex order/service resolution)
- **Botcopy** — TrueQ (contact center AI performance analysis)

### Document & Knowledge Management
- **AODocs** — AI Agent (grounded answers from validated enterprise documents)
- **Iron Mountain** — InSight DXP AI Agent (managed content search and Q&A)
- **OpenText** — Content Aviator (enterprise document summarization)
- **LumApps** — AI Agent (knowledge retrieval, workflow triggering)

### Developer & Application Tools
- **Lovable** — Real app/website building from chat prompts
- **Replit** — Enterprise application builder (natural language to BigQuery dashboards)
- **Exa AI** — Developer tooling, recruiting, market mapping

### Industry-Specific
- **Nativeorange** — LexAI Agent (P&C insurance underwriting)
- **Deloitte** — Tariff Management Suite (customs compliance automation)
- **Enigma** — KYB Agent (business verification, sanctions screening)
- **S&P Global** — Data Retrieval Agent (financial metrics, earnings calls)
- **Dun & Bradstreet** — Business Verification Agent
- **Synthpop** — Patient Journey Orchestration (healthcare referrals)

## Governance Model

The gallery uses a two-step governance workflow designed to balance employee productivity with IT control:

1. **Employee layer** — Browse and submit procurement/access requests for any agent
2. **IT layer** — Admins review requests and approve or deny with granular access controls; deployed agents appear directly in the requester's Gemini app

This prevents unsanctioned "shadow AI" deployments while keeping friction low for legitimate use.

## Go-to-Market and Business Model

| Factor | Detail |
|---|---|
| **Partner fund** | $750 million committed for agentic development |
| **Enterprise backlog** | $460 billion+ in committed enterprise spend across Google Cloud |
| **Marketplace deal size** | 112% larger for Marketplace vendors vs. direct |
| **Procurement speed** | Up to 50% faster purchasing cycles via Marketplace |
| **Sales alignment** | Google Cloud reps are incentivized to co-sell with partners |
| **Customer trial** | 30-day trial available via Gemini Enterprise app |
| **Startup path** | Google for Startups AI Agents Challenge includes a Gemini Enterprise-ready track |

## Key Differentiators vs. Other Agent Marketplaces

| Feature | Google Agent Gallery | Traditional Marketplaces |
|---|---|---|
| **Integration point** | Embedded in daily workflow (Gemini app) | Separate storefront, external deployment |
| **Agent autonomy** | End-to-end autonomous execution | Often assistive or single-step |
| **Governance** | Two-step IT approval + cryptographic identity | Varies; often developer-managed |
| **Protocol standard** | A2A (open) | Proprietary per-platform |
| **Coexistence** | Custom + third-party on same infra | Often siloed |

## See Also

- [Gemini Enterprise Agent Platform](../AgentPlatforms/gemini-enterprise-agent-platform.md)
- [A2A Standard](../Standards/a2a.md)
- [AWS AI Agents Marketplace](../Marketplace/aws-marketplace.md)
- [Agent Platforms Overview](../AgentPlatforms/README.md)
- [Security Frameworks — Google SAIF](../SecurityFrameworks/google-saif.md)
- [Agents Marketplace Overview](../Marketplace/Readme.md)

## References

- [Partner-Built Agents Available in Gemini Enterprise](https://cloud.google.com/blog/products/ai-machine-learning/partner-built-agents-available-in-gemini-enterprise) — Google Cloud Blog, 2025
