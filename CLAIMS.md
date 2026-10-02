# Claims Catalogue — The AxonOS Standard

**AxonOS Standard v1.1.0** · **Editor:** Denis Yermakou · **Project:** AxonOS

*This is the **claims catalogue** required by `VALIDATION.md` Section 5: the
single, public, maintained document that lists every quantitative claim the
AxonOS Project makes under the AxonOS name, and records, for each, its claimed
value, its evidence level, the link to the artefact from which the claim can be
re-derived or re-checked, and the finding that would falsify it.*

*The catalogue exists so that the **publishing rule** of `VALIDATION.md`
Section 2 is auditable in one place. A reviewer reads this file and, for each
entry, confirms four things: that an evidence level is stated; that an artefact
is linked; that the artefact is accessible; and that the claim is falsifiable.
The conformance suite's category C6, defined in `CONFORMANCE.md`, performs
exactly this check against this file.*

*The catalogue is maintained separately from the normative text, as
`VALIDATION.md` Section 5.2 directs, because links are the kind of thing
correctly maintained in a versioned file rather than frozen into a standard's
prose. Updating this file — to add a claim, to add an artefact link, or to
re-grade a claim under Section 6 — does not change the Standard's normative
text and does not increment the Standard's version.*

---

## The evidence levels, in one line each

The full definitions are in `VALIDATION.md` Section 1; this is the reminder a
reader of the table needs.

- **L1 — formally proven.** A bound established by a machine-checked proof
  ranging over the *entire* admissible input space. Artefact: the proof
  harness and the checker's transcript. Falsifier: a single admissible input
  for which the bound fails.
- **L2 — measured on reference hardware.** A value observed, on identified
  hardware, under identified conditions, recorded in a trace. Artefact: the
  trace, and the post-processing that derived the headline figure. Falsifier: a
  measurement under the stated conditions that contradicts the value.
- **L3 — independently validated.** An L2 measurement reproduced by an
  independent party on separate hardware, witnessed by a signed report.
  Artefact: that signed report. Falsifier: a competent independent
  reproduction that does not reproduce.
- **derived.** A value computed from other claims rather than proven or
  measured. Tag: `derived`, with inputs cited. Inherits the weakness of its
  weakest input.

A claim is labelled with the **highest** level its evidence supports, and the
absence of a higher level is recorded honestly rather than hidden.

---

## The catalogue

Claim identifiers are stable: an entry's `id` does not change when the entry is
re-graded, so that external citations to a claim remain valid across the
catalogue's history.

> **Correction, published 2026-08-23.** C-4 carried evidence level **L1** in
> this catalogue and cited `handle_withdraw_terminates` as the harness backing
> it. That harness proves termination and target-state correctness; it contains
> no cycle assertion, and a bounded model checker over Rust MIR cannot produce a
> Cortex-M cycle count. `axonos-consent` corrected this on 2026-08-16 in its own
> README and SPEC §4.1; the correction had not propagated here, so for a week
> this catalogue overstated the evidence for the very claim it exists to record.
>
> The row is now split: the ≤ 1648 cycle figure is tagged **analytical**, and a
> separate **C-4·L1** row records what the harness does prove, including its
> open coverage gap. A catalogue that lags its sources is worse than no
> catalogue, because it is trusted; the propagation gap is recorded as an open
> process defect.

> **Correction, published 2026-10-02.** `axonos-consent` 0.9.0 removed the five
> harnesses under `kani/`. They had never been compiled into the crate, so the
> artefact C-4·L1 cited had never run. The same release withdrew the ≤ 1648-cycle
> figure of C-4, derived for a path that no longer exists. Both rows now follow
> the crate: C-4 is retracted, and C-4·L1 cites the ten harnesses in
> `src/proofs.rs` that CI runs on every push. This time the catalogue follows its
> source the same day.
>
> C-1 and C-3 carried **L1** for figures in microseconds. By the reasoning this
> catalogue recorded for C-4 on 2026-08-23, a bounded model checker over Rust MIR
> cannot produce a time: the harnesses behind both rows prove decision logic and
> loop-free structure, not durations. Both figures are re-graded **analytical**,
> and new rows C-1·L1 and C-3·L1 record what the harnesses do prove.

