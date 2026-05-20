# AOS-0009 — Security and Privacy Threat Model

Status: Draft 0.1 — pre-normative.  
Audience: security reviewers, privacy engineers, kernel implementers, SDK authors, application developers, institutional reviewers, and safety assessors.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0009 defines the draft security and privacy threat model for AxonOS.

A BCI system processes data that may be more sensitive than ordinary telemetry.
Raw or high-resolution neural data may encode identity-correlated patterns,
intent, workload, artifacts, affective correlates, health-relevant signals, and
behavioral context.

## 2. Protected assets

Protected assets include raw neural data, intermediate features, typed intent
events, consent records, capability manifests, session identifiers, audit logs,
cryptographic keys, safety-state signals, and timing traces.

## 3. Attacker classes

| ID | Attacker | Capability |
|---|---|---|
| A1 | malicious application | requests excessive permissions or misuses events |
| A2 | compromised application | executes attacker logic inside app boundary |
| A3 | network observer | observes or modifies transport |
| A4 | gateway operator | controls acquisition environment |
| A5 | supply-chain adversary | modifies dependencies, build, firmware, or artifacts |
| A6 | local physical adversary | accesses device or debug ports |
| A7 | confused deputy | trusted component misuses authority |
| A8 | timing observer | observes timing, power, RF, or scheduling side channels |
| A9 | stale-session adversary | replays consent, permission, or session messages |
| A10 | overclaim adversary | relies on misleading claims to bypass review |

## 4. Trust boundaries

Trust boundaries include hardware acquisition, gateway, deterministic substrate,
typed intent boundary, capability gate, consent state machine, IPC transport,
application sandbox, audit log boundary, update/build pipeline, and external
service boundary.

A security claim must identify which boundary enforces it.

## 5. STRIDE mapping

| STRIDE | AxonOS example | Direction |
|---|---|---|
| Spoofing | fake device, app, or consent source | identity, attestation, signed manifests |
| Tampering | modified event, queue state, consent record | integrity checks and audit |
| Repudiation | disputed withdrawal or delivery | transition logs and counters |
| Information disclosure | raw EEG leaked to application | neural permissions and typed events |
| Denial of service | queue flooding or deadline miss | bounded IPC and safe fault |
| Elevation of privilege | unauthorized event class | capability gate and manifest verification |

## 6. Neural data disclosure threats

Disclosure may occur through raw streams, high-rate features, embeddings,
diagnostic streams, logs, exported files, timing, side channels, crash reports,
analytics integrations, or model-training pipelines.

A privacy claim must state which path is covered and which remains open.

## 7. Consent bypass threats

Consent bypass may occur when an app caches old granted state, withdrawal is UI
only, gateway continues streaming after denial, event queue is not cleared,
stale session token is accepted, replayed grant frame is accepted, suspension
does not affect delivery, or hidden background session remains active.

Consent bypass is a security issue.

## 8. Capability bypass threats

Capability bypass may occur when unknown event classes default to allowed,
wildcard permissions are accepted, diagnostic streams bypass manifest checks,
raw features are mislabeled as low-risk events, or permission state is stored
only in application memory.

## 9. Timing and side-channel threats

Timing can disclose information when execution duration, event timing, packet
rate, power draw, RF behavior, or interrupt timing correlates with neural state.

Mitigations may include fixed-size frames, rate bounds, deterministic scheduling,
avoiding data-dependent branches on sensitive paths, coarsened delivery, and
documenting uncovered channels.

## 10. Supply-chain threats

Repositories should consider dependency compromise, build script compromise,
toolchain compromise, unsigned releases, malicious CI changes, compromised
registries, stale forks, and tampered archives.

Mitigations include minimized dependency surface, pinned dependencies for
releases, CI review for workflow changes, signed commits or tags, reproducible
build roadmap, and unsafe-code review.

## 11. Audit log privacy

Audit logs reveal session use, application access, event delivery, withdrawal,
artifact events, and safety faults. They must not become secondary raw-data
leaks. Retention, access, export, and deletion behavior should be documented.

## 12. Disclosure policy

Security reporting should include contact, affected repositories, issue classes,
requested reproduction details, coordinated disclosure expectation, and
encryption method when high-sensitivity data is involved.

Publication of a PGP key for `security@axonos.org` remains pending.

## 13. Minimum threat model record

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

## 14. Risk matrix

Security and privacy issues should be triaged with asset, attacker, boundary,
impact, likelihood, detectability, mitigation, residual risk, and evidence.

This does not replace ISO 14971 risk management, but creates an engineering
bridge between software security and BCI safety.

## 15. Requirements

Draft alignment requires protected assets, attacker classes, trust boundaries,
enforcement points, consent bypass as security-relevant, capability bypass as
security-relevant, raw-data denial by default or explicit non-conformance,
audit-log sensitivity, security contact, privacy threat model, and side-channel
scope when side-channel claims are made.

## 16. Non-conformance examples

"Secure" with no attacker model, "privacy-preserving" with no data class, raw
EEG in logs, diagnostic streams bypassing permissions, UI-only withdrawal,
personal Gmail for security reports, unreviewed CI workflow changes, raw neural
data exported for analytics, timing-channel claims with no scope, and audit logs
treated as ordinary telemetry are not aligned.

## 17. Summary

AxonOS security and privacy claims must be boundary-specific and
threat-model-specific. A privacy policy is not a privacy architecture.
