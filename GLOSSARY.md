# Glossary — The AxonOS Standard, Version 1.1.0

**Status:** Normative for the meaning of every term it defines · **Companion to:** `STANDARD.md` · **License:** CC-BY-SA-4.0

**Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

---

## Preface

This document is the canonical glossary of the AxonOS Standard. It is **normative** for the meaning of every term it defines: where this glossary and any other AxonOS document use the same term, this glossary governs the term's meaning, and where another document's prose appears to use a defined term in a sense at variance with the definition here, the definition here is authoritative and the other document should be read as if it had used the term in this glossary's sense.

The glossary serves three purposes. First, it fixes meaning: a standard whose terms drift in meaning between sections, or between the standard and its companions, is a standard whose requirements cannot be relied upon, and a single canonical glossary is the discipline against that drift. Second, it serves the reader: a reader encountering an unfamiliar term, or an apparently familiar term used in a domain-specific way, has one place to resolve it. Third, it serves alignment: where the AxonOS terminology touches the terminology of adjacent standards — the draft unified terminology for brain-computer interfaces being developed in the relevant standards body, the established vocabulary of real-time systems, the established vocabulary of cryptography — this glossary records the relationship, so that a reader moving between AxonOS and those adjacent bodies of work carries the correct correspondences.

Each entry has a headword, in bold, and a definition. Many entries additionally have a discussion paragraph, set after the definition, which is informative: it elaborates, gives the rationale for the term's particular meaning, notes relationships to other terms, or warns of a common confusion. The definition is normative; the discussion is informative. Where an entry cites a section, the citation is to `STANDARD.md` unless another document is named.

The entries are ordered alphabetically by headword. A reader looking for a term should expect to find it under the noun phrase by which it is most naturally named: "worst-case response time" under W, "capability" under C, "Earliest-Deadline-First scheduling" under E.

---

## A

**Acquisition interface.** The interface across which digital samples pass from the acquisition layer to the kernel. The acquisition interface is required, by Section 10.5, to deliver samples with deterministic completion semantics: delivery is by a direct-memory-access channel whose completion is signalled to the kernel by an interrupt at a known, bounded latency.

*Discussion.* The acquisition interface is one of the four interfaces at which the AxonOS architecture defines a contract — the others being the application binary interface, the consent interlock, and the typed observation interface. The acquisition interface's contract is deliberately minimal: it constrains the *completion semantics* of sample delivery, because those semantics enter the kernel's timing analysis, and it constrains nothing else, because nothing else about the acquisition layer is the Standard's concern.

**Acquisition layer.** The lowest of the four layers of the reference architecture (Section 5.3): the analog front end, the analog-to-digital converter, and any pre-kernel signal conditioning. The acquisition layer converts a physiological signal into a stream of digital samples and delivers that stream to the kernel across the acquisition interface.

*Discussion.* The acquisition layer's internal design — the electrode array, the amplifier, the converter — is outside the Standard's normative scope (Section 1.3). What the Standard governs is only the layer's contract at the kernel boundary. An implementer may build the acquisition layer in any way that honours that boundary contract.

**Admissible input.** An input that lies within the space of inputs a component is required to handle correctly. The worst-case response time (which see) is a maximum over all admissible inputs; a formal proof at evidence level L1 ranges over the entire space of admissible inputs.

*Discussion.* The qualifier "admissible" matters. A component is not required to behave correctly on inputs outside its admissible space — a wire-format record of the wrong length, for instance, is not an admissible input to the deserialiser, and the deserialiser's required behaviour on it is to reject it, not to process it. The admissible space is part of every contract: it states what range of inputs the contract's guarantees cover.

**Admission control.** The procedure, required by Section 7.4, that gates any runtime change to the kernel's task set. Admission control computes the total processor utilisation the task set would have after the proposed change and permits the change only if that post-change utilisation does not exceed the configured utilisation ceiling.

*Discussion.* Admission control is the single permitted exception to the fixed-task-set discipline (which see). It exists so that the task set *can* change — the pipeline is not frozen forever — while ensuring that it never changes into a configuration whose timing has not been re-validated. A change that would breach the ceiling is refused with the admission-refused error.

**Affective state.** A representation of a user's emotional state. Affective state is one of the four structurally prohibited categories of neural data (Section 13.2): the AxonOS Standard provides no capability, type, or interface that exposes an affective-state estimate to the application layer.

*Discussion.* The prohibition exists because a continuously available affective-state estimate, in the hands of a party whose interests diverge from the user's, is an instrument of manipulation: it permits persuasion, pricing, and demands to be timed to the user's moments of greatest vulnerability. The Standard's view, stated in Section 13.3, is that there is no use of such an estimate reliably in the user's interest, and the category is therefore prohibited rather than merely access-controlled.

**Application.** End-user software that consumes intent observations and acts upon them. The application is the highest of the four architectural layers (Section 5.3). It is constrained by the Standard only at two interfaces: it must ship a conformant manifest declaring its capabilities, and it must behave correctly on receipt of the consent-related and rate-related error codes.

