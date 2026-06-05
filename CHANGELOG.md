# Changelog and Release Record — The AxonOS Standard

**AxonOS Standard v1.0.1** · **Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

This document records the release history of the AxonOS Standard. Every release is recorded here, and every change in a release is traceable, through the governance process of `GOVERNANCE.md`, to the Request-for-Comments document that introduced it.

For the first canonical release, version 1.0.0, this document additionally serves as a comprehensive release record: because version 1.0.0 introduces the entire Standard at once, with no prior version against which to record incremental change, the most useful thing this document can do is set out, completely, what version 1.0.0 establishes — what each document contains, what the load-bearing design decisions are, what the honest status of each forward-looking element is — so that a reader returning to this changelog in future, after subsequent releases have recorded their incremental changes against it, can see precisely what the foundation was.

---

## Version 1.0.1 — 2026-06-06

These changes add or populate **companion files** maintained alongside the
normative text. None of them changes the normative text or any conformance
criterion, so, per the versioning discipline of `STANDARD.md` Section 26, version 1.0.1 is a **patch**: an editorial release that changes no normative requirement and no conformance criterion. It folds the companion-file additions below, together with the repository-infrastructure changes that accompany them.

- Added `CLAIMS.md`, the **claims catalogue** required by `VALIDATION.md`
  Section 5, which at version 1.0.0 the repository defined but did not yet
  contain. It records each principal quantitative claim with its value,
  evidence level, artefact link, and falsifier; links the published L1 proofs
  and the consent-withdrawal measurement procedure; and records honestly that
  the reference-hardware soak traces underlying the L2 figures are not yet
  published and that publishing them is the immediate validation task. As
  `VALIDATION.md` Section 5.2 directs, the catalogue is maintained separately
  from the normative text and its upkeep does not increment the Standard's
  version.
- Added `ROADMAP.md`, an informative statement of the intended path forward —
  the evidence progression toward a first L3 claim, the governance transition,
  and the adoption milestones — written in the discipline of `VALIDATION.md`
  and committing to no dates.
- Added, in `README.md`, a "The reference implementation" section that links
  the seven reference repositories described normatively in `STANDARD.md`
  Section 31, so that a reader arriving at the Standard has a navigable path to
  the software that demonstrates it.
- Added a continuous-integration workflow, `.github/workflows/ci.yml`, that checks repository structure, version consistency across the documents, editor and licence attribution, the section numbering and internal cross-references of `STANDARD.md`, internal link resolution, and `CITATION.cff` validity, alongside style and spelling checks — complementing the existing `integrity` workflow. A second tool, `tools/check_consistency.py`, implements the structural checks dependency-free.
- Refreshed the document-version header of each normative document and the `VERSION` and `CITATION.cff` files to 1.0.1, and recorded the editor attribution in every document. No normative text was changed.

---

## Version 1.0.0 — 2026-05-21

The first canonical release of the AxonOS Standard: the complete normative Standard and its companion documents, establishing the open technical standard for deterministic brain-computer-interface software.

### Summary of the release

Version 1.0.0 establishes, in a single coordinated release, the entire AxonOS Standard. It comprises the canonical normative text, the conformance methodology and suite, the validation discipline, the governance, the glossary, and the informative architecture chapters. There is no prior version; version 1.0.0 is the foundation, and subsequent releases will record their changes incrementally against it, each traceable to its Request for Comments, with breaking changes confined to major-version increments per the versioning discipline of `STANDARD.md` Section 26.

### What `STANDARD.md` establishes

`STANDARD.md`, the canonical normative text, is established in this release with thirty-one numbered sections in seven parts, plus five appendices.

Part I, Foundations, establishes the scope of the Standard — the systems it governs, the boundaries of what it defines, and its five intended audiences — together with the conformance definition and the four-layer architectural overview with its three cross-cutting subsystems.

Part II, the Real-Time Substrate, establishes the kernel's real-time guarantees: the dual-core execution model with its fixed task set and fixed-duration processing epoch; the Earliest-Deadline-First scheduling discipline with its utilisation ceiling and admission-control procedure; the worst-case-timing-analysis methodology; the six-clause dual-core real-time contract designated DC1 through DC6; the lock-free single-producer single-consumer inter-process-communication discipline; and the monotonic-clock semantics.

Part III, the Security and Privacy Model, establishes the capability system: the closed set of exactly four capabilities — navigation, workload-advisory, session-quality, artefact-events — each with a rate ceiling; the structural prohibition of exactly four categories of neural data — raw neural signal, affective state, cognitive profile, biometric identity; the signed manifest format; and the three-state consent finite-state machine with its trusted-path requirement.

Part IV, the Application Binary Interface, establishes application-binary-interface version 1: the versioning discipline, the connection handshake, the byte-exact twenty-eight-byte intent-observation wire format, the closed error taxonomy, and the forward- and backward-compatibility rules.

