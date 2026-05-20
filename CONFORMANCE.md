# Conformance Profiles

Status: Draft.

This file defines preliminary AxonOS conformance profiles. These profiles are
not final certification classes. They exist to make implementation claims
specific, testable, and reviewable.

## Profile S0 — Documentation alignment

An implementation may claim S0 alignment if it:

- uses AxonOS terminology consistently;
- links to the AxonOS Standard;
- states its implementation status;
- does not claim clinical, regulatory, or final conformance status.

## Profile S1 — SDK boundary compatibility

An implementation may claim S1 compatibility if it:

- emits or consumes typed AxonOS intent events;
- uses explicit capability manifests;
- does not expose raw neural data to applications by default;
- documents ABI and serialization assumptions.

## Profile K1 — Kernel substrate compatibility

A kernel implementation may claim K1 compatibility if it:

- provides bounded task scheduling;
- exposes monotonic time;
- provides bounded IPC or equivalent transport;
- documents unsafe-code surface;
- provides evidence for timing claims.

## Profile C1 — Consent semantics compatibility

A consent implementation may claim C1 compatibility if it:

- represents consent as an explicit state machine;
- supports grant, withdrawal, suspension, and expiry;
- treats withdrawal as terminal for the current session;
- denies application override of safety suspension;
- provides transition tests.

## Profile V1 — Evidence-tagged validation

An implementation may claim V1 validation discipline if every public technical
claim includes:

- value;
- evidence level;
- artifact;
- limitations;
- falsification threshold where applicable.

## Non-conformance

An implementation is not AxonOS-conformant if it:

- grants raw neural data access by default;
- treats consent as a UI-only preference;
- claims real-time behavior without deadlines and bounds;
- claims safety or certification without evidence;
- claims AxonOS affiliation without authorization.
