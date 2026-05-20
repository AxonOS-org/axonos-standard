# AOS-0009 — Security and Privacy Threat Model

Status: Draft 0.1.1 — pre-normative.  
Audience: security reviewers, privacy engineers, kernel implementers, SDK authors, application developers, institutional reviewers, and safety assessors.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0009 defines the draft security and privacy threat model for AxonOS.

A BCI system processes data that may be more sensitive than ordinary telemetry.
Raw or high-resolution neural data may encode identity-correlated patterns,
intent, workload, artifacts, affective correlates, health-relevant signals, and
behavioral context.

## 2. Protected assets

Protected assets include raw neural data, intermediate features, typed intent
events, consent records, capability manifests, session identifiers, audit logs,
cryptographic keys, safety-state signals, and timing traces.

## 3. Attacker classes

Draft attacker classes include malicious application, compromised application,
network observer, gateway operator, supply-chain adversary, local physical
adversary, confused deputy, timing observer, stale-session adversary, and
overclaim adversary.

## 4. Trust boundaries

Trust boundaries include hardware acquisition, gateway, deterministic substrate,
typed intent boundary, capability gate, consent state machine, IPC transport,
application sandbox, audit log boundary, update/build pipeline, and external
service boundary.

## 5. STRIDE mapping

AxonOS uses STRIDE as a checklist: spoofing, tampering, repudiation, information
disclosure, denial of service, and elevation of privilege. STRIDE is not
sufficient by itself for BCI safety, but it provides useful engineering coverage.

## 6. Consent and capability bypass

Consent bypass is a security issue. Capability bypass is a security issue.
Unknown event classes, wildcard permissions, diagnostic streams that bypass
manifest checks, UI-only withdrawal, stale sessions, and hidden background
sessions are not aligned with AxonOS threat modelling.

## 7. Timing and side channels

Timing can disclose information when execution duration, event timing, packet
rate, power draw, RF behavior, or interrupt timing correlates with neural state.
Side-channel claims must state which channel is covered.

## 8. Supply chain

Repositories should consider dependency compromise, build script compromise,
toolchain compromise, unsigned releases, malicious CI changes, compromised
registries, stale forks, and tampered archives.

## 9. Requirements

Draft alignment requires protected assets, attacker classes, trust boundaries,
enforcement points, consent bypass as security-relevant, capability bypass as
security-relevant, raw-data denial by default or explicit non-conformance,
audit-log sensitivity, security contact, privacy threat model, and side-channel
scope when side-channel claims are made.

## 10. Summary

A privacy policy is not a privacy architecture. AxonOS security and privacy
claims must be boundary-specific and threat-model-specific.
