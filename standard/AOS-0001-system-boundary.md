# AOS-0001 — System Boundary

Status: Draft 0.1 — pre-normative.  
Audience: implementers, reviewers, safety assessors, hardware teams, application developers, and institutional partners.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

This artifact defines the system boundary of AxonOS.

The system boundary is the first normative concern of the AxonOS Standard because most BCI software failures begin as boundary failures. A system that cannot say where raw neural data ends, where the deterministic substrate begins, where application behavior is permitted, and where consent is enforced cannot make credible safety, privacy, or real-time claims.

AxonOS is not an electrode stack, not an amplifier, not an EEG viewer, not a mobile wellness application, not a token project, and not a general-purpose AI-agent runtime. AxonOS is the deterministic operating substrate between neural hardware and intelligent applications. Its boundary model exists to ensure that the transition from neural signal to application-observable event is explicit, constrained, permissioned, and reviewable.

This artifact defines:

- the canonical AxonOS system layers;
- the trust boundary between hardware, gateway, substrate, and applications;
- the raw-neural-data boundary;
- the deterministic-substrate boundary;
- the typed-intent boundary;
- the consent and safety boundary;
- repository status labels;
- minimum boundary conformance requirements;
- examples of non-conforming designs.

## 2. Canonical system model

The canonical AxonOS system model is:

```text
Neural hardware
  ↓
Acquisition / gateway
  ↓
AxonOS deterministic substrate
  ↓
Typed intent and neural-permission boundary
  ↓
Applications
```

Each layer has a different trust model and a different evidence requirement.

| Boundary | Primary question | AxonOS responsibility |
|---|---|---|
| Hardware → Gateway | Is signal acquisition represented correctly? | Define acquisition assumptions, timestamp semantics, and metadata boundaries |
| Gateway → Substrate | Is data entering deterministic processing? | Define timing, buffering, and handoff assumptions |
| Substrate → Typed Intent | Is raw neural data reduced safely? | Define capability-gated transformation and redaction |
| Typed Intent → Application | What may the application observe? | Enforce neural permissions, consent state, and event delivery rules |

The core boundary rule is:

> Raw neural data must not cross into application space by default.

This rule is not merely a privacy preference. It is a structural constraint on the system architecture.

## 3. Neural hardware boundary

Neural hardware includes electrodes, analog front-ends, ADCs, amplifiers, stimulation hardware, galvanic isolation, secure elements, radios, and transport components.

AxonOS does not standardize electrode geometry, clinical therapy protocol, amplifier design, or stimulation waveform design. It standardizes the software boundary that receives neural-derived data and enforces deterministic processing, permissioned access, consent state, and safety behavior.

A hardware integration may be AxonOS-aligned only if it documents:

- acquisition rate;
- channel count;
- sample format;
- timestamp source;
- clock stability assumptions;
- buffering model;
- dropped-sample behavior;
- transport behavior;
- isolation assumptions;
- stimulation safety boundary, if any;
- validation evidence level.

A hardware claim must be evidence-tagged. A hardware-in-the-loop claim without external trace artifacts is not an L3 claim under AOS-0003.

## 4. Acquisition and gateway boundary

An acquisition gateway is an integration layer between acquisition tools and the AxonOS software stack. A gateway can be useful without being safety-critical.

A gateway may provide:

- stream naming;
- acquisition metadata;
- hardware-in-the-loop test access;
- protocol translation;
- file or network transport;
- development visualization;
- interoperability with external acquisition software.

A gateway must not be treated as the AxonOS kernel unless it implements and documents the deterministic substrate requirements. A gateway repository must state its status explicitly as one of:

- reference acquisition gateway;
- integration fork;
- test harness;
- production component;
- research prototype.

The `axon-bci-gateway` repository is an integration gateway. It may support AxonOS testing and development, but it is not by itself the AxonOS real-time substrate.

## 5. Deterministic substrate boundary

The AxonOS deterministic substrate is the software layer responsible for timing, bounded execution, capability enforcement, and safety-relevant state transitions.

A conforming substrate should define:

- task model;
- scheduling policy;
- deadline model;
- admission criterion;
- monotonic time source;
- bounded IPC mechanism;
- unsafe-code surface;
- failure mode for deadline misses;
- overrun behavior;
- evidence level for timing claims.

Application code must not be responsible for hard real-time enforcement of the neural signal path. If an application can introduce unbounded delay into the critical loop, the system may be an AxonOS integration, but it is not a conforming safety-critical substrate.

## 6. Typed intent boundary

The typed intent boundary is the point where application-observable information is separated from raw neural signal data.

The standard distinguishes:

- raw neural data;
- intermediate signal features;
- classifier internal state;
- typed intent events;
- session quality events;
- consent state events;
- safety state events.

Only typed events should cross into application space by default.

Examples of typed event classes include:

