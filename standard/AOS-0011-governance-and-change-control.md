# AOS-0011 — Governance and Change Control

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0011 defines draft governance and change-control expectations.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Change classes

Changes may be editorial, clarifying, normative, compatibility-impacting, security-impacting, or deprecating.

## 4. Decision model

Draft 0.1 uses maintainer-led review. Future versions should define steward roles, review board composition, thresholds, and appeals.

## 5. RFC integration

Standard-impacting changes should originate in or link to RFCs.

## 6. Versioning

The standard should use draft versions before v1.0. Stable releases should be tagged.

## 7. Audit trail

External critiques, remediation plans, and accepted findings should be preserved in a way that strengthens governance.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Classify standard changes.
2. Use RFCs or equivalent review for normative changes.
3. Version stable releases.
4. Record remediation of accepted critiques.
5. Do not silently rewrite conformance semantics.

## 9. Minimum verification expectations

1. CHANGELOG exists.
2. VERSION exists.
3. REMEDIATION exists.
4. CI checks artifact presence.
5. Governance docs update with material changes.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Silent breaking change to conformance profile.
2. No version for standard release.
3. Critical audit ignored or deleted without response.
4. Normative change made only in README.
5. Unclear maintainer authority.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
