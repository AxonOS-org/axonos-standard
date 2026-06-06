# The AxonOS Standard

**Version 1.1.0** — Canonical Technical Standard for Deterministic Brain-Computer Interface Software

**Status:** Normative · **Date:** 2026-06-06 · **License:** CC-BY-SA-4.0

**Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

---

## Preface

This document is the canonical normative text of the **AxonOS Standard**, the open technical standard for deterministic brain-computer interface (BCI) software. It defines the architecture, real-time guarantees, capability system, consent semantics, application binary interface, validation methodology, and conformance requirements that a software implementation must satisfy in order to declare itself conformant with version 1.1.0 of the AxonOS Standard.

The Standard exists because the software layer that mediates between neural acquisition hardware and intelligent applications is, at the time of this writing, undefined. There is no shared contract describing how a BCI's signal-processing substrate must behave with respect to timing, how it must structure access to neural data, how it must enforce a user's revocation of consent, or how its quantitative claims must be evidenced. Every BCI software stack reinvents these decisions privately, with the consequence that no two stacks are interoperable, no claim made by one stack is verifiable against another, and no regulator, clinician, or researcher can reason about a BCI's software behaviour without access to that specific vendor's private documentation.

The AxonOS Standard is an attempt to end that situation by publishing the missing contract. It is the deliberate analogue, for the brain-computer interface domain, of what POSIX did for operating-system interfaces, what the C language standard did for systems programming, and what the IETF's Request-for-Comments series did for network protocols: a single, openly licensed, precisely worded document against which independent implementations can be built and independently verified.

This Standard is not a product. It is not a software development kit, a kernel, or a hardware reference design, although a reference implementation of each of those exists and is identified in Section 31. The Standard is the **specification**: the set of requirements that any conformant implementation — the reference one, or an independent one written by a team that has never communicated with the AxonOS Project — must satisfy.

The Standard is maintained under the governance process documented in Section 27 and elaborated in the companion document `GOVERNANCE.md`. Amendments flow through a Request-for-Comments process. The authoritative version at any time is the file `STANDARD.md` at the Git commit corresponding to the release tag recorded in the repository's `VERSION` file.

This Standard is released under the Creative Commons Attribution-ShareAlike 4.0 International licence. It may be reproduced, translated, and adapted under the terms of that licence. Code samples embedded within this document are additionally available under the Apache License 2.0 or the MIT licence, at the implementer's option, so that they may be incorporated verbatim into reference implementations without licence-compatibility concerns.

---

## Document conventions

### Requirement keywords

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in RFC 2119 and RFC 8174. These key words have their defined meaning only when they appear in all capital letters, as shown. When the same words appear in lower case, they carry their ordinary English meaning and impose no requirement.

The interpretation is as follows. **MUST**, **REQUIRED**, and **SHALL** denote an absolute requirement of this Standard; an implementation that violates such a requirement is not conformant. **MUST NOT** and **SHALL NOT** denote an absolute prohibition. **SHOULD**, **RECOMMENDED**: there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course; an implementation that departs from a **SHOULD** remains conformant but the departure must be justifiable and SHOULD be documented. **SHOULD NOT**, **NOT RECOMMENDED**: there may exist valid reasons in particular circumstances when the particular behaviour is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behaviour described with this label. **MAY** and **OPTIONAL** denote that an item is truly discretionary; one implementation may choose to include the item because a particular marketplace requires it or because it enhances the product, while another may omit the same item, and an implementation which does not include a particular option **MUST** be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality.

An implementation is not compliant if it fails to satisfy one or more of the **MUST** or **MUST NOT** requirements for the protocols and behaviours it implements. An implementation that satisfies all the **MUST** and all the **SHOULD** requirements for its protocols and behaviours is said to be "unconditionally compliant"; one that satisfies all the **MUST** requirements but not all the **SHOULD** requirements is said to be "conditionally compliant."

### Normative and informative material

Every passage in this Standard is classified as either **normative** or **informative**.

Normative material defines requirements. By default, every statement in the numbered sections of Parts II through VI is normative, except where the surrounding prose explicitly marks it otherwise with the words "Informative", "Rationale", "Example", "Note", or "Discussion". Normative material is the material against which conformance is assessed.

Informative material provides context, motivation, worked examples, design rationale, historical background, and implementation guidance. Informative material is genuinely useful and is included deliberately, but it imposes no requirement. An implementation cannot be non-conformant by reason of disagreeing with informative material.

Tables, figures, diagrams, and code listings are informative unless the surrounding normative prose explicitly incorporates them by reference. Where a byte-level wire format is specified, the textual byte-offset table is normative and any accompanying source-code structure definition is informative; the source code is an aid to comprehension, and in the event of any discrepancy between the byte-offset table and the source code, the byte-offset table governs.

Parts I and VII of this document, and all appendices, contain a mixture of normative and informative material; specific passages are tagged.

### The authoritative version

The authoritative text of this Standard is the file `STANDARD.md` in the canonical repository, at the Git commit pointed to by the release tag recorded in the `VERSION` file. Any rendering of this Standard in another medium — an HTML page, a typeset PDF, a printed copy, a translation — is informative. In the event of any discrepancy between such a rendering and the authoritative repository file at the relevant tag, the repository file governs.

### Cross-references

A reference of the form "Section N" refers to a numbered section of this document. A reference of the form "`FILENAME`" refers to a companion document in the same repository. A reference of the form "[RFCxxxx]" refers to an entry in the bibliography in Appendix E. A reference to a "clause" of the dual-core contract (DC1 through DC6) or the swarm contract (SC1 through SC6) refers to the enumerated requirements in Sections 9 and 30 respectively.

---

## How to read this Standard

This Standard is long because the domain is unforgiving: a brain-computer interface that misses a timing deadline, leaks a category of neural data it should not have exposed, or fails to honour a user's revocation of consent is not merely a low-quality product but a safety and rights failure. Precision is therefore not optional, and precision is verbose.

Different readers need different paths through the document.

An **implementer** building a conformant kernel, software development kit, or related component should read the entire Standard, in order, at least once, and should then treat Parts II through V as a reference to be consulted continuously during development. The companion document `CONFORMANCE.md` defines the test suite that the implementation must pass; it should be read immediately after this Standard.

An **application developer** consuming a conformant software development kit needs Sections 12 through 21 — the capability system, the consent semantics, and the application binary interface — in depth, and needs the remainder only as background. Such a reader is not building the substrate; they are building atop it, and the substrate's internal timing analysis is not their concern, but the capability and consent contracts absolutely are, because those define what the developer's application is permitted to observe and how it must behave when consent changes.

A **reviewer or academic** evaluating the Standard's claims should read Parts I and II for the architecture, then read `VALIDATION.md` for the evidence framework, then return to the specific sections whose claims they wish to scrutinise. The evidence taxonomy in Section 22 is the key to the entire document's epistemics: every quantitative claim in this Standard is tagged with an evidence level, and a reviewer's first question of any number should be "at what level is this evidenced, and where is the artefact?"

A **regulator or safety engineer** assessing a device built on AxonOS should read Section 15 (consent), Section 22 (validation), the regulatory-positioning material in Section 30, and Part III in full — the Security and Privacy Model (Sections 12 through 16). Such a reader should understand clearly that this Standard is not a regulatory clearance and makes no claim of one; it is the substrate specification against which a regulatory submission could be drafted, which is a different and more modest thing.

A **contributor** wishing to propose a change to the Standard should read `GOVERNANCE.md` first, then the section of this Standard they wish to amend, then the existing Requests for Comments in the `governance/` directory to understand the prior art and the house style of amendment proposals.

Regardless of the reader, the single most important conceptual move in this Standard is the distinction between the **contract** and the **implementation**. This Standard defines contracts: the contract between the application and the software development kit, the contract between the development kit and the kernel, the internal contract the kernel makes with itself about timing, and the contract the consent subsystem makes with the user. A contract is a statement of what must be true at an interface. It is deliberately silent about how either side of the interface achieves its obligations. Two conformant kernels may schedule their internal tasks completely differently, may be written in different programming languages, may run on different processor families, and may share not a single line of source code — and they are nonetheless both conformant, and both interoperable with the same software development kit, precisely because they both honour the same contracts. The contract is the unit of standardisation. The implementation is free.

---

# Part I — Foundations

## Section 1. Scope and applicability

### 1.1 The systems this Standard governs

This Standard applies to software systems that mediate between biosignal acquisition hardware and applications which operate on a user's voluntary intent.

A **biosignal acquisition system**, for the purposes of this Standard, is any hardware assembly that converts a physiological signal of neural or neuromuscular origin into a stream of digital samples. The canonical example is an electroencephalography front end: an array of electrodes in electrical contact with the scalp, an instrumentation amplifier, and an analog-to-digital converter producing a multi-channel stream of voltage samples at a fixed rate. The Standard's architecture and requirements are, however, deliberately phrased to accommodate electromyography (recording from muscle), electrocorticography (recording from the cortical surface beneath the skull), and other recording modalities, because the software contract this Standard defines is independent of the specific transducer physics. What the Standard requires of the acquisition layer is only that it deliver digital samples to the kernel boundary with deterministic completion semantics; the analog design that produces those samples is outside the Standard's scope, and is addressed only informatively, in the companion hardware-reference material.

An **application**, for the purposes of this Standard, is end-user software that operates on the user's *intent* — a typed, kernel-filtered, deliberately impoverished representation of the user's voluntary signal patterns. An assistive communication application that lets a user with motor impairment move a cursor and select letters is an application. A workload-monitoring tool that advises a user when their cognitive load is high is an application. A research instrument that records intent events for later analysis is an application. What unites these is that they consume *intent*, not raw neural data; the boundary between raw data and intent, and the structural mechanism that enforces it, is one of the central subjects of this Standard.

Between the acquisition system and the application sits the software this Standard governs: the **kernel**, the **software development kit**, and the cross-cutting **consent** subsystem. The Standard defines the contracts at every interface among these and at the interfaces to the acquisition system and the application.

### 1.2 What the Standard defines

Concretely, this Standard defines the following, each in the section indicated:

The **four-layer reference architecture** that connects acquisition hardware to application software through a deterministic substrate (Section 5), and the contracts at each interface between adjacent layers.

The **execution model and real-time guarantees** that the deterministic substrate must offer: the scheduling discipline (Section 7), the worst-case timing analysis methodology (Section 8), the six-clause dual-core real-time contract DC1 through DC6 (Section 9), the inter-process communication discipline (Section 10), and the clock semantics (Section 11).

