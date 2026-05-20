# AOS-0000 — Charter and Scope

Status: Draft 0.1.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0000 defines the charter of the AxonOS Standard.

AxonOS is a deterministic operating layer for brain-computer interface software.
The standard exists because BCI systems require stronger discipline than ordinary
application stacks: timing errors can affect safety, neural data is unusually
sensitive, and consent must be enforced below the user interface.

## 2. Mission

The mission is to establish a technical foundation for safe, private,
real-time BCI software.

This foundation is expressed through deterministic timing boundaries, neural
permissions, consent state semantics, typed intent events, conformance profiles,
evidence-tagged validation, security and privacy threat modelling, and governance
and change control.

## 3. Explicit exclusions

AxonOS does not define a clinical treatment protocol, medical-device approval,
regulatory certification claim, token, DAO, wellness application, general-purpose
AI-agent framework, or proprietary therapeutic waveform.

## 4. Maturity

Draft 0.1.1 is pre-normative. It may be used for architecture alignment and
review, but it must not be cited as a final conformance standard.

## 5. Repository classes

AxonOS repositories should identify themselves as normative, reference,
experimental, integration, research, or historical.

## 6. Requirements

A draft-aligned repository should state its class, maturity, evidence level,
known non-claims, and relationship to `axonos-standard`.

## 7. Non-conformance examples

It is misleading to claim final standard status while Draft 0.1.1 is active, to
use AxonOS to imply affiliation with unrelated projects, to present a research
article as a normative specification, or to claim clinical readiness without
clinical evidence.

## 8. Summary

AOS-0000 defines the institutional boundary of the standard: serious, technical,
pre-normative, evidence-tagged, and deliberately conservative.
