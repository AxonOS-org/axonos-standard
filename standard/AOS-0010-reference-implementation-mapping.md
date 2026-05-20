# AOS-0010 — Reference Implementation Mapping

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0010 maps the AxonOS Standard to reference repositories.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Mapping table

Each reference repository should map to standard artifacts and include role, status, evidence level, version or commit, and known gaps.

## 4. Canonical repositories

Initial repositories include axonos-standard, axonos-kernel, axonos-rfcs, axonos-sdk, axonos-consent, axonos-swarm, and axon-bci-gateway.

## 5. Version pinning

Final conformance cannot depend on unpinned repository heads. Draft 0.1 may reference main branches, but future releases should pin tags or commits.

## 6. Gap disclosure

Reference implementations should state whether a feature is implemented, simulated, stubbed, pending, or not applicable.

## 7. Evidence linkage

Claims in implementation repositories should link back to AOS artifacts and validation records.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Map each repository to AOS artifacts.
2. State implementation role and maturity.
3. Record known gaps.
4. Pin versions for stable releases.
5. Do not treat integration forks as kernel implementations.

## 9. Minimum verification expectations

1. Mapping file exists.
2. README includes reference table.
3. Claims register references implementation artifacts.
4. Known gaps are visible.
5. Release tags are planned.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Floating standard with no implementation mapping.
2. Gateway treated as kernel.
3. Unpinned commits used for final conformance.
4. Stubbed feature presented as implemented.
5. Known gaps hidden from README.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