The **capability system** by which an application may receive only specific, narrowly typed categories of intent observation, and by which entire categories of neural data are rendered structurally inaccessible (Sections 12 and 13), together with the **manifest** format by which an application declares the capabilities it requests (Section 14).

The **consent state semantics**: the three-state finite-state machine by which a user grants, suspends, or irrevocably withdraws permission for intent observations to flow (Section 15), and the **trusted-path** requirement that protects the integrity of consent transitions (Section 16).

The **application binary interface**, version 1: the versioning discipline (Section 17), the connection handshake (Section 18), the byte-exact wire format of the intent observation record (Section 19), the error taxonomy (Section 20), and the forward- and backward-compatibility rules (Section 21).

The **validation methodology**: the three-level evidence taxonomy under which every quantitative claim made under the AxonOS name must be graded and substantiated (Section 22), and the falsifiability requirement that each such claim be stated as a refutable prediction (Section 23).

The **conformance regime**: the criteria an implementation must satisfy to be conformant (Section 24), and the distinction between implementer self-certification and optional Foundation review (Section 25).

The **governance and evolution** of the Standard itself: the versioning scheme (Section 26), the amendment process (Section 27), and the stability commitments that bound what future revisions may change (Section 28).

The **integration** of the Standard with its environment: alignment with external standards (Section 29), regulatory positioning (Section 30), and the identification of the reference implementation (Section 31).

### 1.3 What the Standard does not define

The Standard's scope is deliberately bounded. The following are explicitly outside it.

The Standard does not define the **analog acquisition hardware** or the analog-to-digital conversion path. It requires only that digital samples arrive at the kernel boundary with deterministic completion semantics. A hardware reference design is provided in the companion architecture material, but that reference design is informative; an implementer may use entirely different acquisition hardware and remain conformant, provided the kernel-boundary contract is honoured.

The Standard does not define the **application layer**. Applications are end-user software whose design, user interface, feature set, and internal architecture are the responsibility of their authors. The Standard constrains an application only at one interface: the application declares a set of capabilities in its manifest (Section 14), and the application must behave correctly when it receives the consent-related and rate-related error codes defined in Section 20. Beyond those two constraints, the application layer is unconstrained by this Standard.

The Standard does not define **clinical protocols**, **regulatory submission texts**, or **medical-device class determinations**. It provides the substrate against which such documents may be drafted, and it is designed to compose cleanly with the relevant medical-device software lifecycle and risk-management standards (Section 29), but it is not itself any of those things, and conformance with this Standard is neither necessary nor sufficient for regulatory clearance in any jurisdiction.

The Standard does not define, and explicitly excludes (Section 13.3 and the exclusions in Section 31.4), any mechanism for **affective-state inference**, **cognitive profiling**, **biometric identification from neural patterns**, or **exposure of raw neural signal** to the application layer. These exclusions are not accidental omissions to be filled by a future minor revision; they are deliberate, load-bearing design decisions, and the procedural cost of reversing them is set deliberately high in Section 28.

The Standard does not define an **artificial-intelligence agent framework**, a **multi-device coupling protocol** beyond the swarm-coordination material of Section 30, a **blockchain or token system**, or a **general-purpose real-time operating system**. AxonOS is specific to the neural-signal domain and its particular cadence and freshness constraints; it is not a general-purpose RTOS, and an implementer who needs one should use one of the many excellent general-purpose real-time operating systems rather than attempting to press AxonOS into that role.

### 1.4 The intended audiences

This Standard is written for five audiences, listed here in approximate order of how frequently each will consult the document.

**Implementers** build conformant kernels, software development kits, hardware gateways, and related components. They are the primary audience; the Standard's precision exists for their benefit, because an implementer building from an imprecise specification will make a hundred small decisions that diverge silently from other implementers' hundred small decisions, and interoperability will be lost.

**Application developers** consume a conformant software development kit to build end-user BCI applications. They need the capability, consent, and ABI material in depth.

**Reviewers and academics** evaluate the Standard's claims, scrutinise its evidence, and in the best case attempt to refute its quantitative predictions. The Standard is written to make their work possible: every quantitative claim is evidenced and falsifiable.

**Regulators and safety engineers** assess devices built on AxonOS. They need the consent, validation, and security material, and they need to understand precisely the modest thing this Standard is and the immodest things it is not.

**Standards-body participants** represent the AxonOS Standard in adjacent forums and carry terminology and design decisions between this Standard and others.

### 1.5 The relationship between the Standard and the reference implementation

A recurring source of confusion in open-standard projects is the relationship between the standard document and the reference implementation. This Standard takes an explicit position.

The Standard is primary. The reference implementation is one conformant implementation of the Standard, no more privileged than any other conformant implementation. If the reference implementation and the Standard disagree, the Standard is correct and the reference implementation has a bug. The reference implementation exists to demonstrate that the Standard is implementable, to provide a concrete artefact that implementers may study and that the conformance suite may be validated against, and to serve as the substrate for the AxonOS Project's own clinical and research work. It does not exist to define the Standard; the Standard defines itself.

An independent implementation — one written by a team with no connection to the AxonOS Project, in a different programming language, for a different processor family — is exactly as conformant as the reference implementation, if and only if it passes the conformance suite of `CONFORMANCE.md`. The Standard is the arbiter; the conformance suite is the Standard's executable expression; and any implementation that passes the suite is conformant by definition, regardless of its provenance.

---

## Section 2. Normative references

The following documents are referenced normatively in this Standard. Their requirements are incorporated into this Standard by reference. Where a specific version or edition is cited, that version applies, and a later version does not apply unless and until a Request for Comments amends this section.

**[RFC2119]** Bradner, S. *Key words for use in RFCs to Indicate Requirement Levels.* RFC 2119, BCP 14, March 1997. This document defines the interpretation of the requirement keywords used throughout this Standard.

**[RFC8174]** Leiba, B. *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words.* RFC 8174, BCP 14, May 2017. This document clarifies that the requirement keywords carry their defined meaning only in upper case.

**[RFC8949]** Bormann, C., and Hoffman, P. *Concise Binary Object Representation (CBOR).* RFC 8949, STD 94, December 2020. The manifest format of Section 14 and certain wire formats are CBOR-encoded; this document defines the encoding.

**[RFC4648]** Josefsson, S. *The Base16, Base32, and Base64 Data Encodings.* RFC 4648, October 2006. Where this Standard requires textual encoding of binary data, the Base64 encoding of this document is used.

**[FIPS186-5]** National Institute of Standards and Technology. *Digital Signature Standard (DSS).* FIPS PUB 186-5, February 2023. The Edwards-curve Digital Signature Algorithm referenced for manifest and consent-event signing is specified, in the form used by this Standard, in this publication.

The informative references — documents that inform the Standard's design but whose requirements are not incorporated — are listed separately in Appendix E.

---

## Section 3. Terms and definitions

This Standard uses a substantial body of defined terminology. The complete glossary, with approximately one hundred and fifty defined terms, is the companion document `GLOSSARY.md`, which is normative for the meaning of every term it defines.

This section reproduces, for the reader's immediate convenience, the twelve terms whose precise meaning is most load-bearing in the sections that follow. Where this section and `GLOSSARY.md` differ, `GLOSSARY.md` governs, because it is the maintained canonical source and this section is a convenience extract.

A **capability** is a type-level token that authorises exactly one narrowly defined category of intent observation to flow from the kernel to the application. Capabilities are types in the implementation's source language, are fixed at the application binary interface version, and are exhaustive: the set of capabilities is closed, and no observation outside that set may cross the kernel boundary.

An **intent observation** is the unit of data that crosses the boundary from the kernel to the application. It is a fixed-size record carrying a typed intent, a confidence scalar, a timestamp, and a sequence number. Its byte-exact format is defined in Section 19. An intent observation never carries raw neural signal; it carries only the narrow, typed, kernel-computed conclusion that a particular intent was expressed.

The **kernel** is the deterministic software substrate that ingests digital samples from the acquisition layer, executes the real-time signal-processing pipeline, and produces intent observations. The kernel is the component that bears the real-time guarantees of Part II.

The **software development kit**, abbreviated SDK, is the component that presents the kernel's intent observations to the application through a typed, language-appropriate interface, and that mediates the application's capability declarations.

**Consent** is the user's permission for intent observations to flow. It is modelled as a three-state finite-state machine — granted, suspended, withdrawn — whose semantics are defined in Section 15.

The **worst-case response time**, abbreviated WCRT, is the maximum possible elapsed time, over all admissible inputs and all admissible machine states, from the start of an observation epoch to the delivery of the corresponding intent observation to the software development kit. It is the central quantity bounded by the dual-core contract.

**Jitter** is the standard deviation of the interval between successive intent observations. A low jitter means the observation cadence is regular; a high jitter means it is irregular even if its average is correct.

An **evidence level** is one of the three grades — L1, L2, L3 — that this Standard assigns to a quantitative claim. The grades are defined in Section 22. Every quantitative claim made under the AxonOS name must carry an evidence level.

The **trusted path** is the input channel through which consent state transitions are signalled, and which the application layer provably cannot synthesise. Its requirements are in Section 16.

A **manifest** is the signed, CBOR-encoded record by which an application declares its identity, the capabilities it requests, and its maximum observation rate. Its format is in Section 14.

**Conformance** is the property of an implementation satisfying every applicable normative requirement of this Standard and passing the conformance suite of `CONFORMANCE.md`.

The **application binary interface**, abbreviated ABI, is the byte-exact, version-tagged contract at the boundary between the software development kit and the kernel. The current version is 1.

---

## Section 4. Conformance and the meaning of requirements

### 4.1 What it means to be conformant

An implementation is **conformant with version 1.1.0 of the AxonOS Standard** if and only if it satisfies every normative **MUST** and **MUST NOT** requirement of this Standard that applies to the components it implements, and passes the conformance suite defined in `CONFORMANCE.md` at the corresponding repository tag.

The phrase "that applies to the components it implements" is important. This Standard governs a kernel, a software development kit, a consent subsystem, and optionally a Cognitive Hypervisor and a swarm-coordination layer. An implementation need not implement all of these. A project that implements only a conformant kernel, and relies on the reference software development kit, is assessed for conformance only against the kernel requirements and the requirements of the contracts the kernel participates in. The conformance suite is structured, in `CONFORMANCE.md`, so that the relevant subset of tests can be run against a partial implementation.

### 4.2 Unconditional and conditional conformance

