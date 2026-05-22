# AxonOS Cross-Repository Compatibility Matrix

Status: Draft 0.1.0  
Authority: AxonOS Standard  
Date: 2026-05-22

This document defines the compatibility surface between AxonOS repositories.

## Repository Matrix

| Repository | Role | Current Version | Status |
|---|---|---:|---|
| axonos-standard | Normative standard authority | 0.1.x | Canonical |
| axonos-rfcs | Engineering RFC process | draft/active/final | Normative when finalized |
| axonos-consent | Consent state-machine reference crate | 0.3.x | Pre-clinical reference |
| axonos-sdk | Application-facing SDK | 0.3.x | Requires protocol sync |
| axonos-kernel | Real-time kernel substrate | 0.2.x | Research-grade kernel substrate |
| axonos-swarm | Distributed timing research | 0.2.x | Experimental |
| axon-bci-gateway | Acquisition-boundary fork | 1.0.0 | Non-safety acquisition boundary |

## Interface Authorities

| Interface | Source of Truth | Implementing Repositories |
|---|---|---|
| Consent state machine | AxonOS Standard + consent RFC | axonos-consent, axonos-sdk |
| Intent observation ABI | AOS-0007 / RFC intent ABI | axonos-sdk, axonos-kernel |
| IPC timing contract | AOS-0008 | axonos-kernel |
| Neural intent processing | AOS-0012 | future classifier pipeline |
| Acquisition boundary | AOS-0001 mapping | axon-bci-gateway |
| Distributed timing | RFC / experimental | axonos-swarm |

## Compatibility Rules

1. A repository MUST NOT claim conformance to an AOS artifact unless required evidence exists.
2. A repository MUST declare protocol and ABI versions visibly.
3. Experimental repositories MUST be labelled experimental.
4. Gateway repositories MUST NOT claim kernel-level real-time, clinical, or regulatory status.
5. Consent and SDK versions MUST be synchronized before safety-critical claims.
6. Kernel and SDK ABI changes MUST be reflected in RFCs and this matrix.

## Current Known Gaps

| Gap | Severity | Required Action |
|---|---|---|
| Consent protocol version authority is fragmented | High | Add explicit consent protocol version matrix |
| SDK / consent compatibility not yet frozen | High | Add cross-repo ABI tests |
| Independent review trail not yet visible | High | Add CODEOWNERS and Reviewed-by process |
| Claim registry not yet enforced by CI | Medium | Add claim verification tooling |
| SBOM generation not yet org-wide | Medium | Add cargo-sbom / dependency inventory |
| Security disclosure policy not yet centralized | Medium | Add org-level security policy |

## Release Blocking Rule

A release that changes an ABI, wire format, consent event, or timing claim MUST update this matrix in the same pull request or commit.
