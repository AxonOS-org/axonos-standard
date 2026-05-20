# AOS-0000 — Charter and Scope

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0000 defines the charter of the AxonOS Standard: a deterministic software foundation for safe, private, real-time brain-computer interface systems.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Mission

The mission of AxonOS is to establish the deterministic operating layer between neural hardware and intelligent applications. BCI software needs stricter boundaries than ordinary application software: neural data is sensitive, timing errors can become safety errors, and consent must be enforceable below the UI.

## 4. Explicit exclusions

AxonOS does not define a medical treatment protocol, does not claim regulatory approval, does not define a token, and does not define a DAO. A repository may discuss research or prototypes, but it must not represent draft work as certified medical-device infrastructure.

## 5. Standard maturity

Draft 0.1 is pre-normative and appropriate for terminology alignment, architecture review, conformance planning, and reference implementation mapping.

## 6. Repository classes

AxonOS repositories are classified as normative, reference, experimental, integration, research, or historical. The class must be visible and must not overstate evidence.

## 7. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. State repository class and status.
2. State what claims are not being made.
3. Use evidence levels for technical claims.
4. Avoid certification, clinical, or final-conformance language without evidence.
5. Reference `axonos-standard` as the canonical entry point.

## 8. Minimum verification expectations

1. README contains repository class and status.
2. Claims register contains only evidence-tagged claims.
3. Legal disambiguation is present.
4. Draft status is visible.
5. CI verifies the required AOS artifact set.

## 9. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Claiming final standard status while Draft 0.1 is active.
2. Using AxonOS to imply unrelated affiliation.
3. Presenting a research article as a normative standard.
4. Treating fundraising as governance.
5. Claiming clinical readiness without clinical evidence.

## 10. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 11. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