Following the convention of [RFC2119], this Standard distinguishes two grades of conformance.

An implementation is **unconditionally conformant** if it satisfies every applicable **MUST** requirement and every applicable **SHOULD** requirement.

An implementation is **conditionally conformant** if it satisfies every applicable **MUST** requirement but departs from one or more applicable **SHOULD** requirements.

Both grades are conformant. The distinction exists so that an implementation may honestly describe itself. An implementer who departs from a **SHOULD** requirement does not thereby become non-conformant, but the implementer SHOULD document each such departure and the reasoning behind it, so that the implementation's users can assess whether the departure matters for their use.

An implementation that fails even one applicable **MUST** requirement is **non-conformant** and **MUST NOT** describe itself as conformant, **MUST NOT** use the AxonOS name in a way that implies conformance, and is subject to the trademark provisions of the companion `legal/` material.

### 4.3 The meaning of a requirement on an interface

Many of this Standard's requirements are requirements on an interface — a requirement that a particular byte appear at a particular offset, that a particular handshake precede a particular exchange, that a particular error code be emitted in a particular circumstance. Such a requirement binds both sides of the interface.

When this Standard says that the intent observation record **MUST** be exactly twenty-eight bytes, this binds the kernel, which **MUST** emit exactly twenty-eight bytes, and it binds the software development kit, which **MUST** reject any record that is not exactly twenty-eight bytes. A requirement on an interface is satisfied only when both sides honour it; an implementation of either side that does not honour it is non-conformant.

### 4.4 Conformance is per-version

Conformance is always conformance with a specific version of this Standard. An implementation conformant with version 1.1.0 is not thereby conformant with a hypothetical future version 2.0.0, nor with a past version. When an implementation declares conformance, it **MUST** state the version, and a bare claim of "AxonOS conformance" without a version is incomplete and SHOULD be read as a claim about the latest version current at the time the claim was made.

### 4.5 Loss of conformance

An implementation that was conformant may cease to be conformant — because a later revision of the implementation introduces a regression, because a defect is discovered, or because the implementation is modified in a way that violates a requirement. When this occurs, the implementer has two honest courses, and **MUST** take one of them: either repair the regression before the next public release of the implementation, or cease describing that release as conformant and document the loss of conformance in the release notes. Continuing to describe a non-conformant implementation as conformant is a misrepresentation and a trademark violation.

---

## Section 5. Architectural overview

*The first two subsections of this section are informative; subsection 5.3 onward is normative.*

### 5.1 The problem the architecture solves

A brain-computer interface must satisfy three families of requirement simultaneously, and the tension among those families is what makes the architecture non-trivial.

First, it must be **timely**. The neural signals a BCI processes are not static data to be analysed at leisure; they are a live stream, and the user's experience of the interface — whether it feels like a direct extension of their volition or like a sluggish, unreliable intermediary — is determined almost entirely by the latency and the regularity of the processing. A BCI that takes an unpredictable amount of time to turn an intention into an action is not merely slow; it is, in the precise sense that matters to a user, broken, because the user cannot form a stable mental model of how their own interface behaves. Timeliness, for a BCI, means not merely low average latency but a low and provable worst-case latency, and a low jitter.

Second, it must be **safe with respect to neural data**. The data a BCI processes is among the most sensitive data a human being generates. It is not chosen, the way speech or writing is chosen; it is closer to involuntary, and it is correspondingly more revealing and more dangerous in the wrong hands. An architecture that treats neural data as ordinary application data — that lets any application that asks receive the raw signal, and trusts applications to behave well — has already failed, because the failure mode is not a crash but a slow, invisible erosion of the user's most intimate privacy.

Third, it must be **honest about consent**. A user's permission for their neural data to be processed is not a static fact established once at installation; it is a live, revocable grant, and the architecture must make revocation real — must make it so that when a user withdraws consent, the data genuinely and provably stops flowing, within a bounded and short time, and cannot be made to resume without a fresh, deliberate act by the user.

The AxonOS architecture is the resolution of the tension among these three requirements. It achieves timeliness by confining the real-time work to a deterministic substrate with a provable worst-case response time. It achieves neural-data safety by structuring access through a closed set of capabilities, so that entire categories of sensitive data are not merely access-controlled but are absent from the type system and therefore cannot be requested at all. It achieves honest consent by lifting consent below the application layer, into a kernel-level state machine whose transitions the application cannot forge and whose withdrawn state is terminal.

### 5.2 Why four layers

The architecture has exactly four layers because each layer corresponds to a distinct contract, and each contract corresponds to a distinct concern that must be reasoned about independently.

Fewer layers would conflate concerns. If the real-time signal processing and the application logic shared a layer, then the application's unpredictable execution time would contaminate the signal processing's timing analysis, and the worst-case response time could no longer be proven. If the capability filtering and the application shared a layer, then a bug in the application could leak data the capability system was meant to confine. The layers exist to make the contracts crisp, and the contracts exist to make the system analysable.

More layers would add interfaces without adding distinct concerns, and every interface is a cost: a place where a byte can be misplaced, a place where two implementers can diverge, a place where the timing analysis must account for a crossing. Four layers is the minimum that separates the four genuinely distinct concerns — acquisition, deterministic processing, application-boundary mediation, and application logic — and the architecture uses exactly that minimum.

### 5.3 The four-layer reference model

*This subsection is normative.*

A conformant AxonOS deployment **MUST** be structured as four layers, related as follows. Each layer's contract to the layer above and the layer below is defined in the section indicated.

The **acquisition layer** is the lowest layer. It comprises the analog front end, the analog-to-digital converter, and any pre-kernel signal conditioning. It delivers a stream of digital samples to the kernel across the acquisition interface. The acquisition layer's design is outside the normative scope of this Standard; the contract it must honour at the kernel boundary — deterministic delivery of samples — is stated in Section 10.5.

The **kernel** is the second layer. It ingests samples from the acquisition layer, executes the real-time signal-processing pipeline that transforms samples into typed intents, applies the capability filter, consults the consent state, and emits intent observations across the application binary interface to the software development kit. The kernel bears the real-time guarantees of Part II. Its internal structure is constrained by Sections 7 through 11; its external contracts are the acquisition interface below and the application binary interface above.

The **software development kit** is the third layer. It receives intent observations from the kernel across the application binary interface, presents them to the application through a typed, language-appropriate programming interface, mediates the application's capability declarations, and propagates the kernel's error codes to the application as typed errors. The software development kit's contract to the kernel is the application binary interface of Part IV; its contract to the application is the typed observation interface, which is constrained by Sections 12 through 14 and Section 20 but whose exact ergonomic form is left to the implementer.

The **application layer** is the highest layer. It is end-user software that consumes intent observations and acts on them. It is constrained by this Standard only at the capability-declaration interface (it must ship a conformant manifest, per Section 14) and at the error-handling interface (it must behave correctly when it receives the consent-related and rate-related error codes of Section 20). Beyond those constraints the application layer is outside the Standard's scope.

A conformant deployment **MUST** maintain the separation between these layers. Specifically, the kernel **MUST NOT** execute application-layer code, and the application **MUST NOT** be able to inject code into, or otherwise alter the timing behaviour of, the kernel's real-time pipeline. The reason is the timing analysis: the worst-case response time of Part II is proven on the assumption that the kernel's task set is fixed and known, and that assumption is violated, and the proof voided, if application code can run inside the kernel's timing domain.

### 5.4 The cross-cutting subsystems

*This subsection is normative.*

Three subsystems sit beside the four-layer stack rather than within any single layer, because their concerns cut across layers. Their contracts are normative; but unlike the four layers, not every one of them is present in every deployment.

The **consent subsystem** is present in every conformant deployment. It is the three-state finite-state machine of Section 15. It is logically orthogonal to the layer stack: it is consulted by the kernel before every intent observation is published, and a withdrawal of consent propagates through the kernel and the software development kit to terminate observation flow. Although the consent state machine is most naturally implemented within the kernel, the Standard treats it as a distinct subsystem because its contract — the timing of withdrawal, the non-reversibility of the withdrawn state, the trusted-path requirement — is distinct from the kernel's real-time contract and must be reasoned about separately.

The **Cognitive Hypervisor** is present only in deployments that drive a stimulation channel — that is, deployments in which the BCI not only records neural activity but also delivers electrical stimulation to neural tissue. Such deployments carry a safety obligation that read-only deployments do not: a stimulation pulse that exceeds a charge-density limit can damage tissue. The Cognitive Hypervisor is the subsystem that enforces the charge-density limit and interlocks stimulation with the consent state. It runs in the Secure World of an ARM TrustZone-M partition. A read-only BCI deployment — one that records but does not stimulate — does not include the Cognitive Hypervisor, and the Standard's requirements concerning it do not apply to such a deployment.

The **swarm-coordination subsystem** is present only in deployments with more than one acquisition node — for instance, a deployment in which a head-mounted unit and a separate limb-mounted unit must agree on a common timeline. A conventional single-node clinical deployment does not include swarm coordination, and the Standard's swarm requirements do not apply to it. The swarm subsystem extends the single-node real-time contract to a synchronised multi-node contract, as defined in Section 30.

A conformant deployment **MUST** include the consent subsystem. It **MUST** include the Cognitive Hypervisor if and only if it drives a stimulation channel. It **MUST** include the swarm-coordination subsystem if and only if it comprises more than one acquisition node. An implementer assessing conformance assesses against the requirements for exactly the subsystems the deployment includes.

### 5.5 A worked picture of data flow

*This subsection is informative.*

It is worth tracing, in concrete terms, the path of a single intent from a neuron's electrical activity to an application's response, because the trace makes the architecture's divisions tangible.

A user decides to move a cursor to the left. That decision is, at the level of physics, a pattern of electrical activity across a population of cortical neurons. The acquisition layer's electrodes register a small voltage fluctuation; the instrumentation amplifier raises it to a measurable level; the analog-to-digital converter samples it, producing, at this instant, one multi-channel sample of digital values. That sample, together with the samples before and after it, is delivered across the acquisition interface to the kernel.

The kernel's real-time pipeline now executes. Within a single processing epoch — a fixed window of, in the reference configuration, four milliseconds — the pipeline filters the sample stream to remove noise and artefact, extracts spatial and spectral features, and classifies those features against a model of the user's intent vocabulary. The classifier concludes, with some confidence, that the user intends a leftward movement. This conclusion is a typed intent: not a voltage, not a feature vector, but a single value drawn from the small, closed set of intents the kernel knows how to recognise.

