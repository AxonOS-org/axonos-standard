# Validation — The AxonOS Standard, Version 1.0.0

**Status:** Normative · **Companion to:** `STANDARD.md` · **License:** CC-BY-SA-4.0

**Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

---

## Preface

This document defines the validation discipline of the AxonOS Standard: the framework within which every quantitative claim made under the AxonOS name is graded, evidenced, published, and — when the evidence requires it — retracted. It is the companion to `STANDARD.md` Sections 22 and 23, which establish the evidence taxonomy and the falsifiability requirement; this document elaborates that taxonomy into a complete working discipline, defines the form of the evidence artefacts, sets out the publishing rule that governs what may appear under the AxonOS name, and specifies the procedure for re-grading and retraction.

This document is normative. A claim published under the AxonOS name that violates the discipline defined here is non-conformant with the Standard, and the conformance suite's category C6 tests, defined in `CONFORMANCE.md`, exist precisely to check that an implementation's published claims honour this document.

The document exists because of a specific and corrosive failure mode that the AxonOS Project has set out to avoid. The failure mode is the unevidenced number: the figure that appears on a slide, in a paper's abstract, in a product's marketing, in a README's headline — "sub-millisecond latency," "630 times faster," "zero misses" — with no statement of how it was obtained, no artefact a reader could inspect, no domain over which it is claimed to hold, and no possibility of refutation. Such numbers are not lies, necessarily; they are often true, or true-ish, or true under conditions the author has in mind but has not stated. But they are not *claims* in the sense a rigorous engineering discipline requires, because a claim, properly understood, is a falsifiable prediction backed by an inspectable artefact, and an unevidenced number is neither falsifiable nor backed. The brain-computer-interface field, like many young and commercially energetic fields, is awash in unevidenced numbers, and a reader of the field's literature and marketing cannot easily tell the carefully measured figure from the optimistic guess, because both are presented identically: as a bare number.

The validation discipline is the AxonOS Project's structural defence against contributing to that confusion. It is not a promise to be careful; promises to be careful are themselves unevidenced. It is a mechanical rule — every quantitative claim carries an evidence level and links to an artefact, or it does not appear under the AxonOS name — enforced by a category of the conformance suite. The discipline makes the Project's numbers checkable, and in doing so it makes them worth more: a number that a reader can verify is a number a reader can rely on, and a number a reader cannot verify is, however accurate it happens to be, only a number a reader must take on faith.

A reader who wants the essence of the discipline should read Sections 1 and 2: the three evidence levels and the publishing rule. A reader who must produce or check evidence should read Sections 3 through 5: the artefact forms, the falsifiability requirement, and the claims catalogue. A reader concerned with how the discipline handles error should read Section 6, on re-grading and retraction.

---

## Section 1. The three evidence levels

### 1.1 The taxonomy

`STANDARD.md` Section 22 establishes that every quantitative claim made under the AxonOS name carries an **evidence level**, one of three. This section defines the three levels precisely and states, for each, what claim it licenses, what artefact it requires, and what would falsify a claim made at that level.

**Level L1 — formally proven.** An L1 claim is a bound — an upper bound or a lower bound on some quantity — that has been established by a machine-checked formal proof ranging over the entire admissible input space. The defining property of L1 is universality: the proof does not sample the input space, it covers it, and so an L1 claim is a statement about every admissible input, including inputs never executed and never measured. The artefact an L1 claim requires is the proof itself, in a form a third party can re-check: the harness given to the verification tool, and the tool's transcript reporting success. The falsifier of an L1 claim is a counterexample — a single admissible input for which the bound does not hold — and if the verification tool can produce such a counterexample, the L1 claim is refuted.

**Level L2 — measured on reference hardware.** An L2 claim is a value that has been measured, on the reference hardware, under stated conditions, with the measurement recorded in a published trace. The defining property of L2 is empirical specificity: the claim is a statement about what was observed, on identified hardware, under identified conditions, over an identified duration. An L2 claim is not universal — it does not cover inputs not measured — and it does not pretend to be; it is an honest report of a measurement. The artefact an L2 claim requires is the measurement trace, together with the post-processing that derived the headline figure from the raw trace. The falsifier of an L2 claim is a measurement, performed under the stated conditions on the reference hardware, that contradicts the claimed value.

**Level L3 — independently validated.** An L3 claim is an L2 measurement that has, in addition, been reproduced by an independent third party — a party with no stake in the AxonOS Project — on a separate instance of the reference hardware, and witnessed by a signed report. The defining property of L3 is independence: the claim no longer rests on the Project's own measurement alone but on a reproduction by someone with no incentive to confirm it. The artefact an L3 claim requires is the independent party's signed report, identifying the party, the date, the hardware, the procedure, and the verdict. The falsifier of an L3 claim is a finding, by a competent independent party following the stated procedure, that the measurement does not reproduce.

### 1.2 The levels are monotone

