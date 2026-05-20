# AOS-0002 — Terminology

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0002 defines canonical terminology used across AxonOS repositories.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Core terms

AxonOS is the deterministic operating layer for BCI software. The AxonOS Standard governs terminology, architecture, validation, conformance, neural permissions, and consent semantics.

## 4. Data terms

Neural data means data derived from neural acquisition hardware before application-level redaction or permission filtering. Raw neural data means unredacted samples or equivalent raw sensor streams.

## 5. Timing terms

WCET means worst-case execution time. WCRT means worst-case response time. A real-time claim without a deadline and bound is not an AxonOS claim.

## 6. Security terms

Neural permission means typed authority over a neural-derived event class. Capability gate means an enforcement point checking delivery authority.

## 7. Evidence terms

Evidence level describes how strongly a claim is supported. Reference implementation does not imply certification.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Use canonical terms consistently.
2. Do not use real-time, verified, safe, private, clinical, or certified without scope.
3. Define new terms before making claims with them.
4. Link implementation-specific terms back to the standard.

## 9. Minimum verification expectations

1. Glossary contains core terms.
2. README claims use standard terminology.
3. CI checks core AOS artifact tokens.
4. Implementation docs avoid undefined maturity claims.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Using real-time to mean average latency.
2. Using verified without verification scope.
3. Using privacy-preserving without threat model.
4. Using consent to mean UI checkbox only.
5. Using standard to mean marketing overview.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
