# AOS-0004 — Neural Permissions

Status: Draft 0.1 — pre-normative.  
Audience: implementers, SDK authors, kernel authors, application developers, safety assessors, and privacy reviewers.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

This artifact defines the AxonOS neural-permission model.

The central rule is:

> Neural data is not application data.

A BCI application must not receive arbitrary neural signal data merely because it is installed, authenticated, paired with a device, or running inside a trusted user interface. Access to neural-derived information must be mediated by explicit permissions, typed event boundaries, consent state, and implementation-level enforcement.

The goal is not to make neural data unusable. The goal is to make the permitted data class precise, auditable, and revocable.

## 2. Threat model

The neural-permission model assumes that applications may be:

- honest but over-broad in requested access;
- buggy;
- compromised;
- economically incentivized to collect more data than required;
- capable of correlating neural-derived data with external identifiers;
- capable of exporting application-observable events;
- capable of misrepresenting permission scope in the user interface.

The model does not assume that application code is trusted.

The model also assumes that raw or high-resolution neural data may encode sensitive information beyond the immediate user intent. That information may include identity-correlated features, affective correlates, workload, fatigue, artifacts, health-related signals, or behavioral patterns not required for the stated application purpose.

## 3. Permission object

A neural permission is a typed authority to receive a class of neural-derived event.

A permission should include at least:

| Field | Meaning |
|---|---|
| `permission_id` | Stable identifier for the permission |
| `event_type` | Event class authorized by the permission |
| `scope` | Session, device, task, or application scope |
| `max_rate_hz` | Maximum delivery rate, if applicable |
| `payload_class` | Kind of data exposed |
| `consent_required` | Whether active consent is required |
| `revocation_behavior` | What happens when permission is revoked |
| `evidence_level` | Evidence level of enforcement claim |

A permission is not a text label. It is an enforceable authority.

## 4. Default denial

A conforming implementation must deny access to raw neural data by default.

Default denial means:

- applications do not receive raw EEG or equivalent raw streams unless explicitly authorized by a standard-defined mechanism;
- absence of a permission is denial;
- unknown event classes are denied;
- expired permissions are denied;
- permissions outside scope are denied;
- withdrawn consent disables dependent permissions;
- safety suspension disables dependent permissions.

Default denial must occur below the application user interface.

## 5. Typed event classes

AxonOS applications should receive typed event classes instead of raw neural streams.

Draft event classes may include:

| Event class | Description | Raw data exposure |
|---|---|---|
| `NavigationIntent` | Discrete navigation or motor-intent symbol | No |
| `WorkloadAdvisory` | Low-resolution workload state | No |
| `SessionQuality` | Signal/session quality state | No |
| `ArtifactEvent` | Eye, muscle, motion, electrode artifact class | No |
| `ConsentStateChanged` | Consent state transition notification | No |
| `SafetyInterlockState` | Hardware or software safety gate state | No |

An implementation must document every event class it exposes.

## 6. Prohibited default classes

The following classes must not be available by default:

- raw neural signal streams;
- continuous emotion inference;
- cognitive profile extraction;
- re-identification features;
- background mental-state telemetry;
- unbounded session replay;
- hidden high-rate diagnostic streams;
- arbitrary classifier embeddings;
- raw feature vectors sufficient to reconstruct sensitive state.

A future AxonOS version may define exceptional research profiles for some classes, but such profiles must be explicit, consent-gated, evidence-tagged, and not the default application profile.

## 7. Manifest model

Applications should declare requested permissions in a manifest.

A manifest should state:

- application identity;
- requested event classes;
- requested rate limits;
- purpose string;
- consent dependency;
- storage behavior;
- egress behavior;
- retention behavior;
- version of the AxonOS Standard used.

A manifest is invalid if it requests unknown event classes or attempts to collapse distinct permissions into a generic all-access permission.

## 8. Capability gate

