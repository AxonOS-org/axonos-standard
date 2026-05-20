# AOS-0008 — IPC and Timing Contract

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0008 defines draft expectations for bounded IPC and timing claims.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Timing claim form

A timing claim should include deadline, bound, hardware context, workload, method, evidence level, and falsification threshold.

## 4. IPC claim form

An IPC claim should identify queue type, capacity, producer/consumer model, blocking behavior, overrun behavior, memory ordering, and unsafe-code surface.

## 5. Deadline miss behavior

A safety-relevant implementation should document behavior on deadline miss.

## 6. Bounded behavior

Bounded IPC means operation count and memory use are bounded under stated conditions.

## 7. Evidence mapping

Instruction-count derivations are L1. Runtime fixture measurements are L2. External GPIO or analyzer traces are L3.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. State deadlines and bounds for real-time claims.
2. Document IPC capacity and overrun behavior.
3. Document unsafe-code surface if any.
4. State deadline miss behavior.
5. Tag timing claims with evidence levels.

## 9. Minimum verification expectations

1. Tests cover queue invariants where applicable.
2. Documentation states overrun behavior.
3. Claims register includes timing entries.
4. Hardware claims identify context.
5. L3 claims include trace artifact references.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Real-time claim with only average latency.
2. IPC claim without capacity.
3. Lock-free claim without evidence.
4. Deadline miss behavior undocumented.
5. Measured claim with no artifact.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