*Discussion.* The application layer is, by design, almost entirely outside the Standard's scope. The Standard governs the substrate beneath the application and the contract at the application's lower boundary; what the application *does* with the intent observations it receives — the user interface it presents, the task it accomplishes — is the application author's concern.

**Application binary interface.** Abbreviated ABI. The byte-exact, version-tagged contract at the boundary between the software development kit and the kernel, comprising the version handshake (Section 18), the intent-observation wire format (Section 19), and the error taxonomy (Section 20). The current version is 1.

*Discussion.* The application binary interface is the interface across which two independently built components — a kernel and a software development kit, possibly from different implementers, in different languages — must agree to the byte. Its precise specification is what makes a kernel from one implementer interoperable with a software development kit from another.

**Application core.** The processor core that runs the application and the software development kit (Section 6.1). In the reference hardware it is a Cortex-A53 at 1.2 gigahertz or above, running a general-purpose operating system. The application core is fast but not deterministic, and bears no real-time guarantee.

*Discussion.* The application core's non-determinism is acceptable because the application core's work is soft-real-time at worst, and is required, by the architecture, to be contained: nothing the application core does may delay the signal-processing core. See *bridge* and *containment of non-determinism*.

**Artefact (evidence).** A publicly accessible object — a proof transcript, a measurement trace, an independent report — that substantiates a quantitative claim and from which a competent reader can re-derive or re-check the claim. The validation discipline (`VALIDATION.md`) requires every quantitative claim under the AxonOS name to link to an artefact.

*Discussion.* The artefact is what distinguishes a claim from an assertion. An assertion asks to be believed; a claim with an artefact invites verification. The forms the artefact takes at each evidence level are defined in `VALIDATION.md` Section 3.

**Artefact (signal).** A non-neural disturbance contaminating a biosignal recording: a muscle movement, an electrode disturbance, an electrical interference. The pipeline's artefact-rejection stage identifies epochs corrupted by such disturbances, and the artefact-events capability lets an application observe that an artefact has been detected or has cleared.

*Discussion.* The two senses of "artefact" — an evidence artefact and a signal artefact — are unrelated, and the glossary separates them. Context disambiguates: an evidence artefact is something a claim links to; a signal artefact is something the pipeline detects.

**Artefact-events capability.** One of the four capabilities of the closed capability set (Section 12.3). It authorises edge-triggered observations that a signal artefact has been detected or has cleared. Its maximum observation rate is 10 hertz.

---

## B

**Backpressure.** The condition in which the consumer of the inter-process-communication channel is too slow to keep pace with the producer, and the channel fills. The kernel reports backpressure to the software development kit as error code 0x04 (Section 20).

*Discussion.* Backpressure is a normal, expected condition, not a fault: the application core is non-deterministic and may, transiently, fall behind. The discipline is that backpressure is *reported*, as a typed error, rather than resolved by silently dropping observations; the application then knows it has missed observations and can respond appropriately.

**Biosignal acquisition system.** Any hardware assembly that converts a physiological signal of neural or neuromuscular origin into a stream of digital samples (Section 1.1). The canonical example is an electroencephalography front end.

**Biometric identity.** A representation of neural activity usable to identify a user as an individual, as distinct from interpreting their current intent. Biometric identity is one of the four structurally prohibited categories (Section 13.2).

*Discussion.* The prohibition exists because neural-pattern identification is an instrument of surveillance: a BCI that could identify its user could be made to report who is using it, and a population of such devices could be made into an identification network. The prohibition keeps the BCI an instrument the user wields rather than one that watches the user.

**Bounded model checker.** A formal-verification tool that takes a piece of code, a property, and a bound, and exhaustively explores every execution of the code up to the bound, checking the property on all of them. The AxonOS reference implementation uses a bounded model checker to produce its evidence-level-L1 proofs.

*Discussion.* The bounded model checker is the engine of L1 evidence. Its exhaustiveness within the bound — it considers all executions, not a sample — is what makes its passing verdict a proof rather than a test result. The methodology, including the central subtlety of choosing a sound bound, is elaborated in `VALIDATION.md` Section 7.

**Bridge.** The deterministic bus connecting the signal-processing core and the application core, across which the shared-memory region holding the inter-process-communication channel is reachable from both cores (Section 4.3 of the kernel architecture chapter).

*Discussion.* The bridge, and the single ring-buffer channel that crosses it, are the *only* coupling between the two cores. The architecture's soundness depends on this single coupling transmitting data without transmitting non-determinism, which the lock-free, never-blocking producer discipline ensures.

---

## C

**Capability.** A type-level token that authorises exactly one narrowly defined category of intent observation to flow from the kernel to the application (Section 12.1). The set of capabilities is closed and fixed at the application binary interface version; at version 1 it comprises exactly four members.

*Discussion.* The defining property of a capability is that it is a *type*, not a runtime permission flag. This distinction — elaborated in Section 12.2 and in the capability-system architecture chapter — is the conceptual heart of the Standard's privacy model. A category of data for which no capability type exists cannot be constructed as a boundary-crossing value at all; the protection is structural, enforced by the compiler, not by a runtime check that could be wrong or removed.

