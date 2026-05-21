# AOS-0012 — Deterministic Neural Intent Processing and Typed Event Contract

**Status:** Draft 0.1.1 — pre-normative  
**Classification:** Normative (proposed)  
**Dependencies:** AOS-0001, AOS-0004, AOS-0005, AOS-0007, AOS-0008  
**Date:** 2026-05-21  
**Author:** AxonOS Standard Committee

---

## Abstract

This artifact defines the deterministic neural intent processing pipeline and the typed event contract that governs how raw biological signals are transformed into semantically meaningful, attestable intent events. The specification establishes mathematical bounds on latency, classification accuracy, and event integrity across the signal-to-intent boundary. It formalizes the interface between the neural hardware abstraction layer (HAL) and the application runtime, ensuring that every intent event carries cryptographic provenance, temporal validity, and semantic type safety.

---

## 1. Scope and Purpose

### 1.1 Scope

This artifact applies to all AxonOS implementations that perform real-time neural signal classification and emit intent events to application runtimes. It covers:

- The signal acquisition and preprocessing pipeline (§3)
- The deterministic classification mesh (§4)
- The typed intent event model and its semantic constraints (§5)
- The attestation and provenance chain (§6)
- The timing contract between classification completion and event delivery (§7)
- The error handling and graceful degradation model (§8)

### 1.2 Purpose

The purpose of this artifact is to ensure that:

1. **Every intent event is deterministic**: Given identical neural input and system state, the classification pipeline produces identical intent events within bounded temporal variance.
2. **Every intent event is typed**: The event carries a semantic type from a closed taxonomy; untyped or partially typed events are rejected at the SDK boundary.
3. **Every intent event is attested**: The event carries a cryptographic chain of provenance linking it to the specific signal epoch, hardware configuration, and consent state under which it was generated.
4. **Every intent event is temporally valid**: The event carries an explicit validity interval; consumption outside this interval is a protocol violation.

### 1.3 Out of Scope

This artifact does not define:
- Specific classification algorithms (these are implementation details governed by AOS-0010)
- Hardware-specific signal acquisition protocols (governed by AOS-0001)
- Application-level intent interpretation (governed by AOS-0007)
- Consent negotiation semantics (governed by AOS-0005)

---

## 2. Normative References

The following artifacts contain provisions that, through reference in this text, constitute provisions of this artifact:

- AOS-0000 — Charter and Scope
- AOS-0001 — System Boundary
- AOS-0002 — Terminology
- AOS-0003 — Evidence Levels and Claims
- AOS-0004 — Neural Permissions
- AOS-0005 — Consent Semantics
- AOS-0007 — Intent Event Model
- AOS-0008 — IPC and Timing Contract
- RFC-0001 — EDF Scheduler with Biological Deadlines
- RFC-0004 — Dual-Core Real-Time Contract
- RFC-0005 — Capability-Based Application Manifest

---

## 3. Signal Acquisition and Preprocessing Pipeline

### 3.1 Epoch Definition

A **signal epoch** is the fundamental unit of neural data processing. An epoch is defined as:

- **Temporal extent:** A contiguous interval of neural signal data with duration $T_e$, where $T_e$ is hardware-dependent but bounded: $1\,	ext{ms} \leq T_e \leq 100\,	ext{ms}$.
- **Sample structure:** A matrix $S \in \mathbb{R}^{C 	imes N}$ where $C$ is the channel count and $N$ is the sample count per epoch.
- **Metadata envelope:** Every epoch carries a metadata envelope $M_e$ containing: timestamp $t_0$, hardware identifier $h_{id}$, channel configuration $C_{cfg}$, and consent state $C_{state}$.

### 3.2 Preprocessing Stages

The preprocessing pipeline is strictly ordered and must complete within the **preprocessing deadline** $D_{pre}$, defined as:

$$D_{pre} = rac{T_e}{4}$$

The pipeline stages are:

| Stage | Operation | Bound | Failure Mode |
|-------|-----------|-------|--------------|
| P1 | Hardware artifact rejection | $O(C \cdot N)$ | Drop epoch, log L2 |
| P2 | Bandpass filtering (0.5–100 Hz) | $O(C \cdot N \cdot \log N)$ | Drop epoch, log L2 |
| P3 | Common average referencing | $O(C \cdot N)$ | Drop epoch, log L2 |
| P4 | Notch filtering (50/60 Hz) | $O(C \cdot N)$ | Drop epoch, log L2 |
| P5 | Quality metric computation | $O(C \cdot N)$ | Mark epoch L3, continue |

**Requirement P-1:** If any of stages P1–P4 fail, the epoch MUST be dropped and a failure event MUST be emitted to the audit log. The failure event MUST include the epoch identifier, the failing stage, and the failure reason code.

**Requirement P-2:** Stage P5 computes signal quality metrics (SNR, impedance, motion artifact index). Epochs with quality below threshold are marked as L3 evidence (per AOS-0003) and forwarded to the classifier with a quality flag, but are NOT dropped.

### 3.3 Buffer Management

Preprocessed epochs are stored in a **circular buffer** $B_{pre}$ with the following properties:

- **Capacity:** $B_{pre}$ holds exactly $N_{buf}$ epochs, where $N_{buf} \geq 3$ and is configured at kernel initialization.
- **Overwrite policy:** When $B_{pre}$ is full, the oldest epoch is overwritten. Overwritten epochs are not recoverable.
- **Ephemerality:** $B_{pre}$ is allocated in non-persistent memory. System reset clears $B_{pre}$ unconditionally.

**Requirement P-3:** No preprocessed epoch may be written to persistent storage without explicit user consent and a separate consent event per AOS-0005.

---

## 4. Deterministic Classification Mesh

### 4.1 Classification Task Model

The classification mesh transforms a preprocessed epoch $E$ into a typed intent observation $I$. This is modeled as a function:

$$\mathcal{C}: E 	imes \Theta 	imes C_{state} ightarrow I \cup \{ot\}$$

Where:
- $E$ is the preprocessed epoch
- $\Theta$ is the classifier parameter set (trained model weights)
- $C_{state}$ is the current consent state
- $I$ is the intent observation (see §5)
- $ot$ denotes classification failure or null output

### 4.2 Determinism Requirements

**Requirement C-1 (Functional Determinism):** For any epoch $E$, parameter set $\Theta$, and consent state $C_{state}$, the output $\mathcal{C}(E, \Theta, C_{state})$ is a pure function. Given identical inputs, the output MUST be bit-identical across all implementations and invocations.

**Requirement C-2 (Temporal Determinism):** The classification latency $L_c$ MUST satisfy:

$$L_c \leq D_{class} = rac{T_e}{2}$$

Where $D_{class}$ is the classification deadline. The worst-case classification latency MUST be verified by bounded model checking (e.g., Kani harness) or static analysis.

**Requirement C-3 (State Isolation):** The classification mesh MUST NOT maintain hidden state between epochs that influences the output for epoch $E_i$ beyond the explicitly defined state transfer mechanism (see §4.4).

### 4.3 Classifier Taxonomy

AxonOS defines a closed taxonomy of classifier types. Each classifier type maps to a specific intent event type:

| Classifier Type | Intent Event Type | Evidence Level | Typical Latency |
|-----------------|-------------------|----------------|-----------------|
| Motor Imagery (MI) | `MotorIntent` | L2 | 50–100 ms |
| P300 Evoked Potential | `SelectIntent` | L2 | 300–600 ms |
| Steady-State Visually Evoked Potential (SSVEP) | `FocusIntent` | L2 | 100–200 ms |
| Error-Related Negativity (ERN) | `ErrorIntent` | L3 | 200–400 ms |
| Affective State Inference | `AffectIntent` | L3 | 1000–5000 ms |
| Cognitive Workload Index | `WorkloadIntent` | L3 | 500–2000 ms |

**Requirement C-4:** An implementation MUST NOT emit intent events of a type not listed in the taxonomy without an approved RFC and standard artifact update.

