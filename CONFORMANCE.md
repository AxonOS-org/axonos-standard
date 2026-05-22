# Conformance — The AxonOS Standard, Version 1.0.0

**Status:** Normative · **Companion to:** `STANDARD.md` · **License:** CC-BY-SA-4.0

**Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

---

## Preface

This document defines how an implementation of the AxonOS Standard is tested for conformance. It defines what it means to be conformant, what the conformance suite consists of, how each of the suite's fifty-seven tests is specified, what evidence artefact each test produces, how the suite is invoked and its results recorded, the optional Foundation-review procedure, and the consequences of a previously conformant implementation losing its conformance.

This document is normative. It is the executable expression of the AxonOS Standard. Where the file `STANDARD.md` defines requirements in prose, this document defines the tests that decide, mechanically and reproducibly, whether an implementation has met them. An implementation is conformant with version 1.0.0 of the AxonOS Standard if and only if it satisfies every applicable normative requirement of `STANDARD.md` and passes the conformance suite defined here.

The relationship between a prose standard and a conformance suite is worth stating carefully at the outset, because it is easy to misunderstand in either of two directions. One misunderstanding holds that the suite *is* the standard — that conformance simply means passing the tests, and the prose is decorative. The opposite misunderstanding holds that the prose is the standard and the suite is a mere convenience — that an implementation which satisfies the prose is conformant whether or not anyone runs a test. Both are wrong, and the truth is a specific middle position. The prose of `STANDARD.md` is the definition of conformance: it is the authoritative statement of what an implementation must do. The suite is the prose made executable: it is a large, carefully constructed, but necessarily finite set of checks, each of which exercises one or more of the prose requirements, and which together provide strong, reproducible, mechanical evidence that the prose requirements are met. The suite is necessary — an implementation that has not passed it has not demonstrated conformance — and it is very nearly sufficient, because it is constructed to exercise every requirement that can be exercised by a test. But it is not *logically* equivalent to the prose, because no finite suite can be equivalent to a body of requirements ranging over an infinite space of behaviours, and so the definition of conformance in Section 1 names both: the prose requirements and the suite.

This document is long because conformance, to be meaningful, must be precise, and precision about fifty-seven distinct tests, each with its inputs, its pass condition, its evidence artefact, and its blocking status, is necessarily verbose. The document is structured so that a reader can take the path their role requires. A reader who wants only the shape of the conformance regime should read Sections 1 through 4: the definition of conformance, the structure of the suite, the test-specification format, and the invocation and reporting procedure. A reader who is implementing the Standard, and who needs to know exactly what each test demands, should read Section 5, which specifies every one of the fifty-seven tests. A reader concerned with the review process and with what happens when conformance is lost should read Sections 6 and 7. Section 8 addresses the stability of the suite itself across revisions of the Standard.

---

## Section 1. What conformance means

### 1.1 The definition

An implementation is **conformant with version 1.0.0 of the AxonOS Standard** if and only if both of the following conditions hold.

The first condition is that the implementation satisfies every normative requirement of `STANDARD.md` — every requirement expressed with the keywords MUST, MUST NOT, REQUIRED, SHALL, or SHALL NOT — that applies to the components the implementation provides.

The second condition is that the implementation passes every applicable blocking test of the conformance suite defined in Section 5 of this document, at the repository tag corresponding to the Standard version claimed.

These two conditions are stated separately and deliberately. The conformance suite is constructed so that passing it is strong evidence of satisfying the normative requirements; the suite is, as the preface said, the requirements made executable. But the suite is not logically equivalent to the requirements. No finite test suite can be equivalent to a body of prose requirements that range over an infinite space of inputs, machine states, and usage sequences. The suite samples that space — densely, deliberately, at the points where requirements are most likely to be violated and where violations are most consequential — but it samples it. An implementation that passed every test in the suite while violating a normative requirement the suite happened not to exercise would not be conformant, because the first condition would fail even though the second held. The suite is a necessary and very strong component of the conformance test; the prose requirements remain the ultimate standard against which conformance is defined.

In practice this distinction rarely bites, because the suite is constructed precisely to leave as little of the requirement space unexercised as a finite suite can. But the distinction is stated because it determines what an implementer's obligation actually is. The obligation is not "pass the tests"; it is "satisfy the Standard, and demonstrate that you have by passing the tests." An implementer who reads a requirement of `STANDARD.md`, notices that no test in Section 5 exercises it, and concludes that the requirement may therefore be ignored, has misunderstood conformance. The requirement binds; the absence of a test for it means only that conformance with that particular requirement rests on the implementer's faithful reading of the prose rather than on a mechanical check.

### 1.2 Conformance is scoped to the components implemented

The AxonOS Standard governs several components: a kernel, a software development kit, a consent subsystem, and — for the deployments that require them — a Cognitive Hypervisor and a swarm-coordination layer. An implementation need not provide every one of these components. A project might implement only a conformant kernel, intending it to be used beneath the reference software development kit. A different project might implement a software development kit in a programming language the reference kit does not support, intending it to be used above the reference kernel. A third might provide a complete stack.

Conformance is assessed against exactly the components an implementation provides, together with the interface contracts those components participate in. An implementation that provides only a kernel is assessed against the kernel requirements of `STANDARD.md`, and against the kernel's side of every interface contract the kernel participates in — the acquisition interface below it, the application binary interface above it, the consent interlock that crosses into it. It is not assessed against requirements that bind only the internal behaviour of a software development kit, because it provides no software development kit.

The conformance suite of Section 5 is organised, through its six categories, so that the subset of tests relevant to a partial implementation can be selected and run. An implementer of a kernel alone runs the real-time-contract tests of category C1 in full, the wire-format tests of category C4 that exercise the kernel's emission of the wire format, the error tests of category C5 that exercise errors the kernel emits, the consent tests of category C3 that exercise the kernel's side of the consent interlock, and the validation-policy meta-tests of category C6. The suite driver, described in Section 4, supports this selective invocation.