| id | Claim | Value | Level | Artefact | Falsifier |
|---|---|---|---|---|---|
| **C-1** | End-to-end worst-case response time, upper bound | **≤ 1000 µs** | **analytical** | Response-time analysis over the reference pipeline's per-task worst-case execution times, which are themselves analytical (datasheet cycle counts); derivation artefact **publication pending**. **Not** a Kani output: a bounded model checker over Rust MIR cannot compute a time. Interrupt interference and blocking are not yet terms in the analysis ([axonos-kernel#1](https://github.com/AxonOS-org/axonos-kernel/issues/1)) | An error in the derivation or its inputs, or an execution on the reference hardware whose response time exceeds 1000 µs |
| **C-1·L1** | Admission and earliest-deadline selection in the scheduler | admission sound; earliest deadline selected, ties by lower id; single-task busy period equal to its WCET; demand-bound function monotone | **L1** | [`axonos-scheduler` BMC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-scheduler/kani-proofs/src/main.rs): S1–S5 and the two demand-bound harnesses, over bounded inputs (two-task admission with periods ≤ 8). The multi-task busy-period iteration is tested and cross-checked, not BMC-proved | A counterexample from any harness within its stated bounds |
| **C-1·L2** | End-to-end worst-case response time, worst observed (complement to C-1) | **972 µs** over a 12-hour soak of ≈ 10.8 million epochs, **0 deadline misses** | L2 | Soak trace — **publication pending** (see *Artefact availability* below) | A soak under the stated conditions on the reference hardware observing a response time above 972 µs, or any deadline miss |
| **C-2** | Observation-cadence jitter, one standard deviation | **2.1 µs** | **L2** | Soak trace — **publication pending** | A soak under the stated conditions measuring σ above 2.1 µs |
| **C-3** | Inter-process-communication slot latency, upper bound | **≤ 0.5 µs** | **analytical** | Derivation artefact **publication pending**. **Not** a Kani output: a bounded model checker over Rust MIR cannot compute a time; what the harnesses prove is recorded as C-3·L1 | An error in the derivation, or a slot operation on the reference hardware exceeding 0.5 µs |
| **C-3·L1** | Single-producer single-consumer slot behaviour | exact round trip; `try_push` loop-free and terminating; FIFO order; full and empty signalled | **L1** | [`axonos-spsc` BMC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-spsc/kani-proofs/src/main.rs): K1–K5 | A counterexample from any harness within its stated bounds |
| **C-3·L2** | Inter-process-communication slot latency, measured (complement to C-3) | **0.2 µs** | L2 | Measurement trace — **publication pending** | A measurement under the stated conditions exceeding 0.2 µs |
| **C-4** | Consent-withdrawal transition time, upper bound | **retracted**: no bound at this revision | **retracted** | [`axonos-consent` SPEC §4.1](https://github.com/AxonOS-org/axonos-consent/blob/main/SPEC.md#41-the-transition): the ≤ 1648-cycle figure was derived for the 4-byte-tag path that 0.9.0 removed, and is withdrawn. Ed25519 verification now dominates the admission of every frame and is budgeted per deployment (SPEC §4.2, §4.3). A bound returns only with its derivation and an on-device measurement at L2 | None while retracted; a re-instated bound states its own |
| **C-4·L1** | Consent changes only on an authenticated frame, and withdrawal is final | no transition without a verified signature; no sequence admitted twice; `Withdrawn` absorbing in the state machine and in the publication gate; publication only while `Granted` | **L1** | [`axonos-consent` `src/proofs.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/src/proofs.rs): ten harnesses, run in CI as a blocking job; all ten complete since 0.9.1. The five harnesses formerly cited here, under `kani/`, were never compiled into the crate and were removed in 0.9.0 | A reachable execution, within a harness's bounds, that changes state on an unverified frame, admits a sequence twice, or leaves `Withdrawn` |
| **C-4·L2** | Consent-withdrawal transition time, measured (complement to C-4) | Median and worst-observed over an 18-hour soak | L2 | [`axonos-consent` `benches/withdrawal_latency.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/benches/withdrawal_latency.rs) — the re-runnable measurement procedure; reference-hardware soak trace **publication pending** | A soak under the stated conditions contradicting the measured bound |
| **C-5** | Jitter improvement factor of the reference kernel over a baseline general-purpose OS on the same hardware | **derived** from C-2 and the baseline measurement | **derived** | Computed by division from C-2 (reference-kernel jitter, L2) and the baseline-OS jitter measurement (L2) — **baseline trace publication pending** | A re-measurement of either input that changes the ratio, or an arithmetic error in the division |

---

## Artefact availability

The discipline distinguishes a claim that is *evidenced and linked* from a
claim whose evidence exists but is *not yet published*, and this catalogue
states which is which rather than letting the distinction blur.

**Published and linked.** The L1 proofs (C-1, C-3, C-4) are machine-checkable
harnesses in the reference repositories, linked above; a reader with the
toolchain can re-run them. The consent-withdrawal measurement procedure
(C-4·L2) is a re-runnable benchmark, linked above.

**Publication pending.** The reference-hardware **soak traces** underlying the
worst-observed L2 values — the 972 µs response-time soak (C-1·L2), the jitter
soak (C-2), the IPC-latency measurement (C-3·L2), the 18-hour consent soak
(C-4·L2), and the baseline-OS jitter measurement that is an input to the
derived factor (C-5) — are **not yet published as inspectable traces**. Until
each trace is published, the corresponding L2 (and derived) figure does not yet
satisfy the second condition of the publishing rule, and this catalogue records
that openly.

Publishing these traces — as a maintained validation record, with each trace
accompanied by the post-processing that derived its headline figure — is the
**immediate validation task** the catalogue surfaces, and it is the precondition
for the C-1·L2, C-2, C-3·L2, C-4·L2, and C-5 entries to pass conformance
category C6. It is the natural first step of `ROADMAP.md` Phase 1, ahead of the
independent reproduction that Phase 1 ultimately targets.

This is, deliberately, the kind of visible accounting `VALIDATION.md`
Section 5.3 describes: a project that will write plainly in its own catalogue
"this trace is not yet published" is a project whose linked artefacts can be
believed, because it has shown that it records by the evidence and not by the
aspiration.

---

## The absence of L3 claims

This catalogue contains **no L3 claim**, and the absence is recorded here
explicitly, as `VALIDATION.md` Section 5.3 requires.

L3 evidence requires an independent reproduction, by a party with no stake in
the Project, on separate reference hardware, witnessed by a signed report. No
such reproduction has yet occurred, so the Project holds no L3 artefact, and the
discipline forbids labelling any claim L3 in its absence. The catalogue
therefore records, for each claim, the highest level the Project genuinely holds
— L1 for the proven bounds, L2 for the measured values, derived for the
computed factor — and nothing higher.

The first L3 claim the Project intends to pursue is an **independent
reproduction of the end-to-end worst-case response time (C-1·L2)**, to be sought
in conjunction with the first clinical-pilot deployment, where an independent
clinical-engineering party will have both the reference hardware and the
motivation to perform the reproduction. `ROADMAP.md` Phase 1 describes that
intent; this catalogue is where the resulting L3 entry will be recorded if and
when the reproduction succeeds.

---

## Maintenance

This file is updated whenever a claim is added, an artefact is published and
linked, or a claim is re-graded or retracted under `VALIDATION.md` Section 6.
Re-grading is expected and disciplined: when a pending trace is published, its
entry's artefact link is filled in; when an independent reproduction succeeds, an
L2 entry is re-graded to L3 with the signed report as artefact; and if any
artefact ceases to support its claim, the claim is re-graded down or retracted,
with the change recorded here. An entry's `id` is stable across all such
changes.

A quantitative claim made under the AxonOS name on any public surface — the
website, any repository's documentation, any specification, any paper, deck, or
post — must correspond to an entry in this catalogue. A public claim with no
catalogue entry is a defect in the catalogue's maintenance, to be corrected by
adding the entry (with its level, artefact, and falsifier) or by retracting the
claim.

---

— The AxonOS Project
