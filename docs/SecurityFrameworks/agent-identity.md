---
type: Playbook
title: Agent Identity
description: "Agent identity gives each autonomous agent its own short-lived, verifiable identity so that its access can be authorized, audited, and revoked separately from the humans and shared service accounts it works with"
tags: [security, identity, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# Agent Identity

## Overview

Agents act on their own: they call APIs, read data, and invoke other agents, often for long periods and without a human approving each step. Most existing cloud identity models were designed for humans and for workloads that run a fixed program. Shared service accounts and long-lived API keys make it hard to answer basic questions: which agent did this, on whose behalf, with what authority, and how do we revoke that one agent without affecting the others.

Agent identity addresses this by giving each agent (or each agent runtime instance) its own identity, short-lived credentials bound to that identity, and an audit trail attributed to it. It builds on workload identity standards such as [SPIFFE](../Standards/spiffe-spire.md) rather than inventing a new credential format.

## Key Concepts

- **Per-agent identity.** Each agent has a distinct identifier, so access can be granted and revoked per agent rather than per shared account.
- **Short-lived, bound credentials.** Tokens or certificates expire quickly and are cryptographically tied to the identity, so a copied credential is hard to replay.
- **Credential brokering.** The agent does not hold third-party secrets. A broker or egress gateway holds them and attaches them to approved outbound requests only. [OpenShell](openshell.md) and [Agent Substrate](../Standards/k8s-agent-sandbox.md#agent-substrate-new-separate-open-source-project) both use this pattern.
- **Delegated user identity.** When an agent acts for a person, the audit trail should record both the agent and the person. Brokered delegated tokens are one way to do this.
- **Attribution.** Every access event should be attributable to the agent's identity, so incident review can reconstruct what the agent did.

## Case Study: Google Cloud Agent Identity

Google's Agent Identity documentation describes a per-agent identity built on SPIFFE, plus an auth manager for outbound credentials. Details below come from search summaries of the documentation and have not been checked against the live pages.

- **SPIFFE-based identity.** Each agent receives a SPIFFE ID in the form `spiffe://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH`. Access tokens for Google Cloud are bound to the agent's X.509 certificates. IAM allow policies use a matching `principal://` form.
- **Lifecycle.** The identity is tied to the agent's lifecycle and mapped to the resource where the agent runs.
- **Differences from service accounts.** Agent identities are not shared by multiple workloads by default, cannot be impersonated, and do not permit developers to generate long-lived service account keys.
- **Auth manager.** A centralized credentials vault and authentication broker for outbound tool calls. It handles API keys, OAuth client credentials, and delegated end-user tokens. Access to it is governed by IAM, and end-user access events are attributable to the agent's SPIFFE ID.
- **Transport.** Agents authenticate with mTLS for first-party access to the gateway and use DPoP for interactions beyond the gateway.
- **Naming.** Some documentation paths now sit under a "gemini-enterprise-agent-platform" prefix, so product naming may still be changing. See [Gemini Enterprise Agent Platform](../AgentPlatforms/gemini-enterprise-agent-platform.md).

## Comparing Identity Models

| Dimension | Shared service account | Per-agent identity (Google Agent Identity) | Sandboxed actor identity (Agent Substrate) |
|---|---|---|---|
| Identity granularity | Shared by many workloads | One identity per agent | One short-lived SPIFFE certificate per actor |
| Credential lifetime | Often long-lived keys | Short-lived, bound to the identity | Short-lived; actor holds no cloud credentials |
| Impersonation | Possible within the shared account | Not permitted by default | Not applicable: credentials stay at the egress gateway |
| Third-party secrets | Held by the workload | Held by the auth manager | Injected by the egress gateway |
| Audit attribution | To the shared account | To the agent's identity | To the actor and its SPIFFE ID |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Shared credentials | Many agents use one service account, so logs and revocation are coarse | Issue one identity per agent or per agent runtime instance |
| Long-lived secrets | Agents with stored API keys are a persistent exfiltration target | Use short-lived tokens; keep third-party secrets in a broker, not in agent code or context |
| Delegation ambiguity | It is unclear whether an action was taken by the agent or by the person it acts for | Record both identities in the audit trail; scope delegated tokens narrowly |
| Identity without policy | An authenticated agent can still do harmful things | Pair identity with an authorization policy layer such as the [Agent Governance Toolkit](agent-governance-toolkit.md) |

## Considerations

- **Identity is necessary, not sufficient.** Knowing which agent acted does not decide whether it should have acted. Authorization policy and sandboxing still apply ([Agent Sandboxing](agent-sandboxing.md)).
- **Platform dependence.** Where the identity model is provided by a cloud platform, portability and revocation semantics depend on that platform's implementation.
- **Standards alignment.** The NIST agent-standards concept paper points toward SPIFFE/SVID and OAuth 2.0 for agents. See [NIST AI Agent Standards](../Standards/nist-ai-agent-standards.md).

## See Also

- [SPIFFE and SPIRE](../Standards/spiffe-spire.md) — the workload identity standard that agent identities are built on
- [Gemini Enterprise Agent Platform](../AgentPlatforms/gemini-enterprise-agent-platform.md) — platform that provides Google's Agent Identity
- [Agent Governance Toolkit](agent-governance-toolkit.md) — policy enforcement that uses identity for authorization
- [Agent Sandboxing](agent-sandboxing.md) — isolation tiers that complement identity controls
- [OpenShell (NVIDIA)](openshell.md) — credential injection at approved endpoints
- [Kubernetes Agent Sandbox](../Standards/k8s-agent-sandbox.md) — Agent Substrate's SPIFFE-based actor identity
- [NIST AI Agent Standards](../Standards/nist-ai-agent-standards.md) — standards direction for agent identity
- [Production Best Practices — Security](../ProductionBestPractices/security.md) — cross-cutting security guidance

## References

- [Agent identity overview (Google Cloud IAM documentation)](https://docs.cloud.google.com/iam/docs/agent-identity-overview) — primary source for Google's Agent Identity model (summarized from search results; not retrieved directly)
- [SPIFFE](https://spiffe.io/) — workload identity standard (not retrieved directly)
