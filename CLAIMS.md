# Claims Catalogue — The AxonOS Standard

**AxonOS Standard v1.1.1** · **Editor:** Denis Yermakou · **Project:** AxonOS

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

**Open question, recorded 2026-10-09.** Each L1 row below proves a property over
a *stated, bounded* domain — two tasks with periods ≤ 8, a four-slot ring —
which `STANDARD.md` Section 23 requires a claim to state, but which is narrower
than the "entire admissible input space" of Section 22's definition of L1. The
catalogue therefore states every domain in the row. Whether Section 22 should
read "over a stated domain" is a normative question for the next minor
version, to be settled by RFC; until then, no L1 row claims anything beyond its
stated domain.

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

<!-- next correction -->

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

<!-- next correction -->

> **Correction, published 2026-10-09.** Two defects are corrected here, and
> with them every row that depended on a timing figure.
>
> First, the reference-hardware traces this catalogue listed as *publication
> pending* — the 972 µs worst observed response time (C-1·L2), the 2.1 µs
> jitter (C-2), the 0.2 µs slot latency (C-3·L2), the 18-hour consent soak
> (C-4·L2) and the baseline-OS measurement behind C-5 — do not exist as
> publishable traces. A figure whose artefact does not exist fails the second
> condition of the publishing rule outright, not provisionally. Those figures
> are **withdrawn** from every public surface under the AxonOS name.
>
> Second, C-1 (≤ 1000 µs) and C-3 (≤ 0.5 µs) carried the tag *analytical*.
> `STANDARD.md` Section 22 admits three evidence levels, L1, L2 and L3, and
> `VALIDATION.md` Section 2 adds *derived*; *analytical* is none of them, so a
> figure carrying only that tag may not be published as a claim. Both values
> remain what they always were in the Standard — the DC1 and DC3
> **requirements** — and the reference implementation does **not** claim to
> meet them. `STANDARD.md` Section 9.3 states the reference implementation's
> status clause by clause.
>
> What remains claimed is what the harnesses prove: properties of code, at L1,
> each over its stated domain.

| id | Claim | Value | Level | Artefact | Falsifier |
|---|---|---|---|---|---|
| **C-1** | End-to-end worst-case response time of the reference pipeline | **not claimed.** ≤ 1000 µs is the DC1 requirement, not a result | — | The only evidence is an unpublished response-time analysis over nominal worst-case execution times, without interrupt interference or blocking terms ([axonos-kernel#1](https://github.com/AxonOS-org/axonos-kernel/issues/1)). That is not an evidence level of `STANDARD.md` Section 22. A bounded model checker over Rust MIR cannot compute a time | — |
| **C-1·L1** | Admission and earliest-deadline selection in the scheduler | admission sound; earliest deadline selected, ties by lower id; single-task busy period equal to its WCET; demand-bound function monotone | **L1** | [`axonos-scheduler` BMC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-scheduler/kani-proofs/src/main.rs): S1–S5 and the two demand-bound harnesses. **Domain:** bounded inputs (two-task admission with periods ≤ 8). The multi-task busy-period iteration is tested and cross-checked, not BMC-proved. Re-run in CI on every push as an advisory job, and as a blocking gate on release tags and pull requests ([`release-gate.yml`](https://github.com/AxonOS-org/axonos-kernel/blob/main/.github/workflows/release-gate.yml)) | A counterexample from any harness within its stated domain |
| **C-1·L2** | End-to-end worst-case response time, worst observed | **withdrawn 2026-10-09** (formerly 972 µs) | — | No trace exists | — |
| **C-2** | Observation-cadence jitter, one standard deviation | **withdrawn 2026-10-09** (formerly 2.1 µs) | — | No trace exists | — |
| **C-3** | Inter-process-communication slot latency | **not claimed.** ≤ 0.5 µs is the DC3 requirement, not a result | — | No proof of a time exists; what the harnesses prove is C-3·L1 | — |
| **C-3·L1** | Single-producer single-consumer slot behaviour | exact round trip; `try_push` loop-free and terminating; FIFO order; full and empty signalled | **L1** | [`axonos-spsc` BMC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-spsc/kani-proofs/src/main.rs): K1–K5. **Domain:** a four-slot ring of `u32`. CI as for C-1·L1 | A counterexample from any harness within its stated domain |
| **C-3·L2** | Inter-process-communication slot latency, measured | **withdrawn 2026-10-09** (formerly 0.2 µs) | — | No trace exists | — |
| **C-4** | Consent-withdrawal transition time, upper bound | **retracted** 2026-10-02: no bound at this revision | — | [`axonos-consent` SPEC §4.1](https://github.com/AxonOS-org/axonos-consent/blob/main/SPEC.md#41-the-transition): the ≤ 1648-cycle figure was derived for the 4-byte-tag path that 0.9.0 removed. Ed25519 verification now dominates the admission of every frame and is budgeted per deployment (SPEC §4.2, §4.3). A bound returns only with its proof or an on-device measurement at L2 | — |
| **C-4·L1** | Consent changes only on an authenticated frame, and withdrawal is final | no transition without a verified signature; no sequence admitted twice; `Withdrawn` absorbing in the state machine and in the publication gate; publication only while `Granted` | **L1** | [`axonos-consent` `src/proofs.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/src/proofs.rs): ten harnesses, run in CI as a blocking job on every push; all ten complete since 0.9.1. The five harnesses formerly cited here, under `kani/`, were never compiled into the crate and were removed in 0.9.0 | A reachable execution, within a harness's bounds, that changes state on an unverified frame, admits a sequence twice, or leaves `Withdrawn` |
| **C-4·L2** | Consent-withdrawal transition time, measured | **withdrawn 2026-10-09** | — | No trace exists. [`benches/withdrawal_latency.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/benches/withdrawal_latency.rs) is a re-runnable host benchmark procedure, not a reference-hardware measurement | — |
| **C-5** | Jitter improvement factor over a baseline general-purpose OS | **withdrawn 2026-10-09** | — | Both inputs (C-2 and the baseline-OS measurement) have no trace | — |

---

## Artefact availability

**Published and linked.** The three L1 rows — C-1·L1, C-3·L1 and C-4·L1 —
are machine-checkable harnesses in the reference repositories, linked above; a
reader with the toolchain can re-run them.

**Not in existence.** No reference-hardware trace of any kind has been
published, and none of the traces earlier versions of this catalogue described
as pending exists in publishable form. Every timing figure that depended on one
is withdrawn above. Producing the first trace — a GPIO-instrumented pipeline on
the reference board, captured by a logic analyser, published raw with its
post-processing, whatever it shows — is the **immediate validation task**, and
the first step of `ROADMAP.md` Phase 1.

A project that writes "this trace does not exist" in its own catalogue, and
takes the figure down, is a project whose remaining claims can be believed.

---

## The absence of L3 claims

This catalogue contains **no L3 claim**, and the absence is recorded here
explicitly, as `VALIDATION.md` Section 5.3 requires.

L3 evidence requires an independent reproduction, by a party with no stake in
the Project, on separate reference hardware, witnessed by a signed report. No
such reproduction has yet occurred, so the Project holds no L3 artefact, and the
discipline forbids labelling any claim L3 in its absence. The catalogue
therefore records, for each claim, the highest level the Project genuinely holds
— at this revision, L1 for the proven properties and nothing else — and
nothing higher.

The first L3 claim the Project intends to pursue is an **independent
reproduction of the end-to-end worst-case response time**, once a first L2
measurement of it exists, to be sought
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
