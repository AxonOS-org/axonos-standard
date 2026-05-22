# AxonOS Claims and Evidence Register

Status: Draft 0.1.0  
Authority: AxonOS Standard  
Date: 2026-05-22

This document separates claims from aspirations.

A claim is valid only when it has:

1. a repository owner;
2. a source artifact;
3. an evidence level;
4. a falsification method;
5. a current status.

## Evidence Levels

| Level | Meaning |
|---|---|
| L0 | Stated design intent, not yet verified |
| L1 | Static proof, model checking, type-level guarantee, or deterministic unit proof |
| L2 | Software test, fuzzing, simulation, property test, CI result |
| L3 | Hardware-in-the-loop or measured physical validation |
| L4 | Independent third-party audit or lab validation |

## Claim Register

| Claim | Repository | Evidence | Status | Notes |
|---|---|---:|---|---|
| AxonOS is a cognitive operating-system architecture for BCI/AI boundary infrastructure | axonos-standard | L0/L1 | Draft | Architecture claim, not clinical claim |
| Consent state transitions are represented as a bounded finite-state machine | axonos-consent | L1/L2 | Active | Requires exact harness mapping |
| Withdrawn is terminal | axonos-consent | L1/L2 | Active | Must remain invariant |
| Consent reference crate is not a full clinical persistence layer | axonos-consent | L0 | Active | Must be explicit in README/SPEC |
| Gateway is acquisition-boundary tooling, not a hard real-time kernel | axon-bci-gateway | L0/L2 | Active | Enforced by CI wording checks |
| AOS-0012 defines deterministic neural intent processing contract | axonos-standard | L0/L1 | Draft | Specification-level claim |
| Kernel timing claims require explicit WCET/WCRT evidence | axonos-kernel | TBD | Pending | No blanket claim without evidence |
| Swarm timing is experimental | axonos-swarm | L0 | Active | Must not be presented as clinical-grade |
| SDK ABI is stable only for declared version pairs | axonos-sdk | TBD | Pending | Requires compatibility matrix |

## Non-Claims

The following are not currently claimed by AxonOS Standard:

- FDA clearance;
- CE mark;
- clinical efficacy;
- certified medical-device status;
- production implantation readiness;
- complete ISO 14971 risk-management file;
- complete IEC 62304 lifecycle package;
- independent L3 laboratory validation;
- production secure-element persistence implementation across all repositories.

## Falsification Discipline

Every quantitative claim must answer:

1. What measurement or proof would disprove it?
2. Which repository owns the test?
3. Is the result L1, L2, L3, or L4?
4. Is the claim derived, simulated, or physically measured?

## Review Rule

Claims involving clinical, regulatory, safety-critical, WCET, WCRT, cryptographic authentication, or formal verification language require explicit review before release.
