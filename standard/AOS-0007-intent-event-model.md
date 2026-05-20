# AOS-0007 — Intent Event Model

Status: Draft 0.1 — pre-normative.  
Audience: SDK authors, application developers, kernel authors, and privacy reviewers.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0007 defines the draft model for typed intent events.

Intent events prevent applications from treating raw neural signal as their API.

## 2. Event boundary

An intent event is an application-observable event derived from neural processing
and delivered through permissions.

## 3. Minimum fields

An event should carry event type, payload, timestamp or monotonic counter,
session id, source component, quality state where relevant, and integrity
metadata if transported across a boundary.

## 4. Event categories

Draft categories include intent, quality, artifact, consent, safety, diagnostic,
and administrative events.

Diagnostic events must not become hidden raw-data channels.

## 5. Payload minimization

Payloads should contain information needed by the application and no more by
default. Raw feature vectors should not be exposed as ordinary intent events.

## 6. Versioning

Event schemas must be versioned. Unknown versions should fail closed or enter a
compatibility path that denies sensitive delivery.

## 7. Requirements

Draft alignment requires typed events, documented payloads, rate bounds,
versioning, and denial of unknown sensitive event types.

## 8. Non-conformance examples

Application access to arbitrary classifier embeddings, diagnostic streams with
high-rate raw features, unversioned event schemas, or raw samples in ordinary
events are not aligned.

## 9. Summary

The event model is the application-facing expression of the AxonOS boundary.