**Capability set.** The 32-bit field of a manifest in which each of the low four bits declares whether the application requests one of the four capabilities (Section 14.2). The admissible mask is the constant 0x0000000F; a capability set with any higher bit set is refused.

**Claims catalogue.** The single, public, maintained document that lists every quantitative claim the AxonOS Project makes under the AxonOS name, recording for each the claimed value, the evidence level, and the artefact link (`VALIDATION.md` Section 5).

*Discussion.* The catalogue exists so that the publishing rule is auditable in one place. The conformance suite's category C6 tests check the implementation's published claims against the catalogue discipline.

**Closed set.** A set that is fixed and exhaustive: no member may be added without a change to the thing of which it is a set. The capability set is closed (Section 12.3); the error taxonomy is closed (Section 20). A closed set is contrasted with an open set, to which members may be added freely.

*Discussion.* Closure is a deliberate and recurring design choice in the Standard. A closed capability set means an application's possible accesses are enumerable and bounded; a closed error taxonomy means a consumer can handle every error a producer can emit. Closure trades extensibility for analysability, and in the Standard's domain that trade is correct.

**Cognitive Hypervisor.** The cross-cutting subsystem, present only in deployments that drive a stimulation channel, that enforces a neural-tissue charge-density limit and interlocks stimulation with the consent state (Section 5.4). It runs in the Secure World of an ARM TrustZone-M partition.

*Discussion.* The Cognitive Hypervisor is *optional*: a read-only BCI deployment, one that records but does not stimulate, does not include it, and the Standard's requirements concerning it do not apply to such a deployment. Its purpose is the safety obligation that stimulation, and only stimulation, carries.

**Cognitive profile.** A persistent, identifying representation of a user's cognitive characteristics — a representation accumulable across sessions into a stable fingerprint of how a particular mind works. Cognitive profile is one of the four structurally prohibited categories (Section 13.2).

*Discussion.* The prohibition exists because a persistent cognitive fingerprint is an instrument of discrimination: in the hands of an employer, an insurer, or a credentialing body it becomes a basis for exclusion. The prohibition exists so that using a BCI cannot become a precondition for being profiled.

**Confidence.** The classifier's posterior probability that the intent it has reported is the intent the user actually expressed. The confidence is carried in the intent-observation record (Section 19) as a Q1.15 fixed-point fraction.

**Conformance.** The property of an implementation satisfying every applicable normative requirement of the Standard and passing the conformance suite (Section 24, `CONFORMANCE.md` Section 1). Conformance is always conformance with a specific version.

**Conformance suite.** The set of fifty-seven tests, defined in `CONFORMANCE.md` Section 5, that constitutes the executable expression of the Standard's requirements. Passing the suite is a necessary component of conformance.

**Consent.** A user's permission for intent observations to flow, modelled as a three-state finite-state machine — granted, suspended, withdrawn (Section 15). Consent is a cross-cutting subsystem present in every conformant deployment.

*Discussion.* Consent in AxonOS is not an application-layer preference but a kernel-level state, consulted before every intent observation is published. This placement — below the application — is what makes a withdrawal of consent enforceable rather than advisory: see the consent-architecture chapter.

**Consent interlock.** The mechanism by which the consent state is consulted by the kernel before every intent-observation publication, and by which a withdrawal of consent propagates to terminate observation flow within the withdrawal timing bound (Section 15).

**Containment of non-determinism.** The architectural property that the non-determinism of the application core is confined to the application core and cannot delay the deterministic signal-processing core (Section 4.3 of the kernel chapter). Containment is ensured by the lock-free, never-blocking producer discipline of the inter-process-communication channel.

---

## D

**Deadline.** The time by which a task must complete. Under Earliest-Deadline-First scheduling, a task's absolute deadline — its release time plus its relative deadline — determines its dynamic priority.

**Deadline miss.** The event of a task failing to complete by its deadline. Clause DC4 of the dual-core contract requires a deadline miss to be detected within two scheduler ticks.

*Discussion.* In a correctly admitted task set, a deadline miss is not supposed to be reachable — the timing analysis exists to prove it cannot occur. The deadline-miss detection requirement is therefore a last-line-of-defence assertion: if the analysis was somehow wrong, or a hardware fault perturbed the timing, the kernel detects the miss promptly rather than continuing silently with a violated guarantee.

**Derived quantity.** A number obtained by calculation from other claims rather than by direct proof or measurement. A derived quantity is published with the tag "derived" and with its input claims cited (`VALIDATION.md` Section 2.4). The canonical example is an improvement factor, derived by dividing one measurement by another.

**Dual-core contract.** The six-clause real-time contract, designated DC1 through DC6, that a conformant kernel must satisfy (Section 9). The clauses bound the worst-case response time, the jitter, the inter-process-communication latency, the deadline-miss detection latency, the graceful-degradation behaviour, and the sensor-reconnection recovery latency.

**Dual-core premise.** The architectural premise (Section 6.1) that the kernel is analysable as a dual-core system: a deterministic signal-processing core and a non-deterministic application core, coupled only by the inter-process-communication channel.

---

## E

**Earliest-Deadline-First scheduling.** Abbreviated EDF. The dynamic-priority scheduling discipline, required of the signal-processing core by Section 7.1, under which the scheduler always runs, among the ready tasks, the one whose absolute deadline is nearest.