The three levels are monotone in strength: L3 implies L2, and L2 implies that L1 has at least been attempted where L1 is applicable. An L3 claim — independently reproduced — is necessarily also an L2 claim, because the independent reproduction is itself a measurement on reference hardware. An L2 claim about a quantity for which a formal bound is meaningful does not imply an L1 proof exists, but it does imply that the question of an L1 proof has been confronted, because the validation discipline requires, for any quantity the Standard bounds at L1, that the L1 proof be the primary evidence and the L2 measurement a complement to it.

The monotonicity matters for how a claim is labelled. A claim is labelled with the *highest* level its evidence supports. A worst-case response time that has been both proven over the whole input space and measured over a twelve-hour soak is an L1 claim — the L1 proof is the strongest evidence and the label reflects it — and the L2 soak measurement is reported alongside as a complement, a corroboration, an additional reassurance, but not as the claim's primary evidence. A jitter figure that has been measured but, in the nature of jitter, not formally proven is an L2 claim, labelled L2, with no pretence of L1.

### 1.3 What each level may and may not be used to say

The evidence levels are not interchangeable, and the discipline forbids certain substitutions that the field commonly makes.

An L2 measurement **may not** be used to make an L1 claim. This is the most important and most commonly violated rule. A team that has measured a worst-case response time over a soak — even a long soak, even a soak of billions of epochs — and observed a maximum of, say, nine hundred and seventy-two microseconds, **may not** claim a worst-case response time of one millisecond as though it were proven. What the team has is an L2 claim: "over this soak, on this hardware, under these conditions, the maximum observed response time was nine hundred and seventy-two microseconds." That is a true and valuable claim and the team may make it, at L2, with the trace as artefact. What the team may not do is relabel it as a proven bound, because the soak sampled the input space and the worst case may lie in the unsampled remainder. The honest L1 claim requires the proof; the soak, however long, is not the proof.

An L1 proof **may** stand without an L2 measurement, but the discipline recommends against it. A bound proven over the whole input space is, logically, sufficient on its own; the measurement adds nothing to the proof's coverage. But the discipline recommends that an L1 claim be accompanied by an L2 measurement anyway, for two reasons. The measurement corroborates the proof — if the proof and the measurement disagree, something is wrong, and the disagreement is worth discovering. And the measurement guards against the proof being a proof of the wrong thing — a proof can be valid and yet not bound the quantity the reader cares about, if the model the proof ranges over has drifted from the system that actually runs, and a measurement of the real system is a check on that drift.

An L3 claim **may not** be self-certified. The independence is the entire content of L3; a claim of L3 evidence where the "independent" party is the Project itself, or a party the Project controls or pays for a favourable verdict, is not an L3 claim and labelling it L3 is a misrepresentation. The discipline is explicit: at version 1.0.0 the AxonOS Project makes no L3 claim, because no genuinely independent reproduction has yet occurred, and the catalogue of Section 5 records that absence honestly rather than dressing an L2 claim in an L3 label.

---

## Section 2. The publishing rule

### 2.1 The rule

The validation discipline's central operative requirement is the **publishing rule**, and it is stated here in full.

*A quantitative claim MUST NOT appear on any public surface under the AxonOS name unless it satisfies all three of the following. First, it carries an explicit evidence-level tag — L1, L2, or L3 — or, if it is a quantity derived by calculation from other claims, it is explicitly tagged as derived and its input claims are cited. Second, it links to a publicly accessible artefact of the form Section 3 requires for its level, from which a competent reader can re-derive or re-check the claim. Third, it is stated as a falsifiable prediction in the sense of Section 4, with an identifiable falsifier.*

A "public surface under the AxonOS name" includes, without limitation: the project's website; the README and documentation of any repository in the project's organisation; any specification, standard, or companion document; any slide deck, paper, preprint, or article published under the AxonOS name or by the project's maintainers in their capacity as such; and any post, on any platform, made under the AxonOS name. A quantitative claim is any statement asserting a number: a latency, a rate, a count, a percentage, a factor, a bound.

### 2.2 What the rule forbids

The publishing rule forbids, specifically and deliberately, the unevidenced number described in the preface. It forbids the headline figure with no evidence-level tag. It forbids the figure tagged with a level but linking to no artefact, or linking to an artefact that is not publicly accessible — behind a login, behind a payment, in a private repository. It forbids the figure stated so vaguely that no measurement could refute it. Each of these is a number that the reader cannot check, and the rule's purpose is that every number under the AxonOS name be a number the reader can check.

The rule does not forbid being wrong. A claim can satisfy the publishing rule — carry a level, link to an artefact, be falsifiable — and still turn out to be false, because the artefact had a flaw, because the proof's model had drifted, because the measurement was contaminated. That is not a violation of the rule; it is the normal way evidence-based claims fail, and Section 6 defines how the discipline handles it: through honest re-grading and retraction. What the rule forbids is not error but *uncheckability* — the publication of a number that no reader and no future evidence could ever test.

### 2.3 The test of public accessibility

The publishing rule requires the artefact to be "publicly accessible," and that phrase has a precise operational test. An artefact is publicly accessible if a competent technical reader, without registering for an account, without paying, and without any relationship to the AxonOS Project, can retrieve the artefact and, given access to the reference hardware described in the architecture material, re-derive or re-check the claim within one working day.