### 1.3 Unconditional and conditional conformance

Following `STANDARD.md` Section 4.2, conformance has two grades, and the conformance suite reflects the distinction.

An implementation is **unconditionally conformant** if it satisfies every applicable MUST requirement and every applicable SHOULD requirement of the Standard, and passes every applicable test of the suite, both the blocking tests and the advisory tests.

An implementation is **conditionally conformant** if it satisfies every applicable MUST requirement and passes every applicable blocking test, but departs from one or more applicable SHOULD requirements, which will manifest as the failure of one or more advisory tests.

Both grades are conformant. The distinction exists so that an implementation can describe itself honestly: an unconditionally conformant implementation has met not only the absolute requirements but also the recommendations, while a conditionally conformant one has met the absolute requirements and has, for reasons it should document, departed from one or more recommendations.

The vast majority of the suite's fifty-seven tests are blocking, because the vast majority of the Standard's testable requirements are MUST requirements. A small number of tests are advisory; each such test is identified as advisory in its specification in Section 5. An implementation that fails an advisory test is conditionally conformant. An implementation that fails any blocking test is non-conformant — not conditionally conformant, but non-conformant — and MUST NOT describe itself as conformant at all.

### 1.4 Conformance is always conformance with a specific version

A conformance claim is always a claim about a specific version of the Standard. An implementation conformant with version 1.0.0 makes, by that fact alone, no claim about any other version, past or future. When an implementation publishes a conformance claim it MUST state the version with which it claims conformance, and the conformance suite it runs to substantiate that claim MUST be the suite at the repository tag of the stated version. A bare claim of "AxonOS conformance," with no version, is incomplete; where it appears it should be read as a claim about whatever version was current when the claim was made, and the implementer should be asked to make the version explicit.

---

## Section 2. The structure of the conformance suite

### 2.1 Six categories, fifty-seven tests

The conformance suite for version 1.0.0 of the Standard comprises **fifty-seven tests**, organised into **six categories**. Each category corresponds to a part of `STANDARD.md`, and each test within a category corresponds to one normative requirement or to a small group of closely related normative requirements.

The six categories, with their test counts and the part of the Standard each exercises, are as follows.

**Category C1, the real-time contract**, comprises twelve tests. It exercises the six clauses of the dual-core real-time contract defined in `STANDARD.md` Section 9, and the scheduling, timing-analysis, and execution-model requirements of Sections 6 through 8 and Sections 10 and 11 that underpin those clauses. Its tests are numbered C1-T01 through C1-T12.

**Category C2, the capability system**, comprises nine tests. It exercises the closed capability set, the per-capability rate ceilings, the structural prohibitions on the four forbidden categories of neural data, the manifest format, and manifest verification, as defined in `STANDARD.md` Sections 12 through 14. Its tests are numbered C2-T01 through C2-T09.

**Category C3, the consent state machine**, comprises eight tests. It exercises the three-state consent finite-state machine, the admissible and inadmissible transitions, the timing bound on withdrawal, the trusted-path requirement, and the kernel interlock, as defined in `STANDARD.md` Sections 15 and 16. Its tests are numbered C3-T01 through C3-T08.

**Category C4, the wire format**, comprises fifteen tests. It exercises the application binary interface: the version handshake, the byte-exact intent-observation record, the reserved-field discipline, and the forward- and backward-compatibility rules, as defined in `STANDARD.md` Sections 17 through 19 and Section 21. Its tests are numbered C4-T01 through C4-T15.

**Category C5, the error taxonomy**, comprises ten tests. It exercises the closed enumeration of one-byte error codes and the circumstances in which each MUST be emitted, as defined in `STANDARD.md` Section 20. Its tests are numbered C5-T01 through C5-T10.

**Category C6, the validation policy**, comprises three tests. These three are of a different character from the preceding fifty-four: they do not exercise the implementation's runtime behaviour but examine the implementation's published claims, checking that each quantitative claim carries an evidence level and links to its artefact, as `STANDARD.md` Sections 22 and 23 require. Its tests are numbered C6-T01 through C6-T03.

Twelve, nine, eight, fifteen, ten, and three sum to fifty-seven.

### 2.2 The two evidence characters of tests

The fifty-seven tests are of two characters, distinguished by the kind of evidence each produces and the method by which each reaches its verdict.

A **proof test** reaches its verdict by formal verification. The test is, or it drives, a harness for a bounded model checker or an equivalent formal-verification tool. The tool explores the entire admissible input space of the property under test — symbolically, considering all admissible inputs at once rather than sampling them — and either confirms that the property holds for every one of them or produces a concrete counterexample. A proof test's passing verdict is therefore a machine-checked proof, and the evidence it produces is at evidence level L1 in the sense of `STANDARD.md` Section 22. The properties tested by proof tests are those for which a universal claim over the whole input space is both required and achievable: the worst-case response time, the inter-process-communication latency, the deadline-miss detection latency, the consent state machine's transition properties, the wire decoder's bound checks.

A **measurement test** reaches its verdict by execution. The test runs the implementation — on the reference hardware, or in a specified host environment — applies a stimulus, observes the result, and compares the observed result against the requirement. A measurement test's verdict is therefore an empirical finding, and the evidence it produces is at evidence level L2 for a test that checks a quantitative bound over a soak, or a plain pass-or-fail verdict for a test that checks a structural or behavioural property that is either present or absent. The properties tested by measurement tests are those for which execution is the appropriate evidence: the jitter, which is a statistical property of a long run; the graceful-degradation and reconnection behaviours, which are responses to physical events; the error emissions, which are behavioural; the wire-format round trips, which are structural.

