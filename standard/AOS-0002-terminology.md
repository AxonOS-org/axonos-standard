# AOS-0002 — Terminology

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0002 defines canonical terminology used across AxonOS repositories.

A standard fails when the same words mean different things in the kernel, SDK,
consent layer, gateway, and research artifacts.

## 2. Core terms

**AxonOS** means the deterministic operating layer for BCI software.

**AxonOS Standard** means the canonical draft standard governing terminology,
architecture, validation, conformance, neural permissions, and consent
semantics.

**Reference implementation** means a public implementation of part of the
standard. It does not imply certification.

## 3. Data terms

**Neural data** means data derived from neural acquisition hardware before
application-level redaction or permission filtering.

**Raw neural data** means unredacted samples or equivalent raw sensor streams.

**Intent event** means a typed, bounded event derived from neural processing and
exposed across the application boundary.

## 4. Timing terms

**WCET** means worst-case execution time under stated assumptions.

**WCRT** means worst-case response time from release to completion under a
specified scheduling model.

A real-time claim without deadline and bound is not an AxonOS claim.

## 5. Security terms

**Neural permission** means typed authority over a neural-derived event class.

**Capability gate** means an enforcement point checking whether delivery is
authorized.

**Consent state machine** means explicit model of grant, withdrawal, suspension,
expiry, and fault.

## 6. Evidence terms

**Evidence level** describes how strongly a claim is supported.

**Conformance profile** means a named implementation class with testable
requirements.

## 7. Requirements

Repositories should use these terms consistently and should not use words such
as real-time, verified, safe, private, clinical, or certified without scope and
evidence.

## 8. Non-conformance examples

Using real-time to mean average latency, verified without verification scope,
privacy-preserving without threat model, or consent to mean UI checkbox only is
not aligned with this artifact.

## 9. Summary

Terminology is not cosmetic. It is the first layer of claims discipline.
