# AOS-0008 — IPC and Timing Contract

Status: Draft 0.1 — pre-normative.  
Audience: kernel implementers, embedded systems engineers, safety reviewers, validation engineers, SDK authors, and hardware-in-the-loop test authors.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

This artifact defines the draft IPC and timing contract for AxonOS implementations.

AxonOS exists because BCI software cannot treat timing as a convenience metric.
In a closed-loop neural system, timing violations can corrupt signal continuity,
misalign intent windows, invalidate classifier state, or produce unsafe actuation
behavior. Therefore a timing claim must be stated as a bounded claim under stated
assumptions, not as an average or marketing number.

This artifact defines the required shape of a real-time claim, the required
shape of an IPC claim, deadline and response-time terminology, buffer and queue
contract fields, failure behavior for overrun and deadline miss, evidence levels
for timing claims, minimum conformance tests, and non-conformance examples.

Draft 0.1 does not define a final byte-level ABI. It defines the contract that
future ABI and wire-format artifacts must satisfy.

## 2. Timing vocabulary

| Term | Meaning |
|---|---|
| `T_i` | Period of task `i` |
| `D_i` | Relative deadline of task `i` |
| `C_i` | Worst-case execution time of task `i` |
| `R_i` | Worst-case response time of task `i` |
| `U_i` | Utilisation contribution `C_i / T_i` |
| `U_total` | Sum of admitted task utilisations |
| `U_max` | Implementation-defined admission ceiling |
| WCET | Worst-case execution time under stated assumptions |
| WCRT | Worst-case response time under stated scheduling model |
| IPC | Inter-process or inter-core communication mechanism |
| overrun | Producer cannot enqueue because bounded capacity is exhausted |
| deadline miss | Job completion occurs after its declared deadline |

A timing claim without a declared deadline and bound is not an AxonOS timing claim.

## 3. Minimum real-time claim record

Every AxonOS timing claim should be expressible in the following form:

```text
Claim:
  component:
  task/stage:
  hardware:
  clock:
  period:
  deadline:
  WCET or WCRT bound:
  scheduling model:
  workload assumptions:
  evidence level:
  artifact:
  falsification threshold:
  limitations:
```

This format prevents mixing predicted, measured, and certified claims.

## 4. IPC contract record

Every IPC mechanism used in an AxonOS real-time boundary should declare:

| Field | Required description |
|---|---|
| `name` | IPC mechanism name |
| `role` | signal path, control path, diagnostic path, or application path |
| `producer` | single producer, multiple producer, interrupt producer, DMA producer |
| `consumer` | single consumer, task consumer, application consumer, inter-core consumer |
| `capacity` | slot count or byte capacity |
| `slot_size` | byte size of each slot, if fixed |
| `alignment` | required alignment in bytes |
| `endianness` | byte order for serialized fields |
| `blocking_behavior` | wait-free, lock-free, bounded wait, blocking, or unknown |
| `overrun_behavior` | reject, drop-newest, drop-oldest, backpressure, fault |
| `memory_ordering` | ordering discipline for payload visibility |
| `unsafe_surface` | unsafe code or equivalent low-level primitive |
| `evidence_level` | evidence supporting the claim |

If a repository cannot fill this table, it should not claim AxonOS IPC conformance.

## 5. Draft queue profile: SPSC-RT

Draft 0.1 defines an initial queue profile named `SPSC-RT`.

`SPSC-RT` is a single-producer/single-consumer bounded queue suitable for a
real-time signal path if all of the following hold:

1. capacity is fixed at compile time or initialization time;
2. producer operation has bounded step count;
3. consumer operation has bounded step count;
4. no heap allocation occurs on the hot path;
5. overrun behavior is explicit;
6. payload visibility is governed by documented memory ordering;
7. unsafe code surface is documented and tested;
8. queue state can be reset or faulted safely.

`SPSC-RT` does not require a specific implementation. A ring buffer, static queue,
or hardware mailbox may qualify if the contract is satisfied.

## 6. Draft packet layout requirements

A future stable ABI may define byte-level packet formats. Until then, any IPC
packet or event frame crossing an AxonOS boundary should document at minimum:

| Field | Requirement |
|---|---|
| magic/version | identifies frame family and version |
| frame_type | typed event, control, consent, safety, diagnostic, etc. |
| length | payload length in bytes |
| sequence | monotonic counter or sequence number if ordered |
| timestamp | monotonic timestamp or declared absence |
| source | component or node identity |
| flags | delivery, safety, or compatibility flags |
| payload | typed payload, schema-defined |
| integrity | checksum, MAC, signature, or declared absence |

Endianness must be explicit. Alignment requirements must be explicit. Reserved
fields must have defined default values.

## 7. Example frame envelope

Draft 0.1 does not freeze ABI bytes, but a future frame envelope should be able
to express the following conceptual layout:

```text
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-------------------------------+-------------------------------+
| magic/version                 | frame_type                    |
+-------------------------------+-------------------------------+
| header_len                    | payload_len                   |
+-------------------------------+-------------------------------+
| sequence_low                                                  |
+---------------------------------------------------------------+
| sequence_high                                                 |
+---------------------------------------------------------------+
| timestamp_low                                                 |
+---------------------------------------------------------------+
| timestamp_high                                                |
+---------------------------------------------------------------+
| source_id                                                     |
+---------------------------------------------------------------+
| flags                         | reserved                      |
+-------------------------------+-------------------------------+
| payload ...                                                   |
+---------------------------------------------------------------+
| integrity ...                                                 |
+---------------------------------------------------------------+
```

The exact byte width of each field is not normative in Draft 0.1. The normative
requirement is that future byte-level definitions must not leave versioning,
length, ordering, timestamp semantics, or integrity semantics implicit.

## 8. Deadline miss behavior

A safety-relevant implementation must document behavior on deadline miss.

Acceptable responses may include reject current output, enter degraded mode,
trigger backpressure, clear affected queue, enter safe idle, disable stimulation,
emit safety event, fault session, or log transition.

Unacceptable default behavior includes silently delivering stale intent, silently
skipping safety state update, continuing stimulation with stale classification,
hiding the deadline miss from audit trail, or converting hard deadlines into
best-effort scheduling without documentation.

## 9. Overrun behavior

Overrun behavior must be explicit.

| Policy | Meaning | Safety note |
|---|---|---|
| reject-new | producer returns error; existing data preserved | often safest for control paths |
| drop-new | incoming item discarded | must be audited |
| drop-old | oldest item discarded | dangerous for signal continuity |
| backpressure | producer slows or blocks | must be bounded |
| fault | system enters fault state | appropriate for safety-critical paths |

For a safety-critical neural signal path, silent drop-old behavior is presumptively
non-conformant unless justified by a bounded safety case.

## 10. Priority inversion and blocking

If the IPC or timing path can block, the implementation must document maximum
blocking time, priority inheritance or ceiling protocol, scheduler interaction,
interrupt masking duration, critical-section duration, and deadlock avoidance
argument.

A system with unbounded blocking in the critical neural path cannot claim hard
real-time AxonOS alignment.

## 11. Timing jitter

Jitter claims must distinguish release jitter, completion jitter, transport
jitter, scheduler jitter, measurement jitter, clock drift, and timestamp
quantization.

A claim such as "low jitter" is insufficient. The claim must state what jitter
is being measured and how.

## 12. Evidence mapping

| Evidence level | Timing evidence example |
|---|---|
| L0 | design intent or architecture sketch |
| L1 | analytical bound, instruction-count derivation, model check |
| L2 | measured on development fixture |
| L3 | externally instrumented trace: GPIO, logic analyzer, oscilloscope |
| L4 | independent reproduction or review |
| L5 | formal regulatory/certification evidence |

An L1 timing proof does not become L3 because it is precise. L3 requires an
external measurement artifact.

## 13. Minimum test expectations

A draft AxonOS timing implementation should provide tests or artifacts for queue
capacity enforcement, overrun behavior, enqueue/dequeue invariants, memory
ordering or equivalent visibility argument, deadline miss reporting, timestamp
monotonicity, reset behavior, fault behavior after corrupted queue state, no heap
allocation on declared hot path, and documentation of unsafe surface.

## 14. Conformance requirements

A draft AxonOS IPC/timing implementation should satisfy:

1. timing claims include deadline and bound;
2. IPC capacity is documented;
3. IPC overrun behavior is documented;
4. blocking behavior is documented;
5. memory ordering or visibility semantics are documented;
6. unsafe or low-level surface is documented;
7. deadline miss behavior is documented;
8. evidence level is declared;
9. L3 claims include trace artifact references;
10. hidden best-effort conversion is prohibited.

## 15. Non-conformance examples

The following are non-conforming or misleading: real-time claim with only average
latency, queue with undocumented capacity, lock-free claim without implementation
evidence, wait-free claim with hidden retry loop, L3 claim without trace artifact,
silent deadline miss, silent drop-old overrun in signal path, unbounded mutex in
critical neural path, IPC packet with no version field, and serialized event with
unknown endianness.

## 16. Release checklist for an IPC/timing claim

Before an AxonOS repository publishes an IPC/timing claim, the maintainer should
verify:

- the hardware target is named;
- the clock source is named;
- the scheduler or execution model is named;
- queue capacity is named;
- overrun behavior is named;
- deadline miss behavior is named;
- blocking behavior is named;
- memory ordering or equivalent visibility semantics are named;
- the claim appears in the claims register;
- the evidence level is stated;
- the artifact is linked;
- the falsification threshold is stated.

This checklist is intentionally strict because real-time BCI claims are easy to
overstate and difficult to repair after publication.

## 17. Open issues

Draft 0.1 leaves unresolved: stable ABI for typed intent events, canonical packet
byte layout, canonical capability descriptor layout, shared-memory mailbox
profile, multi-producer queue profile, inter-core timing profile, conformance
test vectors, and hardware trace artifact schema.

## 18. Summary

AxonOS timing claims must be bounded, falsifiable, and evidence-tagged.

The standard does not forbid experimentation. It forbids presenting best-effort
behavior as hard real-time evidence.
