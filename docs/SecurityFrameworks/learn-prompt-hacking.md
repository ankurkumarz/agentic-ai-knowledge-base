---
type: Playbook
title: Learn Prompt Hacking
description: Learn Prompt Hacking is an open-source educational repository covering LLM jailbreaking, prompt injection attacks, and red team/blue team defenses for language model applications.
tags: [security, agentic-ai, prompt-engineering, prompt-injection]
timestamp: 2026-08-09T00:00:00Z
---

# Learn Prompt Hacking

## Overview

Learn Prompt Hacking (TrustAI-laboratory) is an open-source educational repository aimed at helping developers, data scientists, and security professionals build a deep understanding of prompt engineering techniques alongside the risks LLM applications face from adversarial prompting. It frames 2023 as the turning point for mass adoption of general-purpose LLMs, and treats the resulting security exposure as a distinct discipline worth structured, course-style coverage rather than ad hoc tips.

## Key Concepts / Scope

The repository organizes its material into offensive and defensive tracks:

**Offensive techniques (attack vectors)**:
- ChatGPT jailbreaks and safety-training bypasses
- Prompt injection attacks against GPT Assistants and custom GPTs
- General LLM prompt vulnerabilities
- Adversarial machine learning techniques applied to language models

**Defensive techniques**:
- Blue team defense strategies for LLM applications
- Inference reinforcement and safety-hardening techniques
- Evaluation benchmarks for testing model and application robustness

## Structure

The material is organized into modules covering: Basics (foundational concepts), Applications (practical implementations), Offensive techniques (prompt hacking methods), Red team exercises (attack simulations), Blue team defenses (mitigation strategies), Evaluation frameworks, and a collection of conference presentations and academic papers.

## Suitable for (Target Audience)

- Data scientists and AI developers who want a practical, structured understanding of how to use LLMs effectively and how those same mechanisms can be abused
- Security professionals building red-team or blue-team competency specific to LLM and agentic applications

## Relation to Agentic AI Security

The techniques the repository catalogs (jailbreaks, prompt injection, adversarial prompting) are the single-turn LLM predecessors to the multi-step, tool-using attack surface covered by agentic red-teaming methodologies such as the [CSA Agentic AI Red Teaming Guide](./agentic-ai-red-teaming-guide.md) — e.g., prompt injection here maps directly onto that guide's "Agent Goal and Instruction Manipulation" (4.4) threat category, and jailbreak/bypass techniques underpin "Agent Hallucination Exploitation" (4.5) and related failure modes once an agent, rather than a single chat turn, is the target.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Prompt injection | Attacker-controlled input overrides system instructions | Privilege separation, input/output filtering, prompt hardening — see [Prompt Engineering — Defenses Against Prompt Injection](../PromptEngineering/README.md#defenses-against-prompt-injection) |
| Jailbreaking | Crafted prompts bypass safety training | Model-based classifiers, inference reinforcement, continuous red-team evaluation against known jailbreak corpora |
| Custom GPT / Assistant exposure | Third-party GPTs and Assistants inherit prompt-injection and system-prompt-exfiltration risk | Treat custom-GPT configuration as a system prompt: avoid embedding secrets, monitor for extraction attempts |
| Skill gap between offense and defense | Teams often learn defensive practice without hands-on exposure to attack techniques | Structured red team / blue team exercises, as modeled by this repository's course structure |

## See Also

- [Agentic AI Red Teaming Guide (CSA)](./agentic-ai-red-teaming-guide.md) — extends single-turn prompt attack taxonomy to multi-step, tool-using agentic systems
- [Prompt Engineering](../PromptEngineering/README.md) — defensive prompt engineering, prompt injection threat model, and structured-output mitigations
- [Agent Security Best Practices](../ProductionBestPractices/security.md) — prompt injection, least privilege, and audit trails in production
- [Agentic AI Security Overview](./Readme.md) — NIST AI RMF, Google SAIF, AWS, Microsoft, Anthropic perspectives

## References

- [GitHub — TrustAI-laboratory/Learn-Prompt-Hacking](https://github.com/TrustAI-laboratory/Learn-Prompt-Hacking)
