# AOS-0006 — Conformance Profiles

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0006 defines draft AxonOS conformance profiles.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Profile S0

S0 means documentation alignment: terminology, status, standard link, and no overclaim.

## 4. Profile S1

S1 means SDK boundary compatibility: typed events, explicit manifests, raw-data denial by default, and documented ABI assumptions.

## 5. Profile K1

K1 means kernel substrate compatibility: bounded scheduling, monotonic time, bounded IPC, unsafe surface, and evidence for timing claims.

## 6. Profile C1

C1 means consent semantics compatibility: explicit state machine, terminal withdrawal, denial semantics, and invalid escalation tests.

## 7. Profile V1

V1 means evidence-tagged validation discipline.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. State conformance profile explicitly.
2. Do not imply final conformance while Draft 0.1 is active.
3. Map repository claims to at least one profile.
4. Provide tests or artifacts for claimed profile.
5. State known gaps.

## 9. Minimum verification expectations

1. README lists profile and status.
2. Conformance checks link to artifacts.
3. CI verifies AOS artifact set.
4. Claims register maps evidence.
5. Known gaps are documented.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Claiming AxonOS conformance with no profile.
2. Claiming kernel conformance from gateway repo.
3. Claiming consent conformance without terminal withdrawal tests.
4. Claiming validation discipline without claims register.
5. Claiming certification through draft profiles.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
