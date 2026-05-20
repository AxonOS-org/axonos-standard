# AOS-0007 — Intent Event Model

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0007 defines the draft model for typed intent events.

## 2. Scope

This artifact defines draft standard semantics for AxonOS implementations. It is not a clinical protocol, regulatory approval, or certification claim. It exists to make implementation claims explicit, reviewable, and testable.

AxonOS repositories should reference this artifact when their README, API, tests, or documentation make claims in this area.


## 3. Event boundary

An intent event is an application-observable event derived from neural processing and delivered through permissions.

## 4. Minimum fields

An event should carry event type, payload, timestamp or monotonic counter, session id, source component, quality state where relevant, and integrity metadata if transported.

## 5. Event categories

Draft categories include intent, quality, artifact, consent, safety, diagnostic, and administrative events.

## 6. Payload minimization

Payloads should contain the information needed by the application and no more by default.

## 7. Versioning

Event schemas must be versioned. Unknown versions should fail closed or enter a compatibility pathway that denies sensitive delivery.

## 8. Draft requirements

A draft implementation aligned with this artifact should satisfy:

1. Represent neural output as typed events.
2. Document event payloads and rate bounds.
3. Version event schemas.
4. Deny unknown sensitive event types.
5. Prevent diagnostic events from becoming raw-data backdoors.

## 9. Minimum verification expectations

1. Schema examples exist for public event classes.
2. Unknown event type tests deny delivery.
3. Version mismatch behavior is documented.
4. Payloads are reviewed against permission scope.
5. Diagnostic stream behavior is documented.

## 10. Non-conformance examples

The following are examples of non-conforming or misleading use:

1. Application receives arbitrary classifier embeddings.
2. Diagnostics stream high-rate raw features.
3. Events have no version or schema.
4. Unknown events are delivered by default.
5. Payload includes raw samples without research-only labeling.

## 11. Open issues

Draft 0.1 intentionally leaves some details unresolved. Future revisions may add machine-readable schemas, test vectors, stricter conformance profiles, and implementation-version mappings. Any promotion from draft text to normative text must be recorded through the governance process.

## 12. Summary

This artifact defines one part of the AxonOS Standard boundary. It should be read together with AOS-0000 through AOS-0011 and the repository-level `CONFORMANCE.md`, `VALIDATION.md`, and `GOVERNANCE.md` documents.