The "within one working day" clause is not a casual figure. It is the operational definition of the difference between an artefact that genuinely substantiates a claim and an artefact that merely gestures at substantiation. An artefact that a reader could in principle check, but only by reconstructing a measurement environment from scratch over weeks, does not satisfy the rule, because in practice no reader will do that and the claim is therefore, in practice, unchecked. The artefact must be complete enough — the harness, the trace, the post-processing, the procedure — that the check is a working day's effort, not a research project. This is a demanding standard for the artefact, and it is meant to be: the demand on the artefact is what makes the claim's evidence real.

### 2.4 Derived quantities

The publishing rule's first condition admits, alongside the three evidence levels, a fourth tag: **derived**. A derived quantity is a number obtained by calculation from other claims rather than by proof or measurement of its own. The canonical example is the improvement factor: the AxonOS reference kernel's jitter, an L2 measurement, divided by a baseline operating system's jitter, another L2 measurement, yields an improvement factor, and that factor is not itself measured — it is derived by division from two measurements.

A derived quantity is published with the tag "derived" and with its input claims explicitly cited, so that a reader can see both the calculation and the evidence beneath each input. A derived quantity inherits the weakness of its weakest input: an improvement factor derived from two L2 measurements is, at best, as strong as an L2 claim, and it is labelled derived rather than L2 to make clear that it is a calculation, not a measurement, and that its correctness depends on both the inputs and the arithmetic. A derived quantity whose inputs are not cited is a violation of the publishing rule exactly as an untagged measurement would be.

---

## Section 3. The evidence artefacts

This section defines, for each evidence level, the precise form the artefact must take. The publishing rule of Section 2 requires every claim to link to an artefact; this section says what an artefact is.

### 3.1 The L1 artefact: the proof

An L1 claim's artefact is the formal proof, and it comprises three components.

The first component is the **harness**: the formal statement, in the input language of the verification tool, of the property being proven. The harness declares the symbolic inputs — the variables the tool will range over the entire space of — states any assumptions that constrain those inputs to the admissible space, invokes the code under verification, and asserts the property. The harness is the precise, machine-readable expression of what the L1 claim actually claims, and it is the first thing a checker reads, because it tells the checker what was proven.

The second component is the **tool transcript**: the output of the verification tool, run against the harness, reporting either that verification succeeded — the property holds for every admissible input — or that it failed, with a counterexample. For a published L1 claim the transcript reports success; the failing transcript appears only transiently, during development, before the claim is either repaired into truth or abandoned.

The third component is the **tool identification**: the name and version of the verification tool, and enough of the invocation detail — the command, the relevant options, the bounds within which the tool explored — that a checker can re-run the identical verification. The AxonOS reference implementation uses a bounded model checker for its L1 proofs, and the tool identification names that checker and its version, so that a checker can install the same version and reproduce the same transcript from the same harness.

These three components together let a third party re-check an L1 claim without trusting the original run: the checker installs the identified tool, runs it against the published harness, and confirms that the transcript reports success. The check is mechanical and its result does not depend on trusting the AxonOS Project; it depends only on trusting the verification tool, and the verification tool is itself an independently developed, widely used artefact whose trustworthiness is established outside the AxonOS Project entirely.

### 3.2 The L2 artefact: the trace and its post-processing

An L2 claim's artefact comprises two components.

The first is the **measurement trace**: the raw record of the measurement, as captured. For a soak measuring worst-case response time and jitter, the trace is a record, for each of the millions of processing epochs in the soak, of the epoch's response time and the interval since the previous observation. The trace is the raw evidence; it is large, it is detailed, and it is published in full — compressed for size, but complete, not summarised — because a summary is not an artefact a reader can independently re-analyse.

The second is the **post-processing**: the script or procedure that derived the claim's headline figure from the raw trace. If the L2 claim is "the worst observed response time over the soak was nine hundred and seventy-two microseconds," the post-processing is the procedure that took the millions of per-epoch records and computed the maximum. Publishing the post-processing alongside the trace lets a reader confirm not only the raw data but the calculation that turned the raw data into the headline figure — and a surprising fraction of disputes about measured claims turn out, on inspection, to be disputes about the post-processing rather than the data.

The L2 artefact additionally records the **measurement conditions**: the identification of the reference-hardware instance, the configuration under which the measurement ran, the duration of the soak, and the date. The conditions are part of the artefact because an L2 claim is a claim about a measurement under specific conditions, and a reader checking the claim must know what those conditions were in order to reproduce them.

### 3.3 The L3 artefact: the independent report

An L3 claim's artefact is the **signed report of the independent party**. It identifies the party and their affiliation; states the date and the location of the reproduction; identifies the reference-hardware instance the independent party used, which is a separate instance from the Project's own; describes the procedure the independent party followed, which is the procedure the L2 artefact's measurement conditions specify; states the result the independent party observed; and states the party's verdict — reproduced, not reproduced, or reproduced with stated qualifications. The report is signed, cryptographically or by a verifiable equivalent, by the independent party, so that its provenance is established.

