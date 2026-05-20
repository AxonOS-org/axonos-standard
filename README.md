# AxonOS Standard

[![CI](https://github.com/AxonOS-org/axonos-standard/actions/workflows/ci.yml/badge.svg)](https://github.com/AxonOS-org/axonos-standard/actions/workflows/ci.yml)

**The canonical technical standard for deterministic brain-computer interface software.**

AxonOS defines the missing operating layer between neural hardware and intelligent applications: a deterministic, privacy-preserving, capability-gated software foundation for brain-computer interface systems.

This repository is the normative documentation hub for the AxonOS standard: architecture, terminology, governance, validation levels, neural permissions, consent semantics, safety boundaries, and reference implementation scope.

AxonOS is not an AI-agent framework, not a wellness app, and not a token project.

It is an operating standard for brain-computer interfaces.

---

## Mission

To establish the deterministic software foundation for safe, private, real-time brain-computer interfaces.

---

## Mandate

AxonOS Standard exists to:

- define the deterministic BCI software architecture;
- maintain neural permissions and consent semantics;
- publish validation levels and evidence requirements;
- coordinate reference implementations;
- prevent unsafe or misleading claims in BCI software infrastructure;
- provide a stable technical vocabulary for researchers, engineers, hardware teams, and institutional partners.

---

## Principles

1. Neural data is not application data.
2. Consent withdrawal must be enforceable below the application layer.
3. Real-time claims must be falsifiable.
4. Privacy must be structural, not policy-only.
5. Reference implementations must not claim beyond their evidence level.
6. Safety boundaries must be inspectable.
7. Public infrastructure should outlive any single product cycle.

---

## Reference implementations

| Repository | Role |
|---|---|
| [`axonos-kernel`](https://github.com/AxonOS-org/axonos-kernel) | Deterministic real-time kernel substrate |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Application-facing typed intent and capability API |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | Engineering RFC process |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Consent state machine and safety-gating semantics |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Experimental distributed timing layer |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | OpenBCI hardware-in-the-loop acquisition gateway |

---

## Repository map

| File | Purpose |
|---|---|
| [`STANDARD.md`](./STANDARD.md) | Canonical standard overview |
| [`GOVERNANCE.md`](./GOVERNANCE.md) | Governance model and change process |
| [`VALIDATION.md`](./VALIDATION.md) | Evidence levels and validation policy |
| [`SECURITY.md`](./SECURITY.md) | Security and disclosure policy |
| [`GLOSSARY.md`](./GLOSSARY.md) | Canonical terminology |
| [`ROADMAP.md`](./ROADMAP.md) | Public roadmap |
| [`architecture/`](./architecture) | Architecture chapters |
| [`validation/`](./validation) | Claims, evidence levels, falsifiable predictions |
| [`legal/`](./legal) | Disambiguation and attribution notes |
| [`rfcs/`](./rfcs) | RFC index and linkage |

---

## Institutional posture

AxonOS is maintained as an open technical standard with public reference implementations.

Institutional conversations are considered selectively where the collaboration strengthens the standard, validation program, safety review, or reference implementation.

Capital is not treated as a substitute for technical evidence.

---

## Contact

- General / institutional: [connect@axonos.org](mailto:connect@axonos.org)
- Security: [security@axonos.org](mailto:security@axonos.org)
- Project: [axonos.org](https://axonos.org)
