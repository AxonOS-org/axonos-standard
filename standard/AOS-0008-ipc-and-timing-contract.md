# AOS-0008 — IPC and Timing Contract

Status: Draft 0.1.1 — pre-normative.  
Audience: kernel implementers, embedded systems engineers, safety reviewers, validation engineers, SDK authors, and hardware-in-the-loop test authors.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0008 defines the draft IPC and timing contract for AxonOS implementations.

AxonOS exists because BCI software cannot treat timing as a convenience metric.
In a closed-loop neural system, timing violations can corrupt signal continuity,
misalign intent windows, invalidate classifier state, or produce unsafe actuation
behavior. A timing claim must therefore be bounded and evidence-tagged.

## 2. Timing vocabulary

| Term | Meaning |
|---|---|
| `T_i` | period of task `i` |
| `D_i` | relative deadline of task `i` |
| `C_i` | worst-case execution time of task `i` |
| `R_i` | worst-case response time of task `i` |
| WCET | worst-case execution time under stated assumptions |
| WCRT | worst-case response time under stated scheduling model |
| IPC | inter-process or inter-core communication |
| overrun | producer cannot enqueue because bounded capacity is exhausted |
| deadline miss | completion occurs after declared deadline |

## 3. Minimum real-time claim record

A real-time claim should identify component, stage, hardware, clock, period,
deadline, WCET or WCRT bound, scheduling model, workload assumptions, evidence
level, artifact, falsification threshold, and limitations.

## 4. IPC contract record

Every IPC mechanism used in a real-time boundary should declare name, role,
producer, consumer, capacity, slot size, alignment, endianness, blocking
behavior, overrun behavior, memory ordering, unsafe surface, and evidence level.

## 5. Draft queue profile: SPSC-RT

`SPSC-RT` is a single-producer/single-consumer bounded queue suitable for a
real-time signal path when capacity is fixed, operations are bounded, no heap
allocation occurs on the hot path, overrun behavior is explicit, payload
visibility is documented, and reset/fault behavior is safe.

## 6. Draft packet layout requirements

A future ABI may define byte-level packet formats. Until then, any IPC packet
crossing an AxonOS boundary should document magic/version, frame type, length,
sequence, timestamp, source, flags, payload, and integrity field.

## 7. Example envelope

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

## 8. Deadline miss and overrun behavior

A safety-relevant implementation must document behavior on deadline miss and
overrun. Acceptable responses include rejecting output, degraded mode,
backpressure, clearing affected queue, safe idle, disabling stimulation, emitting
safety event, faulting session, or logging transition.

Silent stale output, silent drop-old behavior in a critical path, and best-effort
conversion without documentation are not aligned.

## 9. Requirements

Draft alignment requires deadline and bound, documented capacity, overrun
behavior, blocking behavior, visibility semantics, unsafe surface, deadline miss
behavior, evidence level, trace artifacts for L3, and no hidden best-effort
conversion.

## 10. Summary

AxonOS timing claims must be bounded, falsifiable, and evidence-tagged.