Each test's specification in Section 5 states explicitly which character it is.

### 2.3 The evidence level a test produces and why it matters

For each test, Section 5 states the evidence level the test produces: L1 for a proof test, L2 for a measurement test that checks a quantitative bound over a soak, or a plain pass-or-fail for a measurement test that checks a structural property.

The evidence level a test produces is not a mere annotation; it is itself part of what conformance requires, because `STANDARD.md` Section 9 requires certain real-time-contract clauses to be evidenced at a specific level. Clause DC1, the end-to-end worst-case response time, MUST be evidenced at level L1. This means that the conformance test for DC1 — test C1-T01 — must be a proof test, and that an implementation which had only a measurement of its worst-case response time, however extensive that measurement, would not satisfy DC1. A measurement, by its nature, samples the input space; the worst case may lie in the unsampled remainder; and so a measured worst case is an L2 claim and cannot discharge a requirement stated at L1. The suite respects this throughout: where the Standard requires a clause at L1, the corresponding test is a proof test, and an implementation cannot pass it with measurement evidence alone.

The converse also holds and is equally important. Clause DC2, the jitter, is required by the Standard at level L2, not L1. Jitter is a physical, statistical quantity — the standard deviation of an inter-observation interval over a long run — and the appropriate evidence for it is a measurement over a soak of stated duration. The conformance test for DC2, test C1-T02, is therefore a measurement test, and an implementation satisfies it with an L2 soak trace; a formal proof of a jitter bound would be welcome but is not required, because the Standard does not require DC2 at L1. The suite matches each test's character and evidence level to what the corresponding clause of the Standard actually requires.

---

## Section 3. The test-specification format

Every one of the fifty-seven tests is specified, in Section 5, using the same eight-field format. This section defines the eight fields; Section 5 then applies the format fifty-seven times.

The **identifier** is the stable, permanent name of the test. It has the form of the letter C, followed by the category number, followed by the letter T, followed by the test number within the category, so that for example the first test of the first category is C1-T01. Identifiers are permanent. Once a test has been assigned an identifier, that identifier does not change, even if the test's prose is later clarified or its diagnostic output improved. The permanence of identifiers means that a conformance report, which records results by identifier, remains interpretable indefinitely, and that a discussion of "test C3-T04" refers to the same test this year and next.

The **requirement** field cites the section or sections of `STANDARD.md` whose normative requirements the test exercises. This citation is the link between the executable test and the prose requirement it expresses, and it is what allows a reader to move from a test failure to the requirement that was violated.

The **character** field states whether the test is a proof test or a measurement test, in the sense of Section 2.2.

The **evidence level** field states the level of evidence the test produces: L1 for a proof test, L2 for a measurement test checking a quantitative bound, or pass-or-fail for a measurement test checking a structural property, in the sense of Section 2.3.

The **inputs** field describes the input domain over which the test operates. For a proof test, this is the symbolic domain the verification tool explores — described as a space of values, because the tool considers all of them. For a measurement test, this is the concrete stimulus applied to the implementation.

The **pass condition** field states the falsifiable predicate the test asserts: the precise property that must hold for the test to return a passing verdict. The pass condition is stated as a predicate so that it is unambiguous what would constitute a failure.

The **artefact** field describes what the test produces, both on a passing verdict and on a failing one. On a pass, the artefact is the evidence that substantiates the verdict: the verification transcript for a proof test, the measurement trace for a measurement test. On a fail, the artefact is the diagnostic that localises the failure: the counterexample for a proof test, the violating measurement for a measurement test.

The **blocking field** states whether the test is blocking or advisory, in the sense of Section 1.3. A failed blocking test renders the implementation non-conformant. A failed advisory test renders it conditionally conformant. Unless a test's specification explicitly states that it is advisory, the test is blocking.

---

## Section 4. Invoking the suite and recording the result

### 4.1 The suite driver

The conformance suite is invoked through a driver, a program in the canonical repository's tools directory. The driver is invoked with the path to the implementation under test. It discovers the implementation's commit identifier from the implementation's version-control metadata, determines from the implementation's declared components which categories of tests apply, runs each applicable test, collects each test's verdict and evidence artefact, and assembles the two outputs described in Sections 4.2 and 4.3: the conformance report and the evidence archive.

The driver is structured so that the six categories can be invoked independently. This supports the assessment of partial implementations described in Section 1.2: an implementer of a kernel alone invokes the driver in a mode that runs category C1 in full, runs the kernel-relevant tests of categories C3, C4, and C5, and runs category C6, while skipping the tests that exercise only a software development kit's internals. The driver records, in the report, which tests were run and which were skipped as inapplicable, so that the report is unambiguous about the scope of the assessment.

### 4.2 The conformance report

The driver produces a **conformance report**: a structured document that records, for each test that was run, the test's identifier, the section of `STANDARD.md` it cites, the verdict — pass, fail, or skipped-as-inapplicable — the evidence level the test produced, and a reference to the evidence artefact the test deposited in the archive. The report additionally records, in a header, the version of the Standard against which the assessment was performed, the implementation's commit identifier, and the date and time at which the run was performed.

The report concludes with a summary section recording the total number of tests in the applicable set, the number that passed, the number that failed, the number skipped as inapplicable, and a single Boolean **conformance verdict**. The conformance verdict is true if and only if every applicable blocking test passed and no applicable test was erroneously skipped. An implementation whose report shows a true conformance verdict, with every blocking test passed, is conformant. The report is the primary evidence of conformance, and it is the cryptographic hash of the report that a Foundation review, per Section 6, verifies against the report as submitted, to establish that the report has not been altered between the run and the review.

### 4.3 The evidence archive