*Discussion.* EDF is chosen over the fixed-priority Rate-Monotonic discipline for two reasons given in Section 7.2: its utilisation bound is exactly 1.0 rather than approximately 0.693, and its schedulability analysis is a single utilisation inequality that is stable under revision of the task set. The second reason is, for the kernel's maintainers, the more valuable in practice.

**Epoch.** See *processing epoch*.

**Evidence level.** One of the three grades — L1, L2, L3 — that the validation discipline assigns to a quantitative claim (Section 22, `VALIDATION.md` Section 1). L1 is a formal proof over the whole input space; L2 is a measurement on reference hardware; L3 is an independent reproduction.

**Execution model.** The model, defined in Section 6, of how the signal-processing core's work is organised: into fixed-duration processing epochs, each executing a fixed task set once.

---

## F

**Falsifiable prediction.** A claim with three identifiable parts — a stated domain, a stated property, and an identifiable falsifier — such that a reader knows exactly what the claim asserts, where it asserts it, and what observation would refute it (`VALIDATION.md` Section 4). Every L1 and L2 claim under the AxonOS name must be a falsifiable prediction.

*Discussion.* Falsifiability is required because a claim that cannot be refuted cannot be checked, and a claim that cannot be checked gives a reader no information beyond the bare word of its author. The requirement converts the Project's numbers from assertions into evidence.

**Finite-impulse-response filter.** The second stage of the reference signal-processing pipeline, which shapes the signal's frequency content by convolving each channel against a fixed filter kernel. It is the pipeline's most expensive stage, at a worst-case execution time of 320 microseconds.

**Fixed-task-set discipline.** The requirement (Section 6.3) that the kernel's task set be fixed and known at the time the timing analysis is performed, and that no task be added, and no task's timing parameters changed, at runtime except through admission control.

*Discussion.* The discipline exists because the worst-case response time is proven for a specific task set; a task set that could change without re-validation would be a task set for which no worst-case response time had been proven. The discipline, and the admission-control gate that is its sole exception, ensure the kernel is never running with an unproven task set.

**Foundation review.** The optional procedure (`CONFORMANCE.md` Section 6) by which the AxonOS Project independently confirms an implementer's self-certification of conformance, by verifying the conformance report, re-running a sample of tests, and examining the evidence artefacts.

*Discussion.* A Foundation review is not a higher grade of conformance — a self-certified conformant implementation and a Foundation-reviewed one are equally conformant — but an independent confirmation. It certifies *software conformance with the Standard* and explicitly does not certify a device or constitute a regulatory clearance.

---

## G

**Graceful degradation.** The required behaviour, clause DC5 of the dual-core contract, by which the signal-processing core continues to operate, losing no intent observation, through at least one second of application-core suspension.

**Granted.** One of the three consent states (Section 15). In the granted state, intent observations flow normally. A freshly installed manifest begins in the granted state.

---

## H

**Handshake.** The exchange, required by Section 18, that begins every connection between a software development kit and a kernel: each side transmits the application-binary-interface version it implements, and the connection proceeds only if the versions match exactly.

*Discussion.* The handshake admits no fallback and no negotiation. A version mismatch terminates the connection; a partial interoperation between mismatched versions is exactly the silent incompatibility the version discipline exists to prevent.

**Hardware-abstraction layer.** The thin, separately audited module, permitted the `unsafe` escape hatch of the implementation language, through which the kernel reaches hardware registers (Section 3.1 of the kernel chapter). The kernel proper forbids `unsafe` entirely and treats the hardware-abstraction layer as a trusted dependency.

*Discussion.* The boundary between the kernel proper, which forbids `unsafe`, and the hardware-abstraction layer, which permits it, is drawn to minimise and isolate the trusted base — the part of the system whose memory safety rests on human reasoning rather than compiler enforcement. See Section A.3 of the kernel chapter.

---

## I

**Idempotency.** The property, required of the consent state machine (Section 15), that re-applying the machine's current state succeeds without changing the state and without error. Idempotency permits the trusted path to recover from message loss without producing a spurious state change.

**Informative.** A classification of standard text (Document conventions) denoting material that provides context, motivation, rationale, or guidance but imposes no requirement. Informative material is contrasted with normative material. An implementation cannot be non-conformant by reason of disagreeing with informative material.

**Intent.** A typed, kernel-filtered, deliberately impoverished representation of a user's voluntary signal pattern: a value drawn from the small, closed set of intents the kernel is built to recognise. The application operates on intents, never on raw neural data.

**Intent observation.** The unit of data crossing the boundary from the kernel to the application: a fixed-size, 28-byte record carrying a typed intent, a confidence scalar, a timestamp, and a sequence number (Section 19). An intent observation never carries raw neural signal.

**Inter-process communication.** Abbreviated IPC. The mechanism, defined in Section 10, by which the signal-processing core and the application core communicate: a single-producer, single-consumer, lock-free ring buffer in shared memory.

---

## J

