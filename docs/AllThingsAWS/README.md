# AWS — Agentic AI Overview

## Overview

Amazon Web Services offers a broad portfolio of agentic AI services spanning agent development frameworks, managed runtime platforms, maturity guidance, and a growing agent marketplace. AWS emphasises serverless, event-driven deployment patterns tightly integrated with the broader AWS ecosystem.

## Key Offerings

| Product / Area | One-liner | Wiki Reference |
|---|---|---|
| Kiro | Amazon's spec-driven agentic IDE — specs as source of truth, agent hooks, Bedrock multi-model routing | [AgenticFrameworks/ai-coding-agents.md](../AgenticFrameworks/ai-coding-agents.md) |
| AWS Strands Agents | Open-source SDK for building agents with tool use and multi-agent orchestration | [AgenticFrameworks/aws-strands.md](../AgenticFrameworks/aws-strands.md) |
| AWS AgentCore | Managed runtime for deploying, scaling, and monitoring agents | [AgentPlatforms/aws-agentcore.md](../AgentPlatforms/aws-agentcore.md) |
| AWS AI Agents Marketplace | Catalogue of pre-built agents and integrations available via AWS Marketplace | [Marketplace/aws-marketplace.md](../Marketplace/aws-marketplace.md) |
| AWS GenAI Maturity Model | Framework for assessing and advancing generative AI adoption | [MaturityModels/aws-genai.md](../MaturityModels/aws-genai.md) |
| AWS Agentic Maturity Model | Staged model for measuring agent deployment readiness | [MaturityModels/aws.md](../MaturityModels/aws.md) |
| AWS Security Perspective | AWS guidance on securing agentic AI workloads | [SecurityFrameworks/Readme.md](../SecurityFrameworks/Readme.md) |
| AIDLC Workflows | AI-Driven Development Life Cycle — methodology-first framework guiding AI coding agents through structured Inception → Construction → Operations phases with approval gates | [Standards/aidlc.md](../Standards/aidlc.md) |
| AWS Skills Registry | Provider skills installable via `npx skills add aws/agent-toolkit-for-aws/skills`; targets Strands Agents and Kiro harnesses | [Standards/skills.md#provider-skills-repositories](../Standards/skills.md) |
| AWS Lambda MicroVMs | Firecracker microVM isolation per Lambda invocation; up to 8hr runtime, 10GB memory, configurable auto-suspend/resume | [SecurityFrameworks/agent-sandboxing.md](../SecurityFrameworks/agent-sandboxing.md) |
| AWS Agent-EvalKit | Apache-2.0 OSS eval toolkit; six-phase workflow combining code-based and LLM-as-judge evaluators; integrates with Claude Code, Kiro CLI, Kilo Code | [EvaluationFrameworks/platforms.md](../EvaluationFrameworks/platforms.md) |
| AWS AgentOps Four-Pillar Framework | Governance & Security / Build & Operations / Evaluation / Observability & Monitoring framework for operationalizing agents on Amazon Bedrock AgentCore | [AgentOps/README.md](../AgentOps/README.md) |
| AWS QuickSight Topics | BI-native semantic layer for QuickSight — business terms, synonyms, field roles, and semantic types powering natural-language Q&A via Amazon Q | [AgenticTechStack/semantic-data-layer-radar.md](../AgenticTechStack/semantic-data-layer-radar.md) |
| AWS AgentCore Memory | Fully managed short-term + long-term memory service; Extraction → Consolidation → Reflection pipeline; configurable retention up to 365 days; three extraction tiers (zero-config / guided / custom) | [AgentPlatforms/aws-agentcore.md](../AgentPlatforms/aws-agentcore.md) |
| Agent Memory Systems (Module 7 Workshop) | Deep-dive on memory taxonomy, HNSW vs IVF+PQ vector indexes, hybrid BM25+dense+RRF+reranker pipeline, GraphRAG with Neo4j, Redis/MongoDB hot-cold handoff, memory governance (lineage, retention, PII, right-to-delete) | [AgentMemory/ltm-strategies.md](../AgentMemory/ltm-strategies.md) |
| AWS Bedrock Evaluations | Managed Bedrock evaluation service — model comparison, LLM-as-a-judge (GA Mar 2025), Knowledge Bases RAG evaluation, and SageMaker Ground Truth human review | [EvaluationFrameworks/platforms.md](../EvaluationFrameworks/platforms.md) |

## See Also

- [Agent Platforms Overview](../AgentPlatforms/README.md)
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Production Best Practices — State & Memory](../ProductionBestPractices/state-memory.md)
- [Evaluation Tech Radar](../EvaluationFrameworks/tech-radar.md)