Part V, Validation and Conformance, establishes the three-level evidence taxonomy, the falsifiability requirement, the conformance criteria, and the distinction between implementer self-certification and optional Foundation review.

Part VI, Governance and Evolution, establishes the semantic-versioning scheme, the Request-for-Comments amendment process, and the stability commitments, including the four constitutional commitments.

Part VII, Integration, establishes the alignment with external standards, the regulatory positioning together with the Cognitive Hypervisor and swarm-coordination subsystems, and the identification of the reference implementation.

The five appendices establish a worked worst-case-response-time calculation, the complete error-code table, the Concise Binary Object Representation encoding summary, the reference task set with its worst-case execution times, and the bibliography.

### What `CONFORMANCE.md` establishes

`CONFORMANCE.md` is established in this release with the complete conformance methodology and the fifty-seven-test conformance suite.

The suite is organised into six categories. Category C1, twelve tests, exercises the real-time contract and its underpinnings. Category C2, nine tests, exercises the capability system. Category C3, eight tests, exercises the consent state machine. Category C4, fifteen tests, exercises the wire format. Category C5, ten tests, exercises the error taxonomy. Category C6, three tests, exercises the validation policy by examining the implementation's published claims. Each of the fifty-seven tests is specified in an eight-field format giving its identifier, the requirement it cites, its character as a proof test or a measurement test, the evidence level it produces, its inputs, its pass condition, its evidence artefact, and its blocking status.

`CONFORMANCE.md` also establishes the suite-invocation procedure, the conformance-report and evidence-archive outputs, the optional Foundation-review procedure, and the discipline governing loss and re-attainment of conformance.

### What `VALIDATION.md` establishes

`VALIDATION.md` is established in this release with the complete validation discipline: the three-level evidence taxonomy — L1 formally proven, L2 measured on reference hardware, L3 independently validated; the publishing rule, which forbids any quantitative claim under the AxonOS name that does not carry an evidence level and link to an inspectable artefact; the falsifiability requirement; the forms the evidence artefacts must take; the claims catalogue; the procedure for re-grading and retraction; the bounded-model-checking methodology for L1 evidence; the soak methodology for L2 evidence; and a worked example tracing a single claim through the entire discipline.

### What `GOVERNANCE.md` establishes

`GOVERNANCE.md` is established in this release with the complete governance: the five governance principles; the four constitutional commitments and the exceptional procedure for changing them; the seven-section Request-for-Comments process and its review procedure; the breaking-change procedure; the three-phase transition of authority from the founding maintainer, through a technical steering committee, to a constituted Foundation, with the gates between the phases; the description of the Foundation; and worked examples of the governance in operation.

### What `GLOSSARY.md` establishes

`GLOSSARY.md` is established in this release as the canonical glossary, normative for the meaning of every term it defines, with approximately one hundred and fifty alphabetically ordered terms, each with a definition and many with an informative discussion, together with appendices giving the conceptual map of the term families, the commonly confused term pairs, and the terminology alignment with adjacent standards.

### What the architecture chapters establish

The `architecture/` directory is established in this release with four informative chapters: `kernel.md`, on the real-time microkernel, its three structural commitments, and its measured behaviour; `scheduling.md`, on the Earliest-Deadline-First discipline, the schedulability theory, and the worked worst-case-timing analysis; `capability-system.md`, on the type-versus-flag distinction at the heart of the privacy model; and `consent.md`, on the three-state consent machine, the trusted path, and the terminality of the withdrawn state.

### The load-bearing design decisions established at version 1.0.0

Because version 1.0.0 is the foundation, this release record sets out the design decisions that the release bakes in — the decisions that subsequent revisions, within the major-version line, may not undo, and that an implementer or a reviewer should understand as the fixed points of the Standard. Each is recorded here with its rationale in brief; the full reasoning is in the architecture chapters.

**The worst case is the optimisation target.** Version 1.0.0 establishes that the kernel optimises for a provable, small worst-case response time, not for throughput or average-case latency. This inverts the usual optimisation target of general-purpose software, and it is the decision from which the choice of a deterministic core, the conservative utilisation ceiling, the fixed task set, and the non-blocking inter-process-communication discipline all follow. The rationale is that a brain-computer interface's user experiences the worst case, not the average, as the interface's character, and that a worst-case bound, unlike an average, can underwrite a safety argument.

**The worst-case response time is established by proof, at evidence level L1.** Version 1.0.0 establishes that clause DC1's bound is required at L1 — a machine-checked formal proof over the entire admissible input space — and that a measurement, however extensive, is L2 evidence and cannot discharge an L1 requirement. The rationale is that a measurement samples the input space and the worst case may lie unsampled; only a proof ranges over the whole space.