Alongside the report, the driver assembles an **evidence archive**: a bundle containing every evidence artefact that every test produced. For each proof test, the archive contains the verification transcript and the harness against which the verification tool was run. For each measurement test, the archive contains the measurement trace and the post-processing script that derived the test's headline figure from the raw trace.

The evidence archive is what makes a conformance claim auditable rather than merely asserted. A third party in possession of the conformance report and the evidence archive can, for any test, retrieve that test's artefact and re-examine it. For a measurement test, the third party can inspect the trace and re-run the post-processing. For a proof test, the third party can re-run the verification tool against the archived harness and re-derive the verdict independently, without trusting the original run. The combination of the report and the archive is therefore a self-contained, independently checkable demonstration of conformance, and it is this combination that an implementer submits when requesting the Foundation review of Section 6.

---

## Section 5. The fifty-seven tests

This section specifies every test in the conformance suite. The tests are presented category by category, and within each category in identifier order. Each test is specified in the eight-field format defined in Section 3. Where several tests within a category share a context, that context is given once in introductory prose and not repeated.

### Category C1 — the real-time contract

The twelve tests of category C1 exercise the dual-core real-time contract of `STANDARD.md` Section 9 and the execution-model, scheduling, timing-analysis, inter-process-communication, and clock requirements of Sections 6 through 8 and 10 and 11 that the contract rests upon. Six of the twelve tests, C1-T01 through C1-T06, correspond one-to-one with the six clauses DC1 through DC6 of the contract. The remaining six, C1-T07 through C1-T12, exercise the requirements that underpin the contract: the scheduling discipline, the utilisation ceiling, the admission-control procedure, the fixed-task-set discipline, the monotonic clock, and the non-blocking producer discipline.

It is worth a word on why the underpinning requirements are tested separately rather than being left implicit in the tests of the six clauses. A kernel could, in principle, pass the test of clause DC1 — exhibit a worst-case response time within the bound — while violating the fixed-task-set discipline, because a particular run of the verification might happen not to exercise a task-set change. The contract clauses and their underpinnings are logically distinct requirements, and a suite that tested only the clauses would leave the underpinnings unverified. The six underpinning tests close that gap: they verify directly that the kernel has the structural properties — the right scheduling discipline, the enforced ceiling, the gated admission control, the fixed task set, the monotonic clock, the non-blocking producer — on which the contract's clauses depend.

**C1-T01 — end-to-end worst-case response time.** *Requirement:* `STANDARD.md` Section 9 clause DC1, and Section 8. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of admissible pipeline inputs together with the symbolic space of admissible machine states, the latter including cold instruction and data caches, adverse branch-predictor history, and the maximum admissible interrupt load. *Pass condition:* for every point in the combined symbolic space, the elapsed time from the start of a processing epoch to the publication of the corresponding intent observation across the application binary interface does not exceed one thousand microseconds. *Artefact:* on a passing verdict, the transcript of the bounded model checker reporting verification success, together with the harness; on a failing verdict, the concrete counterexample input and machine state, and the response time that input induces. *Blocking.*

**C1-T02 — observation-cadence jitter.** *Requirement:* clause DC2. *Character:* measurement test. *Evidence level:* L2. *Inputs:* a continuous soak of the implementation on the reference hardware, of at least twelve hours' duration, during which every intent observation's emission timestamp is recorded. *Pass condition:* the standard deviation of the interval between consecutive observations, evaluated at the three-sigma envelope, does not exceed ten microseconds. *Artefact:* on a pass, the complete soak trace and the statistical post-processing that derived the jitter figure; on a fail, the trace, with the interval or intervals exhibiting the excessive deviation identified. *Blocking.*

**C1-T03 — inter-process-communication slot latency.** *Requirement:* clause DC3, and Section 10. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of channel states, including an empty channel, a full channel, and every degree of partial fill. *Pass condition:* the elapsed time to transmit one intent-observation slot across the shared-memory channel, in one direction, does not exceed half a microsecond, for every channel state. *Artefact:* the verification transcript on a pass, the counterexample channel state on a fail. *Blocking.*

**C1-T04 — deadline-miss detection latency.** *Requirement:* clause DC4. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of task-completion states, including states in which one or more tasks have missed their deadlines. *Pass condition:* for every state in which a task has missed its deadline, the kernel detects that miss within two scheduler ticks of the miss. *Artefact:* the verification transcript on a pass, the counterexample state on a fail. *Blocking.*

**C1-T05 — graceful degradation under application-core suspension.** *Requirement:* clause DC5. *Character:* measurement test. *Evidence level:* L2. *Inputs:* a controlled one-second suspension of the application core, induced on the reference hardware by a mechanism — a debugger halt, a deliberate scheduling stall — that suspends the application core without affecting the signal-processing core. *Pass condition:* across the one-second suspension, the signal-processing core continues to operate and loses no intent observation; every observation produced during the suspension is buffered and delivered on resumption. *Artefact:* the trace covering the suspension interval, showing the observation sequence numbers continuous across it. *Blocking.*

**C1-T06 — sensor-reconnection recovery latency.** *Requirement:* clause DC6. *Character:* measurement test. *Evidence level:* L2. *Inputs:* a disconnection of the acquisition layer, followed after an interval by a reconnection, performed on the reference hardware. *Pass condition:* within one hundred milliseconds of the reconnection, the kernel resumes producing valid intent observations. *Artefact:* the trace covering the disconnect-and-reconnect interval, with the reconnection instant and the first valid post-reconnection observation marked. *Blocking.*

**C1-T07 — the Earliest-Deadline-First scheduling discipline.** *Requirement:* Section 7.1. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of ready-task sets — every combination of tasks that could simultaneously be ready, with every combination of their absolute deadlines. *Pass condition:* at every scheduling decision, the task the scheduler selects to run is the ready task whose absolute deadline is nearest. *Artefact:* the verification transcript on a pass, the counterexample ready-task set on a fail. *Blocking.*

