---
type: Platform
title: Discovery Loop
description: Discovery Loop is a public benefit corporation, founded by Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, and Quoc Le, building AI systems that run thousands of automated research experiments in parallel to accelerate machine learning, science, and engineering.
tags: [platforms, agentic-ai, research-automation, self-learning]
timestamp: 2026-08-09T00:00:00Z
---

# Discovery Loop

## Overview

Discovery Loop is a Public Benefit Corporation (PBC) announced in August 2026, founded by Jeff Dean (CEO), Sanjay Ghemawat, Oriol Vinyals, and Quoc Le — all departing senior Google / Google DeepMind researchers, with Jeff Dean leaving after 27 years at the company. Its stated mission is to use AI to "turbo-charge" scientific research by automating the research loop itself: instead of humans running experiments one at a time in series, Discovery Loop is building AI systems that propose an experiment, execute the run, learn from the result, and iterate recursively — at a scale of thousands of parallel experiments. The company frames this as expanding the throughput of experimentation broadly, not just accelerating any single experiment.

## Key Concepts / Architecture

- **Continuous exploration loop** — the core primitive is an automated propose → run → learn → iterate cycle, executed by AI agents rather than human researchers, with the explicit goal of running many such loops concurrently rather than sequentially.
- **Massive parallelism as the scaling lever** — the company's stated differentiator versus prior automated-research efforts is scaling the *number* of simultaneous experiment loops, not just the sophistication of any individual agent.
- **Phased domain rollout** — launch focus is automating machine learning research and engineering; the company has stated intent to expand into hardware design, drug discovery, and clean-energy research as later domains.

## Suitable for (Pros)

- Organizations seeking heavily automated, high-throughput ML research and engineering experimentation once the platform is available
- A model for evaluating "AI-for-science" platforms that scale by parallel experiment throughput rather than single-agent capability alone

## Limitations (Cons)

- Pre-product as of announcement (August 2026) — seed round not yet closed, no public product, pricing, or technical architecture documentation available
- Founding team's stated roadmap (ML research → hardware design → drug discovery → clean energy) is aspirational at launch; only ML research/engineering automation is the initial focus
- Details not available in current sources on model architecture, safety/verification approach for autonomously generated experimental claims, or integration surface

## Funding and Backing

- **Investors**: Radical Ventures and Khosla Ventures are co-leading the seed round (round not yet closed; valuation undisclosed)
- **Alphabet** backs the venture both as a founding investor and as a cloud computing partner

## See Also

- [FreePHDLabor](../AgenticFrameworks/freephdlabor.md) — open-source multiagent framework for automating the scientific research lifecycle, a related but independently developed approach to research automation
- [Self-Learning Agents Reference Architecture](../ReferenceArchitecture/self-learning-agents.md) — Agent0 and Claude Managed Agents' Dreaming/Outcomes loop, other approaches to autonomous, iterative agent improvement
- [Agentic AI Platforms](README.md) — survey of managed cloud/SaaS platforms for running agents
- [AgentOps Overview](../AgentOps/README.md) — operational lifecycle considerations for large-scale automated agent fleets

## References

- [Discovery Loop — Continuous Exploration](https://www.discoveryloop.com/)
- [Jeff Dean and other top AI researchers are leaving Google to launch their own startup — TechCrunch](https://techcrunch.com/2026/08/05/jeff-dean-and-other-top-ai-researchers-are-leaving-google-to-launch-their-own-startup/)
- [Our Investment in Discovery Loop — Radical Ventures](https://radical.vc/our-investment-in-discovery-loop/)
- [Jeff Dean and Sanjay Ghemawat Depart Google to Co-Found Discovery Loop — Tech Times](https://www.techtimes.com/articles/323197/20260805/jeff-dean-sanjay-ghemawat-depart-google-co-found-discovery-loop.htm)
- [The startup idea that convinced a UW computer science legend to leave Google after 27 years — GeekWire](https://www.geekwire.com/2026/the-startup-idea-that-convinced-a-uw-computer-science-legend-to-leave-google-after-27-years/)
