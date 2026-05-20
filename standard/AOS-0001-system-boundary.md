# AOS-0001 — System Boundary

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, hardware teams, application developers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0001 defines where AxonOS sits in a BCI system.

Most BCI software failures begin as boundary failures. A system that cannot say
where raw neural data ends, where deterministic processing begins, where
application behavior is permitted, and where consent is enforced cannot make
credible safety, privacy, or real-time claims.

## 2. Canonical model

```text
Neural hardware
  ↓
Acquisition / gateway
  ↓
AxonOS deterministic substrate
  ↓
Typed intent and neural-permission boundary
  ↓
Applications
```

The core rule is:

> Raw neural data must not cross into application space by default.

## 3. Hardware boundary

Neural hardware includes electrodes, analog front-ends, ADCs, amplifiers,
stimulation hardware, isolation components, secure elements, radios, and
transport components.

AxonOS does not standardize electrode geometry or clinical therapy. It
standardizes the software boundary receiving neural-derived data and enforcing
deterministic processing, permissioned access, consent state, and safety
behavior.

## 4. Gateway boundary

A gateway may integrate external tools and provide hardware-in-the-loop
acquisition. A gateway is not automatically a safety-critical substrate.

A gateway repository must state whether it is an integration fork, reference
gateway, test harness, research prototype, or production component.

## 5. Deterministic substrate

The deterministic substrate owns real-time scheduling, monotonic time, bounded
IPC, safety-state handling, and capability enforcement.

Application code must not be responsible for hard real-time enforcement of the
neural signal path. If application behavior can introduce unbounded delay into
the critical path, the system is not a conforming safety-critical substrate.

## 6. Typed intent boundary

The typed intent boundary separates raw neural data from application-observable
events.

Applications should receive typed events such as navigation intent, workload
advisory, session quality, artifact event, consent state change, or safety
interlock state.

## 7. Application boundary

Applications may request permissions, receive authorized typed events, display
consent state, and respond to safety transitions.

Applications must not override withdrawal, safety suspension, capability checks,
or kernel timing policy.

## 8. Consent and safety boundary

Consent enforcement belongs below application policy. A UI can present consent,
but withdrawal and expiry must affect event delivery through system state.

Safety behavior must be explicit. Deadline miss, buffer overrun, gateway
disconnect, invalid input, and application crash must have documented behavior.

## 9. Requirements

A draft-aligned implementation should identify its system role, prevent raw
neural data from entering application space by default, define where consent is
enforced, define where permissions are checked, and document fail-closed
behavior.

## 10. Non-conformance examples

A GUI that streams raw EEG to plugins, an application that treats withdrawal as
a UI-only flag, a gateway that claims kernel safety without scheduling evidence,
and an SDK that grants all event classes by default are not aligned with this
artifact.

## 11. Summary

The boundary model is the foundation for neural permissions, consent semantics,
conformance profiles, and claims discipline.
