# AOS-0005 — Consent Semantics

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0005 defines consent as a deterministic safety-state model. Consent in AxonOS is runtime state enforced below the application layer.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Consent versus permission

Permission asks what class of event an application may receive. Consent asks whether the current session is authorized. Safety state asks whether delivery or actuation is allowed.

## 4. Minimum state model

The draft model includes NoConsent, Granted, Suspended, Withdrawn, Expired, and Faulted.

## 5. Terminal withdrawal

Terminal withdrawal means withdrawal is terminal for the current session. After withdrawal, the system must not silently return to Granted.

## 6. Suspension and expiry

Suspension is temporary denial. Expiry is end of session authorization. Both deny delivery while active.

## 7. Fault behavior

Faulted state represents invalid transitions, corrupted records, replay attempts, conflicting state, interlock mismatch, authentication failure, or counter violation.

## 8. Hardware-gated consent

Hardware-gated consent may connect consent state to stimulation enable lines, safety relays, actuator interlocks, watchdog safe idle, secure-world state, or equivalent controls.

## 9. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Represent consent as an explicit state machine.
2. Treat withdrawal as terminal for the current session.
3. Deny delivery under suspension, expiry, withdrawal, and fault.
4. Prevent application override of withdrawal.
5. Label hardware-gating status accurately.
6. Provide transition auditability.

## 10. Minimum verification expectations

1. Tests cover grant, withdraw, suspend, resume, expire, fault, and reset-session paths.
2. Negative tests reject resume after withdrawal.
3. Delivery after expiry is denied.
4. Delivery after suspension is denied.
5. Delivery after fault is denied.
6. Hardware-gated claims include status and evidence level.

## 11. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Consent stored only as a UI checkbox.
2. Automatic re-grant after withdrawal.
3. Expired session continuing event delivery.
4. Hidden background session after UI close.
5. Hardware-gating claim with only host-side state.

## 12. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 13. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