**Jitter.** The standard deviation of the interval between successive intent observations (Section 3, Section 9 clause DC2). Low jitter means a regular observation cadence; high jitter means an irregular one even if the average interval is correct.

*Discussion.* Jitter is bounded by clause DC2 at 10 microseconds at the three-sigma envelope, and is required at evidence level L2 — a measured bound over a soak — because jitter is a physical, statistical quantity for which a long measurement is the appropriate and achievable form of evidence.

---

## K

**Kalman filter.** The first stage of the reference signal-processing pipeline: a predictor-corrector estimator that maintains a running estimate of the underlying neural state and uses it to smooth the incoming sample stream. Its worst-case execution time is 80 microseconds.

**Kernel.** The deterministic software substrate (Section 5.3) that ingests digital samples from the acquisition layer, executes the real-time signal-processing pipeline, applies the capability filter, consults the consent state, and emits intent observations. The kernel bears the real-time guarantees of Part II of the Standard.

---

## L

**L1, L2, L3.** See *evidence level*.

**Layer.** One of the four tiers of the reference architecture (Section 5.3): the acquisition layer, the kernel, the software development kit, and the application layer. Each layer has a defined contract to the layer above and the layer below.

**Lock-free.** The property of a concurrent algorithm that uses no lock — no construct by which one party waits for another to relinquish access to shared data. The inter-process-communication channel is lock-free (Section 10.1), so that the producer can never be made to wait on the consumer.

*Discussion.* Lock-freedom is essential to the architecture's soundness: a lock on the channel would couple the deterministic signal-processing core's timing to the non-deterministic application core, voiding the timing analysis. The channel's lock-freedom is what keeps the non-determinism contained.

---

## M

**Manifest.** The signed, CBOR-encoded record by which an application declares its identity, the capabilities it requests, and its maximum observation rate (Section 14). The kernel verifies and installs the manifest before the application receives any observation.

**Measurement test.** A conformance test that reaches its verdict by executing the implementation and comparing the observed result against the requirement (`CONFORMANCE.md` Section 2.2). Measurement tests produce evidence at level L2 or a plain pass-or-fail verdict. Contrasted with a proof test.

**Monotonic clock.** The single authoritative timeline the kernel exposes (Section 11): a clock of one-microsecond resolution or finer, derived from a hardware time source, never adjusted, and strictly non-decreasing across successive reads.

---

## N

**Navigation capability.** One of the four capabilities of the closed set (Section 12.3). It authorises observations of directional intent — cursor movement, focus changes, scrolling. Its maximum observation rate is 50 hertz.

**Normative.** A classification of standard text (Document conventions) denoting material that defines a requirement. Normative material is the material against which conformance is assessed. Contrasted with informative.

**Notch filter.** The third stage of the reference pipeline: a filter that removes the narrow-band interference at the local electrical-mains frequency. Its worst-case execution time is 40 microseconds.

---

## O

**Observation.** See *intent observation*.

**Observation epoch.** See *processing epoch*.

---

## P

**Pipeline.** The fixed sequence of signal-processing stages the signal-processing core executes once per processing epoch (Section 6.3, Section 5 of the kernel chapter): in the reference configuration, the Kalman filter, the finite-impulse-response filter, the notch filter, the artefact-rejection stage, the common-spatial-pattern feature extractor, the linear-discriminant classifier, and the inter-process-communication publication task.

**Processing epoch.** The fixed-duration window within which the entire signal-processing pipeline executes exactly once (Section 6.2). In the reference configuration the epoch is 4 milliseconds, corresponding to a 250-hertz observation rate. The worst-case response time must not exceed the epoch duration.

**Proof test.** A conformance test that reaches its verdict by formal verification, exhaustively over the admissible input space, producing evidence at level L1 (`CONFORMANCE.md` Section 2.2). Contrasted with a measurement test.

**Prohibited category.** One of the four categories of neural data — raw neural signal, affective state, cognitive profile, biometric identity — that the Standard structurally prohibits (Section 13.2): no capability, type, or interface exposes any of them to the application layer.

**Publishing rule.** The central operative requirement of the validation discipline (`VALIDATION.md` Section 2): a quantitative claim must not appear under the AxonOS name unless it carries an evidence-level tag, links to an accessible artefact, and is stated as a falsifiable prediction.

---

## Q

**Q1.15.** A fixed-point number format: a 16-bit value interpreted as a fraction with one sign bit and fifteen fractional bits, representing values in the range minus one to just under one. The confidence field of the intent-observation record is encoded in Q1.15 (Section 19).

---

## R

**Rate ceiling.** The maximum observation rate associated with each capability (Section 12.3): 50 hertz for navigation, 1 hertz for workload-advisory, 2 hertz for session-quality, 10 hertz for artefact-events. The kernel enforces the ceilings.

*Discussion.* The workload-advisory ceiling of 1 hertz is, in particular, a privacy control: a coarse cognitive-load estimate sampled once per second cannot be assembled into a fine-grained cognitive timeline.

**Raw neural signal.** The unprocessed or lightly processed sample stream from the acquisition layer. Raw neural signal is one of the four structurally prohibited categories (Section 13.2); the application receives typed intents, never the signal from which they were derived.