**C1-T08 — utilisation-ceiling enforcement.** *Requirement:* Section 7.3. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a sequence of task-set definitions presented to the kernel, some with total utilisation within the configured ceiling and some exceeding it. *Pass condition:* every task set within the ceiling is admitted and every task set exceeding the ceiling is refused. *Artefact:* the admission log recording the verdict for each presented task set. *Blocking.*

**C1-T09 — admission-control re-validation.** *Requirement:* Section 7.4. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a sequence of runtime task-set-change requests — additions, removals, and parameter changes — presented to the kernel. *Pass condition:* every change request is gated by a re-computation of the post-change utilisation, and any change that would push the utilisation past the ceiling is refused with the admission-refused error of `STANDARD.md` Section 20. *Artefact:* the admission log. *Blocking.*

**C1-T10 — the fixed-task-set discipline.** *Requirement:* Section 6.3. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* three attempts to alter the task set outside the admission-control procedure — an attempt to add a task directly, an attempt to alter an existing task's worst-case execution time directly, and an attempt to alter an existing task's period directly. *Pass condition:* every such attempt is refused; the only path by which the task set changes is the admission-control procedure. *Artefact:* the refusal log. *Blocking.*

**C1-T11 — the monotonic-clock discipline.** *Requirement:* Section 11. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of clock-read sequences. *Pass condition:* no sequence of reads of the monotonic clock returns a value that is less than a previously returned value; the clock is monotonic non-decreasing for every read sequence. *Artefact:* the verification transcript on a pass, the counterexample read sequence on a fail. *Blocking.*

**C1-T12 — the non-blocking producer discipline.** *Requirement:* Section 10.3. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of channel states, including a full channel, considered against the producer's publication code path. *Pass condition:* the producer's publication path contains no operation that can block and no operation that allocates memory from a heap, for any channel state. *Artefact:* the verification transcript on a pass, the counterexample on a fail. *Blocking.*

### Category C2 — the capability system

The nine tests of category C2 exercise the capability system of `STANDARD.md` Sections 12 through 14: the closed four-member capability set, the per-capability rate ceilings, the structural prohibition of the four forbidden categories of neural data, and the manifest format and its verification. The capability system is the Standard's privacy model, and the nine tests are correspondingly careful: they verify not only that the permitted capabilities behave correctly but also, in test C2-T07, that the prohibited categories are genuinely absent.

**C2-T01 — the capability set is exactly the four members.** *Requirement:* Section 12.3. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an enumeration, extracted from the implementation, of every capability the implementation supports. *Pass condition:* the enumeration contains exactly the four capabilities navigation, workload-advisory, session-quality, and artefact-events, and contains nothing else. *Artefact:* the enumeration. *Blocking.*

**C2-T02 — the admissible-bit mask of the capability set.** *Requirement:* Section 14.2. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of all thirty-two-bit capability-set field values. *Pass condition:* a capability-set field with any bit set outside the admissible mask 0x0000000F is refused. *Artefact:* the verification transcript on a pass, the counterexample field value on a fail. *Blocking.*

**C2-T03 — the navigation rate ceiling.** *Requirement:* Sections 12.3 and 12.4. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a manifest declaring the navigation capability together with a maximum-rate field exceeding fifty hertz. *Pass condition:* the manifest is refused at installation time. *Artefact:* the refusal record. *Blocking.*

**C2-T04 — the workload-advisory rate ceiling.** *Requirement:* Sections 12.3 and 12.4. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a manifest declaring the workload-advisory capability together with a maximum-rate field exceeding one hertz. *Pass condition:* the manifest is refused. *Artefact:* the refusal record. *Blocking.*

**C2-T05 — the session-quality and artefact-events rate ceilings.** *Requirement:* Sections 12.3 and 12.4. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a manifest declaring the session-quality capability above two hertz, and a manifest declaring the artefact-events capability above ten hertz. *Pass condition:* both manifests are refused. *Artefact:* the two refusal records. *Blocking.*

**C2-T06 — runtime rate enforcement.** *Requirement:* Section 12.4. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a software development kit requesting intent observations at a rate exceeding the maximum rate its manifest declared. *Pass condition:* the kit receives the rate-exceeded error of `STANDARD.md` Section 20, and does not receive observations beyond its declared rate. *Artefact:* the error log and the observation-rate trace. *Blocking.*

**C2-T07 — the structural prohibition of the four forbidden categories.** *Requirement:* Section 13.2. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an enumeration of every type and every interface the implementation exposes across the application binary interface. *Pass condition:* no type and no interface in the enumeration exposes raw neural signal, affective state, cognitive profile, or biometric identity; the four forbidden categories have no representation that can cross the kernel boundary. *Artefact:* the enumeration together with the analysis that confirms the absence. *Blocking.*

**C2-T08 — manifest signature verification.** *Requirement:* Section 14.3. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a manifest bearing a valid signature, and an otherwise-identical manifest bearing an invalid signature. *Pass condition:* the validly signed manifest is accepted and the invalidly signed manifest is refused with the signature-invalid error. *Artefact:* the verification log for both manifests. *Blocking.*

**C2-T09 — manifest field-bound checks.** *Requirement:* Section 14.3. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* three manifests, each violating one field bound: one with an application identifier exceeding sixty-four bytes, one with a reserved bit set in the capability-set field, and one with a maximum-rate field exceeding the smallest rate ceiling among the capabilities it declares. *Pass condition:* all three manifests are refused. *Artefact:* the three refusal records. *Blocking.*

### Category C3 — the consent state machine