### 4.4 State Transfer Mechanism

Some classifiers require state transfer between epochs (e.g., adaptive classifiers, Kalman filters). State transfer is governed by:

**Requirement C-5:** All inter-epoch state MUST be:
1. Explicitly declared in the classifier manifest
2. Bounded in size (maximum state size $S_{max}$ is classifier-dependent but $\leq 1\,	ext{KB}$)
3. Subject to the same ephemerality constraints as $B_{pre}$ (§3.3)
4. Attested in the provenance chain (§6)

### 4.5 Confidence and Uncertainty Quantification

Every intent observation $I$ MUST carry a confidence metric $c \in [0, 1]$ and an uncertainty estimate $u \in [0, 1]$.

**Requirement C-6:** The confidence $c$ and uncertainty $u$ MUST be computed using a method declared in the classifier manifest. The method MUST be reproducible and its implementation MUST be subject to the same determinism requirements as the classifier itself.

**Requirement C-7:** If $c < c_{min}$ or $u > u_{max}$ (where $c_{min}$ and $u_{max}$ are classifier-specific thresholds declared in the manifest), the classifier MUST emit $ot$ (null output) rather than an intent observation with low confidence.

---

## 5. Typed Intent Event Model

### 5.1 Event Structure

An intent event $I$ is a structured record with the following mandatory fields:

| Field | Type | Description | Cardinality |
|-------|------|-------------|-------------|
| `event_id` | UUIDv7 | Unique event identifier | 1 |
| `event_type` | Enum | Intent type from closed taxonomy | 1 |
| `timestamp` | Timestamp | Epoch start time (UTC, μs precision) | 1 |
| `validity_interval` | Interval | $[t_{start}, t_{end}]$ in μs | 1 |
| `confidence` | Float | $c \in [0, 1]$ | 1 |
| `uncertainty` | Float | $u \in [0, 1]$ | 1 |
| `provenance` | ProvenanceChain | Cryptographic attestation chain | 1 |
| `payload` | TypedRecord | Semantically typed payload | 1 |
| `quality_flag` | Enum | Signal quality indicator | 0..1 |
| `consent_reference` | UUID | Reference to active consent event | 1 |

### 5.2 Event Type Taxonomy

The event type taxonomy is hierarchical and extensible only through the governance process (AOS-0011):

```
IntentEvent
├── MotorIntent
│   ├── DirectionalIntent (up, down, left, right)
│   ├── GraspIntent (open, close)
│   └── LimbIntent (specific limb + action)
├── SelectIntent
│   ├── TargetSelect (target identifier)
│   └── OptionSelect (option index)
├── FocusIntent
│   ├── FrequencyFocus (SSVEP frequency)
│   └── SpatialFocus (spatial location)
├── ErrorIntent
│   └── ErrorDetect (binary: error detected)
├── AffectIntent
│   ├── ValenceIntent (positive, neutral, negative)
│   └── ArousalIntent (low, medium, high)
└── WorkloadIntent
    └── CognitiveLoad (low, medium, high, overload)
```

**Requirement E-1:** Events with `event_type` not in the taxonomy MUST be rejected at the SDK boundary with error code `INVALID_EVENT_TYPE`.

### 5.3 Payload Typing

The `payload` field is a typed record whose structure depends on `event_type`:

**Example: MotorIntent.DirectionalIntent**
```
payload: {
  direction: Enum { UP, DOWN, LEFT, RIGHT },
  magnitude: Float [0.0, 1.0],
  duration_ms: UInt32
}
```

**Example: SelectIntent.TargetSelect**
```
payload: {
  target_id: String [max 64 chars],
  selection_method: Enum { GAZE, P300, SSVEP, HYBRID },
  dwell_time_ms: UInt32
}
```

**Requirement E-2:** The payload MUST be validated against the schema for its event type. Schema violations MUST result in event rejection at the SDK boundary.

### 5.4 Validity Interval

The `validity_interval` defines the temporal window during which the intent observation is considered valid for consumption:

$$[t_{start}, t_{end}] = [t_{epoch} + L_c, t_{epoch} + T_e + D_{consume}]$$

Where:
- $t_{epoch}$ is the epoch start time
- $L_c$ is the classification latency
- $T_e$ is the epoch duration
- $D_{consume}$ is the maximum consumption delay (implementation-specific, but $\leq 500\,	ext{ms}$)

**Requirement E-3:** An application MUST NOT act upon an intent event whose current time exceeds $t_{end}$. The SDK MUST provide a mechanism to check validity before event delivery.

---

## 6. Attestation and Provenance Chain

### 6.1 Provenance Structure

The `provenance` field is a chain of attestation records:

```
ProvenanceChain := [Attestation_0, Attestation_1, ..., Attestation_n]
```

Each `Attestation_i` contains:

| Field | Description |
|-------|-------------|
| `attestation_id` | UUID of this attestation step |
| `previous_id` | UUID of previous attestation (or null for Attestation_0) |
| `attester` | Identifier of the attesting component |
| `claim` | The claim being attested |
| `evidence` | Evidence supporting the claim |
| `signature` | Ed25519 signature over (claim + evidence) |
| `timestamp` | Attestation time |

### 6.2 Attestation Steps

The standard provenance chain includes the following attestation steps:

**Attestation_0 — Hardware Origin:**
- Claim: "Epoch $E$ was acquired by hardware $h_{id}$ at time $t_0$"
- Evidence: Hardware timestamp, channel configuration hash
- Attester: Neural HAL (Hardware Abstraction Layer)

**Attestation_1 — Preprocessing Integrity:**
- Claim: "Epoch $E$ was preprocessed through stages P1–P5 with parameters $\phi_{pre}$"
- Evidence: Preprocessing parameter hash, quality metrics
- Attester: Preprocessing Pipeline

**Attestation_2 — Classification Integrity:**
- Claim: "Intent $I$ was generated by classifier $\mathcal{C}$ with parameters $\Theta$ and confidence $c$"
- Evidence: Classifier manifest hash, model weight hash, confidence computation trace
- Attester: Classification Mesh

**Attestation_3 — Consent Verification:**
- Claim: "Intent $I$ was generated under consent state $C_{state}$ which was active at time $t_0$"
- Evidence: Consent event reference, consent state hash
- Attester: Consent Engine (axonos-consent)

**Attestation_4 — SDK Boundary:**
- Claim: "Intent $I$ was delivered to application $A$ with capability manifest $M_A$"
- Evidence: Application capability manifest hash, delivery timestamp
- Attester: SDK Runtime

### 6.3 Signature Requirements

**Requirement A-1:** Every attestation step MUST be signed by the attesting component using Ed25519. The public key of each attesting component MUST be registered in the kernel's attestation key registry at boot time.

**Requirement A-2:** The provenance chain MUST be verifiable in $O(n)$ time where $n$ is the number of attestation steps. Verification MUST be possible without network access.

**Requirement A-3:** If any attestation step fails verification, the intent event MUST be rejected at the SDK boundary with error code `ATTESTATION_FAILURE`.

---

## 7. Timing Contract

### 7.1 End-to-End Latency Bound

The total latency from signal acquisition to intent event delivery is bounded by:

$$L_{total} = L_{acq} + L_{pre} + L_c + L_{ipc} + L_{deliver}$$

Where:
- $L_{acq}$: Acquisition latency (hardware-dependent, typically $< 1\,	ext{ms}$)
- $L_{pre}$: Preprocessing latency ($\leq D_{pre} = T_e/4$)
- $L_c$: Classification latency ($\leq D_{class} = T_e/2$)
- $L_{ipc}$: Inter-process communication latency ($\leq 100\,\mu	ext{s}$ for shared-SRAM IPC per RFC-0004)
- $L_{deliver}$: SDK delivery latency ($\leq 1\,	ext{ms}$)

**Requirement T-1:** The total latency MUST satisfy:

$$L_{total} \leq 2 \cdot T_e$$

For typical values ($T_e = 50\,	ext{ms}$): $L_{total} \leq 100\,	ext{ms}$.

### 7.2 Deadline Miss Handling

**Requirement T-2:** If any stage exceeds its deadline, the pipeline MUST enter **graceful degradation** mode:

1. The current epoch is dropped
2. A `DEADLINE_MISS` event is emitted to the audit log with: stage identifier, expected deadline, actual latency, epoch identifier
3. The pipeline continues with the next epoch (no restart required)
4. If 3 consecutive deadline misses occur in the same stage, the pipeline MUST signal `PIPELINE_DEGRADED` to the system health monitor

### 7.3 Jitter Bound

**Requirement T-3:** The jitter (variance in $L_{total}$ across consecutive epochs) MUST satisfy:

$$\sigma(L_{total}) \leq rac{T_e}{10}$$

For $T_e = 50\,	ext{ms}$: $\sigma(L_{total}) \leq 5\,	ext{ms}$.

---

## 8. Error Handling and Graceful Degradation

### 8.1 Error Taxonomy

Errors in the intent processing pipeline are classified into four levels per AOS-0003:

| Level | Description | Example | Response |
|-------|-------------|---------|----------|
| L1 | Fatal system error | Hardware failure, kernel panic | System reset, alert caregiver |
| L2 | Recoverable pipeline error | Stage failure, deadline miss | Drop epoch, log, continue |
| L3 | Quality degradation | Low SNR, high uncertainty | Forward with quality flag |
| L4 | Informational | Suboptimal but usable | Log only, normal processing |

### 8.2 Graceful Degradation Modes

The classification mesh supports three degradation modes:

**Mode G1 — Full Operation:** All stages operational, normal latency, full taxonomy available.

**Mode G2 — Reduced Taxonomy:** Some classifiers disabled due to resource constraints or quality issues. Only a subset of intent types are emitted. The SDK MUST notify the application of the reduced taxonomy.

**Mode G3 — Intent Passthrough:** Classification disabled. Raw signal quality metrics are forwarded as `QualityIntent` events. No semantic intent events are emitted. This mode is used when the classifier is offline for update or calibration.

**Requirement G-1:** Mode transitions MUST be atomic and announced via a `MODE_CHANGE` event to all subscribed applications. Mode transitions MUST NOT drop in-flight epochs.

### 8.3 Failure Recovery

**Requirement G-2:** After any L1 or L2 error, the pipeline MUST recover to at least G3 mode within $5 \cdot T_e$ without manual intervention.

**Requirement G-3:** Recovery to G1 mode MAY require manual intervention (e.g., recalibration, consent renewal) but MUST be possible without system restart.

---

## 9. Conformance

### 9.1 Conformance Levels

Implementations MAY claim conformance at one of three levels:

**Level 1 — Basic Conformance:**
- Implements all MUST requirements (§3–§8)
- Passes the canonical interop test vectors (§9.2)
- Does not claim real-time guarantees

**Level 2 — Real-Time Conformance:**
- Implements all MUST and SHOULD requirements
- Provides bounded worst-case latency analysis (static analysis or BMC)
- Passes real-time stress test vectors (§9.2)

**Level 3 — Safety-Critical Conformance:**
- Implements all requirements (MUST, SHOULD, MAY)
- Provides formal verification of critical paths (Kani, Coq, or equivalent)
- Passes all test vectors including fault injection (§9.2)
- Submitted to independent third-party audit

### 9.2 Test Vectors

The canonical test vector suite includes:

| Vector ID | Description | Expected Result |
|-----------|-------------|-------------------|
| TV-001 | Normal epoch, full pipeline | Valid intent event emitted |
| TV-002 | Epoch with artifact (P1 failure) | Epoch dropped, failure event logged |
| TV-003 | Low SNR epoch (P5 flag) | Intent emitted with quality_flag=L3 |
| TV-004 | Classification deadline miss | Graceful degradation, deadline event logged |
| TV-005 | Invalid event type in taxonomy | Rejected at SDK boundary |
| TV-006 | Attestation chain break | Rejected at SDK boundary |
| TV-007 | Consent withdrawal mid-epoch | Epoch dropped, consent reference invalidated |
| TV-008 | Three consecutive deadline misses | PIPELINE_DEGRADED signal emitted |
| TV-009 | Jitter exceeding bound | Logged as L3 quality event |
| TV-010 | Mode transition G1→G2→G1 | Atomic transition, no epoch loss |
| TV-011 | Fault injection: HAL crash | Recovery to G3 within $5 \cdot T_e$ |
| TV-012 | Determinism check: identical input | Bit-identical output across 1000 runs |
| TV-013 | Confidence below threshold | Null output ($ot$) emitted |
| TV-014 | Validity interval expiration | SDK rejects expired event |
| TV-015 | Full provenance verification | All signatures valid, chain complete |

---

## 10. Security Considerations

### 10.1 Threats Addressed

This artifact addresses the following threats from AOS-0009:

- **T-001 — Signal Injection:** Attestation_0 ensures epoch origin authenticity
- **T-002 — Classification Tampering:** Attestation_2 and deterministic requirements prevent undetected modification
- **T-003 — Intent Replay:** Validity intervals and event IDs prevent replay attacks
- **T-004 — Type Confusion:** Typed payload schemas prevent semantic confusion
- **T-005 — Timing Side-Channel:** Bounded latency and jitter limits leak temporal information

### 10.2 Threats Not Addressed

- **T-006 — Physical Hardware Tampering:** Requires hardware-level countermeasures outside this artifact's scope
- **T-007 — Adversarial Machine Learning:** Requires classifier-specific defenses

---

## 11. Privacy Considerations

### 11.1 Data Minimization

**Requirement PR-1:** The classification mesh MUST NOT retain raw neural signal data beyond the epoch currently being processed. Ephemeral buffers (§3.3) are the only permitted retention mechanism.

**Requirement PR-2:** Intent events MUST NOT include raw signal samples, power spectral density, or any representation from which raw signal could be reconstructed.

### 11.2 Consent Binding

**Requirement PR-3:** Every intent event MUST include a `consent_reference` linking to the active consent event. If consent is withdrawn, all intent events generated under that consent MUST be considered invalid for new actions (though they may remain in audit logs per AOS-0005).

---

## 12. Glossary

| Term | Definition |
|------|------------|
| **Epoch** | The fundamental unit of neural signal processing; a contiguous temporal interval of sampled neural data |
| **Intent Event** | A typed, attested, temporally bounded record representing a classified neural intent |
| **Provenance Chain** | A cryptographically signed sequence of attestation records linking an intent event to its origin |
| **Classification Mesh** | The deterministic computational pipeline that transforms preprocessed epochs into intent events |
| **Graceful Degradation** | The pipeline's ability to continue operating at reduced capability after component failure |
| **SDK Boundary** | The interface between the AxonOS kernel/runtime and application code |

---

## 13. References

1. RFC-0001 — EDF Scheduler with Biological Deadlines. AxonOS Engineering RFCs, 2026.
2. RFC-0004 — Dual-Core Real-Time Contract. AxonOS Engineering RFCs, 2026.
3. RFC-0005 — Capability-Based Application Manifest. AxonOS Engineering RFCs, 2026.
4. Liu, C.L. and Layland, J.W. "Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment." Journal of the ACM, 1973.
5. AOS-0003 — Evidence Levels and Claims. AxonOS Standard, Draft 0.1.1.
6. AOS-0005 — Consent Semantics. AxonOS Standard, Draft 0.1.1.

---

## 14. Change Log

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-05-21 | Initial draft |
| 0.1.1 | 2026-05-21 | Editorial: added TV-015, clarified G3 mode |

---

*This artifact is pre-normative. It is suitable for architecture review, implementation alignment, and conformance planning. It is not a certified medical-device standard, a clinical protocol, or a regulatory approval claim.*