At version 1.0.0 of the Standard, the AxonOS Project holds no L3 artefact, because no independent reproduction has yet been performed. Section 5 records this, and the discipline's honesty about it — the refusal to label any claim L3 in the absence of a genuine independent report — is itself a demonstration of the discipline.

---

## Section 4. The falsifiability requirement

### 4.1 The requirement

`STANDARD.md` Section 23 requires every L1 and L2 claim to be a **falsifiable prediction**. This section states what that means operationally.

A claim is a falsifiable prediction if it has three identifiable parts. It has a **domain**: a stated set of inputs, conditions, or circumstances over which the claim is asserted to hold. It has a **property**: a stated, precise predicate that the claim asserts holds over that domain. And it has an **identifiable falsifier**: a clearly describable observation that, if made, would refute the claim.

A claim that has all three parts is falsifiable: a reader knows exactly what the claim asserts, exactly where it asserts it, and exactly what would prove it wrong. A claim missing any of the three is not falsifiable in the sense the discipline requires, and MUST NOT be published under the AxonOS name as though it were a claim.

### 4.2 The falsifier of each evidence level

The identifiable falsifier differs by evidence level, and the difference is instructive.

The falsifier of an **L1 claim** is a counterexample produced by the verification tool: a single admissible input for which the proven property does not hold. An L1 claim's domain is the entire admissible input space, its property is the bound, and its falsifier is one input in that space that violates the bound. If the verification tool, run correctly against a correct harness, produces such a counterexample, the L1 claim is refuted, definitively, by that one counterexample.

The falsifier of an **L2 claim** is a contradicting measurement: a measurement, performed on the reference hardware under the stated conditions, that contradicts the claimed value. An L2 claim's domain is the stated measurement conditions, its property is the claimed value or bound, and its falsifier is a measurement under those same conditions that does not exhibit that value. Note that a measurement under *different* conditions does not falsify an L2 claim — an L2 claim is explicitly conditional on its stated conditions, and a measurement on different hardware, or with a different configuration, is simply a measurement of something else.

The falsifier of an **L3 claim** is a failed independent reproduction: a finding, by a competent independent party following the stated procedure, that the measurement does not reproduce.

### 4.3 Why falsifiability is required

The falsifiability requirement is not philosophical decoration; it has a concrete function. A claim that cannot be falsified cannot be checked, and a claim that cannot be checked provides a reader with no information beyond the bare assertion of the person making it. The requirement that every claim be falsifiable is the requirement that every claim be, in principle, checkable — and the publishing rule's demand for an accessible artefact is the requirement that the check be, in practice, performable. Together, falsifiability and the artefact requirement convert the project's numbers from assertions into evidence: an assertion asks the reader to trust, and evidence invites the reader to verify.

---

## Section 5. The claims catalogue

### 5.1 The catalogue's purpose

The validation discipline requires that the AxonOS Project maintain a **claims catalogue**: a single, public, maintained document that lists every quantitative claim the Project makes under the AxonOS name, and records, for each, the claimed value, the evidence level, and the link to the artefact.

The catalogue exists so that the publishing rule is auditable in one place. Without a catalogue, checking that the Project honours the publishing rule would mean scouring every public surface for every number and checking each individually. With a catalogue, the check has a single locus: a reviewer reads the catalogue, and for each entry confirms that the evidence level is stated, the artefact is linked, the artefact is accessible, and the claim is falsifiable. The conformance suite's category C6 tests, defined in `CONFORMANCE.md`, perform exactly this check against the catalogue.

### 5.2 The catalogue at version 1.0.0

The claims catalogue at version 1.0.0 of the Standard records the following principal claims. Each is stated here with its value and evidence level; the artefact links are maintained in the catalogue file itself in the repository, because links are the kind of thing that is correctly maintained in a versioned file rather than frozen into a standard's prose.

The **end-to-end worst-case response time** is claimed at one thousand microseconds as an upper bound, at evidence level L1, with the bounded-model-checker proof as artefact. The corresponding L2 measurement, reported as a complement, is a worst observed value of nine hundred and seventy-two microseconds over a twelve-hour soak of approximately 10.8 million epochs, with zero deadline misses.

The **observation-cadence jitter** is claimed at two point one microseconds at one standard deviation, at evidence level L2, with the soak trace as artefact.

The **inter-process-communication slot latency** is claimed at half a microsecond as an upper bound at evidence level L1, with the corresponding measured value of two-tenths of a microsecond reported as an L2 complement.

The **consent-withdrawal transition time** is claimed as a bounded number of processor cycles at evidence level L1, with a measured median and worst-observed value over an eighteen-hour soak reported at L2.

The **improvement factor** of the reference kernel's jitter over a baseline general-purpose operating system's jitter on the same hardware is reported as a derived quantity, tagged derived, with both input measurements — the reference kernel's jitter and the baseline's jitter — cited as L2 claims.

### 5.3 The absence of L3 claims at version 1.0.0

The claims catalogue at version 1.0.0 contains **no L3 claim**. This absence is recorded here explicitly, and recorded in the catalogue itself, because the discipline's integrity depends on the absence being visible rather than hidden.