**The scheduling discipline is Earliest-Deadline-First.** Version 1.0.0 establishes Earliest-Deadline-First as the required discipline, chosen over fixed-priority scheduling for its single, exact, task-count-independent schedulability inequality, which is stable under the revisions the pipeline will undergo.

**The capability is a type, and a prohibited category is a type that does not exist.** Version 1.0.0 establishes the structural privacy model: the capability system makes a permission a type-level token, not a runtime check, and renders the four prohibited categories structurally inaccessible by giving them no type at the application-facing boundary. The rationale is that a structural guarantee, enforced by the compiler before the system runs, eliminates the three weaknesses of a runtime check — that it can be mis-written, that it can be removed, that the data exists to be leaked.

**The capability set is closed at exactly four members.** Version 1.0.0 establishes the closed set of four capabilities. The rationale for closure is that a closed set makes an application's possible accesses enumerable and bounded, which is itself a privacy property; a fifth capability can be added only through the Request-for-Comments process and a future minor version.

**The four prohibited categories are constitutional.** Version 1.0.0 establishes the structural prohibition of raw neural signal, affective state, cognitive profile, and biometric identity as a constitutional commitment, reversible only by the exceptional constitutional-amendment procedure. The rationale is that a user must be able to rely on these prohibitions absolutely, and absolute reliance requires insulation from ordinary amendment.

**Consent is a kernel-level, three-state machine with a terminal withdrawn state.** Version 1.0.0 establishes consent as a kernel-enforced three-state finite-state machine, with the withdrawn state terminal. The rationale for kernel-level enforcement is that consent enforced by the application would depend on the good behaviour of the software the user may be revoking; the rationale for terminality is that a reversible withdrawal is a withdrawal subject to coercion.

**The wire format is a fixed twenty-eight-byte record.** Version 1.0.0 establishes the byte-exact twenty-eight-byte intent-observation record with its fields at defined offsets, and the reserved-field discipline that allows future non-breaking extension. The rationale for the byte-exact specification is that it is the contract across which independently built components must agree, and a divergence of even one byte's offset destroys interoperability silently.

**Every quantitative claim carries an evidence level and an artefact.** Version 1.0.0 establishes the publishing rule as a constitutional commitment. The rationale is that a checkable number is worth more than an unverifiable one, and the discipline makes every AxonOS number checkable.

**The Standard is openly licensed, and the open licence is constitutional.** Version 1.0.0 establishes the release of the normative text under the Creative Commons Attribution-ShareAlike licence, with the open licensing a constitutional commitment so that the right to fork, once granted, cannot be revoked.

### The honest status of forward-looking elements at version 1.0.0

In keeping with the validation discipline's insistence on recording what is true, including the truth of what is not yet accomplished, this release record states plainly the status of the Standard's forward-looking elements.

The **AxonOS Foundation does not yet exist.** Version 1.0.0 places the Standard in Phase A of the governance transition: under the stewardship of its founding maintainer. `GOVERNANCE.md` defines and commits the gated path toward Phase B, a technical steering committee, and Phase C, the constituted Foundation, but at version 1.0.0 neither the committee nor the Foundation has been formed. The transition is a published, committed design, not a present state.

**No claim has been independently validated at evidence level L3.** Version 1.0.0's claims catalogue records the highest evidence level genuinely held for each claim — L1 for the proven bounds, L2 for the measured values — and records no L3 claim, because no genuinely independent reproduction has yet been performed. `VALIDATION.md` Section 5.3 records this absence and identifies the first L3 claim the Project intends to pursue.

**The conformance suite's reference results are the reference implementation's.** Version 1.0.0's conformance regime is defined and the reference implementation passes it; conformance results from independent implementations will be recorded as independent implementations are built and assessed.

These honest statements are part of the release record because the Standard's discipline is to record what is true. A foundational release that presented its aspirations — the Foundation, the L3 evidence, the independent implementations — as accomplishments would have failed, in its own first changelog, the discipline of honest claims the Standard exists to uphold.

### The conformance-suite inventory established at version 1.0.0

For the release record, the complete inventory of the fifty-seven conformance tests established by version 1.0.0 is set out here, each with a one-line statement of what it verifies. The full specification of each test, in the eight-field format, is in `CONFORMANCE.md` Section 5.

Category C1, the real-time contract, twelve tests. C1-T01 verifies the end-to-end worst-case response time bound of one thousand microseconds, by proof, at level L1. C1-T02 verifies the observation-cadence jitter bound, by measurement, at L2. C1-T03 verifies the inter-process-communication slot-latency bound, by proof, at L1. C1-T04 verifies the deadline-miss detection-latency bound, by proof, at L1. C1-T05 verifies graceful degradation under application-core suspension, by measurement, at L2. C1-T06 verifies sensor-reconnection recovery latency, by measurement, at L2. C1-T07 verifies the Earliest-Deadline-First scheduling discipline, by proof. C1-T08 verifies utilisation-ceiling enforcement. C1-T09 verifies admission-control re-validation. C1-T10 verifies the fixed-task-set discipline. C1-T11 verifies the monotonic-clock discipline, by proof. C1-T12 verifies the non-blocking producer discipline, by proof.

