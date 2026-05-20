# AxonOS Standard

**Draft technical standard for deterministic brain-computer interface software.**

Status: **Draft 0.1 — pre-normative**.

AxonOS defines the operating layer between neural hardware and intelligent
applications: deterministic timing, neural permissions, consent enforcement,
typed intent events, and evidence-tagged validation.

This repository is the canonical entry point for the AxonOS Standard. It is not
a fundraising page, not a wellness application specification, not a token
project, and not an AI-agent framework.

## What this repository contains

The normative draft sequence is maintained in `standard/`.

Current Draft 0.1 artifacts:

```text
AOS-0000  Charter and Scope
AOS-0001  System Boundary
AOS-0002  Terminology
AOS-0003  Evidence Levels and Claims
AOS-0004  Neural Permissions
AOS-0005  Consent Semantics
AOS-0006  Conformance Profiles
AOS-0007  Intent Event Model
AOS-0008  IPC and Timing Contract
AOS-0009  Security and Privacy Threat Model
AOS-0010  Reference Implementation Mapping
AOS-0011  Governance and Change Control
```

## Core principles

1. Neural data is not application data.
2. Consent withdrawal must be enforceable below the application layer.
3. Real-time claims must be bounded and falsifiable.
4. Privacy must be structural, not policy-only.
5. Reference implementations must not claim beyond their evidence level.
6. Safety boundaries must be inspectable.
7. Research artifacts are non-normative until adopted through governance.

## Current maturity

Draft 0.1 is suitable for:

- architecture review;
- implementation alignment;
- vocabulary stabilization;
- early conformance planning;
- due-diligence orientation.

Draft 0.1 is not:

- a certified medical-device standard;
- a clinical protocol;
- a regulatory approval claim;
- a final conformance test suite.

## Repository roles

```text
standard/       canonical AOS artifacts
validation/     claims register and validation notes
legal/          disambiguation and attribution notes
tools/          CI verifiers for standard integrity
research/       non-normative research context
```

Legacy navigation directories are retained only as redirects to `standard/`.

## Reference implementation families

AxonOS reference implementation work is split across kernel, SDK, RFC, consent,
swarm, and gateway repositories. This repository defines the vocabulary and
draft conformance expectations they should align with. Implementation maturity
is determined by evidence level, not by repository naming.

## Contact

General / institutional: connect@axonos.org  
Security: security@axonos.org  
Website: https://axonos.org