The eight tests of category C3 exercise the consent state machine of `STANDARD.md` Sections 15 and 16: the three states, the transition graph, the timing of withdrawal, the terminality of the withdrawn state, the kernel interlock, the trusted-path requirement, idempotency, and the suppression of observations in the suspended state. Consent is the Standard's mechanism for honouring a user's revocation, and the eight tests verify both the functional correctness of the state machine and the timing of the safety-critical withdrawal transition.

**C3-T01 — the three states.** *Requirement:* Section 15. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an enumeration, extracted from the implementation, of the consent states the implementation models. *Pass condition:* the implementation models exactly the three states granted, suspended, and withdrawn. *Artefact:* the enumeration. *Blocking.*

**C3-T02 — the withdrawal-transition timing.** *Requirement:* Section 15, the withdrawal timing bound. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of starting consent states together with the symbolic space of well-formed withdrawal events. *Pass condition:* for every starting state and every well-formed withdrawal event, the consent-transition function completes within the bounded number of processor cycles the Standard specifies. *Artefact:* the verification transcript on a pass, the counterexample on a fail. *Blocking.*

**C3-T03 — the admissible transitions.** *Requirement:* Section 15, the transition graph. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of from-state and to-state pairs. *Pass condition:* exactly the admissible transitions of the graph are accepted, and exactly the inadmissible transitions — the transition from withdrawn to granted and the transition from withdrawn to suspended — are refused. *Artefact:* the verification transcript on a pass, the counterexample pair on a fail. *Blocking.*

**C3-T04 — the terminality of the withdrawn state.** *Requirement:* Section 15, the non-reversibility of withdrawn. *Character:* proof test. *Evidence level:* L1. *Inputs:* the symbolic space of event sequences applied to a consent machine that is in the withdrawn state. *Pass condition:* no sequence of events, however long, drives the machine out of the withdrawn state; the withdrawn state is terminal under every event sequence. *Artefact:* the verification transcript on a pass, the counterexample event sequence on a fail. *Blocking.*

**C3-T05 — the kernel interlock.** *Requirement:* Section 15, the consent interlock with the kernel publication path. *Character:* measurement test. *Evidence level:* L2. *Inputs:* a withdrawal of consent performed during an active intent-observation stream, on the reference hardware. *Pass condition:* the observation stream terminates within the ten-millisecond wall-clock bound the Standard specifies for withdrawal. *Artefact:* the trace covering the withdrawal, with the withdrawal instant and the final observation marked. *Blocking.*

**C3-T06 — the trusted-path requirement.** *Requirement:* Section 16. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a consent event submitted to the kernel from an application-layer source rather than from the trusted path. *Pass condition:* the event is refused; an application-layer source cannot effect a consent transition. *Artefact:* the refusal record. *Blocking.*

**C3-T07 — idempotent re-application.** *Requirement:* Section 15, the idempotency requirement. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a consent event that re-applies the consent machine's current state. *Pass condition:* the event succeeds, leaves the state unchanged, raises no error, and completes within the same timing bound as a non-trivial transition. *Artefact:* the transition log. *Blocking.*

**C3-T08 — suspended-state observation suppression.** *Requirement:* Section 15, the effect of the suspended state. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an active observation request issued while the consent machine is in the suspended state. *Pass condition:* no intent observation flows to the consumer, and the consumer receives the consent-suspended error. *Artefact:* the error log.* Blocking.*

### Category C4 — the wire format

The fifteen tests of category C4 exercise the application binary interface: the handshake, the byte-exact intent-observation record, the reserved-field discipline, and the compatibility rules. The wire format is the interface across which the kernel and the software development kit must agree byte for byte, and a divergence of even one byte's offset or one bit's meaning destroys interoperability silently; the fifteen tests are correspondingly thorough.

**C4-T01 — the record is exactly twenty-eight bytes.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an intent observation constructed by the implementation and serialised to wire form. *Pass condition:* the serialised record is exactly twenty-eight bytes. *Artefact:* the hex dump of the record. *Blocking.*

**C4-T02 — the field offsets.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an intent observation with each field set to a distinctive constant, serialised. *Pass condition:* each field appears at exactly the byte offset Section 19 specifies — kind at offset zero, flags at one, confidence at two, timestamp at four, sequence number at twelve, source node identifier at twenty, reserved at twenty-four. *Artefact:* the annotated hex dump. *Blocking.*

**C4-T03 — little-endian encoding.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an intent observation whose multi-byte fields hold values whose byte order is observable. *Pass condition:* every multi-byte field is encoded little-endian. *Artefact:* the hex dump. *Blocking.*

**C4-T04 — round-trip fidelity.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an intent observation, serialised and then deserialised. *Pass condition:* the deserialised observation equals the original bit for bit. *Artefact:* the comparison record. *Blocking.*

**C4-T05 — rejection of an over-length record.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a twenty-nine-byte buffer presented to the deserialiser. *Pass condition:* the deserialiser rejects it. *Artefact:* the rejection record. *Blocking.*

**C4-T06 — rejection of an under-length record.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a twenty-seven-byte buffer presented to the deserialiser. *Pass condition:* the deserialiser rejects it. *Artefact:* the rejection record. *Blocking.*

**C4-T07 — rejection of a non-zero reserved field.** *Requirement:* Section 19, 21. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a twenty-eight-byte record with a non-zero value in the reserved field at offset twenty-four. *Pass condition:* the deserialiser rejects it and terminates the connection. *Artefact:* the rejection record. *Blocking.*

**C4-T08 — rejection of a reserved flag bit.** *Requirement:* Section 19, 21. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a record with one of the reserved flag bits, bits one through seven of the flags byte, set. *Pass condition:* the deserialiser rejects it. *Artefact:* the rejection record. *Blocking.*

