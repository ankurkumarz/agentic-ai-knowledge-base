---
type: Standard
title: SPIFFE and SPIRE
description: "SPIFFE is an open standard for issuing short-lived, cryptographically verifiable identities to software workloads, and SPIRE is its CNCF reference implementation"
tags: [standards, security, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# SPIFFE and SPIRE

## Overview

SPIFFE (Secure Production Identity Framework For Everyone) is a specification for giving software workloads a verifiable identity that does not depend on static secrets. SPIRE is the reference implementation: it attests workloads and issues their identities. Both are CNCF projects. They matter to agentic AI because agents are non-human workloads that call tools, APIs, and other agents, and the identity model needs to tell one agent apart from another and from the humans who launched it.

The standard defines the identity format, the document types that carry an identity, and the API a workload uses to fetch them. It does not specify how a workload is attested. That job belongs to SPIRE.

## Key Concepts / Architecture

- **SPIFFE ID.** A URI of the form `spiffe://trust-domain/path`, naming a workload within a trust domain.
- **SVIDs.** SPIFFE Verifiable Identity Documents, in two forms: X.509-SVID (a certificate) and JWT-SVID (a token).
- **Workload API.** The local interface through which a workload obtains its SVIDs and the trust bundle needed to verify others.
- **Attestation (SPIRE).** Before issuing an identity, SPIRE checks workload properties such as Kubernetes namespace, service account, cloud instance, or binary hash. A stolen static key cannot simply be replayed from another host, because the identity is bound to attested properties.
- **Short lifetimes.** One secondary source says SPIRE defaults are one hour for X.509-SVIDs and five minutes for JWT-SVIDs, and that operators can change them. Confirm against current SPIRE documentation before relying on these values.

## Governance and Status

- **CNCF status.** Secondary sources disagree on the timeline. One says SPIFFE and SPIRE entered the CNCF Sandbox in 2018 and graduated on September 20, 2022. Another says the CNCF accepted them as incubation-level projects in 2020. The sources agree that both reached graduation, with 2022 as the graduation year.
- **Security review.** The CNCF Special Interest Group for Security (SIG-Security) completed a security assessment, and one source reports no critical findings.

## Where SPIFFE Appears in This Wiki

| Context | How SPIFFE is used |
|---|---|
| [Google Agent Identity](../SecurityFrameworks/agent-identity.md) | Each agent receives a SPIFFE ID, and its Google Cloud access tokens are bound to X.509 certificates |
| [Agent Substrate](k8s-agent-sandbox.md#agent-substrate-new-separate-open-source-project) | Each actor receives a short-lived SPIFFE X.509 certificate by default |
| [Agent Governance Toolkit](../SecurityFrameworks/agent-governance-toolkit.md) | Lists SPIFFE/SVID compatibility for integration with service-mesh identity |
| [NIST AI Agent Standards](nist-ai-agent-standards.md) | Concept-paper direction suggests SPIFFE/SVID for agent identity |

## Considerations

- **Standard is not a policy.** SPIFFE establishes who a workload is. It does not decide what that workload may do. Authorization still needs a policy layer.
- **Attestation is the hard part.** An identity is only as strong as the attestation behind it, so the choice of SPIRE attestation plugins determines the real assurance.
- **Agent-specific gaps.** The standard predates agents. It does not define how to represent a human user who delegated authority to an agent. Delegation is handled by the platform layer, as the Google Agent Identity design shows.

## See Also

- [Agent Identity](../SecurityFrameworks/agent-identity.md) — how agent identities built on SPIFFE are used for authorization and credential brokering
- [Kubernetes Agent Sandbox](k8s-agent-sandbox.md) — Kubernetes-native sandboxing, including Agent Substrate's SPIFFE-based actor identity
- [NIST AI Agent Standards Initiative](nist-ai-agent-standards.md) — standards direction that names SPIFFE/SVID for agent identity
- [Agent Governance Toolkit](../SecurityFrameworks/agent-governance-toolkit.md) — policy enforcement that consumes workload identity
- [Agentic AI Industry Standards](README.md) — standards overview

## References

- [SPIFFE](https://spiffe.io/) — specification and project home (not retrievable while preparing this page; details come from the secondary sources below)
- [SPIRE identity framework (InfoQ, June 2020)](https://www.infoq.com/news/2020/06/spire-identity-framework/) — SPIRE's attestation-based issuance model
- [SPIFFE and SPIRE workload identity for cloud-native environments (SC Media)](https://www.scworld.com/tech-explainer/spiffe-and-spire-workload-identity-for-cloud-native-environments) — explainer on SVIDs and attestation
