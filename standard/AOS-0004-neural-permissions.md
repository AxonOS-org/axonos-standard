# AOS-0004 — Neural Permissions

Status: Draft 0.1 — pre-normative.  
Audience: SDK authors, kernel authors, application developers, safety assessors, and privacy reviewers.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0004 defines the AxonOS neural-permission model.

The central rule is:

> Neural data is not application data.

A BCI application must not receive arbitrary neural signal data merely because it
is installed, authenticated, paired with a device, or running inside a trusted UI.

## 2. Threat model

Applications may be honest but over-broad, buggy, compromised, economically
incentivized to over-collect, or capable of correlating neural-derived events
with external identifiers.

The model does not assume application code is trusted.

## 3. Permission object

A neural permission is typed authority to receive a class of neural-derived
event. It should include permission id, event type, scope, max rate, payload
class, consent dependency, revocation behavior, and evidence level.

## 4. Default denial

Raw neural data is denied by default. Unknown event classes are denied. Expired
permissions are denied. Permissions outside scope are denied. Withdrawn consent
disables dependent permissions.

## 5. Typed events

Applications should consume typed events such as navigation intent, workload
advisory, session quality, artifact event, consent state change, and safety
interlock state.

## 6. Prohibited default classes

Raw streams, continuous emotion inference, cognitive profile extraction,
re-identification features, background mental-state telemetry, unbounded session
replay, hidden diagnostics, and classifier embeddings are prohibited by default.

## 7. Capability gate

The gate checks permission, scope, active session, consent state, safety state,
event rate, event class, and version compatibility. If any check fails, delivery
is denied.

## 8. Storage and egress

Permission to observe is not permission to store, transmit, aggregate, train a
model, or share with third parties.

## 9. Auditability

The system should be able to identify which application received which event
class, under which permission, during which session, and under which consent
state.

## 10. Requirements

Draft alignment requires raw data denial by default, explicit permissions,
documented event classes, consent dependency, fail-closed unknown events, and
auditable delivery decisions.

## 11. Non-conformance examples

A wildcard `neural:*` permission, raw EEG delivery to all apps, continuous emotion
inference hidden as analytics, UI-only permission checks, or withdrawal that does
not disable event delivery is not aligned.

## 12. Summary

Neural permissions are the structural privacy boundary of AxonOS.