**C4-T09 — rejection of an undeclared kind.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a record whose kind discriminant corresponds to a capability the consuming application did not declare. *Pass condition:* the consumer rejects the record and terminates the connection. *Artefact:* the rejection record. *Blocking.*

**C4-T10 — the version handshake on match.** *Requirement:* Section 18. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a connection between a kernel and a software development kit declaring the same application-binary-interface version. *Pass condition:* the handshake succeeds and the connection proceeds. *Artefact:* the handshake log. *Blocking.*

**C4-T11 — the version handshake on mismatch.** *Requirement:* Section 18. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a connection between counterparts declaring differing versions. *Pass condition:* the handshake fails, both sides terminate the connection, and the version-mismatch error is reported. *Artefact:* the handshake log. *Blocking.*

**C4-T12 — no silent version fallback.** *Requirement:* Section 18. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a connection between counterparts declaring differing versions where one side could, in principle, operate at the other's version. *Pass condition:* the connection nonetheless fails; the implementation does not fall back or negotiate. *Artefact:* the handshake log. *Blocking.*

**C4-T13 — the confidence fixed-point encoding.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* intent observations whose confidence field is set to several values across the representable range. *Pass condition:* the confidence field is encoded as a Q1.15 fixed-point fraction and decodes to the original value within the encoding's precision. *Artefact:* the encode-decode comparison. *Blocking.*

**C4-T14 — sequence-number monotonicity.** *Requirement:* Section 19. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a stream of consecutive intent observations. *Pass condition:* the sequence numbers begin at zero and increase by exactly one per observation, with no gaps. *Artefact:* the sequence-number trace. *Blocking.*

**C4-T15 — timestamp monotonicity.** *Requirement:* Section 19, Section 11. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a stream of consecutive intent observations. *Pass condition:* the timestamps are strictly increasing. *Artefact:* the timestamp trace. *Blocking.*

### Category C5 — the error taxonomy

The ten tests of category C5 exercise the closed enumeration of error codes. There is one test for each of the nine assigned codes that an implementation can be made to emit under test conditions, plus one test for the reserved-range discipline.

**C5-T01 — version-mismatch error.** *Requirement:* Section 20, code 0x01. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a version-mismatched handshake. *Pass condition:* error code 0x01 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T02 — capability-not-declared error.** *Requirement:* Section 20, code 0x02. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an application request for an observation of an undeclared capability. *Pass condition:* error code 0x02 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T03 — rate-exceeded error.** *Requirement:* Section 20, code 0x03. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an observation request exceeding the declared rate. *Pass condition:* error code 0x03 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T04 — backpressure error.** *Requirement:* Section 20, code 0x04. *Character:* measurement test. *Evidence level:* L2. *Inputs:* a consumer deliberately slowed until the inter-process-communication channel fills, on the reference hardware. *Pass condition:* error code 0x04 is emitted and no observation is silently dropped. *Artefact:* the trace covering the channel-full interval. *Blocking.*

**C5-T05 — consent-suspended error.** *Requirement:* Section 20, code 0x05. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an observation request while consent is suspended. *Pass condition:* error code 0x05 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T06 — consent-withdrawn error.** *Requirement:* Section 20, code 0x06. *Character:* measurement test. *Evidence level:* L2. *Inputs:* a withdrawal of consent during an active stream, on the reference hardware. *Pass condition:* error code 0x06 is emitted within the ten-millisecond wall-clock bound of the withdrawal. *Artefact:* the trace covering the withdrawal. *Blocking.*

**C5-T07 — reserved-field error.** *Requirement:* Section 20, code 0x07. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a wire-format record violating a reserved-field or reserved-bit requirement. *Pass condition:* error code 0x07 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T08 — signature-invalid error.** *Requirement:* Section 20, code 0x08. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a manifest with an invalid signature. *Pass condition:* error code 0x08 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T09 — admission-refused error.** *Requirement:* Section 20, code 0x09. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* a task-set-change request that would exceed the utilisation ceiling. *Pass condition:* error code 0x09 is emitted. *Artefact:* the error log. *Blocking.*

**C5-T10 — the reserved-range discipline.** *Requirement:* Section 20, codes 0x10 through 0xFE. *Character:* measurement test. *Evidence level:* pass-or-fail. *Inputs:* an exhaustive observation of every error the implementation emits across the whole conformance run. *Pass condition:* no error code in the reserved range 0x10 through 0xFE is ever emitted. *Artefact:* the aggregated error log. *Blocking.*

### Category C6 — the validation policy

The three tests of category C6 are of a different character from the preceding fifty-four. They do not exercise the implementation's runtime behaviour at all; they examine the implementation's *published material* — its website, its documentation, its repository — and check that the implementation honours the validation-policy requirements of `STANDARD.md` Sections 22 and 23. They are described as meta-tests because their subject is not the software but the claims made about the software.

**C6-T01 — every quantitative claim carries an evidence level.** *Requirement:* Section 22. *Character:* measurement test, applied to published material. *Evidence level:* pass-or-fail. *Inputs:* the complete set of quantitative claims made under the AxonOS name across the implementation's published surfaces. *Pass condition:* every such claim carries one of the evidence-level tags L1, L2, or L3, or is explicitly tagged as a derived quantity with its inputs cited. *Artefact:* the claims catalogue with the evidence-level annotation of each. *Blocking.*

**C6-T02 — every claim links to its artefact.** *Requirement:* Section 22. *Character:* measurement test, applied to published material. *Evidence level:* pass-or-fail. *Inputs:* the claims catalogue of C6-T01. *Pass condition:* every L1 and L2 claim links to a publicly accessible artefact — a proof transcript for an L1 claim, a measurement trace for an L2 claim — from which the claim can be re-derived. *Artefact:* the catalogue with each artefact link verified reachable. *Blocking.*