The kernel now checks the capability filter. The application has declared, in its manifest, that it holds the navigation capability. A leftward-movement intent is a navigation intent. The capability check passes. The kernel checks the consent state. The user has granted consent and has not suspended or withdrawn it; the consent check passes.

The kernel now constructs an intent observation: a twenty-eight-byte record carrying the leftward-movement intent, the classifier's confidence, the timestamp from the kernel's monotonic clock, and the next sequence number for this observation stream. The kernel publishes that record across the application binary interface into the inter-process communication channel.

The software development kit, polling that channel, receives the twenty-eight-byte record, validates its structure, decodes it into a typed observation object appropriate to the application's programming language, and delivers it to the application through the application's registered observation handler.

The application receives a typed leftward-movement observation with a known confidence and a known timestamp, and moves the cursor.

The entire path, from the acquisition layer delivering the sample to the software development kit delivering the typed observation, completed within a bounded time — the worst-case response time of Part II — and the regularity of successive such paths is the jitter of Part II. The neural data never left the kernel; what left the kernel was the single, narrow, typed conclusion. The user's consent was checked, structurally, before the conclusion was allowed to flow. Every division in the architecture did a specific job in that trace, and the trace is the architecture's justification.

---

# Part II — The Real-Time Substrate

## Section 6. The execution model

### 6.1 The dual-core premise

*This subsection is normative.*

The reference architecture is a **dual-core** system, and the real-time guarantees of this Part are stated in terms of that architecture. A conformant kernel **MUST** be analysable as a dual-core system in the sense defined here, although it **MAY** be physically realised on hardware with a different core count provided the analysis remains valid.

The two cores have distinct roles. The **signal-processing core** executes the real-time signal-processing pipeline. It is, in the reference hardware, an ARM Cortex-M4F clocked at 168 megahertz: a core chosen for the determinism of its instruction timing, the presence of a hardware floating-point unit suited to the pipeline's filter arithmetic, and the maturity of its development tooling. The signal-processing core is the core on which the worst-case response time is proven; it is the core whose timing this Part governs.

The **application core** executes the application and the software development kit. It is, in the reference hardware, an ARM Cortex-A53 clocked at 1.2 gigahertz or higher, running a general-purpose operating system. The application core is fast but not deterministic: the general-purpose operating system it runs may preempt the software development kit at any time, may page memory, may service interrupts of its own. The application core therefore bears no real-time guarantee, and this Part says almost nothing about it; the one thing this Part requires of the application core is that its non-determinism be confined to itself and not be permitted to contaminate the signal-processing core's timing.

The two cores communicate through a region of shared static random-access memory, across a deterministic bus bridge, using the inter-process communication discipline of Section 10. That communication channel is the sole coupling between the deterministic world of the signal-processing core and the non-deterministic world of the application core, and the discipline of Section 10 exists precisely to ensure that the coupling transmits data without transmitting non-determinism.

### 6.2 The processing epoch

*This subsection is normative.*

The signal-processing core's work is organised into **processing epochs**. A processing epoch is a fixed-duration window within which the entire real-time pipeline executes exactly once, consuming the samples that arrived during the previous epoch and producing exactly one intent observation.

The epoch duration is a configuration parameter of the kernel. In the reference configuration it is four milliseconds, corresponding to an observation rate of 250 hertz. A conformant kernel **MUST** document its epoch duration, **MUST** hold that duration constant for the lifetime of a session, and **MUST** ensure that the worst-case response time, as defined in Section 8 and bounded in Section 9, does not exceed the epoch duration. The last requirement is the fundamental schedulability condition of the system: if the pipeline's worst-case response time exceeded the epoch duration, then an epoch could begin before the previous epoch's pipeline had finished, the two would contend, and the timing analysis would collapse. The worst-case response time being strictly less than the epoch duration is the condition that makes the system a hard-real-time system rather than a best-effort one.

### 6.3 The task set

*This subsection is normative.*

The work performed within a processing epoch is decomposed into a fixed set of **tasks**. A task is a unit of computation with a known worst-case execution time and a known deadline. The complete set of tasks that the signal-processing core executes is the **task set**.

A conformant kernel **MUST** have a task set that is **fixed and known at the time the timing analysis is performed**. This is the single most important constraint in this Part, and it is worth stating its consequence plainly: a conformant kernel **MUST NOT** admit a new task, **MUST NOT** alter the worst-case execution time of an existing task, and **MUST NOT** alter the period or deadline of an existing task, at runtime, except through the admission-control procedure of Section 7.4, which re-validates the timing analysis before permitting the change. The reason is that the worst-case response time is proven for a specific task set; a task set that can change without re-validation is a task set for which no worst-case response time has been proven.

The reference task set is documented in Appendix D. It comprises six signal-processing tasks — a Kalman-filter state update, a finite-impulse-response filter, a notch filter, an artefact-rejection stage, a common-spatial-pattern feature extractor, and a linear-discriminant classifier — together with one inter-process-communication publication task. The appendix gives each task's worst-case execution time and period.

### 6.4 Determinism as the design objective

*This subsection is informative.*

It is worth being explicit about what the execution model is optimising for, because the objective is unusual.

A general-purpose operating system optimises, broadly, for **throughput** and for **average-case latency**. It wants to complete as much work as possible per unit time, and it wants the typical request to be served quickly. It is, correspondingly, willing to tolerate a poor worst case: an occasional request that takes a hundred times longer than the typical one is an acceptable price for excellent typical performance, because the general-purpose operating system's users — interactive desktops, web servers, batch-processing clusters — are not harmed by an occasional outlier.

The AxonOS kernel optimises for neither throughput nor average-case latency. It optimises for a **provable and small worst case**. It does not care how much work it can do per unit time, because the work per epoch is fixed and small. It does not especially care about the average case, because the average case is not what the user experiences as the interface's character; the worst case is. A kernel whose pipeline averages four hundred microseconds but has a worst case of twelve hundred microseconds is, for the purpose of this Standard, worse than a kernel whose pipeline always takes nine hundred and seventy microseconds, even though the first kernel is faster on average — because the first kernel cannot be proven to fit within a four-millisecond epoch with margin, and the second kernel can.

This inversion of the usual objective — worst case over average case, provability over speed — is the conceptual core of the execution model, and it explains design decisions throughout this Part that would seem perverse in a general-purpose context. The choice of scheduling discipline in Section 7, the conservative utilisation ceiling in Section 7.3, the prohibition on heap allocation in the pipeline, the requirement that the inter-process communication never block — each of these trades average-case performance, or flexibility, or convenience, for worst-case provability. In the BCI domain that trade is correct, because in the BCI domain the worst case is what the user feels and what the safety case rests on.

---

*Part II continues in the sections that follow with the scheduling discipline, the timing analysis methodology, the dual-core contract, the inter-process communication discipline, and the clock semantics. Parts III through VII and the appendices complete the Standard. The architecture chapters in the `architecture/` directory elaborate each subsystem informatively and at length.*

## Section 7. Scheduling discipline

### 7.1 The required discipline

*This subsection is normative.*

A conformant kernel **MUST** schedule the tasks of its signal-processing core under the **Earliest-Deadline-First** discipline. Under Earliest-Deadline-First, abbreviated EDF, the scheduler always executes, among the tasks that are ready to run, the one whose absolute deadline is nearest. When a task with a nearer deadline becomes ready while a task with a farther deadline is running, the running task is preempted.

EDF is a dynamic-priority discipline: a task's effective priority is not a fixed attribute but is derived, at every scheduling decision, from how close its deadline is. This distinguishes EDF from fixed-priority disciplines such as Rate-Monotonic scheduling, in which each task is assigned a priority once and that priority never changes.

### 7.2 Why Earliest-Deadline-First

*This subsection is informative.*

The choice of EDF over the more common Rate-Monotonic discipline is deliberate and rests on a precise theoretical result.

For a set of independent, preemptible, periodic tasks on a single processor, the question "can this task set be scheduled such that every task always meets its deadline?" has a known answer for each discipline. Under Rate-Monotonic scheduling, a task set is guaranteed schedulable if its total processor utilisation — the sum, over all tasks, of each task's worst-case execution time divided by its period — does not exceed a bound that depends on the number of tasks and that approaches the natural logarithm of two, approximately 0.693, as the number of tasks grows. Under Earliest-Deadline-First, a task set is schedulable if and only if its total utilisation does not exceed 1.0.

The difference between a utilisation bound of approximately 0.693 and a utilisation bound of exactly 1.0 is the difference between a discipline that strands roughly thirty per cent of the processor as unusable headroom and a discipline that can in principle use the entire processor. For a system whose design objective is provable worst-case behaviour, the EDF bound is not merely more efficient; it is conceptually cleaner, because the schedulability test is a single inequality with no dependence on task count, and a single clean inequality is easier to incorporate into the admission-control procedure of Section 7.4 and easier to reason about when the task set is revised.

There is a second, subtler reason. Under Rate-Monotonic scheduling, the headroom is not distributed evenly: the lowest-priority task is the one that suffers first when the task set grows, and adding a task forces a re-examination of every lower-priority task's schedulability. Under EDF, the headroom is a single shared pool, and the schedulability of the whole task set is governed by the single utilisation sum. When the task set is revised — as it will be, across the lifetime of the Standard, as the pipeline evolves — the EDF analysis is revised by recomputing one sum, whereas the Rate-Monotonic analysis is revised by re-deriving a priority assignment and re-checking every task. For a Standard that intends to live for many years and to accommodate many revisions of the pipeline, the discipline whose analysis is stable under revision is the correct choice.

### 7.3 The utilisation ceiling

*This subsection is normative.*

Although Earliest-Deadline-First can in theory schedule any task set whose utilisation does not exceed 1.0, a conformant kernel **MUST NOT** admit a task set whose total utilisation exceeds a configured ceiling, and that ceiling **MUST** by default be 0.25.

The ceiling is far below the theoretical bound of 1.0, and the gap is deliberate. The theoretical bound assumes a model — independent, preemptible, periodic tasks with known and exact worst-case execution times, on a processor with no interrupts and no other demands — that no real system perfectly satisfies. A real signal-processing core services interrupts from the analog-to-digital converter, from the inter-core communication hardware, and from the radio; a real worst-case execution time is an estimate, tight but not infinitely tight; a real processor has cache and pipeline effects that the periodic-task model abstracts away. The gap between the 0.25 ceiling and the 1.0 theoretical bound is the margin that absorbs all of this: the interrupt load, the imprecision in the worst-case execution time estimates, the micro-architectural effects. A task set admitted at 0.25 utilisation against a 1.0 theoretical bound has a factor of four of margin, and that margin is what converts a theoretical schedulability result into a claim robust enough to underwrite a safety case.

