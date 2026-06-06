# The AxonOS Standard

**Version 1.1.0** — the canonical open technical standard for deterministic brain-computer interface software.

**Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

---

## What this repository is

This repository contains the **AxonOS Standard**: the open technical standard that defines the architecture, the real-time guarantees, the capability system, the consent semantics, the application binary interface, the validation methodology, and the conformance requirements that a software implementation must satisfy in order to declare itself a conformant brain-computer-interface software substrate.

The Standard exists to fill a specific and consequential gap. The software layer that sits between a brain-computer interface's neural-acquisition hardware and the intelligent applications that act on a user's intent is, at the time of this writing, undefined by any shared, openly published contract. Every brain-computer-interface software stack reinvents, privately, the decisions about how its signal-processing substrate must behave with respect to timing, how it must structure an application's access to neural data, how it must enforce a user's revocation of consent, and how its quantitative claims must be evidenced. The consequence of that private reinvention is that no two stacks interoperate, no claim made by one stack can be verified against another, and no clinician, researcher, or regulator can reason about a brain-computer interface's software behaviour without access to that one vendor's private documentation.

The AxonOS Standard ends that situation, for any implementer who adopts it, by publishing the missing contract. It is the deliberate analogue, for the brain-computer-interface domain, of what the POSIX specification did for operating-system interfaces, what the C language standard did for systems programming, and what the IETF's Request-for-Comments series did for network protocols: a single, openly licensed, precisely worded document against which independent implementations can be built and independently verified.

This repository is **the Standard itself** — the specification — not an implementation of it. The Standard defines a set of contracts; an implementation is a piece of software that honours those contracts. A reference implementation exists, in separate repositories identified in `STANDARD.md` Section 31, but the reference implementation is one conformant implementation among the many that the Standard makes possible, and it is no more authoritative than any other. The Standard, the text in this repository, is what defines conformance; the reference implementation merely demonstrates that the Standard is implementable.

## The documents in this repository

The Standard is not a single file but a small, deliberately organised set of documents. Each is **normative** — it defines requirements against which conformance is assessed — except where a document, or a passage within it, explicitly marks itself **informative**. The documents are as follows.

**`STANDARD.md`** is the canonical normative text. It is the heart of the repository and the authoritative definition of conformance. It comprises thirty-one numbered sections, organised into seven parts — Foundations; the Real-Time Substrate; the Security and Privacy Model; the Application Binary Interface; Validation and Conformance; Governance and Evolution; Integration — followed by five appendices. Every other document in the repository is a companion to this one, and in the event of any disagreement between `STANDARD.md` and a companion, `STANDARD.md` governs.

**`CONFORMANCE.md`** defines how an implementation is tested for conformance. It specifies the conformance suite: fifty-seven distinct tests, organised into six categories corresponding to the real-time contract, the capability system, the consent state machine, the wire format, the error taxonomy, and the validation policy. It is the executable expression of the Standard — where `STANDARD.md` states a requirement in prose, `CONFORMANCE.md` defines the test that decides, mechanically and reproducibly, whether an implementation has met it.

**`VALIDATION.md`** defines the evidence discipline. It establishes the three-level evidence taxonomy — L1, formally proven; L2, measured on reference hardware; L3, independently validated — under which every quantitative claim made under the AxonOS name must be graded and substantiated. It defines the publishing rule, which forbids any quantitative claim that does not carry an evidence level and link to an inspectable artefact, and the falsifiability requirement, which demands that every claim be a refutable prediction. It defines how a claim is re-graded or retracted when the evidence behind it changes.

**`CLAIMS.md`** is the **claims catalogue** that `VALIDATION.md` Section 5 requires: the single, maintained document that lists every quantitative claim the Project makes under the AxonOS name, each with its value, its evidence level, the link to the artefact from which it can be re-checked, and the finding that would falsify it. It is the one place where the publishing rule is auditable, and conformance category C6 checks it. It is maintained separately from the normative text — adding a claim, filling in an artefact link, or re-grading a claim does not change the Standard or its version — and it records honestly both what is evidenced and linked and what is measured but not yet published.

**`GOVERNANCE.md`** defines how the Standard itself changes. It establishes the Request-for-Comments amendment process through which every substantive change must flow; the constitutional commitments — the privacy prohibitions, the evidence discipline, the open licensing — that may be changed only by an exceptional procedure; and the three-phase transition of governing authority from the founding maintainer, through a technical steering committee, to a constituted Foundation.

**`GLOSSARY.md`** is the canonical glossary. It is normative for the meaning of every term it defines: where the glossary and any other AxonOS document use the same term, the glossary governs the term's meaning. It defines approximately one hundred and fifty terms, alphabetically, with a definition for each and, for many, an informative discussion.

The **`architecture/`** directory contains the architecture chapters. These are informative throughout — they impose no requirement — but they are substantial and genuinely useful: they elaborate the design and the reasoning of each major subsystem at a depth the normative Standard, which must be concise about requirements, cannot reach. The directory contains four chapters: `kernel.md`, on the real-time microkernel; `scheduling.md`, on the scheduling discipline and the worst-case-timing analysis; `capability-system.md`, on the capability system and neural permissions; and `consent.md`, on the consent subsystem.

