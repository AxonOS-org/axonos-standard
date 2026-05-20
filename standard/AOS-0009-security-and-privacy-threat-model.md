# AOS-0009 — Security and Privacy Threat Model

Status: Draft 0.1 — pre-normative.  
Audience: security reviewers, privacy engineers, kernel implementers, SDK authors, application developers, institutional reviewers, and safety assessors.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

This artifact defines the draft security and privacy threat model for AxonOS.

A BCI system processes data that may be more sensitive than ordinary telemetry.
Raw or high-resolution neural data may encode identity-correlated patterns,
intent, workload, artifacts, affective correlates, health-relevant signals, and
behavioral context. Therefore an AxonOS security claim must name the protected
asset, attacker model, trust boundary, and enforcement mechanism.

The goal of this artifact is to prevent vague claims such as "secure",
"privacy-preserving", or "safe" from appearing without a reviewable threat model.

## 2. Protected assets

AxonOS implementations should identify which assets they protect.

| Asset | Description |
|---|---|
| Raw neural data | unredacted samples or equivalent raw streams |
| Intermediate features | classifier features, embeddings, filtered signals |
| Typed intent events | application-observable neural-derived events |
| Consent records | grant, withdrawal, expiry, suspension, reason codes |
| Capability manifests | declared permissions and application authority |
| Session identifiers | session, device, application, or user-context identifiers |
| Audit logs | records of permission, consent, and delivery decisions |
| Cryptographic keys | attestation, signing, encryption, or transport keys |
| Safety-state signals | interlock, safe-idle, stimulation enable, watchdog state |
| Timing traces | observable timing, jitter, scheduling, or transport metadata |

A repository should state which of these it handles.

## 3. Attacker classes

| ID | Attacker | Capability |
|---|---|---|
| A1 | malicious application | requests excessive permissions or misuses delivered events |
| A2 | compromised application | executes attacker-controlled logic inside app boundary |
| A3 | network observer | observes or modifies transport traffic |
| A4 | gateway operator | controls acquisition/integration environment |
| A5 | supply-chain adversary | modifies dependencies, build, firmware, or artifacts |
| A6 | local physical adversary | has physical access to device or debug ports |
| A7 | confused deputy | trusted component misuses authority for untrusted caller |
| A8 | timing observer | observes timing, power, RF, or scheduling side channels |
| A9 | stale-session adversary | replays old consent, permission, or session messages |
| A10 | overclaim adversary | relies on misleading claims to bypass review |

Draft 0.1 does not require every repository to address every attacker. It requires
the relevant attacker set to be explicit.

## 4. Trust boundaries

AxonOS trust boundaries include the hardware acquisition boundary, gateway
boundary, deterministic substrate boundary, typed intent boundary, capability
gate, consent state machine, IPC transport, application sandbox, audit log
boundary, update/build pipeline, and external service boundary.

A security claim must identify which boundary enforces it.

## 5. STRIDE mapping

| STRIDE class | AxonOS example | Mitigation direction |
|---|---|---|
| Spoofing | fake device, fake application, fake consent source | identity, attestation, signed manifests |
| Tampering | modified event, queue state, consent record | integrity checks, bounded state, audit |
| Repudiation | disputed withdrawal or event delivery | transition logs, monotonic counters |
| Information disclosure | raw EEG leaked to application | neural permissions, typed events |
| Denial of service | queue flooding, deadline miss | bounded IPC, backpressure, safe fault |
| Elevation of privilege | app obtains unauthorized event class | capability gate, manifest verification |

STRIDE is not sufficient by itself for BCI safety, but it provides a useful
engineering checklist.

## 6. Neural data disclosure threats

Neural data disclosure may occur through raw signal delivery, high-rate feature
delivery, classifier embeddings, diagnostic streams, logs, exported files, event
timing, side channels, crash reports, analytics integrations, or model-training
pipelines.

A privacy claim must state which path is covered and which paths remain open.

## 7. Consent bypass threats

Consent bypass may occur when application caches an old granted state, withdrawal
is processed only in UI, gateway continues streaming after denial, event queue is
not cleared after withdrawal, stale session token is accepted, replayed grant
frame is accepted, safety suspension does not affect delivery, or hidden
background session remains active.

Consent bypass is a security issue, not merely a UX issue.

## 8. Capability bypass threats

Capability bypass may occur when unknown event classes default to allowed,
wildcard permissions are accepted, diagnostic streams bypass manifest checks,
raw features are mislabeled as low-risk events, one application consumes another
application's session events, or permission state is stored only in application
memory.