A conformant kernel **MAY** provide a configuration option to raise the ceiling above 0.25, up to a maximum of 0.50. Raising the ceiling above 0.50 is **NOT RECOMMENDED** and an implementation that permits it cannot be unconditionally conformant. The reference configuration uses the default ceiling of 0.25, and the reference task set of Appendix D has a measured total utilisation of 0.160, comfortably within that ceiling.

### 7.4 Admission control

*This subsection is normative.*

Any runtime change to the task set — the addition of a task, the removal of a task, or a change to an existing task's worst-case execution time, period, or deadline — **MUST** be gated by an **admission-control** procedure that re-validates the timing analysis before the change takes effect.

The admission-control procedure **MUST** compute the total utilisation that the task set would have after the proposed change, and **MUST** permit the change if and only if that post-change utilisation does not exceed the configured ceiling. A proposed change that would push the utilisation past the ceiling **MUST** be refused, and the refusal **MUST** be reported to the requesting component as a typed error — the admission-refused error of Section 20.

A conformant kernel **MUST NOT** silently overcommit. It is not acceptable for a kernel, faced with a task-set change that would exceed the ceiling, to admit the change anyway and hope; the timing guarantee of Part II is void for an overcommitted task set, and a kernel that overcommits has silently ceased to be a hard-real-time system. The only conformant responses to a change that would exceed the ceiling are to refuse the change or — if the implementer has provided the configuration option of Section 7.3 — to have previously raised the ceiling, within the permitted range, by a deliberate configuration act whose consequences the implementer has accepted.

## Section 8. Timing analysis and worst-case response time

### 8.1 The quantity to be bounded

*This subsection is normative.*

The **worst-case response time** of the signal-processing pipeline is the maximum, taken over every admissible input and every admissible machine state, of the elapsed time from the start of a processing epoch to the moment the corresponding intent observation is published across the application binary interface.

The phrase "every admissible input and every admissible machine state" is essential and is what distinguishes a worst-case response time from an average or a typical measurement. The worst-case response time is not the slowest time observed during testing; it is the slowest time that could ever occur, including for inputs not yet tested and for machine states — cache contents, branch-predictor history, interrupt timing — not yet encountered. A worst-case response time is therefore not a measurement at all in the ordinary sense; it is an upper bound, and an upper bound must be established by an argument that covers cases never observed.

### 8.2 How the bound is established

*This subsection is normative.*

A conformant kernel's worst-case response time **MUST** be established at evidence level L1, as that level is defined in Section 22 — that is, by a formal argument, machine-checked, that covers every admissible input rather than a sample of inputs.

The reference implementation establishes its worst-case response time using a bounded model checker, a tool that explores the entire space of admissible inputs symbolically and either proves that the bound holds for every one of them or produces a concrete input for which it fails. The Standard does not mandate a specific tool; it mandates the property — a machine-checked proof over the entire input space — and any tool that delivers that property is acceptable. Section 22 elaborates the evidence levels and the acceptable tools.

A worst-case response time established only by measurement — by running the pipeline many times and taking the slowest observed time — is an evidence-level-L2 claim, not L1, and is **NOT** sufficient on its own to satisfy the requirement of this section. Measurement is valuable; the reference implementation measures extensively, and Section 9 requires certain clauses to carry L2 measured evidence in addition to L1 proof. But measurement alone cannot establish a worst-case response time, because measurement samples the input space and the worst case may lie in an unsampled region. The requirement of this section is for an L1 proof, and L2 measurement is a complement to that proof, not a substitute for it.

### 8.3 The composition of the bound

*This subsection is informative.*

The worst-case response time of the whole pipeline is, in the reference analysis, composed from the worst-case execution times of the individual tasks and the worst-case interference each task can suffer.

In a preemptive system, a task's response time is not merely its own execution time; it is its own execution time plus the time during which it is preempted by tasks with nearer deadlines. The reference analysis accounts for this by the standard response-time recurrence: the response time of a task is computed as its own worst-case execution time plus the sum of the interference from every task that can preempt it, where the interference from a preempting task is the number of times that task can be released during the response-time window multiplied by that task's worst-case execution time. The recurrence is solved iteratively, converging to a fixed point, and the fixed point is the task's worst-case response time. The worst-case response time of the whole pipeline is then bounded by the analysis of the last task to complete in the epoch.

The reference analysis additionally accounts for interference from interrupts, for the blocking that can occur when a task accesses a resource shared with the inter-process-communication publication task, and for the micro-architectural effects — cache misses, pipeline stalls — that the periodic-task model abstracts away. Each of these contributions is bounded conservatively, and the conservative bounds are what the factor-of-four utilisation margin of Section 7.3 absorbs. The detailed analysis, with the recurrence worked through for the reference task set, is in the architecture chapter on scheduling; Appendix D records the resulting numbers.

## Section 9. The dual-core real-time contract

### 9.1 The contract

*This subsection is normative.*

A conformant kernel **MUST** satisfy all six clauses of the **dual-core real-time contract**. The clauses are designated DC1 through DC6. For each clause, the contract states the requirement, the numerical bound, and the evidence level at which the bound **MUST** be substantiated. Evidence levels are defined in Section 22.

**DC1 — end-to-end worst-case response time.** The worst-case response time of the signal-processing pipeline, as defined in Section 8.1, **MUST NOT** exceed 1000 microseconds. This bound **MUST** be substantiated at evidence level L1.

**DC2 — observation cadence jitter.** The jitter of the intent-observation cadence — the standard deviation of the interval between successive observations, measured over a soak of at least twelve hours — **MUST NOT** exceed 10 microseconds at the three-sigma envelope. This bound **MUST** be substantiated at evidence level L2.

**DC3 — inter-process-communication slot latency.** The time to transmit one intent-observation slot across the shared-memory inter-process-communication channel, in one direction, **MUST NOT** exceed 0.5 microseconds. This bound **MUST** be substantiated at evidence level L1.

**DC4 — deadline-miss detection latency.** If a task of the signal-processing core misses its deadline, the kernel **MUST** detect that miss within two scheduler ticks. This bound **MUST** be substantiated at evidence level L1.

**DC5 — graceful degradation under application-core suspension.** If the application core is suspended — by its general-purpose operating system, by a debugger, by a power-management event — the signal-processing core **MUST** continue to operate, and **MUST NOT** lose any intent observation, for at least one second of application-core suspension. This bound **MUST** be substantiated at evidence level L2.

**DC6 — sensor-reconnection recovery latency.** If the acquisition layer is disconnected and subsequently reconnected, the kernel **MUST** resume producing valid intent observations within 100 milliseconds of reconnection. This bound **MUST** be substantiated at evidence level L2.

### 9.2 The meaning of the evidence-level annotations

*This subsection is normative.*

The evidence-level annotation on each clause is itself a normative requirement. A kernel that satisfies the numerical bound of DC1 but has established it only by measurement, not by proof, does not satisfy DC1, because DC1 requires the bound at level L1 and measurement is level L2. Conversely, a kernel that satisfies the numerical bound of DC2 by measurement satisfies DC2, because DC2 requires level L2 and does not require a proof; a proof of DC2 would be welcome but is not mandated, in recognition of the fact that jitter is a physical, statistical quantity for which a measured bound over a long soak is the appropriate and achievable form of evidence.

A claim of conformance with the dual-core contract **MUST** be accompanied, in the implementation's published material, by the evidence artefact for each clause at the level the clause requires: the proof artefact for the L1 clauses, the soak-test trace for the L2 clauses. The companion `VALIDATION.md` defines the form these artefacts take and the catalogue in which they are recorded.

### 9.3 The reference implementation's measured values

*This subsection is informative.*

The reference implementation, on the reference hardware, satisfies the dual-core contract with the following measured values, recorded here for the reader's orientation. The authoritative, evidence-linked catalogue is in `VALIDATION.md`.

For DC1, the L1-proven upper bound is 1000 microseconds and the L2-measured worst observed value, over a twelve-hour soak comprising approximately 10.8 million epochs, is 972 microseconds, with zero deadline misses. For DC2, the measured jitter is 2.1 microseconds at one sigma. For DC3, the L1-proven bound is 0.5 microseconds and the measured value is 0.2 microseconds. The reference implementation thus satisfies every clause with margin, and the margin is itself part of the evidence: a system that satisfied the contract with no margin would be a system whose next minor revision would likely violate it.

## Section 10. Inter-process communication

### 10.1 The channel

*This subsection is normative.*

The signal-processing core and the application core **MUST** communicate through a single-producer, single-consumer, lock-free ring buffer located in a region of static random-access memory accessible to both cores.

The producer is a task of the signal-processing core; the consumer is the software development kit on the application core. The channel is single-producer and single-consumer because exactly one task writes and exactly one component reads; this is the simplest possible concurrency discipline and the one most amenable to a worst-case timing analysis. The channel is lock-free because a lock would introduce the possibility of the producer blocking on the consumer, and a producer that can block is a producer whose worst-case timing depends on the consumer's behaviour, which would couple the deterministic signal-processing core to the non-deterministic application core and void the timing analysis.

### 10.2 The slot

*This subsection is normative.*

The ring buffer is divided into fixed-size **slots**. Each slot **MUST** be exactly 32 bytes: 28 bytes for the intent-observation record of Section 19, followed by a 4-byte trailing copy of the low 32 bits of the record's sequence number.

The trailing sequence-number copy implements the consistency-checking discipline of Section 10.4. The slot size of 32 bytes is chosen so that one slot occupies exactly one half of a 64-byte cache line, ensuring that a slot never straddles a cache-line boundary and therefore never requires two cache-coherency transactions to read or write.

### 10.3 The producer discipline

*This subsection is normative.*

The producer — the inter-process-communication publication task of the signal-processing core — **MUST NOT**, on the path that publishes a slot, perform any operation that could block or that could allocate memory from a heap.

This is an absolute prohibition and it is the inter-process-communication counterpart of the fixed-task-set requirement of Section 6.3. A blocking operation on the publication path would couple the producer's timing to whatever it blocked on; a heap allocation on the publication path would introduce an operation whose worst-case time is, in general, unbounded. The publication path **MUST** consist only of operations whose worst-case time is bounded and known: writes to the slot, a memory barrier, and an update of the ring buffer's write index.

