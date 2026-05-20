# AOS-0005 — Consent Semantics

Status: Draft 0.1.1 — pre-normative.  
Audience: consent-layer authors, SDK authors, kernel authors, safety assessors, and institutional reviewers.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0005 defines consent as deterministic safety state.

Consent in AxonOS is not a banner, checkbox, preference flag, or legal text
display. Consent is runtime state enforced below the application layer.

## 2. Core rule

Consent withdrawal must be enforceable below the application layer.

## 3. Consent versus permission

Permission answers what event class an application may receive. Consent answers
whether the current session is authorized to deliver consent-dependent events.
Safety state answers whether delivery or actuation is currently allowed.

## 4. Minimum state model

Draft states include NoConsent, Granted, Suspended, Withdrawn, Expired, and
Faulted. Implementations may add states but must not weaken these semantics.

## 5. Terminal withdrawal

Withdrawal is terminal for the current session. The system must not silently
return to Granted after withdrawal. A new session or explicit re-grant is
required.

## 6. Hardware-gated consent

Hardware gating may connect consent state to stimulation enable lines, safety
relays, actuator interlocks, watchdog safe idle, secure-world state, or
equivalent controls. Status must be labelled implemented, simulated, stubbed,
pending, or not applicable.

## 7. Requirements

Draft alignment requires an explicit state machine, terminal withdrawal,
suspension and expiry denial semantics, fail-closed fault behavior, permission
integration, no application override, auditability, and tests for invalid
escalation.

## 8. Summary

Consent in AxonOS is a system state, not a UI artifact.