Category C2, the capability system, nine tests. C2-T01 verifies that the capability set is exactly the four members. C2-T02 verifies the admissible-bit mask, by proof. C2-T03, C2-T04, and C2-T05 verify the navigation, workload-advisory, session-quality, and artefact-events rate ceilings. C2-T06 verifies runtime rate enforcement. C2-T07 verifies the structural prohibition of the four forbidden categories. C2-T08 verifies manifest signature verification. C2-T09 verifies the manifest field-bound checks.

Category C3, the consent state machine, eight tests. C3-T01 verifies the three states. C3-T02 verifies the withdrawal-transition timing, by proof, at L1. C3-T03 verifies the admissible transitions, by proof. C3-T04 verifies the terminality of the withdrawn state, by proof. C3-T05 verifies the kernel interlock, by measurement, at L2. C3-T06 verifies the trusted-path requirement. C3-T07 verifies idempotent re-application. C3-T08 verifies suspended-state observation suppression.

Category C4, the wire format, fifteen tests. C4-T01 through C4-T04 verify the twenty-eight-byte record size, the field offsets, the little-endian encoding, and round-trip fidelity. C4-T05 through C4-T09 verify rejection of over-length, under-length, non-zero-reserved-field, reserved-flag-bit, and undeclared-kind records. C4-T10 through C4-T12 verify the version handshake on match, on mismatch, and the absence of silent fallback. C4-T13 verifies the confidence fixed-point encoding. C4-T14 and C4-T15 verify sequence-number and timestamp monotonicity.

Category C5, the error taxonomy, ten tests. C5-T01 through C5-T09 verify the emission of each of the nine assigned error codes — version mismatch, capability not declared, rate exceeded, backpressure, consent suspended, consent withdrawn, reserved field, signature invalid, admission refused — in its defined circumstance. C5-T10 verifies the reserved-range discipline, that no error code in the reserved range is ever emitted.

Category C6, the validation policy, three tests. C6-T01 verifies that every published quantitative claim carries an evidence level. C6-T02 verifies that every claim links to its artefact. C6-T03 verifies that every claim is a falsifiable prediction.

### The reference task set and measured results established at version 1.0.0

For the release record, the reference task set established by version 1.0.0, with its worst-case execution times, is as follows. The Kalman-filter state update: eighty microseconds. The finite-impulse-response filter: three hundred and twenty microseconds. The notch filter: forty microseconds. The artefact-rejection stage: fifteen microseconds. The common-spatial-pattern feature extractor: one hundred and sixty microseconds. The linear-discriminant classifier: twenty-five microseconds. The inter-process-communication publication task: two-tenths of a microsecond. Every task has the period four thousand microseconds. The straight-line sum of the worst-case execution times is six hundred and forty point two microseconds, and the total processor utilisation is approximately 0.160, within the default utilisation ceiling of 0.25.

The reference implementation's measured results, established as the version 1.0.0 baseline, are as follows. The end-to-end worst-case response time: proven at level L1 not to exceed one thousand microseconds, and measured over a twelve-hour soak of approximately 10.8 million epochs at a worst observed value of nine hundred and seventy-two microseconds, with zero deadline misses. The observation-cadence jitter: measured at two point one microseconds at one standard deviation. The inter-process-communication slot latency: proven at L1 not to exceed half a microsecond, and measured at two-tenths of a microsecond. These figures are the version 1.0.0 baseline; each is recorded, with its evidence artefact, in the claims catalogue under the validation discipline of `VALIDATION.md`.

### The format of future entries

Version 1.0.0, as the foundational release, has been recorded in full above. Future releases will be recorded more briefly, because they will record incremental change against this foundation rather than re-establishing it. Each future entry will record the version number and date, a summary of the release, and an enumeration of the changes, with each substantive change traceable to the Request-for-Comments document that introduced it. Breaking changes will be clearly marked as such and, per the versioning discipline, will appear only in major-version increments and will be accompanied by a migration document. Patch-level entries will record editorial corrections that change no requirement. The principle governing every future entry is the principle of `GOVERNANCE.md`: every change is public, every change is traceable to its Request for Comments, and the changelog together with the Request-for-Comments archive constitutes the complete and authoritative record of how the Standard evolved from the version 1.0.0 foundation recorded here.

---

*This document is the release record of the AxonOS Standard. The authoritative Standard at any version is the content of the repository at that version's release tag.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
