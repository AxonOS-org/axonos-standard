# AOS-0010 — Reference Implementation Mapping

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0010 maps the AxonOS Standard to reference repositories.

A standard that cannot map to implementation reality becomes decorative. This
artifact prevents the standard from floating above the code.

## 2. Mapping fields

Each repository should map to standard artifacts with role, status, evidence
level, version or commit, and known gaps.

## 3. Initial repository families

The initial families are standard, kernel, RFC, SDK, consent, swarm, and gateway.

## 4. Version pinning

Draft 0.1 may reference main branches for iteration. Stable conformance must not
depend on unpinned heads. Future releases should pin tags or commits.

## 5. Gap disclosure

Features should be labelled implemented, simulated, stubbed, pending, or not
applicable.

## 6. Requirements

Draft alignment requires repository-to-AOS mapping, maturity status, evidence
level, known gaps, and planned tag policy.

## 7. Non-conformance examples

Treating a gateway as kernel, using unpinned commits for final conformance,
hiding stubbed features, or claiming implementation maturity without tests is
not aligned.

## 8. Summary

Mapping makes the standard auditable.