*Discussion.* Raw neural signal is prohibited because it is the universal solvent: from it, given enough computation, every other prohibited category can in principle be derived. Prohibiting the raw signal is what makes the other prohibitions meaningful.

**Real-time.** The property of a system whose correctness depends not only on the logical result of its computations but on the time at which they are produced. A *hard*-real-time system, which the AxonOS kernel is, is one in which a missed deadline is a failure; a *soft*-real-time system is one in which a missed deadline degrades quality but is not a failure.

**Reference hardware.** The specific, commodity hardware platform on which the AxonOS Project's evidence-level-L2 measurements are produced and against which conformance is measured. An L2 measurement on hardware other than the reference hardware is not L2 evidence.

**Reference implementation.** The set of seven openly licensed repositories that constitute one conformant implementation of the Standard (Section 31). The reference implementation is no more authoritative than any other conformant implementation; the Standard, not the reference implementation, defines conformance.

**Request for Comments.** Abbreviated RFC. The mechanism, defined in `GOVERNANCE.md`, by which the Standard is amended: a proposed amendment is filed as a numbered document, is open for review for a defined period, and is accepted only when the review concludes without unresolved substantive objection.

**Reserved.** The classification of a field, a bit, or a code-point value that has no assigned meaning at the current version but is held for possible assignment by a future revision. A reserved field or bit must be zero on emission and checked for zero on receipt (Section 21); a reserved error code must not be emitted.

---

## S

**Schedulability.** The property of a task set that it can be scheduled, under a given discipline, such that every task always meets its deadline. Under Earliest-Deadline-First, a task set is schedulable if and only if its total utilisation does not exceed 1.0.

**Secure World.** The isolated execution domain of an ARM TrustZone-M partition, in which the Cognitive Hypervisor runs (Section 5.4). The Secure World is hardware-isolated from the Normal World, which runs the ordinary kernel and the application core's software.

**Sequence number.** The per-stream counter, beginning at zero and incremented by one for each observation, carried in the intent-observation record (Section 19). Sequence numbers let a consumer detect a gap — a lost observation — and, in the inter-process-communication channel, underpin the consistency check.

**Session-quality capability.** One of the four capabilities (Section 12.3). It authorises observations of a scalar signal-quality metric in the range zero to one. Its maximum observation rate is 2 hertz.

**Signal-processing core.** The deterministic processor core that executes the real-time pipeline (Section 6.1). In the reference hardware it is a Cortex-M4F at 168 megahertz. The signal-processing core is the core whose timing the dual-core contract governs.

**Soak.** A continuous run of the implementation on the reference hardware, under representative load, for a stated long duration, during which every quantity of interest is recorded for every epoch (`VALIDATION.md` Section 8). A soak is the source of evidence-level-L2 timing claims.

**Software development kit.** Abbreviated SDK. The architectural layer (Section 5.3) that receives intent observations from the kernel across the application binary interface and presents them to the application through a typed, language-appropriate programming interface.

**Structural prohibition.** The mechanism (Section 13.1) by which a category of neural data is rendered inaccessible not by a runtime check but by the absence of any type representing it: a structurally prohibited category cannot be constructed as a boundary-crossing value because no type for it exists.

**Suspended.** One of the three consent states (Section 15). In the suspended state, intent observations do not flow and the consumer receives a backpressure-style consent-suspended error; the suspended state is resumable to granted through the trusted path.

**Swarm-coordination subsystem.** The cross-cutting subsystem, present only in deployments with more than one acquisition node (Section 5.4), that extends the single-node dual-core contract to a synchronised multi-node contract designated SC1 through SC6.

---

## T

**Task.** A unit of computation with a known worst-case execution time and a known deadline (Section 6.3). The kernel's signal-processing core executes a fixed set of tasks, the task set.

**Task set.** The complete, fixed set of tasks the signal-processing core executes (Section 6.3). The worst-case response time is proven for a specific task set; the fixed-task-set discipline forbids changing it except through admission control.

**Three-sigma envelope.** The range within three standard deviations of a mean, encompassing approximately 99.7 per cent of a normally distributed quantity's values. Clause DC2 bounds jitter at the three-sigma envelope.

**Timestamp.** The value of the monotonic clock, in microseconds, at the instant the kernel emitted an intent observation (Section 11.3, Section 19). The timestamps of a stream's observations are strictly increasing.

**Trusted path.** The input channel through which consent state transitions are signalled, and which the application layer provably cannot synthesise (Section 16): a physical hardware button, a Secure-World user-interface partition, or an equivalent software-unforgeable channel.

*Discussion.* The trusted path is the most security-critical input in the consent subsystem. If a consent event could be synthesised by application-layer software, the kernel could not distinguish a genuine user revocation from an application masquerading as the user.

**TrustZone-M.** The hardware security extension of the ARMv8-M architecture that partitions a processor into a Secure World and a Normal World. The Cognitive Hypervisor runs in the Secure World of a TrustZone-M partition.

---

## U

**Unconditional conformance.** The grade of conformance (Section 4.2) in which an implementation satisfies every applicable MUST requirement and every applicable SHOULD requirement. Contrasted with conditional conformance.

