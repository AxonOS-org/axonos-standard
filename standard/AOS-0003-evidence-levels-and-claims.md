# AOS-0003 — Evidence Levels and Claims

Status: Draft 0.1.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, researchers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0003 defines evidence levels and claims discipline.

The standard distinguishes design intent, analytical proof, runtime measurement,
external instrumentation, independent review, and regulatory approval.

## 2. Evidence levels

| Level | Meaning |
|---|---|
| L0 | design intent |
| L1 | analytical or code-level evidence |
| L2 | runtime measurement on development fixtures |
| L3 | external instrumentation such as GPIO, logic analyzer, oscilloscope |
| L4 | independent review or reproduction |
| L5 | regulatory or certification evidence |

## 3. Claim record

A technical claim should state value, evidence level, artifact, version or
commit, limitations, and falsification threshold.

## 4. Research artifacts

Preprints and articles may support L1 evidence or provide background context.
They do not automatically become normative standard text.

## 5. Claims register

The claims register is the canonical place for standard-level claims. It must not
contain only meta-claims about repository existence.

## 6. Summary

Evidence levels protect the project from claim inflation.
