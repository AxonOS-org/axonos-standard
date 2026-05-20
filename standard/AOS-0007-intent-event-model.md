# AOS-0007 — Intent Event Model

Status: Draft 0.1.1 — pre-normative.  
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

## 4. Versioning

Event schemas must be versioned. Unknown versions should fail closed or enter a
compatibility path that denies sensitive delivery.

## 5. Requirements

Draft alignment requires typed events, documented payloads, rate bounds,
versioning, and denial of unknown sensitive event types.

## 6. Summary

The event model is the application-facing expression of the AxonOS boundary.