L3 evidence requires an independent reproduction by a party with no stake in the Project, and at version 1.0.0 no such reproduction has occurred. The Project could not honestly label any claim L3, and the discipline forbids it from doing so. The catalogue therefore records the highest evidence level the Project genuinely holds for each claim — L1 for the proven bounds, L2 for the measured values — and records, as a stated item of future work, that the first L3 claim the Project intends to pursue is an independent reproduction of the end-to-end worst-case response time, to be sought in conjunction with the first clinical-pilot deployment, where an independent clinical-engineering party will have both the reference hardware and the motivation to perform the reproduction.

The honest recording of an absence is a small thing, but it is the kind of small thing the whole discipline is built to make habitual. A project that will honestly write "we have no L3 evidence" in its own catalogue is a project whose L1 and L2 labels can be believed, because it has demonstrated that it labels by the evidence and not by the aspiration.

---

## Section 6. Re-grading and retraction

### 6.1 Evidence changes

The evidence behind a claim is not static. New evidence can strengthen a claim, and new evidence can undermine one. The validation discipline defines how the catalogue, and the claims, respond to each.

### 6.2 Upgrading

A claim is **upgraded** when new evidence raises the level its evidence supports. An L2 claim becomes an L1 claim when a formal proof is completed for a quantity previously only measured. An L2 claim becomes an L3 claim when an independent party reproduces the measurement and signs a report. An upgrade is a straightforward and welcome event: the catalogue entry is revised to the new level, the new artefact is linked, and the change is recorded in the Standard's changelog at the next revision. An upgrade requires no retraction and no notice period; it is simply the catalogue catching up with strengthened evidence.

### 6.3 Downgrading and retraction

A claim is **downgraded**, or in the limit **retracted**, when new evidence undermines it. The canonical case is a counterexample to an L1 proof: the verification tool, perhaps run with corrected assumptions, perhaps after a change to the code, produces an input for which the proven bound does not hold. The L1 claim is then false, and the discipline requires a specific, prompt response.

First, **the claim is removed from every public surface within fourteen days** of the undermining evidence being confirmed. The fourteen-day bound is deliberate and short: a false claim that remains published is actively misleading every reader who encounters it in the interim, and the discipline does not permit a leisurely correction. Removal means the claim comes down from the website, the README, the documentation, every surface — not merely that a correction is appended somewhere.

Second, **the downgrade or retraction is recorded** in the Project's public remediation log, with the date, the claim, the undermining evidence, and the action taken. The remediation log is a permanent, public record; a retraction is not quietly absorbed but openly logged, so that the history of what was claimed and what was retracted is available to anyone who wishes to assess the Project's track record.

Third, **the claim is either re-established or permanently abandoned** at the next revision of the Standard. If the undermining evidence revealed a repairable flaw — a proof whose model had drifted, a measurement that had been contaminated — the underlying issue is repaired, the evidence is regenerated, and the claim returns to the catalogue at whatever level the regenerated evidence supports. If the undermining evidence revealed that the claim was simply false — that the bound does not hold and cannot be made to hold — the claim is permanently abandoned, and the catalogue records its abandonment.

### 6.4 Retraction is a normal operation

The discipline states explicitly, and means, that **retraction is a normal scientific operation, not a disgrace**. Every evidence-based discipline retracts; the alternative to retracting a claim shown false is defending a claim shown false, which is the actual disgrace. The validation discipline is designed so that retraction is procedurally smooth — a defined fourteen-day removal, a defined log entry, a defined path to re-establishment or abandonment — precisely so that the Project, faced with evidence against one of its own claims, finds retraction the path of least resistance. A discipline that made retraction painful would incentivise the concealment of undermining evidence; a discipline that makes retraction routine incentivises its honest disclosure. The AxonOS Project commits, through this discipline, to perform retraction openly and promptly whenever the evidence requires it, and regards the willingness to do so as a measure of the discipline's success rather than a sign of its failure.

---

---

## Section 7. The bounded-model-checking methodology for L1 evidence

This section elaborates, in informative depth, how the AxonOS reference implementation produces L1 evidence, so that an implementer can produce L1 evidence of their own and a reviewer can understand what an L1 artefact is the artefact *of*.

### 7.1 What a bounded model checker does

A bounded model checker is a tool that takes a piece of code, a property asserted about that code, and a bound, and exhaustively explores every execution of the code up to the bound, checking whether the property holds on all of them. The word "bounded" refers to the bound on exploration depth — loop iterations, recursion depth, the ranges of symbolic inputs — and the word "model checking" refers to the exhaustive exploration. Within the bound, the exploration is complete: the tool does not sample executions, it considers all of them, and so a property the tool reports as holding holds for every execution within the bound.

The exhaustiveness is what makes the tool a source of L1 evidence. A test runs one execution; a fuzzer runs many executions chosen by a heuristic; a bounded model checker runs, in effect, all executions within the bound at once, by reasoning symbolically about the inputs rather than instantiating them. When the AxonOS verification harness declares an input symbolic, the checker does not pick a value for it; it reasons about all values simultaneously, and a property it proves is proven for all of them.

