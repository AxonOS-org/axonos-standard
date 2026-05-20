# AOS-0001 — System Boundary

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0001 defines where AxonOS sits in a BCI system: between neural hardware and applications, below the typed intent boundary, and above acquisition hardware.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Canonical boundary

The canonical model is: neural hardware → acquisition/gateway → AxonOS deterministic substrate → typed intent and neural-permission boundary → applications. Raw neural data must not cross into application space by default.

## 4. Hardware boundary

Neural hardware includes electrodes, analog front-ends, ADCs, amplifiers, stimulation hardware, isolation components, secure elements, radios, and transport.

## 5. Gateway boundary

A gateway may integrate external tools and provide hardware-in-the-loop acquisition. A gateway is not automatically a safety-critical substrate.

## 6. Deterministic substrate boundary

The deterministic substrate owns real-time scheduling, monotonic time, bounded IPC, safety-state handling, and capability enforcement.

## 7. Application boundary

Applications may receive authorized typed events but must not override withdrawal, safety suspension, capability checks, or kernel timing policy.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Identify the system role of each repository.
2. Prevent raw neural data from entering application space by default.
3. Define where consent is enforced.
4. Define where permission checks occur.
5. State failure behavior for ambiguous boundary states.
6. Do not call an integration gateway a kernel unless it implements substrate requirements.

## 9. Minimum verification expectations

1. Repository README declares boundary role.
2. Gateway docs state integration status unless otherwise evidenced.
3. Application-facing APIs expose typed events rather than raw streams by default.
4. Safety-relevant failures are documented.
5. Boundary claims are mapped to evidence levels.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. A GUI directly streams raw EEG to plugins without permissions.
2. An application treats withdrawal as a UI-only flag.
3. A gateway claims kernel safety without schedulability evidence.
4. An SDK grants all event classes by default.
5. Timing guarantees depend on arbitrary application behavior.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
