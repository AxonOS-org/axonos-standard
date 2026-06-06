# Claims Catalogue — The AxonOS Standard

**AxonOS Standard v1.1.0** · **Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

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

| id | Claim | Value | Level | Artefact | Falsifier |
|---|---|---|---|---|---|
| **C-1** | End-to-end worst-case response time, upper bound | **≤ 1000 µs** | **L1** | [`axonos-scheduler` BMC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-scheduler/kani-proofs/src/main.rs) — the bounded-model-checking proofs of the response-time analysis from which the bound is derived for the reference pipeline's verified per-task WCETs | A reachable schedule, within the model's admissible inputs, whose response time exceeds 1000 µs |
| **C-1·L2** | End-to-end worst-case response time, worst observed (complement to C-1) | **972 µs** over a 12-hour soak of ≈ 10.8 million epochs, **0 deadline misses** | L2 | Soak trace — **publication pending** (see *Artefact availability* below) | A soak under the stated conditions on the reference hardware observing a response time above 972 µs, or any deadline miss |
| **C-2** | Observation-cadence jitter, one standard deviation | **2.1 µs** | **L2** | Soak trace — **publication pending** | A soak under the stated conditions measuring σ above 2.1 µs |
| **C-3** | Inter-process-communication slot latency, upper bound | **≤ 0.5 µs** | **L1** | [`axonos-spsc` BMC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-spsc/kani-proofs/src/main.rs) — proofs of the single-producer single-consumer slot's bounded behaviour | A reachable slot operation, within the model, exceeding 0.5 µs |
| **C-3·L2** | Inter-process-communication slot latency, measured (complement to C-3) | **0.2 µs** | L2 | Measurement trace — **publication pending** | A measurement under the stated conditions exceeding 0.2 µs |
| **C-4** | Consent-withdrawal transition time, upper bound | **≤ 1648 cycles** (≈ 9.8 µs at 168 MHz, Cortex-M4F) | **L1** | [`axonos-consent` `kani/handle_withdraw_terminates.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/kani/handle_withdraw_terminates.rs) — proof that withdrawal terminates within a bounded number of steps | A reachable withdrawal, within the model, exceeding the bound |
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

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
