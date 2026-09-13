# Graph Report - .  (2026-09-13)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 474 nodes · 449 edges · 128 communities (52 shown, 76 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 2,935 input · 3,904 output

## Graph Freshness
- Built from commit: `c273306a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Agent Frameworks & Research
- Agent Marketplace Platforms
- Agent Evaluation Benchmarks
- AI Coding Agent Frameworks
- Documentation Content Tests
- AI Coding Agent Tools
- MkDocs Configuration Tests
- Vendor Docs Consistency Tests
- Frontmatter & Metadata Tools
- Agent Standards & Protocols
- Agent Harness & Observability
- Documentation Index Generator
- Context Engineering & Primitives
- Agent Security & Testing
- Prompting & RAG Architecture
- Log Ingestion & Formatting
- Agent Memory Strategies
- Agent Operations & Orchestration
- Production Deployment Best Practices
- Agent Technology Stack
- Agent Harness Optimization
- Build Hook Utilities
- Documentation Repository Root
- AgentOps Framework Docs
- AI Governance & Regulation
- Anthropic Agents & MCP
- Agent Standards Organizations
- MkDocs Test Runner
- Microsoft Agent Platforms
- Governance Solutions
- Agent Architecture Patterns
- Graph Visualization Docs
- Self-Evolving Agents
- Agent Communication Protocols
- Contributor README
- Doc-to-Markdown Script
- Introduction
- Disclaimer & Usage
- Introduction Index
- Marketplace Index
- Agentic AI Maturity Models
- Agentic Engineering Levels
- Arsanjani Maturity Model
- AWS Maturity Perspective
- AWS Generative AI Maturity
- Gartner Maturity Perspective
- Google Maturity Perspective
- IDC Maturity Perspective
- Maturity Models Index
- Observability Goals
- Observability Index
- Agent Observability Radar
- Production Best Practices Index
- Agent Security
- Code-as-Harness Concepts
- Loop Engineering
- Pi Platform
- Eve Framework
- LangSmith Observability
- Spring AI
- Agentic Tech Stack Index
- Semantic Data Layer Radar
- Agent Memory Index
- KAOS Orchestration System
- Databricks Genie
- Discovery Loop
- Enterprise Agentic Platforms
- Gemini Enterprise Platform
- Other SaaS Platforms
- Microsoft Agentic Overview
- OpenAI Agentic Overview
- 12-Factor Agents
- Architecture Component Selection
- Dataset Engineering
- Fine-tuning
- Inference Optimization
- Benchmarks Index
- Benchmarks Overview
- Prompt Engineering Index
- RAG Index
- AI Assistant Reference (stub)
- AI Assistant Reference (detailed)
- AI Automation Reference Architecture
- AI Engineering Architecture
- Reference Architecture Index
- AI Automation Framework
- Specialized Domain Blueprints
- Google SAIF Framework
- Security Frameworks Index
- Visual Identity for Agents
- Agent UI Protocol Standards
- LLM Wiki Documentation
- Agent Operations
- Comet Opik Tool
- Datadog Monitoring
- Dynatrace Monitoring
- Jaeger Tracing
- New Relic Monitoring
- Metrics & Dashboards
- SigNoz Monitoring
- W&B Weave Integration
- Zipkin Tracing

## God Nodes (most connected - your core abstractions)
1. `Agent Evaluation Benchmarks` - 21 edges
2. `Agent Evaluation Platforms` - 14 edges
3. `AI Coding Agents (page)` - 13 edges
4. `TestSectionCompleteness` - 12 edges
5. `Evaluation Tech Radar` - 12 edges
6. `TestMkDocsConfiguration` - 11 edges
7. `TestVendorSectionConsistency` - 10 edges
8. `Claude Code (page)` - 9 edges
9. `Harness Engineering` - 9 edges
10. `build_frontmatter()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Harness Engineering` --cites--> `Birgitta Böckeler — Harness Engineering (martinfowler.com, 2026)`  [EXTRACTED]
  docs/AgentHarness/harness-engineering.md → https://martinfowler.com/articles/harness-engineering.html
- `Harness Engineering` --cites--> `Meng et al., arXiv:2605.29682 (2026)`  [EXTRACTED]
  docs/AgentHarness/harness-engineering.md → https://arxiv.org/pdf/2605.29682
- `Harness Engineering` --cites--> `Meta-Harness — Lee et al., arXiv:2603.28052 (2026)`  [EXTRACTED]
  docs/AgentHarness/harness-engineering.md → https://arxiv.org/abs/2603.28052
- `Harness Engineering` --cites--> `Ning et al., Code as Agent Harness, arXiv:2605.18747 (2026)`  [EXTRACTED]
  docs/AgentHarness/harness-engineering.md → https://arxiv.org/abs/2605.18747
- `Context Engineering` --references--> `Key Challenges in Context Management`  [EXTRACTED]
  docs/ContextEngineering/README.md → docs/ContextEngineering/challenges.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **GenAI observability specification ecosystem** — docs_observability_otel_genai_conventions_playbook, docs_observability_solutions_playbook, docs_productionbestpractices_observability_playbook [EXTRACTED 0.75]
- **AI coding agents category (representative tools)** — docs_aicodingagents_claude-code_claude_code, docs_aicodingagents_ai-coding-agents_openai_codex, docs_aicodingagents_ai-coding-agents_antigravity_cli, docs_aicodingagents_ai-coding-agents_kiro, docs_aicodingagents_ai-coding-agents_snowflake_coco, docs_aicodingagents_ai-coding-agents_databricks_genie_code, docs_aicodingagents_ai-coding-agents_devin, docs_aicodingagents_ai-coding-agents_cline, docs_aicodingagents_ai-coding-agents_goose, docs_aicodingagents_ai-coding-agents_opencode [EXTRACTED 0.75]
- **Agent Memory Section Pages** — docs_agentmemory_readme_agent_memory_management, docs_agentmemory_functional_tiers_the_four_memory_types_of_agent_memory, docs_agentmemory_ltm_strategies_long_term_memory_ltm_strategies, docs_agentmemory_short_term_working_memory_management, docs_agentmemory_research_papers_research_papers_on_agent_memory, docs_agentmemory_solutions_agent_memory_solutions [EXTRACTED 0.90]
- **AgentOps Core Pages** — docs_agentops_readme_agentops, docs_agentops_index_agent_operations_index, docs_agentops_agentic_ops_framework_agentic_ops_framework_aof, docs_agentops_kagent_kagent, docs_agentops_kaos_kaos [EXTRACTED 0.90]
- **AWS AgentCore — supported frameworks group** — docs_agentplatforms_aws-agentcore_doc, docs_agenticframeworks_crewai_doc, docs_agenticframeworks_langgraph_concept, docs_agenticframeworks_llamaindex_concept, docs_agenticframeworks_aws-strands_doc [EXTRACTED 0.75]
- **Agentic Frameworks — Adopt ring (solutions.md)** — docs_agenticframeworks_langchain_langchain, docs_agenticframeworks_langgraph_langgraph, docs_agenticframeworks_crewai_crewai, docs_agenticframeworks_llamaindex_llamaindex, docs_agenticframeworks_pydantic_ai_pydantic_ai, docs_agenticframeworks_microsoft_framework_microsoft_agent_framework [EXTRACTED 0.75]
- **Adopt ring — Evaluation Tech Radar** — platform_deepeval, platform_ragas, platform_mlflow_llm_evaluate, platform_galileo, platform_aws_bedrock_evaluations, platform_azure_ai_foundry_evaluation [EXTRACTED 1.00]
- **Prompt Engineering concept group** — docs_promptengineering_readme_prompt_engineering, docs_promptengineering_gepa_gepa, docs_promptengineering_skillopt_skillopt [EXTRACTED 0.75]

## Communities (128 total, 76 thin omitted)

### Community 0 - "Agent Frameworks & Research"
Cohesion: 0.08
Nodes (32): CrewAI, AI-Scientist-v2, arXiv:2510.15624 (FreePHDLabor paper), FreePHDLabor, GitHub — ltjed/freephdlabor, .llm_config.yaml, Phoenix (telemetry), smolagents (+24 more)

### Community 1 - "Agent Marketplace Platforms"
Cohesion: 0.09
Nodes (28): Agent Evaluation Platforms, Evaluation Tech Radar, Agents Marketplace Overview, AgentOps Marketplace, Anthropic Agents Marketplace Presence, AWS AI Agents Marketplace, Google Cloud Agent Gallery, Agent Observability (+20 more)

### Community 2 - "Agent Evaluation Benchmarks"
Cohesion: 0.08
Nodes (28): AgentBench, ALE-Bench, DeepResearch Bench (DRB), Finance Agent v2, GAIA (General AI Assistants), LongMemEval (ICLR 2025), LongMemEval-V2 (arXiv 2605.12493), METR (Model Evaluation & Threat Research) (+20 more)

### Community 3 - "AI Coding Agent Frameworks"
Cohesion: 0.10
Nodes (26): AI Coding Agents (Frameworks), AutoGen Framework, AutoGPT Framework, AWS Strands Agents, CrewAI Framework, Flue Framework, LangGraph (concept), LlamaIndex (concept) (+18 more)

### Community 4 - "Documentation Content Tests"
Cohesion: 0.08
Nodes (14): given, settings, Test that navigation structure references preserved content appropriately., Recursively extract all file paths from navigation structure., Test that substantial content is preserved across all folders., Test that internal and external links are preserved in content., Property-based tests for section completeness validation., Test that image references are preserved in content. (+6 more)

### Community 5 - "AI Coding Agent Tools"
Cohesion: 0.08
Nodes (24): Agent Harness (page), Code as Agent Harness (survey / paper), Meta-Harness (paper), Loop Engineering (page), Antigravity CLI, Cline, Databricks Genie Code, Devin (+16 more)

### Community 6 - "MkDocs Configuration Tests"
Cohesion: 0.09
Nodes (13): given, settings, Recursively extract all file paths from navigation structure., Test that YAML structure maintains proper indentation and format., Test that enhanced Material theme features are properly enabled., Property-based tests for MkDocs configuration validation., Set up test environment., Test that mkdocs.yml exists and is valid YAML. (+5 more)

### Community 7 - "Vendor Docs Consistency Tests"
Cohesion: 0.10
Nodes (12): given, settings, Test that each vendor section has unique, vendor-specific content., Test that vendor sections provide comprehensive coverage., Property-based tests for vendor section consistency validation., Set up test environment., Test that all required vendor directories exist., Test that all vendor directories have README.md files. (+4 more)

### Community 8 - "Frontmatter & Metadata Tools"
Cohesion: 0.16
Nodes (18): build_frontmatter(), extract_description(), extract_title(), has_frontmatter(), main(), process_file(), Path, Extract the first H1 heading from markdown content. (+10 more)

### Community 9 - "Agent Standards & Protocols"
Cohesion: 0.25
Nodes (18): AGENTS.md Standard, AI-Driven Development Life Cycle (AIDLC), Cloud Security Alliance (CSA), Industry Standards Index, Kubernetes Agent Sandbox, Model Context Protocol (MCP), Open Knowledge Format (OKF), OpenSpec (+10 more)

### Community 10 - "Agent Harness & Observability"
Cohesion: 0.14
Nodes (15): Harness Engineering, OpenTelemetry GenAI Semantic Conventions, Observability Solutions, Observability (Production Best Practices), agents-best-practices — DenisSergeevitch (2025), Birgitta Böckeler — Harness Engineering (martinfowler.com, 2026), Langfuse, Harness Engineering — Ryan Lopopolo, OpenAI (2026) (+7 more)

### Community 11 - "Documentation Index Generator"
Cohesion: 0.26
Nodes (14): dir_description(), extract_first_sentence(), generate_index(), get_concept_info(), main(), process_directory(), Path, Return (title, description) for a concept doc. (+6 more)

### Community 12 - "Context Engineering & Primitives"
Cohesion: 0.26
Nodes (12): Anthropic primitive: clear_tool_uses_20250919, Anthropic primitive: compact_20260112, Anthropic primitive: memory_20250818, Anthropic Context Engineering, Key Challenges in Context Management, Context Graph, Cognition / Devin: Context Engineering Principles, The Efficiency Frontier (Context Management) (+4 more)

### Community 13 - "Agent Security & Testing"
Cohesion: 0.25
Nodes (9): Agent Testing & Evaluations, Microsoft Agent Governance Toolkit (AGT), Agent Sandboxing (Cross-Vendor Overview), Agentic AI Red Teaming Guide (CSA), Anthropic Sandbox Runtime (srt), Learn Prompt Hacking, NIST AI RMF (Risk Management Framework), Agentic AI Security Overview (+1 more)

### Community 15 - "Prompting & RAG Architecture"
Cohesion: 0.43
Nodes (7): GEPA: Genetic-Pareto Prompt Optimization, Prompt Engineering (Overview), SkillOpt: Executive Strategy for Self-Evolving Agent Skills, RAG Overview, Search as Code (SaC), RAG Reference Architecture, Agentic AI Reference Architecture (Overview)

### Community 16 - "Log Ingestion & Formatting"
Cohesion: 0.33
Nodes (6): build_log_md(), format_entry(), parse_entries(), Build the full log.md content., Return list of entry dicts parsed from ingest-log.md., Format a single entry as an OKF log bullet.

### Community 17 - "Agent Memory Strategies"
Cohesion: 1.00
Nodes (6): The Four Memory Types of Agent Memory, Long-Term Memory (LTM) Strategies, Agent Memory Management, Research Papers & Technical White Papers on Agent Memory, Working Memory Management, Agent Memory Solutions

### Community 18 - "Agent Operations & Orchestration"
Cohesion: 0.60
Nodes (6): Agentic Ops Framework (AOF), GenOps – Evolution of MLOps for GenAI, Agent Operations Index, kagent, KAOS (K8s Agent Orchestration System), Agentic AI Operations (AgentOps)

### Community 19 - "Production Deployment Best Practices"
Cohesion: 0.40
Nodes (5): Production Best Practices & Guidelines, Context Engineering, Cost Management for Agentic AI, Deployment, State & Memory Management

### Community 20 - "Agent Technology Stack"
Cohesion: 0.40
Nodes (5): Agent Technology Stack, AWS AgentCore, AWS — Agentic AI Overview, AWS Strands Agents, Kiro (AWS)

### Community 21 - "Agent Harness Optimization"
Cohesion: 0.67
Nodes (4): Harness Optimization, Harness Self-Evolution, Agent Harness Index, Agent Harness Engineering: Survey & Taxonomy

### Community 22 - "Build Hook Utilities"
Cohesion: 0.83
Nodes (3): on_pre_build(), _page_url(), Path

### Community 24 - "AgentOps Framework Docs"
Cohesion: 0.67
Nodes (3): Agentic Ops Framework (AOF) (page), kagent (page), Agent Sandboxing (page)

### Community 25 - "AI Governance & Regulation"
Cohesion: 0.67
Nodes (3): Governance Strategy (page), EU AI Act, NIST AI RMF 1.0

### Community 26 - "Anthropic Agents & MCP"
Cohesion: 0.67
Nodes (3): Anthropic — Agentic AI Overview, Claude Code, Model Context Protocol (MCP)

### Community 28 - "Agent Standards Organizations"
Cohesion: 0.67
Nodes (3): Agentic AI Foundation (AAIF), NIST AI Agent Standards Initiative, W3C AI Agent Protocol Community Group

## Knowledge Gaps
- **174 isolated node(s):** `doc2md.sh script`, `Key Challenges in Context Management`, `Antigravity CLI`, `Gemini CLI`, `OpenAI Codex` (+169 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **76 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `doc2md.sh script`, `Key Challenges in Context Management`, `Antigravity CLI` to the rest of the system?**
  _174 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Agent Frameworks & Research` be split into smaller, more focused modules?**
  _Cohesion score 0.08266129032258064 - nodes in this community are weakly interconnected._
- **Should `Agent Marketplace Platforms` be split into smaller, more focused modules?**
  _Cohesion score 0.08994708994708994 - nodes in this community are weakly interconnected._
- **Should `Agent Evaluation Benchmarks` be split into smaller, more focused modules?**
  _Cohesion score 0.07671957671957672 - nodes in this community are weakly interconnected._
- **Should `AI Coding Agent Frameworks` be split into smaller, more focused modules?**
  _Cohesion score 0.09846153846153846 - nodes in this community are weakly interconnected._
- **Should `Documentation Content Tests` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._
- **Should `AI Coding Agent Tools` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._