### 10.4 The consistency discipline

*This subsection is normative.*

Because the channel is lock-free, the consumer may attempt to read a slot at the same moment the producer is writing it. The kernel **MUST** implement a consistency discipline that allows the consumer to detect such a concurrent access and retry, rather than reading a torn, half-written slot as if it were valid.

The required discipline is the **sequence-number consistency check**. The producer writes the slot's sequence number into the intent-observation record at the start of the slot, then writes the remaining 24 bytes of the record, then writes the trailing 4-byte copy of the sequence number at the end of the slot, with a memory barrier ensuring the trailing copy is not made visible before the body. The consumer reads the trailing copy first, then the body, then the leading sequence number; if the leading and trailing sequence numbers disagree, the consumer was racing the producer, the slot is inconsistent, and the consumer **MUST** discard the read and retry. If they agree, the slot was written completely before the consumer read it, and the slot is valid.

### 10.5 The acquisition interface

*This subsection is normative.*

The interface between the acquisition layer and the kernel — the path by which digital samples enter the kernel — **MUST** deliver samples with deterministic completion semantics. Concretely, sample delivery **MUST** be by a direct-memory-access channel whose completion is signalled to the kernel by an interrupt at a known, bounded latency, and the kernel's timing analysis **MUST** account for that interrupt as a source of interference per Section 8.3.

The acquisition layer's internal design is, as stated in Section 1.3, outside the Standard's scope. What is within scope, and what this subsection requires, is the completion semantics at the kernel boundary: the kernel must be able to know, at a bounded latency, that a sample has arrived, so that the sample can be incorporated into the timing analysis.

## Section 11. Clock and time

### 11.1 The monotonic clock

*This subsection is normative.*

A conformant kernel **MUST** expose a single **monotonic clock** with a resolution of one microsecond or finer.

The clock is monotonic in the strict sense: successive reads of the clock **MUST NOT** ever return values in decreasing order. The clock **MUST** be derived from a hardware time source — in the reference implementation, the cycle-counter register of the signal-processing core — and **MUST NOT** be subject to adjustment, slewing, or stepping during a session. A clock that could step backward would void the sequence-number and timestamp semantics of the intent observation; a clock that could step forward would corrupt the jitter measurement. The monotonic clock is the system's single authoritative timeline, and its monotonicity is not negotiable.

### 11.2 The clock's range

*This subsection is normative.*

The monotonic clock **MUST** be represented with sufficient range that it does not wrap within the operating lifetime of the device. A 64-bit microsecond counter satisfies this requirement with enormous margin: 2 to the 64th power microseconds is approximately 584,000 years. A conformant kernel **MUST** use a counter of at least 64 bits for the monotonic clock, and **MUST NOT** use a narrower counter whose wrap would have to be handled, because wrap-handling logic is a source of bugs and the 64-bit counter makes it simply unnecessary.

### 11.3 Timestamps in intent observations

*This subsection is normative.*

Every intent observation carries, in the timestamp field defined in Section 19, the value of the monotonic clock at the instant the kernel emitted that observation. The timestamps of successive observations from a single stream are therefore strictly increasing, and the difference between consecutive timestamps is the inter-observation interval whose standard deviation is the jitter of clause DC2.

---

# Part III — The Security and Privacy Model

## Section 12. The capability system

### 12.1 The capability principle

*This subsection is normative.*

Access by the application to intent observations **MUST** be mediated by a **capability system**. A capability is a type-level token authorising exactly one narrowly defined category of intent observation. The set of capabilities is **closed**: it is fixed at the application binary interface version, and an intent observation whose category corresponds to no capability in the set **MUST NOT** cross the kernel boundary.

The defining property of the capability system, the property from which its privacy guarantee flows, is that a capability is a **type**, not a runtime permission flag. The distinction is the subject of Section 12.2 and is the conceptual heart of the privacy model.

### 12.2 Capabilities as types, not flags

*This subsection is informative, but the design decision it explains is normative and is stated in 12.1 and 13.*

There are two ways to build an access-control system for a category of data, and the difference between them is the difference between the AxonOS privacy model and the conventional one.

The conventional way is the **runtime permission flag**. The data exists; the code that could deliver it exists; and a runtime check — an `if` statement testing a permission bit — stands between the data and the recipient. If the check passes, the data flows; if it fails, it does not. This is how file permissions work, how most operating-system capability bits work, how the permission dialogs of mobile applications work.

The runtime-permission-flag approach has three structural weaknesses, and in the BCI domain each of them is serious. First, the check can be wrong: a typo in the permission constant, an inverted condition, a missing check on one of several code paths, and the data flows when it should not, silently, with no crash to signal the error. Second, the check can be removed: a future maintainer, working quickly, deletes the `if` statement — perhaps believing it redundant, perhaps merging a branch carelessly — and a regression ships in which the data flows unconditionally. Third, and most fundamentally, the data exists: even when the check is correct and present, the sensitive data is sitting in the system's memory, and any memory-disclosure bug anywhere in the system — a buffer over-read, a use-after-free, an uninitialised-memory leak — can expose it, because it is there to be exposed.

The AxonOS way is the **capability as type**. A category of data that no capability authorises does not have a type in the kernel's interface. There is no `RawNeuralSignal` type. The function that would deliver raw neural signal cannot be written, because its return type does not exist; the code path that would carry raw neural signal cannot be constructed, because the value it would carry has no type to inhabit. The protection is not an `if` statement that stands between the data and the recipient; the protection is that the data, as a typed value crossing the kernel boundary, never comes into existence at all.

This converts each of the three weaknesses of the runtime flag into a non-issue. The check cannot be wrong, because there is no check; there is a type system, and a type system's enforcement is not a runtime conditional that can be mis-written. The check cannot be removed, because there is nothing to remove; a future maintainer who wished to expose raw neural signal would have to add a type, add the functions that produce and consume values of that type, and add the code paths that carry it — a conspicuous, reviewable, deliberate act, not a quiet deletion of an `if`. And the data does not exist as a boundary-crossing typed value, so a memory-disclosure bug in the application-facing interface has nothing of that category to disclose.

This is the reason the capability system is the privacy model, and not merely a part of it. The privacy guarantee is structural: it is a property of what types exist, and types are checked by the compiler, before the system ever runs.

### 12.3 The closed set of capabilities

*This subsection is normative.*

The set of capabilities at application binary interface version 1 is closed and comprises exactly four members. A conformant kernel **MUST** support exactly these four and **MUST NOT** support any capability outside this set.

The **navigation capability** authorises observations of directional intent: cursor movement, focus changes, scrolling. Its maximum observation rate is 50 hertz.

The **workload-advisory capability** authorises observations of a coarse, three-level estimate of the user's cognitive load — low, medium, or high. Its maximum observation rate is 1 hertz.

The **session-quality capability** authorises observations of a scalar quality metric, in the range zero to one, describing the current signal quality. Its maximum observation rate is 2 hertz.

The **artefact-events capability** authorises edge-triggered observations that an artefact — a muscle movement, an electrode disturbance — has been detected or has cleared. Its maximum observation rate is 10 hertz.

The byte-level discriminants of these four capabilities, and their representation in the capability-set bitfield, are defined in Section 14.

### 12.4 The rate ceilings

*This subsection is normative.*

Each capability carries a maximum observation rate, stated in Section 12.3. The kernel **MUST** enforce these ceilings: an application that, in its manifest, declares a maximum rate exceeding the ceiling for one of its declared capabilities **MUST** be refused at manifest-installation time, and a software development kit that requests observations faster than the declared rate **MUST** receive the rate-exceeded error of Section 20 rather than additional observations.

The ceilings are not arbitrary. The workload-advisory ceiling of 1 hertz, in particular, is a privacy control: a coarse cognitive-load estimate sampled once per second cannot be assembled into the fine-grained cognitive timeline that a higher rate would permit. The ceiling is the mechanism that keeps the workload-advisory capability advisory and prevents it from becoming a profiling instrument.

## Section 13. Neural permissions and the prohibited categories

### 13.1 The principle of structural prohibition

*This subsection is normative.*

Certain categories of neural data are not merely access-controlled by this Standard; they are **structurally prohibited**. A structurally prohibited category is one for which no capability exists, will exist in any minor or patch revision of this Standard, or can be added without the major-version amendment procedure of Section 28.

### 13.2 The four prohibited categories

*This subsection is normative.*

The following four categories of neural data are structurally prohibited at application binary interface version 1. A conformant kernel **MUST NOT** provide any capability, type, or interface that exposes any of them to the application layer.

**Raw neural signal.** The unprocessed or lightly processed sample stream from the acquisition layer. The application receives typed intents, never the signal from which those intents were derived.

**Affective state.** Any representation of the user's emotional state. AxonOS does not infer emotion, and provides no capability that would expose an emotion estimate if one were inferred.

**Cognitive profile.** Any persistent, identifying representation of the user's cognitive characteristics — a representation that could be accumulated across sessions into a stable fingerprint of how this particular mind works.

**Biometric identity.** Any representation of neural activity usable to identify the user as an individual, as distinct from interpreting their current intent.

### 13.3 Why these four

*This subsection is informative.*

The four prohibited categories are not an arbitrary list. They are the four categories whose plausible downstream uses are, on examination, predominantly harmful to the user whose neural data they are.

Raw neural signal is prohibited because it is the universal solvent: from the raw signal, given enough computation, every other category — affective state, cognitive profile, biometric identity — can in principle be derived, and so exposing the raw signal would render every other prohibition meaningless. The raw signal is prohibited so that the other prohibitions can be meaningful.

Affective state is prohibited because an emotion estimate is an instrument of manipulation. A system that knows the user's emotional state, and that is operated by a party whose interests differ from the user's, can time its persuasion, its pricing, its demands, to the moments of the user's greatest vulnerability. There is no use of a continuously available affective-state estimate that is reliably in the user's interest, and many that are reliably against it.

Cognitive profile is prohibited because a persistent cognitive fingerprint is an instrument of discrimination. A profile of how a particular mind works — its speed, its lapses, its characteristic patterns — is exactly the kind of data that, in the hands of an employer, an insurer, or a credentialing body, becomes a basis for exclusion. The prohibition exists so that using a BCI cannot become a precondition for being profiled.

Biometric identity is prohibited because neural-pattern identification is an instrument of surveillance. A BCI that could identify its user from their neural activity could be made to report who is using it, and a population of such BCIs could be made into an identification network. The prohibition keeps the BCI an instrument the user wields, not an instrument that watches the user.