Capability enforcement should occur below the application boundary.

## 9. Timing and side-channel threats

Timing can disclose information when execution duration, event timing, packet
rate, power draw, RF behavior, or interrupt timing correlates with neural state.

Draft mitigations include fixed-size event frames where feasible, rate bounds,
deterministic scheduling, avoiding data-dependent branches on sensitive paths,
avoiding early exits that encode class labels, aggregating or coarsening event
delivery, and documenting uncovered timing channels.

A timing side-channel claim must state whether it covers computation timing,
transport timing, scheduler timing, cache pressure, power channels, or RF
channels.

## 10. Supply-chain threats

AxonOS repositories should consider dependency compromise, build script compromise,
toolchain compromise, unsigned release artifacts, malicious GitHub Actions
changes, compromised package registry, stale fork dependency, and tampered
release archives.

Draft mitigations include minimized dependency surface, pinned dependencies for
releases, CI review for workflow changes, signed commits or tags where practical,
reproducible-build roadmap, and security review of unsafe code.

## 11. Audit log privacy

Audit logs are security artifacts and privacy-sensitive artifacts at the same
time. They may reveal when a user used a BCI session, which application requested
access, which event classes were delivered, when consent was withdrawn, and when
artifacts or safety faults occurred.

Audit logs must not become a secondary raw-data leak. Retention, access, export,
and deletion behavior should be documented.

## 12. Disclosure policy

Security reporting must be clear.

Minimum required information includes security contact, affected repositories,
issue classes in scope, requested reproduction details, coordinated disclosure
expectation, and encryption method if high-sensitivity data is involved.

Draft 0.1 notes that publication of a PGP key for `security@axonos.org` remains
pending.

## 13. Minimum threat model record

A repository making security or privacy claims should include:

```text
Threat model:
  protected assets:
  attacker classes:
  trust boundaries:
  enforcement points:
  assumptions:
  out-of-scope threats:
  evidence level:
  artifacts:
```

This prevents claims from floating without system context.

## 14. Risk matrix format

Security and privacy issues should be triaged with at least:

| Field | Meaning |
|---|---|
| asset | protected asset affected |
| attacker | attacker class |
| boundary | enforcement boundary |
| impact | confidentiality, integrity, availability, safety, privacy |
| likelihood | qualitative likelihood |
| detectability | how likely the issue is to be detected |
| mitigation | proposed mitigation |
| residual risk | risk after mitigation |
| evidence | artifact proving mitigation |

This is not a replacement for ISO 14971 risk management, but it creates a
standard engineering bridge between software security and BCI safety.

## 15. Conformance requirements

A draft AxonOS security/privacy implementation should satisfy:

1. protected assets are identified;
2. relevant attacker classes are identified;
3. trust boundaries are named;
4. enforcement points are documented;
5. consent bypass is treated as security-relevant;
6. capability bypass is treated as security-relevant;
7. raw neural data exposure is denied by default or explicitly labelled non-conformant;
8. audit log sensitivity is acknowledged;
9. security contact is present;
10. privacy claims include threat model;
11. side-channel scope is stated when side-channel claims are made;
12. supply-chain assumptions are documented for release artifacts.

## 16. Non-conformance examples

The following are non-conforming or misleading: "secure" with no attacker model,
"privacy-preserving" with no data class definition, raw EEG stored in logs,
diagnostic stream bypassing permissions, consent withdrawal handled only in UI,
security reports sent to personal Gmail only, CI workflow changes without review,
raw neural data exported for analytics without permission profile, timing-channel
claim with no channel scope, and audit logs treated as non-sensitive telemetry.

## 17. Open issues

Draft 0.1 leaves unresolved: PGP key publication for security reporting, formal
STRIDE matrix per repository, attack tree for consent bypass, attack tree for
capability bypass, audit-log retention profile, secure update profile, dependency
policy, formal side-channel analysis profile, and reproducible-build policy.

## 18. Professor note for Draft 0.1 reviewers

This artifact is intentionally conservative. It does not claim that AxonOS already
closes every listed threat. It defines the minimum form of a credible security
and privacy claim so that implementation repositories can be audited against a
stable vocabulary. A future Draft 0.2 should expand this artifact into
repository-specific STRIDE tables, attack trees, and security test vectors.

## 19. Summary

AxonOS security and privacy claims must be boundary-specific and threat-model-specific.

A BCI system cannot be called privacy-preserving merely because it has a privacy
policy. The enforcement must exist in the system architecture.
