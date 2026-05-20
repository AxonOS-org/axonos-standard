# AOS-0004 — Neural Permissions

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0004 defines the AxonOS neural-permission model. It operationalizes the rule that neural data is not application data.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Threat model

Applications may be honest but over-broad, buggy, compromised, economically incentivized to over-collect, or capable of correlating event streams with external identifiers.

## 4. Permission object

A neural permission is typed authority over an event class. It identifies event type, scope, max rate, payload class, consent dependency, revocation behavior, and evidence.

## 5. Default denial

Default denial states that raw neural data is denied by default. Unknown event classes are denied. Withdrawn consent disables dependent permissions.

## 6. Typed events

Applications should consume typed events such as NavigationIntent, WorkloadAdvisory, SessionQuality, ArtifactEvent, ConsentStateChanged, and SafetyInterlockState.

## 7. Capability gate

The gate checks permission, scope, session, consent, safety state, event rate, event class, and version compatibility.

## 8. Prohibited default classes

Prohibited default classes include raw streams, continuous emotion inference, cognitive profile extraction, re-identification features, unbounded replay, and hidden high-rate diagnostics.

## 9. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Deny raw neural data by default.
2. Represent permissions explicitly.
3. Document typed event classes.
4. Represent consent dependency explicitly.
5. Fail closed on unknown event classes.
6. Separate observe, store, transmit, aggregate, and model-training semantics when claimed.

## 10. Minimum verification expectations

1. Manifest tests deny unknown event classes.
2. Permission checks deny expired and out-of-scope permissions.
3. Consent withdrawal disables dependent permissions.
4. Rate bounds are documented and tested.
5. Audit log can identify delivery authority.

## 11. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. A wildcard `neural:*` permission for ordinary applications.
2. Raw EEG delivery to all installed apps.
3. Continuous emotion inference hidden as analytics.
4. Permission checks only in UI code.
5. Consent withdrawal that does not disable event delivery.

## 12. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 13. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
