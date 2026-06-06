# Roadmap — The AxonOS Standard

**AxonOS Standard v1.1.0** · **Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

*This document is **informative**. It imposes no requirement and defines no
conformance criterion. It describes the AxonOS Project's intended path forward
for the Standard and its reference implementation, so that an implementer, a
reviewer, or a prospective clinical or institutional partner can see where the
work is going and against what milestones progress should be judged. Nothing
here is a commitment to a date, and nothing here may be cited as evidence: the
only evidence the Project recognises is the graded, artefact-backed evidence
defined in `VALIDATION.md`, and a plan is not evidence. Where this document and
any normative document disagree, the normative document governs.*

---

## How to read this roadmap

The roadmap is organised along the two axes the Standard actually cares about,
and a third that follows from them. The first axis is **evidence**: the
progression, defined in `VALIDATION.md`, from claims that are formally proven
(L1) and measured on reference hardware (L2) toward claims that have been
**independently reproduced** (L3). The second axis is **governance**: the
gated, three-phase transition, defined in `GOVERNANCE.md` Section 6, by which
authority over the Standard moves from its founding maintainer, through a
technical steering committee, to a constituted Foundation. The third axis,
**adoption**, follows from the first two: a standard earns adoption by being
evidenced and by being governed in a way that does not depend on any one
person.

The phases below are described by what each is intended to *establish*, not by
when it is intended to happen. A phase is complete when its establishing
condition is met and recorded — an L3 artefact in the claims catalogue, a
governance transition gate passed, an independent implementation appearing —
and not when a calendar says so.

---

## The honest starting point

At version 1.1.0, the Standard's status is exactly what `VALIDATION.md` records
and no more. The headline real-time claims of the reference implementation are
held at **L1 and L2**: the worst-case response-time bound is proven over the
admissible input space and corroborated by a soak measurement on reference
hardware. The Project holds **no L3 claim**, because no genuinely independent
reproduction has yet been performed, and the claims catalogue records that
absence rather than disguising an L2 measurement as an L3 result. The
governance is in its **first phase**: stewardship rests with the founding
maintainer, and the path away from that dependence is defined but not yet
begun. This starting point is the thing the roadmap moves from, and stating it
plainly is a precondition for the roadmap meaning anything.

---

## Phase 1 — Reference validation and the first clinical pilot

The defining goal of Phase 1 is the Project's **first L3 claim**: the first
time a headline quantitative claim — the worst-case response-time bound is the
natural candidate, since it is the claim most consequential to a clinical
deployment — is reproduced by a party with no stake in the AxonOS Project, on a
separate instance of the reference hardware, and witnessed by a signed report
meeting the requirements of `VALIDATION.md` Section 3.

The intended setting for that first independent reproduction is a **clinical
pilot**: a deployment of the reference implementation, on the eight-channel
reference acquisition configuration, at a clinical rehabilitation partner whose
patient population includes people living with amyotrophic lateral sclerosis,
for whom a dependable, consent-respecting brain-computer interface is not a
convenience but a route to communication. Such a partner is independent of the
Project in exactly the sense L3 requires, and a reproduction of the timing
claim under the partner's own measurement, on the partner's own hardware, is
precisely the artefact that turns an L2 claim into an L3 claim.

Phase 1 also exercises the parts of the Standard that only a real deployment
can exercise: the consent subsystem under genuine clinical use, including the
multi-party guardian co-authorisation path for which the reference consent
implementation provides an optional conformance profile; the error-handling
contract under conditions the laboratory does not produce; and the conformance
suite against an implementation running on a clinician's bench rather than a
developer's. The lessons of that exercise feed back into the Standard through
the ordinary amendment process — not as a privileged channel, but as exactly
the kind of evidence-driven refinement the governance is built to absorb.

Phase 1 is complete when the first L3 artefact is recorded in the claims
catalogue and the catalogue's honest accounting at last includes a claim the
Project did not itself certify.

---

## Phase 2 — Regulatory groundwork and external alignment

The defining goal of Phase 2 is to place the Standard and its reference
implementation into the **external frameworks** that a clinically deployed
brain-computer interface must eventually answer to, without compromising the
Standard's independence from any one of them.

This means engaging the regulatory pathway appropriate to the device class —
the early, advisory engagement that a regulator offers before a submission, so
that the evidence the Project gathers is the evidence the regulator will want —
and it means alignment with the established external standards that govern
medical-device software lifecycle, risk management, and, as the field's
neurotechnology-specific standards mature, the emerging standards for
brain-computer interface interoperability and safety. Alignment is not
subordination: the AxonOS Standard remains an openly licensed, independently
governed document, and its relationship to an external standard is one of
explicit, documented correspondence — a mapping that says which of the
Standard's requirements satisfy which of the external standard's clauses — not
one of absorption.

Phase 2 also broadens the conformance suite as the evidence of Phase 1 reveals
what a clinical setting demands that a developer's setting did not, and it
matures the claims catalogue from a record of the reference implementation's
claims into a record that an independent implementer can add their own
independently evidenced claims to.

---

## Phase 3 — Independent implementations and the Foundation

The defining goals of Phase 3 are the two milestones that, together, mark a
standard's passage from a single project's proposal into a genuine shared
contract: the appearance of a **second, independent conformant implementation**,
and the **transition of governance** beyond the founding maintainer.

A standard with one implementation is a specification of that implementation; a
standard with two independent implementations, each conformant, each passing
the same suite, is a standard in the full sense — the point at which the
contract has demonstrably constrained more than its author. The Standard is
written, throughout, to make a second implementation possible: its precision
exists so that a team that has never communicated with the Project can build
against the text alone. Phase 3 is where that possibility is intended to become
actual.

In parallel, Phase 3 is where the governance transition of `GOVERNANCE.md`
Section 6 advances along its gates: from the founding maintainer to a technical
steering committee, and toward a constituted Foundation, so that the Standard's
stewardship comes to rest in an institution rather than a person. The
constitutional commitments — the privacy prohibitions, the evidence discipline,
the open licensing — bind every phase of that transition and are not weakened by
it; the transition changes who governs, not what the governance is constrained
to protect.

---

## What this roadmap deliberately does not promise

It does not promise dates, because a date the Project cannot keep would be a
claim the Project cannot evidence, and the discipline that forbids unevidenced
quantitative claims about the system forbids them no less about the schedule.
It does not promise a commercial product, because this repository is a standard
and a standard's roadmap is a roadmap for the standard, not a business plan. It
does not promise that any particular clinical partner, regulator, or
independent implementer will act on any particular timeline, because none of
those parties is under the Project's control, and the L3 evidence and the
second implementation derive their entire value from that independence.

What it promises is a direction and an order: evidence before claims,
independent reproduction before any L3 label, a second implementation and an
institutional home before the Standard can call itself, without qualification,
a shared contract for the field. The milestones are the measure; the dates will
be whatever the work and the independent parties make them.

---

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