### 7.2 The role of the bound

The bound is the methodology's central subtlety, and an implementer must understand it to produce sound L1 evidence.

The bound limits exploration depth. A loop is explored up to a stated number of iterations; a symbolic integer is explored over a stated range. The tool's exhaustiveness is exhaustiveness *within the bound*: a property proven with a loop bound of sixteen is proven for executions in which the loop runs at most sixteen times, and says nothing directly about an execution in which the loop runs seventeen times.

For the L1 evidence to be sound, the bound must be chosen so that it covers every admissible execution — so that no admissible execution exceeds the bound. This is why the AxonOS pipeline is built the way it is. The pipeline's loops are bounded loops over fixed-size data: the finite-impulse-response filter convolves against a kernel of fixed length, the channel iteration runs over a fixed channel count, and so each loop has a *known maximum* iteration count, and the verification harness sets the loop bound to that known maximum. The bound is then not an arbitrary limit that might exclude admissible executions; it is the actual maximum, and "proven within the bound" coincides with "proven for every admissible execution." A pipeline with an unbounded loop — a loop whose iteration count depended on runtime data without a known maximum — could not be given a sound bound, and could not be the subject of sound L1 evidence; this is one of the reasons the kernel's design forbids such constructs.

### 7.3 Modelling the machine state

An L1 claim about worst-case response time is a claim not only over the space of inputs but over the space of machine states — cache contents, branch-predictor history, the timing of interrupts. The verification harness must range over those states too, and modelling them is the most specialised part of producing L1 timing evidence.

The AxonOS harness models the adverse machine state conservatively. It assumes, for the cache, the worst case: that every memory access the pipeline makes is a cache miss, paying the full miss penalty. It assumes, for the branch predictor, the worst case: that every branch is mispredicted, paying the full misprediction penalty. It assumes, for interrupts, the maximum admissible rate of each interrupt source, each interrupt stealing the maximum cycles its handler can take. These assumptions make the modelled worst case strictly worse than any real machine state could be — a real run will have some cache hits, some correct branch predictions, fewer interrupts — and so a bound proven against the conservatively modelled state is a valid bound for every real state. The conservatism is what makes the proof's machine-state coverage sound, and the gap between the conservatively modelled worst case and the measured typical case is part of why the L1 bound, one thousand microseconds, sits comfortably above the L2 measured worst, nine hundred and seventy-two.

### 7.4 What an L1 proof does not establish

An implementer must be clear about the limits of an L1 proof, because over-claiming what a proof establishes is itself a validation failure.

An L1 proof establishes that a stated property holds, over a stated input and machine-state space, *of the model the harness presented to the tool*. It does not establish that the model faithfully represents the system that actually runs. If the harness models a pipeline that has since been changed, the proof is valid but irrelevant. If the harness's machine-state model omits a source of interference that the real machine has, the proof is valid but unsound for the real machine. The proof is only as good as the harness's fidelity to reality, and that fidelity is not itself something the tool checks — it is something the implementer is responsible for, and something the L2 measurement, run on the real system, exists to corroborate. This is the deepest reason the discipline recommends an L2 measurement alongside every L1 proof: the measurement is the check on whether the proof's model has drifted from the real system, and a disagreement between a valid proof and a careful measurement is the signal that the model and the system have diverged.

---

## Section 8. The soak methodology for L2 evidence

This section elaborates how the reference implementation produces L2 evidence, the measured-on-reference-hardware claims.

### 8.1 The soak

L2 evidence for the timing claims is produced by a **soak**: a continuous run of the implementation, on the reference hardware, under representative load, for a stated long duration, during which every quantity of interest is recorded for every processing epoch. The DC2 jitter clause requires a soak of at least twelve hours; the consent-withdrawal L2 measurement uses a soak of eighteen hours; the reference implementation's headline worst-case-response-time measurement uses a twelve-hour soak comprising approximately 10.8 million epochs.

The soak's duration is not arbitrary. A soak must be long enough that the quantities it measures have stabilised — that the measured worst case is not still climbing as the soak proceeds, that the measured jitter has converged. Twelve hours, at a 250-hertz epoch rate, is roughly ten million epochs, and ten million epochs is enough that the measured maximum has, in the reference implementation's experience, stabilised: extending the soak further does not raise the measured worst case. The soak duration is chosen to be comfortably past the point of stabilisation, so that the measurement is a measurement of a converged quantity rather than a snapshot of one still settling.

### 8.2 Representative load

A soak measures the implementation under load, and the load must be representative — it must exercise the implementation the way real use would. A soak that ran the pipeline on trivial, easily-classified input would measure an unrealistically favourable case. The reference soak drives the pipeline with input representative of real neural-signal characteristics, including the artefact-laden epochs and the ambiguous epochs that real use produces, so that the measured worst case is a worst case over realistic load.

### 8.3 What the trace records