**Utilisation.** The fraction of a processor's capacity a task or a task set consumes: for one task, its worst-case execution time divided by its period; for a task set, the sum over all tasks. The reference task set's total utilisation is approximately 0.160.

**Utilisation ceiling.** The configured upper limit on the total utilisation of an admissible task set (Section 7.3), by default 0.25. The ceiling sits far below the theoretical Earliest-Deadline-First bound of 1.0; the gap is the margin that absorbs interrupt load, worst-case-execution-time imprecision, and micro-architectural effects.

---

## V

**Validation discipline.** The framework, defined in `VALIDATION.md`, within which every quantitative claim under the AxonOS name is graded by evidence level, substantiated by an artefact, published under the publishing rule, and — when evidence requires — retracted.

**Version (ABI).** The single integer tagging the application binary interface (Section 17). The current version is 1. A change to the wire format, the handshake, the capability set, or the error taxonomy requires an increment of the ABI version.

**Version (Standard).** The semantic-versioning identifier of the Standard itself (Section 26), with a major, minor, and patch component. Conformance is always conformance with a specific version.

---

## W

**Wire format.** The byte-exact encoding of the intent-observation record as it crosses the application binary interface (Section 19): a 28-byte, little-endian record with fields at defined offsets.

**Withdrawn.** The terminal consent state (Section 15). A withdrawal of consent terminates all observation streams within the withdrawal timing bound; the withdrawn state cannot be left, and the only path to receiving observations again is the installation of a fresh manifest through the trusted path.

*Discussion.* The terminality of the withdrawn state is the central anti-coercion property of the consent subsystem. If a withdrawal could be silently reversed, the protection would be theatre; the user, and any reasoning built on consent, must be able to rely on the terminal state actually being terminal.

**Worst-case execution time.** Abbreviated WCET. The maximum time a single task can take to execute, over all admissible inputs and machine states. Each task in the task set has a known worst-case execution time, and the task set's worst-case execution times are the inputs to the response-time analysis.

**Worst-case response time.** Abbreviated WCRT. The maximum, over all admissible inputs and all admissible machine states, of the elapsed time from the start of a processing epoch to the delivery of the corresponding intent observation (Section 8.1). Clause DC1 of the dual-core contract bounds the worst-case response time at 1000 microseconds, at evidence level L1.

*Discussion.* The worst-case response time is the single most important quantity in the Standard's real-time argument. It is not a measurement — it is an upper bound, established by a formal proof ranging over the entire input space, because a measurement samples the input space and the worst case may lie in the unsampled remainder.

---

---

## Appendix A — The conceptual map: how the defined terms relate

*Informative. The alphabetical body of this glossary defines each term in isolation. This appendix steps back and describes how the terms fit together, because a reader who has the relationships in mind reads the alphabetical definitions more quickly and retains them better.*

The terms of this glossary cluster into five conceptual families, and the families correspond to the five things a reader of the Standard must understand: the architecture, the timing, the privacy model, the consent model, and the evidence model.

The **architecture family** is built around *layer*. There are four layers — *acquisition layer*, *kernel*, *software development kit*, *application* — and the architecture is the statement of what each layer is and how adjacent layers relate. Between the layers are *interfaces*: the *acquisition interface* below the kernel, the *application binary interface* above it. Beside the layer stack are the three *cross-cutting subsystems*: the *consent* subsystem, present always; the *Cognitive Hypervisor*, present only when there is stimulation; the *swarm-coordination subsystem*, present only when there is more than one node. A reader who holds the four-layer picture, with the interfaces between and the subsystems beside, has the architecture, and the architecture is the frame on which everything else hangs.

The **timing family** is built around *worst-case response time*. The kernel runs a *pipeline* of *tasks* — the *task set* — once per *processing epoch*, scheduled by *Earliest-Deadline-First* scheduling, and the central quantity is the worst-case response time, the maximum time the pipeline can take. The worst-case response time is composed from the *worst-case execution times* of the individual tasks and is bounded by *clause DC1* of the *dual-core contract*. The *utilisation* of the task set must stay under the *utilisation ceiling*; the *fixed-task-set discipline* keeps the task set stable, and *admission control* is the gate through which the only permitted changes pass. The *jitter* — the regularity of the observation cadence — is the second timing quantity, bounded by *clause DC2*. A reader who holds this family understands what the kernel guarantees and how.

The **privacy family** is built around *capability*. A capability is a *type*, not a runtime flag, and that single fact — elaborated in the term *structural prohibition* — is the privacy model. The *closed set* of four capabilities — *navigation*, *workload-advisory*, *session-quality*, *artefact-events* — is exhaustive, each with its *rate ceiling*. The four *prohibited categories* — *raw neural signal*, *affective state*, *cognitive profile*, *biometric identity* — are the categories no capability exposes, and they are prohibited *structurally*: no type for them exists, so no boundary-crossing value of them can be constructed. The *manifest* is how an application declares which capabilities it requests. A reader who holds this family understands why neural data is safe in an AxonOS deployment: not because a check guards it, but because the dangerous categories have no type to inhabit.

