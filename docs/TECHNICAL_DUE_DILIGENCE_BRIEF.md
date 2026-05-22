# AxonOS Technical Due-Diligence Brief

Status: Public technical brief  
Authority: AxonOS Standard  
Date: 2026-05-22  
Maintainer: Denis Yermakou / AxonOS-org

---

## 1. What AxonOS Is

AxonOS is a cognitive operating-system architecture for brain-computer interface systems.

It is designed as the missing software layer between:

- neural hardware;
- real-time signal acquisition;
- consent and permission enforcement;
- deterministic intent processing;
- AI-enabled applications.

AxonOS is not an AI-agent framework.

AxonOS is not a chatbot runtime.

AxonOS is not a speculative token project.

AxonOS is an operating-system layer for the brain-computer interface boundary.

---

## 2. Core Thesis

Future BCI systems require an operating layer with the same architectural seriousness that classical computers required before general-purpose software ecosystems could emerge.

That layer must provide deterministic timing boundaries, explicit consent-state enforcement, typed neural intent events, capability-based access control, minimal trusted computing base, auditability, and clear separation between raw neural data and application-level abstractions.

AxonOS exists to define and implement that layer.

---

## 3. Repository Roles

| Repository | Role |
|---|---|
| axonos-standard | Canonical standard, architecture, compatibility, claims governance |
| axonos-rfcs | Engineering RFCs and design records |
| axonos-kernel | Real-time kernel substrate and timing-oriented primitives |
| axonos-sdk | Application-facing SDK and typed intent boundary |
| axonos-consent | Consent finite-state machine and neural permission reference crate |
| axonos-swarm | Experimental distributed timing and coordination research |
| axon-bci-gateway | Acquisition-boundary fork for OpenBCI / hardware-in-the-loop workflows |

---

## 4. Current Evidence Posture

AxonOS separates engineering evidence into levels.

| Level | Meaning |
|---|---|
| L0 | Design intent or architecture statement |
| L1 | Static proof, model checking, type-level guarantee, deterministic unit proof |
| L2 | Software test, fuzzing, simulation, CI result |
| L3 | Hardware-in-the-loop or measured physical validation |
| L4 | Independent third-party audit or lab validation |

Current public repositories primarily contain L0, L1, and L2 evidence.

AxonOS does not currently claim L3 or L4 clinical validation.

---

## 5. What Is Already Public

The public project already includes:

- a standard repository;
- an RFC process;
- a Rust kernel substrate;
- a Rust SDK;
- a consent-state reference implementation;
- an acquisition gateway;
- experimental distributed timing work;
- CI and repository-contract checks across several repositories;
- signed commits and releases in key repositories.

This is sufficient for serious technical review.

It is not sufficient for clinical deployment.

---

## 6. Non-Claims

AxonOS does not currently claim:

- FDA clearance;
- CE mark;
- clinical efficacy;
- certified medical-device status;
- production implantation readiness;
- complete IEC 62304 lifecycle package;
- complete ISO 14971 risk-management file;
- independent laboratory validation;
- full medical-device quality-management-system compliance.

These are future validation and governance milestones, not current claims.

---

## 7. Near-Term Milestones

| Milestone | Target Outcome |
|---|---|
| Standard cleanup | Canonical AOS sequence and compatibility matrix |
| Consent hardening | Clear distinction between integrity, authentication, persistence, and audit |
| SDK sync | Explicit consent protocol compatibility |
| Kernel evidence cleanup | Timing claims tied to assumptions and evidence level |
| Gateway stabilization | Clean acquisition-boundary documentation and release surface |
| Governance layer | CODEOWNERS, review policy, security policy, claims registry |

---

## 8. Investor / Reviewer Reading Order

Recommended reading order:

1. axonos-standard/README.md
2. axonos-standard/docs/TECHNICAL_DUE_DILIGENCE_BRIEF.md
3. axonos-standard/docs/governance/COMPATIBILITY.md
4. axonos-standard/docs/regulatory/CLAIMS.md
5. axonos-consent/SPEC.md
6. axonos-sdk/README.md
7. axonos-kernel/README.md
8. axon-bci-gateway/README.md

---

## 9. Summary

AxonOS is a serious pre-clinical infrastructure project for the BCI era.

Its strongest current assets are:

- architectural clarity;
- explicit standardization direction;
- Rust-first implementation discipline;
- consent and permission focus;
- deterministic intent-event model;
- public technical surface.

Its next required evolution is not more hype.

Its next required evolution is evidence governance.