The soak trace records, for every epoch, the epoch's end-to-end response time and the interval since the previous observation. From the per-epoch response times the post-processing computes the maximum — the worst observed response time — and the count of epochs that missed their deadline. From the per-epoch intervals the post-processing computes the standard deviation — the jitter. The trace is the complete per-epoch record, published in full and compressed, so that a reader can recompute the maximum, the miss count, and the jitter independently, and can also perform analyses the Project did not — examine the distribution's tail, look for periodicity, check for drift over the soak's duration.

### 8.4 The honest reporting of the soak's limits

An L2 claim from a soak is, the discipline insists, reported with its limits visible. The claim is not "the worst-case response time is nine hundred and seventy-two microseconds"; that phrasing borrows the universality of an L1 claim that the soak has not earned. The claim is "over a twelve-hour soak of approximately 10.8 million epochs on the reference hardware under representative load, the worst observed response time was nine hundred and seventy-two microseconds, with zero deadline misses." The longer phrasing is the honest one: it states the domain — this soak, this hardware, this load — and confines the claim to it. The universal claim, the claim over every admissible input, is the L1 claim, and it is the proof, not the soak, that earns it. The soak earns exactly the conditional, measured claim, and the discipline requires that the soak's claim be stated as exactly that and not dressed as more.

---

## Section 9. A worked example of the discipline in operation

*Informative. This section traces a single claim — the worst-case response time — through the entire discipline, to make the abstract machinery concrete.*

Consider the claim that the reference kernel's end-to-end worst-case response time does not exceed one thousand microseconds.

The claim begins as a **requirement**: clause DC1 of the dual-core contract requires the worst-case response time not to exceed one thousand microseconds, and requires it at evidence level L1.

The implementer produces the **L1 evidence**. They construct a verification harness that declares the pipeline's inputs symbolic, constrains them to the admissible space, models the adverse machine state conservatively per Section 7.3, invokes the pipeline, and asserts that the response time does not exceed one thousand microseconds. They run the bounded model checker against the harness. The checker explores the entire symbolic space and reports verification success. The harness, the transcript, and the tool identification become the **L1 artefact**.

The implementer produces the **L2 corroboration**. They run a twelve-hour soak on the reference hardware, recording every epoch's response time. The post-processing computes the worst observed value: nine hundred and seventy-two microseconds, with zero misses. The trace and the post-processing become the **L2 artefact**.

The implementer **publishes** the claim, honouring the publishing rule. On the public surface the claim appears as: "End-to-end worst-case response time: at most one thousand microseconds [L1]" — with the evidence-level tag, and with a link to the L1 artefact. Alongside it: "Worst observed over a twelve-hour soak of approximately 10.8 million epochs: nine hundred and seventy-two microseconds, zero misses [L2]" — the corroborating measurement, separately tagged, separately linked.

The claim enters the **catalogue**: an entry recording the value, the L1 level, the artefact link, and the L2 corroboration.

The claim is now **falsifiable**: a reader who doubts it can retrieve the L1 artefact, install the named checker, run it against the published harness, and either reproduce the success or — if the claim is false — obtain the counterexample. A reader can also retrieve the L2 trace and recompute the worst observed value. The claim is checkable, by anyone, within a working day.

Suppose, later, a revision to the pipeline inadvertently lengthens a filter stage, and a re-run of the verification produces a **counterexample**: an input for which the response time reaches one thousand and forty microseconds. The L1 claim is now false. The discipline's **retraction** procedure engages: within fourteen days the one-thousand-microsecond L1 claim comes down from every public surface; the retraction is logged in the public remediation log with the date, the claim, and the counterexample; and at the next revision the claim is either re-established — the filter stage is re-optimised, the verification re-run, the proof regenerated — or, if the bound genuinely cannot be met, permanently abandoned and the contract clause itself revisited.

That is the discipline in operation: a requirement, evidence at the required level, an accessible artefact, honest publication with the level visible, catalogue registration, genuine falsifiability, and — when the evidence turns — prompt and logged retraction. Every quantitative claim under the AxonOS name travels this path, and the path is what makes the claim worth more than a bare assertion.

---

---

## Section 10. Validation anti-patterns the discipline forbids

*Informative. This section names, concretely, the specific bad practices the discipline is designed to prevent, because naming them makes them recognisable.*

The validation discipline is best understood through the specific failures it exists to forbid. Each of the following is a real and common practice in young engineering fields, each produces a number that looks like evidence but is not, and each is forbidden by the publishing rule.

**The untagged headline.** A figure presented prominently — in a title, an abstract, a marketing headline — with no evidence-level tag and no artefact link. "Sub-millisecond latency." The reader cannot tell whether this is a proven bound, a measured typical value, a measured best case, or an aspiration. The discipline forbids it: the figure carries a tag and a link or it does not appear.

**The measured worst dressed as proven.** A worst-case figure obtained from a soak — even a long soak — and presented as though it were a guaranteed bound. The soak measured the worst of the inputs it ran; the guarantee would require the worst of all admissible inputs; the two are different claims and the discipline forbids conflating them. The soak's honest claim is L2 and conditional; the guaranteed bound is L1 and requires the proof.

