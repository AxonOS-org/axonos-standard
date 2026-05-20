# AxonOS Standard

## 1. Scope

The AxonOS Standard defines a deterministic software architecture for brain-computer interface systems.

It covers:

- real-time neural signal pipelines;
- neural data permissions;
- consent state semantics;
- hardware-gated safety transitions;
- typed intent events;
- validation evidence levels;
- reference implementation boundaries.

It does not define:

- a clinical treatment protocol;
- a medical-device certification claim;
- a proprietary AI model;
- a token, DAO, or financial instrument;
- a general-purpose AI-agent operating system.

---

## 2. System boundary

AxonOS sits between neural hardware and intelligent applications.

Neural hardware flows into acquisition and gateway components, then into the AxonOS deterministic substrate, then through the typed intent and capability boundary, and only then into applications.

The critical boundary is the transition from raw neural signal to capability-gated typed intent events.

---

## 3. Normative concepts

### Deterministic timing

Real-time claims must be expressed as worst-case or bounded claims. Average latency or percentile latency is not sufficient for safety-critical BCI semantics.

### Neural permissions

Applications do not receive raw neural data by default. Access is mediated through typed capabilities and declared manifests.

### Consent as safety state

Consent is represented as a state machine below the application layer. Withdrawal, suspension, expiry, and fault transitions must be enforceable independently of application behavior.

### Evidence-tagged claims

Every performance, safety, privacy, or validation claim must carry an evidence level.

---

## 4. Reference implementation boundary

The reference implementations demonstrate the standard but do not themselves constitute certification.

A repository may be:

- normative specification;
- reference implementation;
- experimental implementation;
- integration gateway;
- research prototype.

Each repository must state its status explicitly.