- `NavigationIntent`;
- `WorkloadAdvisory`;
- `SessionQuality`;
- `ArtifactEvent`;
- `ConsentStateChanged`;
- `SafetyInterlockState`.

An implementation must document each event class, payload, maximum delivery rate where relevant, permission requirement, consent dependency, and evidence level of enforcement.

## 7. Application boundary

Applications run above the typed intent and neural-permission boundary.

Applications may:

- request permissions;
- receive authorized typed events;
- display consent state;
- request session actions;
- respond to safety state changes;
- provide user-facing workflows;
- integrate with external services if permitted.

Applications must not:

- receive raw neural data by default;
- override consent withdrawal;
- override safety suspension;
- bypass capability checks;
- mutate kernel timing policy;
- directly control stimulation without a safety gate;
- claim AxonOS conformance without a declared permission and consent model.

An application is not AxonOS-conformant merely because it consumes EEG data or exposes a BCI feature. It must respect the AxonOS boundary model.

## 8. Consent boundary

Consent enforcement belongs below application policy.

A user interface can present consent prompts, explain scope, and record user decisions. It must not be the sole enforcement mechanism. Consent withdrawal, expiry, suspension, and fault transitions must be represented as explicit system state and must affect event delivery below the application layer.

This requirement exists because application code may be compromised, buggy, stale, economically incentivized to collect more data than needed, or disconnected from the actual safety state of the device.

## 9. Privacy boundary

The privacy boundary is structural, not policy-only.

AxonOS privacy is implemented through:

- typed event delivery;
- capability gates;
- application manifests;
- denial of raw neural streams by default;
- consent state enforcement;
- explicit evidence levels for privacy claims;
- auditable event delivery decisions.

A privacy claim must identify:

- protected data class;
- attacker model;
- enforcement point;
- evidence level;
- known limitations.

A statement such as "privacy-preserving" is not an AxonOS claim unless the enforcement mechanism is identified.

## 10. Safety boundary

Safety behavior must be explicit and fail-closed.

A safety-critical implementation should document:

- behavior on deadline miss;
- behavior on buffer overrun;
- behavior on consent withdrawal;
- behavior on consent expiry;
- behavior on safety suspension;
- behavior on hardware interlock activation;
- behavior on application crash;
- behavior on gateway disconnect;
- behavior on invalid or unauthenticated input.

Silent continuation after a safety-relevant fault is not acceptable unless explicitly justified and evidence-tagged.

## 11. Repository boundary labels

Every AxonOS repository should use one of the following labels in its README:

| Label | Meaning |
|---|---|
| Normative | Defines standard text |
| Reference | Implements part of the standard |
| Experimental | Explores possible future standard behavior |
| Integration | Bridges AxonOS to external hardware or tools |
| Research | Provides analysis or evidence context |
| Historical | Preserved for compatibility or audit trail |

A repository may have more than one label, but it must not imply stronger maturity than its evidence supports.

## 12. Boundary conformance requirements

An implementation may claim draft AxonOS boundary alignment only if it satisfies all of the following:

1. It identifies its system role.
2. It states its repository boundary label.
3. It does not expose raw neural data to applications by default.
4. It defines where consent is enforced.
5. It defines where permissions are checked.
6. It labels real-time claims with evidence levels.
7. It states what claims are not being made.
8. It defines fail-closed behavior for ambiguous boundary states.

## 13. Non-conformance examples

The following designs are not AxonOS-conformant boundary designs:

- a GUI that directly streams raw EEG to plugins without permissions;
- an application that treats consent withdrawal as a UI flag only;
- a gateway that claims kernel-level safety without schedulability evidence;
- a real-time claim expressed only as average latency;
- an SDK that grants all event classes by default;
- a classifier that exposes continuous emotion inference without explicit review;
- a stimulation controller that can be driven directly by application code;
- a repository that claims standard conformance while hiding its event model.

## 14. Relationship to other artifacts

This artifact is upstream of:

- AOS-0004 — Neural Permissions;
- AOS-0005 — Consent Semantics;
- AOS-0006 — Conformance Profiles;
- `CONFORMANCE.md`;
- `VALIDATION.md`;
- implementation README files.

If a later artifact contradicts this boundary model, the contradiction must be resolved explicitly through the governance process.

## 15. Open issues

Draft 0.1 leaves the following unresolved:

- final event type registry;
- canonical ABI for intent delivery;
- canonical wire format for capability manifests;
- formal gateway conformance test suite;
- version-pinned mapping to reference implementations;
- formal definition of the application sandbox boundary;
- required minimum audit-log schema.

## 16. Summary

AxonOS is defined by its boundary.

If raw neural data flows freely into applications, if consent is only a UI preference, or if timing guarantees depend on application behavior, the system is not implementing the AxonOS boundary model.

The boundary model is the foundation for neural permissions, consent semantics, conformance profiles, and claims discipline.