**The cherry-picked run.** A single favourable execution, reported as representative. The discipline's requirement that L2 evidence come from a soak of stated duration, with the full trace published, forbids this: a single run is not a soak, and a trace that shows only the favourable run is not the full trace.

**The unreproducible benchmark.** A measurement on hardware that is not the reference hardware, or under conditions not stated, or with the measurement environment not described well enough to reproduce. The discipline's requirement that L2 evidence be measured on the reference hardware, under stated conditions, with the conditions in the artefact, forbids this: a measurement nobody else can reproduce is not L2 evidence.

**The self-certified independence.** An evaluation by a party presented as independent but in fact controlled by, or paid for a favourable verdict by, the party whose claim is evaluated. The discipline's definition of L3 — reproduction by a party with no stake — forbids this, and the discipline's insistence that the Project hold no L3 claim at version 1.0.0, because no genuinely independent reproduction has occurred, is the discipline declining to commit this very anti-pattern.

**The vanishing baseline.** A comparative claim — "ten times faster than the alternative" — where the alternative, the baseline, is not identified, or was measured under conditions favourable to the comparison. The discipline's treatment of comparative figures as derived quantities, requiring both the claim's measurement and the baseline's measurement to be cited as L2 claims with their own artefacts, forbids this: the baseline is a claim too, and it carries the same burden.

**The moving claim.** A figure that is quietly revised when it becomes inconvenient, with no record that it ever held a different value. The discipline's catalogue, versioned with the Standard, and its remediation log, which records every retraction, forbid this: a claim's history is preserved, and a revision is a logged event, not a silent edit.

The discipline does not forbid these practices by exhortation. It forbids them structurally: each of them produces a claim that fails the publishing rule — no tag, no accessible artefact, not falsifiable, not on the reference hardware, baseline uncited — and a claim that fails the publishing rule does not appear under the AxonOS name, and the conformance suite's category C6 checks that it does not.

---

## Section 11. Questions the discipline commonly raises

*Informative.*

**"Is the discipline not enormously burdensome? Every number needs a proof or a soak."**

It is a real cost, and the discipline does not pretend otherwise. But the cost is bounded and it is front-loaded. The proof harnesses, once written, are re-run mechanically on every revision; the soak, once set up, runs unattended. The genuinely new cost is the discipline of not publishing a number until its evidence exists, and that cost is the point: a number not worth the evidence to substantiate is a number not worth publishing, and the discipline simply makes that judgement explicit rather than leaving it to the optimism of a deadline.

**"What about a number that is genuinely hard to evidence — an estimate, a projection?"**

The discipline does not forbid estimates and projections; it forbids presenting them as measurements or proofs. An estimate is published as an estimate, labelled as such, with its basis stated — "projected, on the assumption that the filter stage scales linearly with channel count." The label is honest, the reader knows what they are reading, and the discipline is satisfied. What the discipline forbids is the estimate wearing an L1 or L2 tag it has not earned.

**"Who checks the catalogue?"**

The conformance suite's category C6 tests check it mechanically: that every claim has a tag, that every artefact link resolves, that every claim is falsifiable. Beyond the mechanical check, the catalogue is public, and any reviewer, competitor, regulator, or sceptic may audit it; the discipline's purpose is precisely to make that audit possible, and the audit is most valuable when performed by someone with an incentive to find a flaw.

**"What happens if the Project itself violates the discipline?"**

The Project is bound by the discipline exactly as any implementer is. A quantitative claim published under the AxonOS name in violation of the publishing rule is a non-conformance, and the Project's own published material is subject to the category C6 tests. If the Project violates the discipline, the remedy is the remedy for any non-conformance: the violating claim is corrected or retracted, and the retraction is logged. The discipline binds its author.

---

## Section 12. The discipline applied to this Standard itself

It would be incoherent for a Standard to require an evidence discipline of its implementers while exempting the Standard's own quantitative content. The Standard holds itself to the rule.

Every quantitative claim in `STANDARD.md` — every numerical bound in the dual-core contract, every figure in the appendices, every number in the architecture chapters — is subject to the publishing rule of Section 2 and is recorded, with its evidence level and artefact, in the claims catalogue. The worst-case response time bound of clause DC1 appears in the Standard as a requirement and in the catalogue as an L1 claim with its proof artefact. The reference task set's worst-case execution times in Appendix D appear as L2 claims with their measurement traces. The improvement factor mentioned in the kernel architecture chapter appears as a derived quantity with its two input measurements cited.

The Standard's own numbers are held to exactly the discipline the Standard imposes. This is the demonstration that the discipline is liveable — that a real, substantial body of quantitative engineering content can be produced under the rule that every number carries a level and an artefact — and the demonstration that the Project asks of its implementers nothing it has not first asked of itself. A Standard that demanded evidence of others while publishing bare numbers itself would have refuted its own discipline in the act of stating it. This Standard does not, and the claims catalogue is the standing proof that it does not.

---

**End of VALIDATION.md.**

*This document is normative. Every quantitative claim made under the AxonOS name is subject to the discipline defined here. The conformance suite's category C6 tests check an implementation's adherence to it.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
