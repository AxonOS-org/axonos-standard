# AOS-0006 — Conformance Profiles

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0006 defines draft AxonOS conformance profiles.

Profiles make claims specific. A repository may align with documentation,
SDK boundary, kernel substrate, consent semantics, or validation discipline.

## 2. Profile S0 — Documentation alignment

S0 means the repository uses AxonOS terminology, links to the standard, states
maturity, and avoids clinical or regulatory overclaim.

## 3. Profile S1 — SDK boundary compatibility

S1 means the implementation emits or consumes typed intent events, uses explicit
capabilities or manifests, denies raw data by default, and documents ABI or
serialization assumptions.

## 4. Profile K1 — Kernel substrate compatibility

K1 means the implementation defines bounded scheduling, monotonic time, bounded
IPC, unsafe surface, and evidence for timing claims.

## 5. Profile C1 — Consent semantics compatibility

C1 means explicit state machine, terminal withdrawal, suspension and expiry
denial, no application override, and invalid escalation tests.

## 6. Profile V1 — Evidence-tagged validation

V1 means claims are recorded with value, evidence level, artifact, status,
limitations, and falsification threshold where applicable.

## 7. Requirements

Repositories should state claimed profile, known gaps, artifacts, tests, and
evidence level.

## 8. Non-conformance examples

Claiming AxonOS conformance with no profile, claiming kernel conformance from a
gateway repository, or claiming certification through draft profiles is not
aligned.

## 9. Summary

Conformance profiles are not certification. They are a review vocabulary.