**C6-T03 — every claim is falsifiable.** *Requirement:* Section 23. *Character:* measurement test, applied to published material. *Evidence level:* pass-or-fail. *Inputs:* the claims catalogue of C6-T01. *Pass condition:* every L1 and L2 claim is stated as a falsifiable prediction, with a stated input domain, a stated property, and an identifiable falsifier. *Artefact:* the catalogue with the falsifier of each claim identified. *Blocking.*

---

## Section 6. Foundation review

### 6.1 The purpose of Foundation review

An implementer who has run the conformance suite and obtained a report with a true conformance verdict has **self-certified**. Self-certification is a real and sufficient basis for a conformance claim: the suite is the executable expression of the Standard, and an implementation that passes it, run honestly, is conformant.

A **Foundation review** is an optional additional step. It is not a higher grade of conformance — a self-certified conformant implementation and a Foundation-reviewed conformant implementation are equally conformant — but it is an independent confirmation, by the AxonOS Project, that the self-certification was performed correctly and that its evidence is sound. An implementer requests a Foundation review when they want that independent confirmation: typically because a customer, a regulator, or a partner places weight on it.

### 6.2 The review procedure

An implementer requests a Foundation review by submitting three things to the Project: the conformance report produced by the suite driver, the evidence archive of every test's artefact, and a signed declaration of conformance.

The review proceeds in four steps. First, the Project verifies that the submitted conformance report's hash matches the report as submitted, establishing that the report has not been altered since the run. Second, the Project re-runs a randomly chosen sample of at least ten per cent of the measurement tests, on its own instance of the reference hardware, and confirms that the verdicts reproduce. Third, the Project examines the evidence artefacts of the proof tests, re-running the verification tool against the archived harnesses to confirm that the L1 proofs re-derive. Fourth, the Project examines the claims catalogue against the C6 meta-tests.

The review concludes, within thirty days of a complete submission, with one of three verdicts: **acknowledged**, meaning the review confirmed the self-certification without reservation; **acknowledged with notes**, meaning the review confirmed conformance but identified matters the implementer should address; or **declined**, meaning the review could not confirm the self-certification, with the reasons stated.

### 6.3 What Foundation review does not do

A Foundation review certifies **software conformance with this Standard**. It does not certify a **device**. It does not constitute, and MUST NOT be represented as constituting, a regulatory clearance, a medical-device certification, a safety certification, or any approval by any governmental or regulatory body. A device built on a Foundation-reviewed conformant implementation is subject to the full regulatory regime of every jurisdiction in which it is deployed, exactly as it would be without the review. The review's scope is precisely and only the question of whether the software conforms to this Standard, and the implementer MUST NOT represent it as answering any larger question.

---

## Section 7. Loss of conformance

### 7.1 How conformance is lost

An implementation that was conformant ceases to be conformant if a later revision of the implementation introduces a change that violates a normative requirement or causes a previously passing blocking test to fail. This can happen through an ordinary regression, through a refactoring that inadvertently changes a wire format or a timing characteristic, or through a deliberate change made without re-running the suite.

### 7.2 The implementer's obligation on loss of conformance

When an implementation loses conformance, the implementer has exactly two honest courses, and MUST take one of them.

The first course is to **repair the regression** before the next public release, re-run the suite, confirm a true conformance verdict, and release the repaired, conformant implementation. This is the preferred course.

The second course, if repair before the next release is not possible, is to **cease describing the affected release as conformant**: to remove the conformance claim from the release's published material, to refrain from using the AxonOS name in any way that implies conformance for that release, and to document the loss of conformance in the release notes so that the release's users are not misled.

Continuing to describe a non-conformant release as conformant is a misrepresentation. It misleads the release's users about a property — conformance — that they may be relying on for safety or for interoperability, and it is a violation of the trademark terms set out in the Project's legal material. The AxonOS Project, on becoming aware of such a misrepresentation, will record it in the Project's public remediation log and, if a Foundation review had previously acknowledged the implementation, will withdraw that acknowledgement.

### 7.3 Re-attaining conformance

An implementation that lost conformance re-attains it by the ordinary route: it is repaired, the suite is re-run, a true conformance verdict is obtained, and the conformance claim is — honestly, now — re-published. There is no penalty period and no obstacle beyond the work of repair; the Standard's interest is in the accuracy of conformance claims, not in punishing the implementers who, inevitably and like all engineers, sometimes ship a regression. An implementer who loses conformance, says so honestly, repairs the implementation, and re-certifies has behaved exactly as the Standard intends.

---

## Section 8. The stability of the conformance suite

The conformance suite is itself versioned, with the Standard. A test in the version-1.0.0 suite does not change its pass condition without a Request for Comments amending this document; only a test's prose, its diagnostic messages, or its evidence-artefact format may be revised at patch granularity, and only in ways that do not change which implementations pass.

If a defect is discovered in a test — a test that passes an implementation it should fail, or fails one it should pass — the defect is corrected at patch granularity, with a note in the Standard's changelog. Re-running the corrected suite against previously certified implementations is required only if the defect would have changed their verdict; a defect whose correction changes no verdict is a clarification, and prior certifications stand.

A minor-version revision of the Standard may add tests, to exercise newly added requirements. A major-version revision may add, remove, or restructure tests, to track the breaking changes a major revision is permitted to make. In every case the suite's evolution follows the Standard's evolution, through the same governance process, so that the suite is always the executable expression of the Standard at the corresponding version.

---

**End of CONFORMANCE.md.**

*This document is normative. It is the executable expression of the AxonOS Standard. An implementation is conformant with version 1.0.0 if and only if it satisfies the normative requirements of `STANDARD.md` and passes the fifty-seven tests specified here.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