The **consent family** is built around the three states — *granted*, *suspended*, *withdrawn* — of the consent finite-state machine. *Consent* is a kernel-level state, consulted before every observation through the *consent interlock*; a transition is signalled only through the *trusted path*, which application-layer software cannot synthesise; the *withdrawn* state is terminal, and that terminality is the anti-coercion property. *Idempotency* lets the trusted path recover from message loss. A reader who holds this family understands why a withdrawal of consent in an AxonOS deployment is real rather than advisory.

The **evidence family** is built around *evidence level*. Every quantitative claim carries a level — *L1*, a *proof* over the whole input space; *L2*, a *measurement* over a *soak* on the *reference hardware*; *L3*, an independent reproduction. The *publishing rule* forbids any claim under the AxonOS name that lacks a level, an *artefact*, or *falsifiability*. The *claims catalogue* records every claim. A reader who holds this family understands why every number the Project publishes can be checked.

The five families are not independent. The timing family's worst-case response time is an *L1* claim — the evidence family grades it. The privacy family's capabilities are enforced at the *application binary interface* — the architecture family's interface. The consent family's interlock sits inside the kernel's *pipeline* — the timing family's pipeline. The families are five views of one system, and the glossary's alphabetical body defines the terms while this appendix supplies the system they jointly describe.

---

## Appendix B — Terms an implementer most often confuses

*Informative. Certain pairs of terms are routinely confused, and the confusion causes real errors. This appendix names the pairs and draws the distinction sharply.*

**Worst-case execution time versus worst-case response time.** The worst-case execution time is the time *one task* takes in isolation. The worst-case response time is the time the *whole pipeline* takes from epoch start to observation delivery, including the time during which tasks preempt one another. The response time is composed *from* the execution times, but it is not their sum — it accounts for interference — and it is the response time, not the execution time, that clause DC1 bounds.

**Evidence level L1 versus a measurement.** L1 is a proof over the *whole* input space. A measurement, however long, samples the input space. The most common and most serious validation error is presenting a measured worst case as though it were an L1 bound; they are different claims, and the glossary's entries for *evidence level*, *proof test*, and *soak* exist partly to keep them distinct.

**A capability versus a runtime permission.** A capability is a *type*; a runtime permission is a *flag tested by an `if`*. The whole privacy argument turns on the difference: a type that does not exist cannot be inhabited by a value, whereas a flag can be mis-tested or removed. An implementer who builds the capability system as a set of runtime flags has not built the AxonOS capability system, whatever they call it.

**Suspended versus withdrawn.** Both consent states stop observation flow. *Suspended* is resumable — a pause; *withdrawn* is terminal — a revocation. Conflating them destroys either the ability to pause without re-installing a manifest or the anti-coercion guarantee, depending on which way the conflation runs. The two states are two states precisely because the user needs both a pause and a revocation and they are different things.

**Normative versus informative.** Normative text defines a requirement and is what conformance is assessed against. Informative text explains, motivates, and gives rationale, and imposes no requirement. An implementer who treats an informative passage as a requirement wastes effort; one who treats a normative passage as mere explanation ships a non-conformance. Every passage's classification is determinable from the conventions stated in the Standard's front matter.

**The reference implementation versus the Standard.** The Standard *defines* conformance; the reference implementation is *one* conformant implementation of it. If they disagree, the Standard is right and the reference implementation has a bug. An implementer who treats the reference implementation's behaviour as the definition of correct behaviour has mistaken an example for the rule.

---

## Appendix C — Terminology alignment with adjacent standards

*Informative.* Where the AxonOS terminology touches the vocabulary of adjacent fields, the correspondences are as follows.

The AxonOS *worst-case response time* and *worst-case execution time* correspond to the quantities of the same names in the established real-time-systems literature; the AxonOS usage is the standard usage of that literature, and a reader from a real-time-systems background may rely on the terms meaning what they are accustomed to. The AxonOS *Earliest-Deadline-First scheduling* is the discipline of that name in the same literature, and the *utilisation* and *schedulability* terms likewise carry their standard real-time-systems meanings.

The AxonOS *capability*, as a type-level token authorising a narrow category of access, is aligned with the capability concept of the capability-based operating-systems tradition — the tradition of the capability-based research operating systems and of the more recent capability-oriented sandboxing libraries. The AxonOS adaptation is the fixing of a *closed* set of exactly four capabilities specific to the BCI domain; the underlying idea, that a capability is an unforgeable token of authority rather than a checked permission, is the tradition's idea.

The AxonOS cryptographic terms — the *signature* on a manifest, the verification thereof — use the Edwards-curve digital signature algorithm as standardised in the relevant federal standard, and the AxonOS usage of the term "signature" is that standard's usage.

Where the draft unified terminology for brain-computer interfaces, under development in the relevant standards body, defines a term that overlaps an AxonOS term, the AxonOS glossary will be revised toward that terminology once it is published, and any conflict will be resolved in favour of the published unified terminology. Until that terminology is published, this glossary governs AxonOS usage, and an implementer should rely on the definitions here.

---

**End of GLOSSARY.md.**

*This document is normative for the meaning of every term it defines. Where it and any other AxonOS document use the same term, this glossary governs.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
