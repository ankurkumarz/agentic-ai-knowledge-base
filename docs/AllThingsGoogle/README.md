---
type: Vendor Hub
title: Google — Agentic AI Overview
description: "Google's agentic AI portfolio spans foundational research, developer frameworks, managed cloud platforms, and security standards"
tags: [google, vendor, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# Google — Agentic AI Overview

## Overview

Google's agentic AI portfolio spans foundational research, developer frameworks, managed cloud platforms, and security standards. Google introduced the Transformer architecture (2017) and continues to contribute heavily to open agent tooling, multi-agent protocols, and enterprise deployment patterns via Google Cloud.

## Key Offerings

| Product / Area | One-liner | Wiki Reference |
|---|---|---|
| Gemini CLI | *(Sunsetting)* Open-source terminal coding agent (Apache 2.0) for Free/Pro/Ultra tiers — retired June 18, 2026 in favor of Antigravity CLI; Enterprise/Cloud-billed/API-key users retain access | [AICodingAgents/ai-coding-agents.md](../AICodingAgents/ai-coding-agents.md) |
| Google Antigravity (CLI / 2.0 / SDK / IDE) | Agent-first development platform succeeding Gemini CLI — async multi-agent orchestration, Go-based CLI, Gemini 3.5 Flash default | [AICodingAgents/ai-coding-agents.md](../AICodingAgents/ai-coding-agents.md#google-antigravity-cli-ide-sdk) |
| Google ADK | Agent Development Kit — open-source framework for building single and multi-agent systems | [AgenticFrameworks/google-adk.md](../AgenticFrameworks/google-adk.md) |
| Gemini Enterprise Agent Platform | Google Cloud's comprehensive platform for building, scaling, governing, and optimizing agents — successor to Vertex AI; GA April 22, 2026 at Cloud Next '26, absorbing Agentspace into the sibling Gemini Enterprise app | [AgentPlatforms/gemini-enterprise-agent-platform.md](../AgentPlatforms/gemini-enterprise-agent-platform.md) |
| Agent Compute Engine | Agent-first Cloud Hypervisor microVM service with Titanium-backed isolation, copy-on-write memory, idle checkpoint/restore, per-agent identity, external egress credential injection, and persistent Hyperdisk workspaces; custom-agent preview planned in the coming months as of October 22, 2026 | [Agent Platform](../AgentPlatforms/gemini-enterprise-agent-platform.md); [source](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) |
| Expanded agent governance | Gateway, Registry, SPIFFE identity, and OpenTelemetry across Google runtimes; Envoy-based hybrid/multicloud and managed-endpoint governance preview soon; token budgets, spend attribution, model routing, Service Extensions, partner authorization, and Cloud Run Express Link preview planned this quarter (October 22, 2026 announcement) | [Agent Platform](../AgentPlatforms/gemini-enterprise-agent-platform.md); [Agent Identity](../SecurityFrameworks/agent-identity.md); [source](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) |
| SAIF Framework | Secure AI Framework — Google's security reference model for AI workloads | [SecurityFrameworks/google-saif.md](../SecurityFrameworks/google-saif.md) |
| GenOps | Google Cloud's evolution of MLOps adapted for generative AI and agent lifecycle management | [AgentOps/genops.md](../AgentOps/genops.md) |
| Google Maturity Model | Google's perspective on agentic AI adoption maturity stages | [MaturityModels/google.md](../MaturityModels/google.md) |
| Gemini Enterprise — Enterprise Comparison | Gemini platform in the context of the top 10 enterprise agentic AI platforms for 2026 | [AgentPlatforms/enterprise-platforms-2026.md](../AgentPlatforms/enterprise-platforms-2026.md) |
| Google Agent Gallery (Agents Marketplace) | Partner-built agents embedded in the Gemini Enterprise app — 50+ certified partners, A2A protocol, two-step IT governance, $750M partner fund | [Marketplace/google-cloud-marketplace.md](../Marketplace/google-cloud-marketplace.md) |
| Google Skills Repository | Official GitHub repository of ready-made skills for Gemini CLI and Google ADK-based agent harnesses | [Standards/skills.md#provider-skills-repositories](../Standards/skills.md) |
| Open Knowledge Format (OKF) | Open specification (v0.1, June 2026) for portable, agent- and human-readable knowledge bundles — markdown + YAML frontmatter, no SDK or runtime required | [Standards/open-knowledge-format.md](../Standards/open-knowledge-format.md) |
| Agent Client Protocol (ACP) | Gemini CLI was Google's first ACP-native integration, validating Zed's editor-agent interoperability standard | [Standards/agent-client-protocol.md](../Standards/agent-client-protocol.md) |
| Kubernetes Agent Sandbox | Kubernetes SIG Apps subproject (launched KubeCon Atlanta, Nov 2025); GKE productization now GA with Pod Snapshots, sub-second sandbox provisioning, and up to 30% better price-performance on Axion | [Standards/k8s-agent-sandbox.md](../Standards/k8s-agent-sandbox.md) |
| Agent Substrate | Open-source Kubernetes-native execution runtime with idle-memory snapshot/resume, per-agent identity, microVM or gVisor isolation, external credential injection, and Filestore workspaces; Google reports up to 10x compute density and benchmark validation with 200,000 agents, 500 activations/second, and <500 ms suspend/resume latency (October 22, 2026); broader governance integration planned | [Standards/k8s-agent-sandbox.md](../Standards/k8s-agent-sandbox.md#agent-substrate-new-separate-open-source-project); [source](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) |
| Agent Identity | Per-agent SPIFFE-based identity with short-lived, IAM-governed credentials; an auth manager brokers outbound API keys and OAuth credentials, and agents cannot be impersonated | [SecurityFrameworks/agent-identity.md](../SecurityFrameworks/agent-identity.md) |
| Looker Semantic Layer (LookML) | Mature BI-native semantic modeling language — single source of truth for business metrics, grounding gen AI trustworthiness; OSI ecosystem participant | [AgenticTechStack/semantic-data-layer-radar.md](../AgenticTechStack/semantic-data-layer-radar.md) |
| LLM EvalKit | Open-source, self-hostable app on Vertex AI SDKs — no-code UI centralizing prompt creation, testing, versioning, and metric-driven evaluation | [EvaluationFrameworks/platforms.md](../EvaluationFrameworks/platforms.md) |
| DESIGN.md | Google Labs format spec for giving coding agents a persistent, structured understanding of a product's visual identity — YAML design tokens + markdown rationale prose | [Standards/design-md.md](../Standards/design-md.md) |
| Building the Agentic Enterprise (Pantsjoha, 2026) | Practical field guide to designing, deploying, and operating agentic AI systems on Google Cloud using ADK — covers the Three Pillars, RAO loop, architectural patterns, AgentOps/EvalOps, platform engineering, and operating model transformation | [SoftwareAIFactory/building-the-agentic-enterprise.md](../SoftwareAIFactory/building-the-agentic-enterprise.md) |

## See Also

- [Agent Platforms Overview](../AgentPlatforms/README.md)
- [Google Cloud Agents Marketplace](../Marketplace/google-cloud-marketplace.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)
- [Agent Evaluation Platforms](../EvaluationFrameworks/platforms.md)
- [Evaluation Tech Radar](../EvaluationFrameworks/tech-radar.md)

## References

- [Introducing Agent Compute Engine and expanded agent governance](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) — Google Cloud, October 22, 2026; key extracts on compute, Agent Substrate, and governance. Benchmarks are vendor-reported; availability timelines reflect the announcement, not general availability.