### 13.4 The cost of reversal

*This subsection is normative.*

The structural prohibition of the four categories is one of the constitutional commitments of this Standard, in the sense defined in Section 28. It cannot be reversed by a minor or patch revision. Reversing it — adding a capability that exposes a prohibited category — requires a major-version amendment, a published harm analysis, a ninety-day notice period, and the approval of the governance body in effect at the time, as Section 28 specifies. The cost of reversal is set deliberately high, because a commitment that can be cheaply reversed is not a commitment.

## Section 14. The manifest format

### 14.1 The purpose of the manifest

*This subsection is normative.*

Every application **MUST** ship a **manifest**: a signed, structured record by which the application declares its identity, the capabilities it requests, and the maximum observation rate at which it wishes to receive observations. The kernel **MUST** verify and install the manifest before the application receives any observation, and **MUST** refuse to deliver observations to an application whose manifest is absent, malformed, or invalidly signed.

### 14.2 The manifest fields

*This subsection is normative.*

A manifest **MUST** be encoded as a Concise Binary Object Representation map, per [RFC8949], with exactly the following four fields.

The **application identifier** is a string in reverse-DNS form — for example, the string formed by reversing the components of a domain name and appending an application name — of at most 64 bytes encoded as UTF-8. It identifies the application.

The **capability set** is a 32-bit unsigned integer in which each of the low four bits, bits 0 through 3, corresponds to one of the four capabilities of Section 12.3, in the order navigation, workload-advisory, session-quality, artefact-events. A set bit declares that the application requests the corresponding capability. Bits 4 through 31 are reserved and **MUST** be zero; the constant value 0x0000000F is the mask of admissible bits, and a manifest in which any bit outside that mask is set **MUST** be refused.

The **maximum rate** is a 16-bit unsigned integer giving the observation rate, in hertz, that the application requests. It **MUST NOT** exceed the smallest of the rate ceilings, defined in Section 12.3, of the capabilities the application declares.

The **signature** is a 64-byte Edwards-curve digital signature, per [FIPS186-5], computed by the application developer's signing key over the canonical Concise Binary Object Representation encoding of the three preceding fields.

### 14.3 Manifest verification

*This subsection is normative.*

At manifest-installation time the kernel **MUST** perform, and **MUST** pass, all of the following checks before installing the manifest. The signature **MUST** verify against the developer's published signing key. The application identifier **MUST NOT** exceed 64 bytes. The capability set **MUST NOT** have any bit set outside the admissible mask 0x0000000F. The maximum rate **MUST NOT** exceed the smallest rate ceiling among the declared capabilities. A manifest that fails any of these checks **MUST** be refused, and the refusal **MUST** be reported as the signature-invalid or the reserved-field error of Section 20, as appropriate to the failure.

## Section 15. Consent state semantics

### 15.1 The three states

*This subsection is normative.*

Consent is the user's permission for intent observations to flow, and it is enforced by the kernel, not by the application. Consent state is held **per manifest installation**, not per device: distinct applications installed on the same device may be in distinct consent states simultaneously. A manifest installed through the trusted path of Section 16 **MUST** begin in the **Granted** state; there is no separate pending state, and the act of installing a signed manifest through the trusted path constitutes the user's initial grant.

The consent state of a manifest is exactly one of three values, each with a one-byte discriminant. **Granted** (`0x01`): intent observations flow to the application normally. **Suspended** (`0x02`): intent observations do not flow, and a consumer that attempts to receive an observation **MUST** receive the consent-suspended error of Section 20 (code `0x05`). **Withdrawn** (`0x03`): all observation streams for the manifest are terminated and the manifest is invalidated, and a consumer **MUST** receive the consent-withdrawn error of Section 20 (code `0x06`). The discriminant `0x00` and the discriminants `0x04` through `0xFF` are reserved and **MUST NOT** be emitted by a conformant implementation.

### 15.2 The admissible transitions

*This subsection is normative.*

The consent state machine admits exactly the following transitions, each effected only by a trusted-path event of Section 16: from **Granted** to **Suspended**, the user pausing observation; from **Suspended** to **Granted**, the user resuming; from **Granted** to **Withdrawn**; and from **Suspended** to **Withdrawn**. The idempotent re-application of the current state — Granted to Granted, Suspended to Suspended, Withdrawn to Withdrawn — is admissible and **MUST** be treated as a no-op that does not change the state. Every other transition is inadmissible and **MUST** be refused without effecting any state change.

### 15.3 The terminality of withdrawal

*This subsection is normative.*

The **Withdrawn** state is **terminal**. The transitions Withdrawn to Granted and Withdrawn to Suspended are inadmissible and **MUST** be refused. The only path by which a manifest may receive observations again after withdrawal is for the user to install a fresh manifest through the trusted path; a fresh manifest begins in Granted under Section 15.1, but it is a new installation, not a resumption of the withdrawn one.

The non-reversibility of withdrawal is the central anti-coercion property of the consent system: were Withdrawn to Granted admissible, a privileged operator or an application could pressure the system into silently restoring a withdrawn grant, defeating the user's revocation. This property is a constitutional commitment in the sense of Section 28 and **MUST NOT** be relaxed within the major-version line.

### 15.4 The timeliness of withdrawal

*This subsection is normative.*

A transition into the **Withdrawn** state **MUST** terminate every open observation stream for the affected manifest within **ten milliseconds** of wall-clock time from the receipt of the trusted-path withdrawal event. Withdrawal that is not timely is not withdrawal; the bound exists so that a user who revokes consent can rely on the revocation taking effect within a human-perceptible interval.

### 15.5 Persistence and tamper response

*This subsection is normative.*

Consent state **MUST** persist across device power cycles: a manifest Granted at shutdown is restored as Granted, a Suspended manifest as Suspended, a Withdrawn manifest as Withdrawn. The stored state **MUST** be integrity-protected. If, at boot, the integrity of a manifest's stored consent state cannot be verified, the implementation **MUST** default that manifest to **Withdrawn**, **MUST** record an audit event, and **MUST NOT** deliver observations for it until the user installs a fresh manifest through the trusted path. A failed integrity check is treated as a hostile-modification event, not a recoverable error. The wire encoding of a consent event, and the reference implementation of this state machine, are specified in the `axonos-consent` component identified in Section 31.

## Section 16. The trusted path

### 16.1 Definition

*This subsection is normative.*

The **trusted path** is the input channel through which consent-state transitions are signalled to the kernel, and which the application layer provably cannot synthesise. Every transition of the consent state machine of Section 15 **MUST** originate from a trusted-path event; the kernel **MUST NOT** effect a consent transition in response to any input that does not arrive through the trusted path.

### 16.2 Admissible trusted-path mechanisms

*This subsection is normative.*

A conformant implementation **MUST** provide at least one of the following as its trusted path, and **MUST NOT** expose any application-reachable interface capable of forging an event indistinguishable from one. The first is a **physical control** wired directly to the kernel's interrupt path, with debounce such that one actuation yields at most one event regardless of noise. The second is a **secure-world user interface** running in an isolated execution environment — for example a TrustZone-M secure-world partition — that the normal-world application cannot drive, observe, or impersonate.

### 16.3 Authentication

*This subsection is normative.*

Every trusted-path event **MUST** be authenticated before the consent transition it requests is admitted. The event carries a digital signature that the kernel **MUST** verify against the trusted-path public key provisioned in the device's secure element; an event whose signature does not verify **MUST** be refused with the signature-invalid error of Section 20 (code `0x08`) and **MUST NOT** cause any state change. The application layer **MUST NOT** be able to emit, forge, replay, or suppress a trusted-path event.

### 16.4 The audit record

*This subsection is normative.*

Every trusted-path event that the consent state machine accepts **SHOULD** be recorded in a tamper-evident audit log accessible to the device operator and not to the application layer. An audit record **SHOULD** include the kernel monotonic timestamp of the event, the affected manifest identifier, the from-state and the to-state, and a cryptographic hash of the event. The audit log is the evidence from which a withdrawal, and the time at which it took effect, can be reconstructed after the fact.

---

# Part IV — The Application Binary Interface

## Section 17. Application binary interface versioning

*This subsection is normative.* The application binary interface is versioned by a single integer. The current version is **1**. A conformant kernel and a conformant software development kit **MUST** both declare the version they implement, and **MUST** interoperate only with a counterpart declaring the same version. A change to the wire format of Section 19, to the handshake of Section 18, to the capability set, or to the error taxonomy of Section 20 is a change to the application binary interface and **MUST** be accompanied by an increment of the version and a major-version revision of this Standard.

## Section 18. The connection handshake

*This subsection is normative.* Every connection between a software development kit and a kernel **MUST** begin with a handshake in which each side transmits, as a 32-bit little-endian integer, the application binary interface version it implements. Each side **MUST** compare the version it received against the version it implements, and **MUST**, if they differ, terminate the connection and report the version-mismatch error of Section 20. Silent fallback to a lower version, or negotiation toward a common version, is **NOT** permitted: the handshake either confirms an exact match or it fails, because a partial interoperation between mismatched versions is exactly the kind of silent, subtle incompatibility the version discipline exists to prevent.

## Section 19. The intent-observation wire format

*This subsection is normative.* Every intent observation crossing the boundary from the kernel to the software development kit **MUST** be a record of exactly 28 bytes, little-endian, with fields at exactly the following byte offsets.

At offset 0, one byte, the **kind**: the discriminant of the capability to which this observation corresponds. At offset 1, one byte, the **flags**: a bitfield in which bit 0 is a consumer-advisory high-confidence indicator and bits 1 through 7 are reserved and **MUST** be zero. At offset 2, two bytes, the **confidence**: the kernel's classifier posterior, encoded as a Q1.15 fixed-point fraction. At offset 4, eight bytes, the **timestamp**: the value of the monotonic clock, in microseconds, at the instant of emission. At offset 12, eight bytes, the **sequence number**: a per-stream counter beginning at zero and incremented by one for each observation. At offset 20, four bytes, the **source node identifier**: the identifier of the acquisition node, zero for a single-node deployment. At offset 24, four bytes, the **reserved** field, which **MUST** be zero.

A software development kit receiving a record that is not exactly 28 bytes, or in which the reserved field is non-zero, or in which a reserved flag bit is set, or whose kind corresponds to a capability the application did not declare, **MUST** reject the record and terminate the connection with the appropriate error of Section 20.

## Section 20. The error taxonomy