A capability gate is the enforcement point where event delivery is allowed or denied.

The gate should evaluate:

1. Does the application hold the permission?
2. Is the permission within scope?
3. Is the session active?
4. Is consent granted?
5. Is safety state compatible with delivery?
6. Is the event rate within bounds?
7. Is the event class permitted for this application profile?
8. Is the implementation version compatible with the manifest version?

If any check fails, delivery is denied.

## 9. Permission and consent separation

Permission and consent are distinct.

Permission answers:

> What class of neural-derived event may this application receive?

Consent answers:

> Is this session currently authorized to deliver consent-dependent events?

An application may hold a permission while delivery is still denied because consent is suspended, withdrawn, expired, or faulted.

## 10. Rate bounds

Rate bounds are part of privacy.

A low-resolution event delivered at 1 Hz has a different privacy profile from a high-rate event delivered at 250 Hz. An implementation should document maximum delivery rates for each event class.

Rate limits should be enforced below the application layer when the claim is security- or privacy-relevant.

## 11. Raw data exceptions

Draft 0.1 does not define a general-purpose raw neural data permission for ordinary applications.

If an implementation exposes raw neural data for research, debugging, or hardware validation, it must label that access as one of:

- research-only;
- diagnostic-only;
- developer-only;
- hardware-validation-only;
- non-conformant experimental access.

Such access must not be presented as ordinary AxonOS application behavior.

## 12. Storage and egress

A permission to receive an event is not automatically a permission to store, export, transmit, or sell it.

Future versions of the standard should distinguish:

- observe permission;
- store permission;
- transmit permission;
- aggregate permission;
- train-model permission;
- third-party-share permission.

Until those distinctions are normative, implementations must not imply that event delivery alone authorizes unrestricted downstream use.

## 13. Auditability

Permission decisions should be auditable.

An implementation should be able to answer:

- which application received which event class;
- under which permission;
- under which consent state;
- at what rate;
- during which session;
- through which enforcement point;
- under which standard version.

The audit log itself may contain sensitive metadata and must be protected.

## 14. Failure behavior

If permission state is corrupted, missing, ambiguous, stale, incompatible with the current standard version, or inconsistent with consent state, the system should fail closed.

Fail-closed means denial of event delivery, not best-effort delivery.

## 15. Conformance requirements

A draft AxonOS neural-permission implementation should satisfy:

1. raw neural data denied by default;
2. typed event classes documented;
3. permissions represented explicitly;
4. consent dependency represented explicitly;
5. unknown event classes denied;
6. rate limits documented where relevant;
7. prohibited default classes absent;
8. failure behavior is fail-closed;
9. permission decisions auditable;
10. storage and egress scope not implied by observation permission alone.

## 16. Non-conformance examples

The following are not conformant with this artifact:

- a wildcard `neural:*` permission for ordinary applications;
- raw EEG delivery to all installed apps;
- continuous emotion inference hidden under a generic analytics event;
- permission checks only in UI code;
- consent withdrawal that does not disable event delivery;
- rate limits documented but not enforced;
- application-controlled safety override;
- undocumented debug stream with high-rate neural features.

## 17. Relationship to implementations

This artifact informs:

- `axonos-sdk` manifest design;
- `axonos-kernel` capability-gate behavior;
- `axonos-consent` consent dependency behavior;
- `axon-bci-gateway` gateway scope limits;
- future conformance tests.

## 18. Open issues

Draft 0.1 leaves the following unresolved:

- canonical permission descriptor wire format;
- final event type registry;
- machine-readable manifest schema;
- conformance test suite;
- storage and egress permission profiles;
- formal privacy leakage bounds per event class;
- registry for prohibited and research-only classes.

## 19. Summary

Neural permissions are the AxonOS answer to a simple systems problem:

> Applications should receive the neural-derived information they are authorized to use, and nothing else by default.

This principle is foundational for AxonOS privacy, consent, and safety.
