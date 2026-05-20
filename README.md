# AxonOS Standard

[![CI](https://github.com/AxonOS-org/axonos-standard/actions/workflows/ci.yml/badge.svg)](https://github.com/AxonOS-org/axonos-standard/actions/workflows/ci.yml)

**Canonical draft technical standard for deterministic brain-computer interface software.**

AxonOS defines the missing operating layer between neural hardware and intelligent applications:
a deterministic, privacy-preserving, capability-gated software foundation for BCI systems.

Status: **Draft 0.1 — pre-normative.**

This repository is the canonical entry point for AxonOS architecture, terminology,
conformance profiles, validation discipline, neural permissions, consent semantics,
and governance. It is not yet a finalized conformance standard.

## Canonical AOS artifacts

The Draft 0.1 artifact sequence is maintained in [`standard/`](./standard).

| Artifact | Title |
|---|---|
| [`AOS-0000`](./standard/AOS-0000-charter-and-scope.md) | Charter and Scope |
| [`AOS-0001`](./standard/AOS-0001-system-boundary.md) | System Boundary |
| [`AOS-0002`](./standard/AOS-0002-terminology.md) | Terminology |
| [`AOS-0003`](./standard/AOS-0003-evidence-levels-and-claims.md) | Evidence Levels and Claims |
| [`AOS-0004`](./standard/AOS-0004-neural-permissions.md) | Neural Permissions |
| [`AOS-0005`](./standard/AOS-0005-consent-semantics.md) | Consent Semantics |
| [`AOS-0006`](./standard/AOS-0006-conformance-profiles.md) | Conformance Profiles |
| [`AOS-0007`](./standard/AOS-0007-intent-event-model.md) | Intent Event Model |
| [`AOS-0008`](./standard/AOS-0008-ipc-and-timing-contract.md) | IPC and Timing Contract |
| [`AOS-0009`](./standard/AOS-0009-security-and-privacy-threat-model.md) | Security and Privacy Threat Model |
| [`AOS-0010`](./standard/AOS-0010-reference-implementation-mapping.md) | Reference Implementation Mapping |
| [`AOS-0011`](./standard/AOS-0011-governance-and-change-control.md) | Governance and Change Control |

## Principles

1. Neural data is not application data.
2. Consent withdrawal must be enforceable below the application layer.
3. Real-time claims must be falsifiable.
4. Privacy must be structural, not policy-only.
5. Reference implementations must not claim beyond their evidence level.

## Reference implementations

| Repository | Role |
|---|---|
| `axonos-kernel` | deterministic real-time kernel substrate |
| `axonos-sdk` | typed intent and capability API |
| `axonos-rfcs` | engineering RFC process |
| `axonos-consent` | consent state machine and safety-gating semantics |
| `axonos-swarm` | experimental distributed timing layer |
| `axon-bci-gateway` | acquisition integration gateway |

## Contact

General / institutional: connect@axonos.org  
Security: security@axonos.org  
Website: https://axonos.org