*This subsection is normative.* The kernel **MUST** report errors to the software development kit using the following closed enumeration of one-byte codes, and the software development kit **MUST** propagate each as a typed error to the application.

Code 0x01, **version mismatch**: the handshake of Section 18 found differing versions. Code 0x02, **capability not declared**: the application requested an observation of a capability absent from its manifest. Code 0x03, **rate exceeded**: the observation rate exceeded the declared maximum. Code 0x04, **backpressure**: the consumer is too slow and the channel is full. Code 0x05, **consent suspended**: the user has suspended consent. Code 0x06, **consent withdrawn**: the user has withdrawn consent and the stream is terminated. Code 0x07, **reserved field non-zero**: a wire-format record violated a reserved-field or reserved-bit requirement. Code 0x08, **signature invalid**: a manifest or consent-event signature failed verification. Code 0x09, **admission refused**: the admission-control procedure of Section 7.4 refused a task-set change. Code 0xFF, **internal error**: an implementation defect; this code **SHOULD NOT** appear in a correct implementation in production. Codes 0x10 through 0xFE are reserved and **MUST NOT** be emitted.

## Section 21. Forward and backward compatibility

*This subsection is normative.* Within application binary interface version 1, the reserved fields and reserved bits of Section 19, and the reserved error-code range of Section 20, are the sole mechanism by which a future patch or minor revision may extend the interface. A reserved field or bit **MUST** be zero on emission by a version-1 implementation and **MUST** be checked for zero on receipt; this discipline ensures that a future revision which assigns meaning to a reserved field can detect, by the field's non-zero value, that it is communicating with a newer counterpart, while a version-1 implementation correctly rejects the unexpected non-zero value rather than misinterpreting it. A change that cannot be expressed through the reserved fields is a breaking change and requires a new application binary interface version per Section 17.

---

# Part V — Validation and Conformance

## Section 22. The evidence taxonomy

*This subsection is normative.* Every quantitative claim made under the AxonOS name **MUST** carry an **evidence level**, one of the three defined here, and **MUST** be accompanied by the artefact appropriate to that level. A quantitative claim without an evidence level is non-conformant with this Standard and **MUST NOT** be published under the AxonOS name.

**Level L1**, *formally proven*: the claim is a bound established by a machine-checked formal proof that covers the entire admissible input space. The artefact is the proof, in a form a third party can re-check with the named tool. A claimed worst-case bound that has not been proven over the entire input space is not L1.

**Level L2**, *measured on reference hardware*: the claim is a value measured on the reference hardware, under stated conditions, with the measurement trace published. The artefact is the trace, together with the post-processing that derived the headline number. A measurement on hardware other than the reference hardware is not L2.

**Level L3**, *independently validated*: the claim is an L2 measurement that has additionally been reproduced by an independent third party, on a separate instance of the reference hardware, and witnessed by a signed report. The artefact is the signed report identifying the reviewer, the date, the hardware, and the verdict. The AxonOS Project makes no L3 claim at version 1.1.0; the companion `VALIDATION.md` records this and identifies the first L3 claim the Project intends to produce.

## Section 23. Falsifiability

*This subsection is normative.* Every L1 and L2 claim **MUST** be stated as a **falsifiable prediction**: a statement of the form that, for all inputs in a stated domain, a stated property holds, with a stated artefact as witness. The claim's falsifier **MUST** be identifiable: for an L1 claim, a counterexample produced by the proof tool; for an L2 claim, a measurement under the stated conditions that violates the stated bound. A claim that cannot be falsified — because its domain is unstated, or its property vague, or no artefact could refute it — is not a claim in the sense this Standard requires, and **MUST NOT** be published under the AxonOS name as though it were one.

## Section 24. Conformance criteria

*This subsection is normative.* An implementation is conformant with version 1.1.0 of this Standard if and only if it satisfies every applicable normative requirement of Sections 5 through 23 and Sections 26 through 31, and passes the conformance suite defined in `CONFORMANCE.md` at the corresponding repository tag. The conformance suite is the executable expression of the Standard's requirements; the companion document defines its 57 tests, organised in six categories corresponding to the real-time contract, the capability system, the consent state machine, the wire format, the error taxonomy, and the validation policy.

## Section 25. Self-certification and Foundation review

*This subsection is normative.* An implementer **MAY** self-certify conformance by running the conformance suite and publishing the resulting report. An implementer **MAY** additionally request a **Foundation review**, in which the AxonOS Project re-runs a sample of the suite, inspects the evidence artefacts, and publishes an acknowledgement. A Foundation review certifies software conformance with this Standard; it does **not** certify a device, and **MUST NOT** be represented as a device certification or a regulatory clearance.

---

# Part VI — Governance and Evolution

## Section 26. Versioning

*This subsection is normative.* This Standard is versioned under semantic versioning, with a major, minor, and patch component. A **major** increment accompanies a breaking change: a change to a normative requirement, the addition or removal of a capability, a change to the wire format, or a relaxation of a real-time bound. A **minor** increment accompanies a backward-compatible addition. A **patch** increment accompanies an editorial correction that changes no requirement.

## Section 27. The amendment process

*This subsection is normative.* This Standard is amended through a **Request for Comments** process, defined in detail in `GOVERNANCE.md`. In summary: a proposed amendment is filed as a numbered document, is open for review for at least fourteen days, and is accepted only when the review period has elapsed with no unresolved substantive objection and the maintainer has marked it accepted. A breaking amendment additionally requires a ninety-day notice period and a migration document.

## Section 28. Stability commitments

*This subsection is normative.* Within a major-version line, the maintainers commit, and a conformant evolution of this Standard **MUST** honour, the following: no normative requirement is removed; no defined term is removed or redefined; no wire-format field is removed or repurposed; no real-time bound is relaxed, bounds being permitted to move only in the direction of tightening. The structural prohibition of the four neural-data categories of Section 13, the evidence-taxonomy discipline of Section 22, and the open licensing of the Standard are **constitutional commitments**: they may be altered only by a major-version amendment carrying a published harm analysis, and not by any minor or patch revision.

---

# Part VII — Integration

## Section 29. External standards alignment

*This subsection is informative.* This Standard is designed to compose with, not to replace, the established standards of the medical-device and brain-computer-interface domains. A deployment intended for medical use should be developed under a software-lifecycle process conformant with the relevant medical-device software-lifecycle standard, and its risk management should follow the relevant risk-management standard; this Standard is silent on lifecycle and risk process and therefore does not impede conformance with them. The Standard's glossary is aligned, where the two overlap, with the draft unified terminology for brain-computer interfaces being developed in the relevant standards body, and conflicts will be resolved in favour of that terminology once it is published.

## Section 30. Regulatory positioning and the swarm and Cognitive Hypervisor subsystems

*This subsection is informative for its regulatory content and normative for the subsystem contracts it references.* This Standard is not a regulatory clearance and confers none. A device built on a conformant AxonOS implementation is subject to the full regulatory regime of every jurisdiction in which it is deployed, exactly as it would be without AxonOS. What the Standard provides to a regulatory effort is a substrate whose behaviour is specified and evidenced, against which a submission can be drafted with less uncertainty than against an unspecified substrate. The Cognitive Hypervisor subsystem, required of stimulation-driving deployments per Section 5.4, enforces a neural-tissue charge-density limit and interlocks stimulation with consent; its contract is elaborated in the architecture material. The swarm-coordination subsystem, required of multi-node deployments per Section 5.4, extends the dual-core contract to a synchronised multi-node contract designated SC1 through SC6, also elaborated in the architecture material.

## Section 31. The reference implementation

*This subsection is informative.* The reference implementation of this Standard comprises seven openly licensed repositories: the canonical standard itself; the reference kernel; the reference software development kit; the reference consent subsystem; the reference swarm-coordination layer; the engineering Request-for-Comments archive; and the hardware-in-the-loop acquisition gateway. Each is licensed under the Apache License 2.0 or the MIT licence for its code and under the Creative Commons Attribution-ShareAlike 4.0 International licence for its specification text. The reference implementation is one conformant implementation of this Standard and is no more authoritative than any other; the Standard, not the reference implementation, is the definition of conformance.

---

# Appendices

## Appendix A — A worked worst-case-response-time calculation

*Informative.* This appendix works the response-time recurrence of Section 8.3 through the reference task set of Appendix D, showing the iterative solution converging to the worst-case response time, and is provided so that an implementer can validate their own analysis tooling against a known case. The full worked calculation, with each iteration of the recurrence tabulated, is maintained in the architecture chapter on scheduling.

## Appendix B — The complete error-code table

*Normative.* The complete enumeration of error codes is given in Section 20. This appendix reproduces it in tabular form for reference and adds, for each code, the typical circumstance of emission and the recommended application response. Codes 0x01 through 0x09 and 0xFF are assigned; codes 0x10 through 0xFE are reserved.

## Appendix C — The Concise Binary Object Representation encoding

*Informative.* This appendix summarises, for the implementer's convenience, the subset of [RFC8949] used by the manifest format of Section 14: the map type, the integer types, and the byte-string type, with the canonical-encoding requirements that make a manifest's signature well-defined.

## Appendix D — The reference task set

*Informative.* The reference task set comprises seven tasks. The Kalman-filter state update has a worst-case execution time of 80 microseconds and a period of 4 milliseconds. The finite-impulse-response filter, 320 microseconds and 4 milliseconds. The notch filter, 40 microseconds and 4 milliseconds. The artefact-rejection stage, 15 microseconds and 4 milliseconds. The common-spatial-pattern feature extractor, 160 microseconds and 4 milliseconds. The linear-discriminant classifier, 25 microseconds and 4 milliseconds. The inter-process-communication publication task, 0.2 microseconds and 4 milliseconds. The total worst-case execution time per epoch is approximately 640 microseconds, and the total utilisation is approximately 0.160, within the 0.25 ceiling of Section 7.3.

## Appendix E — Bibliography

*Informative.* The informative references that inform this Standard's design include the foundational result of Liu and Layland on scheduling algorithms for hard-real-time environments; the standard texts of Buttazzo and of Kopetz on hard-real-time and on distributed real-time systems respectively; the documentation of the Kani bounded model checker; and the established medical-device software-lifecycle and risk-management standards. Full citations are maintained in the bibliography file of the repository.

---

**End of the AxonOS Standard, version 1.1.0.**

*This document is the canonical normative text. Any rendering of it in another medium is informative. In the event of disagreement between this file, at the tagged commit, and any rendering, this file governs.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
