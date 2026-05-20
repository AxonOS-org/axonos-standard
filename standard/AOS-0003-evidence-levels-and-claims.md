# AOS-0003 — Evidence Levels and Claims

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0003 defines evidence levels and claim discipline.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Evidence levels

L0 is design intent. L1 is analytical or code-level evidence. L2 is runtime measurement on development fixtures. L3 is externally instrumented evidence. L4 is independent review. L5 is regulatory or certified evidence.

## 4. Claim record

A technical claim should state value, evidence level, artifact, version or commit, limitations, and falsification threshold.

## 5. Research artifacts

Preprints and articles may support L1 evidence or background context but do not automatically become normative standard text.

## 6. Validation register

The claims register is the canonical place for standard-level claims and must not contain only meta-claims.

## 7. Falsifiability

Timing claims should specify deadline, bound, hardware context, measurement method, and failure threshold.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Every public technical claim must carry an evidence level.
2. Repository descriptions must not claim beyond artifacts.
3. Research artifacts must be marked non-normative unless adopted.
4. Hardware timing claims require trace artifacts for L3.
5. Clinical and regulatory claims require L5 evidence.

## 9. Minimum verification expectations

1. Claims register entries include value, level, artifact, and status.
2. CI rejects obsolete meta-claim-only registers.
3. Preprints live under research.
4. README top claims are supported by artifacts.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Claiming L3 timing from a non-instrumented benchmark.
2. Calling a preprint a standard.
3. Claiming certification without evidence.
4. Using exact numbers without artifact references.
5. Equating CI passing with safety certification.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
