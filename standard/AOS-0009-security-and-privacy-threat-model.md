# AOS-0009 — Security and Privacy Threat Model

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0009 defines draft threat-model expectations for AxonOS repositories.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Attacker classes

Draft attacker classes include malicious application, compromised application, network observer, gateway operator, supply-chain adversary, physical adversary, and confused deputy.

## 4. Protected assets

Protected assets include raw neural data, typed intent events, consent records, manifests, audit logs, session identifiers, cryptographic keys, and safety-state signals.

## 5. Security boundaries

Relevant boundaries include application API, capability gate, consent state machine, IPC transport, hardware interlock, gateway integration, and update path.

## 6. Privacy boundaries

Privacy requires data minimization, event typing, permission checks, rate limits, auditability, and storage/egress semantics.

## 7. Disclosure

Security reporting requires a clear contact path and future encrypted-reporting option.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. State attacker model for security claims.
2. Identify protected assets.
3. Name enforcement points.
4. Avoid privacy claims without threat model.
5. Document security reporting path.

## 9. Minimum verification expectations

1. SECURITY.md exists.
2. README avoids undefined security claims.
3. Sensitive paths are documented.
4. Consent and permission bypass scenarios are tested or listed.
5. Claims register links to evidence.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Privacy-preserving claim with no attacker model.
2. Security contact without scope.
3. Consent bypass ignored as non-security bug.
4. Audit logs left unprotected.
5. Raw neural data treated as ordinary telemetry.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