Alongside these are the structural files of any well-formed repository: this `README.md`; the `LICENSE`; the `VERSION` file recording the current version; the `CHANGELOG.md` recording the Standard's release history; `SECURITY.md`, the policy for reporting a specification-level security concern; and `ROADMAP.md`, an **informative** statement of the intended path forward for the Standard and its reference implementation. `CITATION.cff` records how to cite the Standard.

## The reference implementation

This repository is the Standard, not its implementation. A reference
implementation exists — described normatively, without links, in
`STANDARD.md` Section 31 — and is provided here, informatively, as a set of
links, so that a reader arriving at the Standard has a path to the software
that demonstrates it. The reference implementation is **one** conformant
implementation among the many the Standard makes possible; it is no more
authoritative than any independent implementation, and the Standard, not the
reference implementation, defines conformance.

| Repository | Role |
|---|---|
| [`axonos-standard`](https://github.com/AxonOS-org/axonos-standard) | The canonical Standard — this repository |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | Engineering Request-for-Comments archive; the design record behind the Standard |
| [`axonos-kernel`](https://github.com/AxonOS-org/axonos-kernel) | Reference real-time microkernel: scheduling, bounded IPC, monotonic time |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Reference application boundary: typed intents, manifests, ABI |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Reference consent subsystem: the deterministic consent state machine |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Reference swarm-coordination layer for multi-node deployments |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | Hardware-in-the-loop acquisition gateway (integration fork) |

Each repository's code is licensed under Apache-2.0 OR MIT and its
specification text under CC-BY-SA-4.0, the same dual arrangement as the
Standard itself.

## How to read the Standard, by role

The Standard is long, because the brain-computer-interface domain is unforgiving and precision in an unforgiving domain is necessarily verbose. Different readers need different paths through it, and `STANDARD.md`'s own "How to read this Standard" section routes each kind of reader; this README summarises those routes so that a reader arriving at the repository can orient themselves before opening the canonical text.

### If you are an implementer

You intend to build a conformant kernel, software development kit, hardware gateway, or related component. You are the Standard's primary audience; its precision exists for your benefit. Read `STANDARD.md` in full, in order, at least once, and then treat Parts II through V — the real-time substrate, the security and privacy model, the application binary interface, and validation and conformance — as a reference to consult continuously during development. Read `CONFORMANCE.md` immediately afterward, because it defines the suite your implementation must pass and is, in effect, your specification's checklist. Read the architecture chapters in `architecture/` for the design reasoning behind the requirements — they will not tell you what conformance demands, but they will tell you *why* it demands it, and an implementer who understands the why makes the hundred small unforced decisions in a way that converges with other implementers rather than diverging from them. The note to the independent implementer at the end of each architecture chapter is addressed specifically to you.

### If you are an application developer

You intend to build an end-user brain-computer-interface application atop a conformant software development kit. You do not need the whole Standard. You need Sections 12 through 21 of `STANDARD.md` — the capability system, the structural prohibitions, the manifest format, and the application binary interface — in depth, because those define what your application is permitted to observe and how it must behave when consent changes or a rate is exceeded. You need the `capability-system.md` and `consent.md` architecture chapters, whose worked examples are written with you in mind — the assistive-application example in `capability-system.md` Section 9 traces an application very like the one you are likely building. You need the remainder of the Standard only as background.

### If you are a reviewer or an academic

You intend to evaluate the Standard's claims, scrutinise its evidence, and — in the best case — attempt to refute its quantitative predictions. Read Parts I and II of `STANDARD.md` for the architecture and the timing argument, then read `VALIDATION.md` in full for the evidence framework, then return to the specific sections whose claims you wish to test. The evidence taxonomy of `VALIDATION.md` Section 1 is the key to the entire repository's epistemics: every quantitative claim is graded by evidence level and linked to an artefact, and your first question of any number in any AxonOS document should be "at what level is this evidenced, and where is the artefact?" The Standard is written to make your work possible — every L1 and L2 claim is a falsifiable prediction with an identifiable falsifier — and the Project regards a serious attempt to refute one of its claims as among the most valuable things a reviewer can do.

### If you are a regulator or a safety engineer

You intend to assess a device built on a conformant AxonOS implementation. Read Section 15 of `STANDARD.md`, on consent; Section 22, on validation; the regulatory-positioning material in Section 30; the `consent.md` architecture chapter; and the security material. Understand clearly the modest thing this Standard is and the immodest things it is not. The Standard is **not a regulatory clearance** and confers none. A device built on a conformant AxonOS implementation is subject to the full regulatory regime of every jurisdiction in which it is deployed, exactly as it would be without AxonOS. What the Standard provides to a regulatory effort is a substrate whose behaviour is specified and evidenced, against which a regulatory submission can be drafted with less uncertainty than against an unspecified substrate. That is a real benefit, and it is a different and more modest thing than a clearance.

### If you are a contributor

You intend to propose a change to the Standard. Read `GOVERNANCE.md` first, in full, because it defines the Request-for-Comments process your proposal must follow and the constitutional commitments your proposal must respect. Then read the section of `STANDARD.md` you wish to amend, and the architecture chapter that elaborates it. Then read the existing Requests for Comments in the governance directory, to understand the prior art and the house style of amendment proposals. The contribution process is genuinely open: anyone may file a Request for Comments, and a proposal from an independent implementer is reviewed by exactly the same process, against exactly the same standard, as a proposal from the founding maintainer.

## The central conceptual moves of the Standard

A reader new to the Standard benefits from knowing, in advance, the handful of ideas on which everything else rests. There are four.

The first is the distinction between **the contract and the implementation**. The Standard defines contracts — statements of what must be true at an interface — and is deliberately silent about how either side of an interface achieves its obligations. Two conformant kernels may schedule their internal work completely differently, may be written in different languages, may run on different processors, and may share not a line of source code, and they are nonetheless both conformant, and both interoperable with the same software development kit, because they both honour the same contracts. The contract is the unit of standardisation; the implementation is free.

The second is the inversion of the usual optimisation target in the real-time substrate: **the worst case dominates the average case**. The kernel does not optimise for throughput or for typical-case latency, as general-purpose software does. It optimises for a provable and small *worst-case* response time, because the worst case is what a brain-computer interface's user actually experiences as the interface's character, and a worst-case bound, unlike an average, can underwrite a safety argument. This inversion explains design decisions throughout the Standard that would seem perverse in a general-purpose context.

The third is the choice of a **structural privacy guarantee over a procedural one**. The capability system makes a permission a *type*, not a runtime check, and makes a prohibited category of neural data a type that *does not exist*. A category with no type cannot be constructed as a value crossing the kernel boundary; the protection is not an `if` statement that can be mis-written or removed but the absence, enforced by the compiler before the system ever runs, of any way to express the dangerous thing. This is the most important idea in the Standard after the real-time guarantee itself.

The fourth is the **evidence discipline**: the rule that every quantitative claim made under the AxonOS name carries an evidence level and links to an inspectable artefact, or it does not appear at all. The discipline converts the Project's numbers from assertions a reader must take on faith into evidence a reader can verify, and the Standard holds its own quantitative content to exactly the discipline it imposes on implementers.

A reader who carries these four ideas into the Standard will find that a great many of its individual requirements, which can seem arbitrary in isolation, fall out almost inevitably from one or another of the four.

## The status of the Standard

This is **version 1.1.0**. The first canonical release was version 1.0.0 (2026-05-21); version 1.1.0 adds Sections 15 and 16 — the consent state semantics and the trusted path — completing the Security and Privacy Model of Part III.

The Standard is, at this release, in **Phase A** of the governance transition described in `GOVERNANCE.md`. Phase A is the founding configuration: the Standard is under the stewardship of its founding maintainer, who is the governing body for the Request-for-Comments process. The governance document defines, and the Project commits to, the gated three-phase path by which that founding stewardship will become first a distributed technical steering committee and then a constituted Foundation — a path designed in advance, at version 1.1.0, precisely so that the transition is an orderly execution of a pre-committed design rather than an improvised response to a future need.

The honest status of several forward-looking elements is recorded plainly in the documents themselves, in keeping with the evidence discipline. The Foundation does not yet exist; `GOVERNANCE.md` Section 7.4 says so. No claim has yet been independently reproduced at evidence level L3; `VALIDATION.md` Section 5.3 says so, and records what the first L3 claim is intended to be. The Project's discipline is to record what is true, including the truth of what is not yet accomplished, rather than to present an aspiration as a fact.

## Versioning

The Standard is versioned under semantic versioning, with a major, a minor, and a patch component, as `STANDARD.md` Section 26 defines. A major increment accompanies a breaking change — a change to a normative requirement, the addition or removal of a capability, a change to the wire format, a relaxation of a real-time bound. A minor increment accompanies a backward-compatible addition. A patch increment accompanies an editorial correction that changes no requirement. Conformance is always conformance with a specific version; an implementation conformant with version 1.1.0 makes no claim about any other version.

The authoritative text of the Standard, at any version, is the content of this repository at the Git commit corresponding to that version's release tag, recorded in the `VERSION` file. Any rendering of the Standard in another medium — an HTML page, a typeset document, a translation — is informative, and in the event of a discrepancy the repository file at the tagged commit governs.

## Conformance, in brief

The full conformance regime is defined in `CONFORMANCE.md`; this section gives the reader arriving at the repository enough to understand what conformance is before they open that document.

An implementation is **conformant with version 1.1.0 of the AxonOS Standard** if and only if it satisfies every applicable normative requirement of `STANDARD.md` and passes the conformance suite — the fifty-seven tests of `CONFORMANCE.md` Section 5 — at the corresponding repository tag.

Conformance is **scoped to the components an implementation provides**. The Standard governs a kernel, a software development kit, a consent subsystem, and — for deployments that need them — a Cognitive Hypervisor and a swarm-coordination layer. An implementation need not provide all of these; one that provides only a kernel is assessed only against the kernel requirements and the kernel's side of the interface contracts, and the conformance suite is organised so that the relevant subset of tests can be run against a partial implementation.

Conformance has **two grades**. An implementation that satisfies every applicable MUST requirement and every applicable SHOULD requirement is *unconditionally conformant*. One that satisfies every MUST but departs from one or more SHOULD requirements is *conditionally conformant*. Both are conformant; the distinction lets an implementation describe itself honestly. An implementation that fails even one applicable MUST requirement is *non-conformant* and must not describe itself as conformant.

An implementer **self-certifies** by running the conformance suite and publishing the resulting report. An implementer may additionally request a **Foundation review**, an optional independent confirmation of the self-certification. A Foundation review certifies *software conformance with this Standard*; it is not, and must not be represented as, a device certification or a regulatory clearance.

## The relationship to the reference implementation

A recurring source of confusion in open-standard projects is the relationship between the standard and its reference implementation, and the AxonOS Standard takes an explicit position, stated in `STANDARD.md` Section 1.5 and worth repeating here.

The Standard is primary. The reference implementation is one conformant implementation of the Standard, no more privileged than any other. If the reference implementation and the Standard disagree, the Standard is correct and the reference implementation has a defect. The reference implementation exists to demonstrate that the Standard is implementable, to provide a concrete artefact that implementers may study and against which the conformance suite is itself validated, and to serve as the substrate for the Project's own clinical and research work. It does not define the Standard; the Standard defines itself.

An independent implementation — one written by a team with no connection to the AxonOS Project, in a different language, for a different processor family — is exactly as conformant as the reference implementation if and only if it passes the conformance suite. The Standard is the arbiter; the conformance suite is the Standard's executable expression; and any implementation that passes the suite is conformant by definition, regardless of its provenance. A standard with only one implementation has not yet proven it is a standard, and the AxonOS Project intends, and the governance is designed around, the existence of independent implementations.

## Contributing

Changes to the AxonOS Standard flow through the public Request-for-Comments process defined in `GOVERNANCE.md`. The process is genuinely open: anyone may file a Request for Comments, and a proposal is judged on its merits regardless of who filed it.

A Request for Comments is a numbered document with seven required sections — a summary, a motivation that states the problem concretely, a detailed design giving the exact proposed text, an honest account of the drawbacks, the alternatives considered, the unresolved questions, and, for a breaking change, a migration guide. It is filed by adding it to the governance directory through the repository's ordinary pull-request mechanism. It is open for public review for a defined minimum period — fourteen days for an ordinary change, ninety days for a breaking change or a change touching a constitutional commitment — and is decided, with public reasoning, by the governing body in effect under the current governance phase.

Not every change requires a Request for Comments. A correction of a typographical error, a repair of a broken cross-reference, an improvement to informative prose that changes no requirement — these are ordinary pull requests. The dividing line is the word *normative*: a change that alters, adds, or removes a normative requirement is substantive and requires a Request for Comments; a change that touches only informative material or corrects an error without changing intent is an ordinary pull request. A contributor uncertain which category a change falls into should treat it as substantive and file a Request for Comments.

Before proposing a change, a contributor should read `GOVERNANCE.md` in full, should read the section of `STANDARD.md` they wish to amend together with its architecture chapter, and should read the existing Requests for Comments to understand the prior art and the expected form of a proposal.

## License

The normative text of the AxonOS Standard and its companion documents is released under the **Creative Commons Attribution-ShareAlike 4.0 International licence** — `SPDX-License-Identifier: CC-BY-SA-4.0`. The Standard may be reproduced, translated, and adapted under the terms of that licence; a derivative must be distributed under the same licence, and must attribute the original.

Code samples embedded within the documents are additionally made available, at the implementer's option, under the **Apache License 2.0** or the **MIT licence**, so that they may be incorporated verbatim into reference implementations without licence-compatibility concerns.

The open licensing of the Standard is a *constitutional commitment* in the sense of `GOVERNANCE.md` Section 2: it may be changed only by the exceptional constitutional-amendment procedure, and not by any ordinary revision. The right to fork the Standard, once granted, cannot be revoked.

The **AxonOS name** and associated marks are not licensed under the Creative Commons licence; their use is governed separately. A derivative or fork of the Standard may be created freely under the Creative Commons licence, but may not represent itself as *the* AxonOS Standard, and may not use the AxonOS name in a manner implying endorsement by, or identity with, the AxonOS Project. The separation of the freely licensed text from the controlled name is what allows the licence to be genuinely open while keeping the AxonOS name a meaningful indicator of the genuine Standard. The full licence terms are in the `LICENSE` file.

## A map of `STANDARD.md`

For the reader about to open the canonical text, the following is a map of its thirty-one sections and five appendices, so that the document's shape is visible before its detail.

**Front matter** establishes the requirement keywords (the RFC-2119 interpretation of MUST, SHOULD, MAY), the distinction between normative and informative material, and the routing of each kind of reader through the document.

**Part I, Foundations**, comprises five sections. Section 1 sets the scope — the systems the Standard governs, what it defines, what it explicitly does not, and its intended audiences. Section 2 lists the normative references. Section 3 gives the twelve most load-bearing defined terms, with `GLOSSARY.md` as the full canonical glossary. Section 4 defines what conformance means. Section 5 gives the architectural overview: the four-layer reference model and the three cross-cutting subsystems.

**Part II, the Real-Time Substrate**, comprises Sections 6 through 11. Section 6 defines the execution model — the dual-core premise, the processing epoch, the fixed task set. Section 7 defines the scheduling discipline, Earliest-Deadline-First, with its utilisation ceiling and admission control. Section 8 defines the timing-analysis methodology and the worst-case response time. Section 9 states the six-clause dual-core real-time contract, DC1 through DC6. Section 10 defines the inter-process-communication discipline. Section 11 defines the monotonic clock.

**Part III, the Security and Privacy Model**, comprises Sections 12 through 16. Section 12 defines the capability system and the closed set of four capabilities. Section 13 defines the four structurally prohibited categories of neural data. Section 14 defines the manifest format. Sections 15 and 16 define the consent state machine and the trusted path.

**Part IV, the Application Binary Interface**, comprises Sections 17 through 21: the versioning discipline, the connection handshake, the byte-exact intent-observation wire format, the error taxonomy, and the forward- and backward-compatibility rules.

**Part V, Validation and Conformance**, comprises Sections 22 through 25: the evidence taxonomy, the falsifiability requirement, the conformance criteria, and the distinction between self-certification and Foundation review.

**Part VI, Governance and Evolution**, comprises Sections 26 through 28: versioning, the amendment process, and the stability commitments including the constitutional commitments.

**Part VII, Integration**, comprises Sections 29 through 31: alignment with external standards, regulatory positioning together with the Cognitive Hypervisor and swarm subsystems, and the identification of the reference implementation.

**The appendices** provide a worked worst-case-response-time calculation, the complete error-code table, the Concise Binary Object Representation encoding summary, the reference task set, and the bibliography.

## The four-layer architecture at a glance

The Standard's architecture, defined normatively in `STANDARD.md` Section 5 and elaborated across the architecture chapters, is a stack of four layers with three cross-cutting subsystems beside it.

The **acquisition layer**, at the bottom, converts a physiological neural signal into a stream of digital samples. Its internal design is outside the Standard's scope; only its contract at the kernel boundary — deterministic delivery of samples — is governed.

The **kernel**, the second layer, is the deterministic substrate. It ingests samples, runs the real-time signal-processing pipeline under a provable worst-case timing bound, applies the capability filter, consults the consent state, and emits typed intent observations. The kernel bears the real-time guarantees.

The **software development kit**, the third layer, receives intent observations from the kernel across the application binary interface and presents them to the application through a typed, language-appropriate programming interface.

The **application layer**, at the top, is end-user software that consumes intent observations and acts on them. It is constrained by the Standard only at two interfaces — it must ship a conformant manifest, and it must behave correctly on receipt of the consent-related and rate-related errors — and is otherwise outside the Standard's scope.

Beside the stack are three cross-cutting subsystems. The **consent subsystem**, present in every deployment, is the three-state finite-state machine that makes a user's permission revocable in fact, enforced below the application, and terminal once withdrawn. The **Cognitive Hypervisor**, present only in deployments that drive a stimulation channel, enforces a neural-tissue charge-density limit and interlocks stimulation with consent. The **swarm-coordination subsystem**, present only in multi-node deployments, extends the single-node real-time contract to a synchronised multi-node contract.

## The dual-core contract at a glance

The kernel's real-time promise is the six-clause dual-core contract of `STANDARD.md` Section 9. In brief: clause DC1 bounds the end-to-end worst-case response time at one thousand microseconds, evidenced at level L1; clause DC2 bounds the observation-cadence jitter at ten microseconds at the three-sigma envelope, at level L2; clause DC3 bounds the inter-process-communication slot latency at half a microsecond, at L1; clause DC4 bounds the deadline-miss detection latency at two scheduler ticks, at L1; clause DC5 requires graceful degradation through at least one second of application-core suspension, at L2; clause DC6 bounds the sensor-reconnection recovery latency at one hundred milliseconds, at L2. The reference implementation satisfies every clause with margin, and the evidence artefacts are catalogued under the validation discipline.

## Frequently asked questions

**Is this a product I can install?** No. This repository is the Standard — the specification. It defines the contracts a conformant implementation must honour. The reference implementation is software, in separate repositories; this repository is the document against which that software, and any independent implementation, is measured.

**Is AxonOS a regulatory clearance for a medical device?** No, emphatically. The Standard is not a regulatory clearance and confers none. A device built on a conformant AxonOS implementation is subject to the full regulatory regime of every jurisdiction in which it is deployed. The Standard provides a specified, evidenced substrate against which a regulatory submission can be drafted; that is a genuine benefit and a different, more modest thing than a clearance.

**Can I build a conformant implementation without the reference code?** Yes; that is the point of a standard. You need `STANDARD.md`, which defines the contracts; `CONFORMANCE.md`, which is the executable test of whether you have honoured them; and the architecture chapters, which explain the reasoning. Your implementation may be in a different language, for a different processor, sharing no code with the reference, and it is exactly as conformant as the reference if it passes the suite.

**Why is the Standard so long?** Because the brain-computer-interface domain is unforgiving — a missed deadline, a leaked category of neural data, an unhonoured revocation of consent are safety and rights failures — and precision in an unforgiving domain is necessarily verbose. The length is the cost of leaving nothing ambiguous, and ambiguity is what causes independent implementers to diverge.

**Who governs the Standard?** At version 1.1.0, the founding maintainer, in Phase A of the governance transition. `GOVERNANCE.md` defines and commits the path toward a distributed technical steering committee and then a constituted Foundation. Every change, in every phase, flows through the public Request-for-Comments process.

**What can I rely on not changing?** Within a major-version line, no normative requirement is removed, no defined term is redefined, no wire-format field is repurposed, and no real-time bound is relaxed. Beyond that, the constitutional commitments — the privacy prohibitions, the evidence discipline, the open licensing — may be changed only by an exceptional procedure carrying an exceptional burden, so a user, an implementer, or a regulator may rely on those absolutely.

**How do I propose a change?** Through a Request for Comments, filed in the governance directory via a pull request, following the seven-section format `GOVERNANCE.md` defines. Anyone may file one.

**What is the most important idea in the Standard?** After the real-time guarantee, it is the structural privacy model: a capability is a type, not a runtime check, and a prohibited category of neural data is a type that does not exist. A dangerous category with no type cannot be constructed as a value crossing the kernel boundary; the protection is the compiler's refusal, before the system runs, not a check that could be mis-written or removed.

## Why a standard for this layer, and why now

It is worth setting out, for the reader deciding whether the Standard merits their attention, the argument for why a standard at this particular layer is needed and why the present moment is the right one to publish it.

The brain-computer-interface field is at a stage of development that other engineering fields have passed through before, and the pattern is recognisable. A field begins with a handful of pioneering systems, each a complete vertical stack built by one team, each solving the whole problem privately and in its own way. The pioneering systems are impressive, but they are islands: nothing one of them does can be reused by another, nothing one of them claims can be checked against another, and the field's collective knowledge is fragmented into as many incompatible pieces as there are teams. The field matures, when it matures, by identifying the layers at which a shared contract would let the islands become an archipelago — would let components be mixed, claims be compared, and knowledge be pooled — and by doing the unglamorous work of writing those contracts down precisely enough to build against.

The operating-systems field passed through this with the POSIX specification, which let a program written against the contract run on any conformant system. The systems-programming field passed through it with the C language standard, which let a compiler from one vendor and a program from another interoperate. The networking field passed through it with the Request-for-Comments series, which let a router from one manufacturer and a host from another speak. In each case the standard did not invent the technology; the technology already existed, in the islands. The standard did something different and equally valuable: it wrote down the contract precisely enough that the islands could connect.

The brain-computer-interface field has not yet passed through this stage at the software-substrate layer. The layer between neural-acquisition hardware and intent-consuming applications — the layer that does the real-time signal processing, that mediates access to neural data, that enforces consent — is, today, an island layer: every serious brain-computer-interface system has one, and no two of them share a contract. The AxonOS Standard is an attempt to write down the contract for that layer, so that the field's substrate layer can begin to connect the way the operating-systems, systems-programming, and networking layers connected before it.

The argument for *now*, rather than later, has two parts. The first is that the cost of standardising a layer rises with the number of incompatible islands that must be reconciled; a contract published while the field is still young, before the incompatible private substrates have ossified into installed bases, is a contract the field can actually adopt. The second is specific to this domain: the brain-computer-interface field is approaching the threshold of broad clinical and consumer deployment, and the behaviours this Standard governs — the timing that determines whether an interface is safe, the handling of neural data that determines whether a user's privacy survives, the consent enforcement that determines whether a user's autonomy is real — are behaviours that, once devices are widely deployed, will be very hard to retrofit a discipline onto. A standard for these behaviours is most valuable published *before* the deployment wave, as a foundation the wave can build on, rather than after it, as a remediation the wave must be forced to accept.

## The design rationale, in summary

The architecture chapters give the design rationale in full informative depth; this section summarises, for the reader who wants the reasoning before the detail, the answers to the questions a sceptical engineer asks first.

**Why a separate kernel, rather than a real-time-patched general-purpose operating system?** Because the Standard requires the worst-case response time to be established by a formal proof ranging over the entire input space, and that proof is tractable for a small, purpose-built kernel of a few thousand analysable lines and intractable for a general-purpose operating system of millions. And because the structural privacy model — the capability system's prohibitions — is a property of a small, purpose-built interface, and retrofitting it onto a general-purpose operating system's far larger and more permissive interface would be far harder than building the small interface correctly from the start.

**Why a dual-core architecture?** Because the deterministic real-time work and the flexible, rich application work have opposite requirements — the first needs a processor whose timing can be proven, the second needs a processor that is fast and runs a general-purpose software environment — and trying to satisfy both on one core means either the application's non-determinism contaminates the timing proof or the timing discipline cripples the application environment. Two cores, coupled only by a lock-free channel that transmits data without transmitting non-determinism, let each kind of work run on the processor suited to it.

**Why Earliest-Deadline-First scheduling rather than fixed-priority?** Because its schedulability condition is a single, exact, task-count-independent inequality — total utilisation at most one — which is stable under the revisions the signal-processing pipeline will undergo across the Standard's life, where a fixed-priority discipline's analysis must be re-derived task by task on every change. The discipline whose re-validation is cheap and mechanical is the discipline that will actually be re-validated correctly each time.

**Why is the capability a type rather than a runtime permission?** Because a runtime permission has three structural weaknesses, each serious for data as sensitive as neural data: the check can be mis-written, the check can be removed by a careless future edit, and the data exists in memory to be leaked by an unrelated bug. A capability as a type, and a prohibited category as a type that does not exist, eliminates all three: there is no check to be wrong or removed, and the prohibited category, having no type at the boundary, cannot be constructed there to be leaked.

**Why must consent be a kernel-level state rather than an application setting?** Because consent enforced by the application is consent the user's "no" depends on the good behaviour of the very software the user may be saying "no" to. Consent as a kernel-level state, on the publication path below the application, is enforced *against* the application: no application can bypass it, because there is no path by which an observation reaches the application without passing the kernel's interlock.

**Why is the withdrawn consent state terminal?** Because a reversible withdrawal is a withdrawal subject to coercion: if some event could turn the data back on, a coercing party could obtain that event, or software could deliver it without the user's knowledge. A terminal withdrawn state removes the entire class of pressure — there is nothing to obtain, no event that reverses it — and the only return is a fresh, deliberate manifest, an act the user performs of their own volition or not at all.

**Why the evidence discipline?** Because the brain-computer-interface field, like many young and commercially energetic fields, is awash in unevidenced numbers, and a reader cannot tell the carefully measured figure from the optimistic guess when both are presented identically as bare numbers. The discipline — every quantitative claim carries an evidence level and links to an inspectable artefact, or it does not appear — makes the Project's numbers checkable, and a checkable number is worth more than an unverifiable one however accurate the unverifiable one happens to be.

## A note on the structure of the repository's documents

The reader will notice that the repository's documents are unusually long and unusually detailed for a software project, and a word on why is warranted.

The length is deliberate and it is the cost of a specific property: that an independent implementer, with no access to the Project and no conversation with its maintainers, can build a conformant implementation from the documents alone. That property is the whole point of a standard — a standard that could only be implemented by someone who could ask its authors questions would not be a standard — and it has a price. The price is that every contract must be stated completely, every edge case addressed, every ambiguity resolved on the page, because the independent implementer cannot resolve an ambiguity by asking. A shorter document would be a document with unresolved ambiguities, and unresolved ambiguities are exactly where independent implementers diverge from each other and from the reference, silently, into incompatibility.

The detail in the architecture chapters serves a related but distinct purpose. The normative Standard states *what* conformance requires; it is, of necessity, concise about requirements, because a requirement padded with explanation is a requirement whose binding force is harder to locate. The architecture chapters carry the *why* — the reasoning, the worked examples, the rationale, the honest account of what is difficult — that the normative text deliberately omits. An implementer who reads only the normative requirements can build something that passes the conformance suite; an implementer who also reads the architecture chapters builds something that passes the suite *and* makes its hundred unforced internal decisions in a way that converges with other conformant implementations, because they understand the reasoning the requirements encode. The architecture chapters are informative — they bind nothing — but they are not optional reading for an implementer who wants to build well.

The reader should therefore not be daunted by the volume. The volume is organised, it is routed by role, and it is the volume necessary for the documents to do the one thing a standard's documents must do: let someone who has never spoken to the Project build, from the text alone, an implementation that is genuinely, verifiably conformant.

## A first implementer's walkthrough

For the reader who has decided to implement the Standard, this section sketches the path from an empty repository to a conformant implementation, so that the scale and the shape of the work are visible before it begins. It is a sketch, not a substitute for `STANDARD.md` and `CONFORMANCE.md`, but it orders the work.

**Begin by reading, completely, before writing anything.** Read `STANDARD.md` in full, then `CONFORMANCE.md`, then the architecture chapter for whichever component you intend to build first. The temptation to begin coding after skimming is strong and is a mistake: the Standard's requirements interlock, and a component built against a partial reading will, somewhere, violate a requirement the implementer had not yet reached, and the violation will surface late, as a conformance-suite failure whose cause is a design decision made a thousand lines earlier. The reading is front-loaded work that prevents far more expensive rework.

**Decide the scope of your implementation.** Will you build a kernel, a software development kit, a complete stack? The Standard permits partial implementations, and conformance is assessed against the components you provide. Decide this first, because it determines which categories of the conformance suite apply to you and therefore what your implementation must satisfy.

**If you are building a kernel, establish the timing foundation before the features.** The kernel's hardest requirement is the worst-case response time, proven at evidence level L1. Build the verification harness early — the bounded-model-checking infrastructure that will prove the timing — and run it from the start, against even a skeletal pipeline, so that the timing discipline is present from the first commit rather than retrofitted onto a pipeline that was built without it. The Project's own experience, recounted in the kernel architecture chapter, is that retrofitting the timing proof onto an unprepared pipeline is far more expensive than building with it from the beginning.

**Build the structural guarantees as structure, not as checks.** The capability system's prohibited categories must have no type at the application-facing boundary; the consent machine's withdrawn state must be terminal because the transition function has no case that leaves it. An implementer who builds these as runtime checks — a check that a prohibited category is not granted, a check that the withdrawn state is not left — has built a procedural imitation that the conformance suite is specifically constructed to detect. Build the absence, not the guard.

**Run the conformance suite continuously, not at the end.** The suite is the executable expression of the Standard; an implementer who runs it only when the implementation is "finished" discovers, at the end, a backlog of accumulated non-conformances whose causes are scattered through the codebase. An implementer who runs the applicable suite continuously, from early in development, catches each non-conformance when its cause is the most recent change and is cheap to locate and fix.

**Produce the evidence as you go.** The validation discipline requires every quantitative claim to carry an evidence level and an artefact. The proof artefacts and the soak traces are not paperwork to assemble after the implementation works; they are the evidence that the implementation works, and they are produced by the same verification and measurement activity that tells the implementer the implementation is correct. Build the claims catalogue alongside the implementation, and it is complete when the implementation is.

**Self-certify honestly.** When the implementation passes the applicable suite, the conformance report it produces is the basis for an honest conformance claim. Publish the report and the evidence archive; describe the implementation as conformant with the specific version it was tested against; and, if a later revision regresses, either repair the regression before the next release or cease describing that release as conformant. The conformance claim is worth exactly as much as the honesty behind it.

The walkthrough is deliberately brief because its detail lives in `STANDARD.md`, `CONFORMANCE.md`, and the architecture chapters. Its purpose is only to show the implementer the shape of the road: read fully first, decide scope, establish the timing foundation early, build guarantees as structure, run the suite continuously, produce evidence as you go, and certify honestly. An implementer who follows that shape will find the Standard a demanding but navigable specification, and the conformance suite a clear and reachable target.

## On the relationship among the documents

A final orientation, for the reader assembling a mental model of how the repository's documents fit together.

`STANDARD.md` is the centre. It defines the contracts. Every other document is a companion to it and is subordinate to it: in any disagreement, `STANDARD.md` governs.

`CONFORMANCE.md` is `STANDARD.md` made executable. Each of its fifty-seven tests cites the section of `STANDARD.md` it exercises. The two move together: a Request for Comments that changes a normative requirement, per `GOVERNANCE.md`, changes the corresponding conformance test in the same act, so the requirement and its test never drift apart.

`VALIDATION.md` governs the *epistemics* of `STANDARD.md`. Every quantitative claim in `STANDARD.md` — every numerical bound in the dual-core contract, every figure in the appendices — is subject to `VALIDATION.md`'s publishing rule and is recorded in its claims catalogue. `VALIDATION.md` is the discipline that makes `STANDARD.md`'s numbers trustworthy, and `STANDARD.md` holds its own numbers to it.

`GOVERNANCE.md` governs the *evolution* of `STANDARD.md`. It is the process by which `STANDARD.md` and, with it, `CONFORMANCE.md` change. It does not govern implementations; it governs the Standard.

`GLOSSARY.md` governs the *vocabulary* of all the others. It is normative for the meaning of every term it defines, and where any other document uses a term `GLOSSARY.md` defines, `GLOSSARY.md` governs that term's meaning.

The `architecture/` chapters carry the *reasoning* behind `STANDARD.md`'s requirements. They are informative — they bind nothing — but they are where an implementer finds the *why* that the normative text, concise about requirements, deliberately omits.

The mental model, then, is: one central normative text; an executable expression of it; a discipline governing its numbers; a process governing its change; a glossary governing its words; and a set of chapters carrying its reasoning. Six kinds of document, one coherent whole, and the whole is the AxonOS Standard.

## What the Standard deliberately leaves to the implementer

A standard is defined as much by what it constrains as by what it leaves free, and an implementer benefits from knowing, explicitly, the large space of decisions the AxonOS Standard does not touch — because that space is the implementer's room to engineer, to differentiate, and to optimise.

The Standard does not constrain the **implementation language**, beyond the requirements that follow from the guarantees themselves. The reference implementation is written in Rust, for the memory-safety reasons the kernel architecture chapter explains, but the Standard requires *memory safety* and a *provable worst-case bound*, not Rust; an implementer who can deliver those guarantees in another language has an implementation the Standard permits.

The Standard does not constrain the **processor family**. The reference implementation runs on a particular commodity dual-core platform, but the Standard requires a system *analysable as* a dual-core architecture with the stated properties, not that specific silicon; an implementer may target a different processor family entirely.

The Standard does not constrain the **internal organisation of the signal-processing pipeline**, beyond the fixed-task-set discipline and the timing bounds. The reference pipeline has six particular stages; an implementer may use a different decomposition, different filters, a different classifier, so long as the task set is fixed, the utilisation stays within the ceiling, and the worst-case response time is proven within the bound.

The Standard does not constrain the **ergonomics of the software development kit's programming interface**. It constrains the wire format the kit consumes and the error codes it must propagate, but the shape of the typed interface the kit presents to the application — its naming, its idioms, its language-appropriate conveniences — is the implementer's design.

The Standard does not constrain the **application layer** at all, beyond requiring a conformant manifest and correct handling of the consent and rate errors. What an application does, how it looks, what it is for — these are entirely the application author's.

The Standard does not constrain the **acquisition hardware**, only its contract at the kernel boundary. The analog front end, the converter, the electrode design — all are the implementer's.

This large free space is deliberate. A standard that constrained these things would be dictating engineering choices that have nothing to do with interoperability or with the guarantees, and it would be excluding implementations that differ only in ways that do not matter. The AxonOS Standard constrains exactly the contracts — the things that must be agreed for components to interoperate and for the guarantees to hold — and leaves everything else free, because everything else is where implementers should be free to engineer, to compete, and to improve.

## A closing note

The AxonOS Standard is an attempt to bring, to the software substrate of brain-computer interfaces, the kind of shared, precise, openly published, independently verifiable contract that other mature engineering domains take for granted and that this domain, for now, lacks. It is offered in the belief that a field handling data as intimate as neural data, and building devices with stakes as high as a brain-computer interface's, should not have its most fundamental software behaviours — its timing, its handling of neural data, its honouring of consent, its standard of evidence — left undefined and privately reinvented by every vendor. The contract in this repository is the Project's proposal for what that shared definition should be. It is openly licensed so that it can be adopted, scrutinised, criticised, and improved by anyone, and it is governed by a published process so that its evolution is visible and accountable. An implementer who builds against it, a reviewer who tests its claims, a contributor who proposes its improvement — each is doing exactly what an open standard exists to invite.

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
