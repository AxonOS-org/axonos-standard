# AOS-0008 — IPC and Timing Contract

Status: Draft 0.1 — pre-normative.  
Audience: kernel implementers, embedded systems engineers, safety reviewers, validation engineers, SDK authors, and hardware-in-the-loop test authors.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0008 defines the draft IPC and timing contract for AxonOS implementations.

AxonOS exists because BCI software cannot treat timing as a convenience metric.
In a closed-loop neural system, timing violations can corrupt signal continuity,
misalign intent windows, invalidate classifier state, or produce unsafe actuation
behavior. Therefore a timing claim must be stated as a bounded claim under stated
assumptions, not as an average or marketing number.

## 2. Timing vocabulary

| Term | Meaning |
|---|---|
| `T_i` | period of task `i` |
| `D_i` | relative deadline of task `i` |
| `C_i` | worst-case execution time of task `i` |
| `R_i` | worst-case response time of task `i` |
| `U_i` | utilisation contribution `C_i / T_i` |
| WCET | worst-case execution time under stated assumptions |
| WCRT | worst-case response time under stated scheduling model |
| IPC | inter-process or inter-core communication |
| overrun | producer cannot enqueue because bounded capacity is exhausted |
| deadline miss | completion occurs after declared deadline |

A timing claim without a declared deadline and bound is not an AxonOS timing claim.

## 3. Minimum real-time claim record

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

Every IPC mechanism used in a real-time boundary should declare name, role,
producer, consumer, capacity, slot size, alignment, endianness, blocking
behavior, overrun behavior, memory ordering, unsafe surface, and evidence level.

If a repository cannot fill this record, it should not claim AxonOS IPC
conformance.

## 5. Draft queue profile: SPSC-RT

`SPSC-RT` is a single-producer/single-consumer bounded queue suitable for a
real-time signal path when capacity is fixed, producer and consumer operations
have bounded step count, no heap allocation occurs on the hot path, overrun
behavior is explicit, payload visibility is documented, unsafe surface is
documented, and reset/fault behavior is safe.

## 6. Draft packet layout requirements

A future ABI may define byte-level packet formats. Until then, any IPC packet
crossing an AxonOS boundary should document magic/version, frame type, length,
sequence, timestamp, source, flags, payload, and integrity field.

Endianness must be explicit. Alignment must be explicit. Reserved fields must
have defined default values.

## 7. Example frame envelope

```text
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

Draft 0.1 does not freeze field widths. It requires that future byte-level
definitions make versioning, length, ordering, timestamp semantics, and integrity
semantics explicit.

## 8. Deadline miss behavior

A safety-relevant implementation must document behavior on deadline miss.

Acceptable responses include rejecting output, entering degraded mode, triggering
backpressure, clearing affected queue, entering safe idle, disabling stimulation,
emitting safety event, faulting session, or logging transition.

Unacceptable behavior includes silently delivering stale intent, silently
skipping safety state update, continuing stimulation with stale classification,
or converting hard deadlines into best-effort scheduling without documentation.

## 9. Overrun behavior

| Policy | Meaning | Safety note |
|---|---|---|
| reject-new | producer returns error; existing data preserved | often safest for control paths |
| drop-new | incoming item discarded | must be audited |
| drop-old | oldest item discarded | dangerous for signal continuity |
| backpressure | producer slows or blocks | must be bounded |
| fault | system enters fault state | appropriate for safety-critical paths |

Silent drop-old behavior in a safety-critical signal path is presumptively
non-conformant unless justified by a bounded safety case.

## 10. Priority inversion and blocking

If the IPC or timing path can block, the implementation must document maximum
blocking time, priority inheritance or ceiling protocol, scheduler interaction,
interrupt masking duration, critical-section duration, and deadlock avoidance
argument.

Unbounded blocking in the critical neural path is not compatible with hard
real-time AxonOS alignment.

## 11. Timing jitter

Jitter claims must distinguish release jitter, completion jitter, transport
jitter, scheduler jitter, measurement jitter, clock drift, and timestamp
quantization.

A claim such as "low jitter" is insufficient.

## 12. Evidence mapping

L1 covers analytical bounds and model checks. L2 covers runtime fixture
measurements. L3 requires external instrumentation such as GPIO, logic analyzer,
or oscilloscope traces.

An L1 proof does not become L3 because it is precise.

## 13. Minimum tests

A draft timing implementation should test queue capacity enforcement, overrun
behavior, enqueue/dequeue invariants, visibility semantics, deadline miss
reporting, timestamp monotonicity, reset behavior, fault behavior after corrupted
state, no heap allocation on declared hot path, and unsafe surface documentation.

## 14. Release checklist

Before publishing an IPC/timing claim, verify hardware target, clock source,
scheduler model, queue capacity, overrun behavior, deadline miss behavior,
blocking behavior, memory ordering, claims register entry, evidence level,
artifact link, and falsification threshold.

## 15. Non-conformance examples

Average-latency real-time claims, undocumented queue capacity, lock-free claims
without evidence, wait-free claims with hidden retry loops, L3 claims without
trace artifacts, silent deadline misses, silent drop-old overrun, unbounded
mutexes, IPC packets without version fields, and unknown endianness are not
aligned.

## 16. Summary

AxonOS timing claims must be bounded, falsifiable, and evidence-tagged.
