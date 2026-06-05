# Governance — The AxonOS Standard, Version 1.0.1

**Status:** Normative · **Companion to:** `STANDARD.md` · **License:** CC-BY-SA-4.0

**Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

---

## Preface

This document defines the governance of the AxonOS Standard: who may change the Standard, by what process, under what constraints, and how the authority to govern the Standard will be transferred, over time, from its founding maintainer to a constituted Foundation. It is the companion to `STANDARD.md` Sections 26 through 28, which establish versioning, the amendment process, and the stability commitments; this document elaborates those into a complete working governance.

This document is normative. A change to the Standard made otherwise than by the process defined here is not a valid change, regardless of who makes it; the authoritative Standard is always the text produced by this process, at the tagged commit the process produced.

Governance is, for a standard, not an administrative afterthought but a load-bearing part of the standard's value. A standard's worth to an implementer rests on a prediction: that the contract the implementer builds against will still be the contract a year from now, that it will not be quietly changed in a way that breaks the implementer's work, that its evolution will be visible and reasoned and bounded. A standard with no governance, or with opaque governance, or with governance that permits arbitrary change, cannot support that prediction, and an implementer cannot safely build against it. Governance is the mechanism by which a standard earns the right to be built against, and this document is that mechanism for the AxonOS Standard.

The governance defined here has three central features, and they may be summarised before the detail. First, **every change flows through a public Request-for-Comments process**: there is no private channel by which the Standard changes, and a change not in the public record has not been made. Second, **certain commitments are constitutional**: a small set of the Standard's properties — its privacy prohibitions, its evidence discipline, its open licensing — may be altered only by an exceptional procedure carrying an exceptional burden, and not by the ordinary amendment process. Third, **authority transfers on a defined path**: the Standard begins under the stewardship of its founding maintainer, and this document specifies the gated, three-phase path by which that stewardship becomes the stewardship of a constituted Foundation, so that the Standard's governance is designed, from the beginning, not to depend permanently on one person.

A reader who wants the essence should read Sections 1 and 2: the governance principles and the constitutional commitments. A reader who will participate in amending the Standard should read Sections 3 through 5: the Request-for-Comments process, the review procedure, and the rules for breaking changes. A reader concerned with the long-term institutional future should read Sections 6 and 7: the three-phase transition and the Foundation.

---

## Section 1. The principles of AxonOS governance

The governance rests on five principles. They are stated here, and the procedural detail of the later sections is, in each case, these principles worked out.

### 1.1 Every change is public

Every change to the Standard is made through the public Request-for-Comments process of Section 3. There is no private channel. A proposed change is a public document from the moment it is filed; its review is conducted in public; its acceptance or rejection is a public act; and the amended Standard is a public commit. A change discussed privately and applied without passing through the public process is not a valid change, and the maintainers undertake never to make one.

The principle's force is in its absoluteness. It is not that change is *usually* public, or public *when convenient*; it is that a change not in the public record has not been made, and the public record is therefore the complete and authoritative history of the Standard. An implementer auditing how a particular requirement came to have its particular form can, by this principle, find the complete answer in the Request-for-Comments archive, because there is no other place an answer could be.

### 1.2 Reasoned change, not arbitrary change

A change to the Standard must be *justified*. The Request-for-Comments process requires every proposal to state the problem it solves, the reason the current Standard is inadequate, the detailed design of the change, the drawbacks the change carries, and the alternatives considered. A proposal that asserts a change without justifying it is incomplete and is not accepted. The Standard changes because a stated problem warrants a stated solution, never because a maintainer prefers the new text to the old.

### 1.3 Stability is the default

The Standard's default state is unchanged. A proposal bears the burden of showing that change is warranted; the absence of a proposal leaves the Standard as it is. This is the opposite of a process in which the Standard drifts continuously and a special effort is required to hold any part of it still. The AxonOS Standard holds still by default, and moves only when a justified proposal moves it, because the implementers building against it need the stability and the burden of justification is the mechanism that delivers it.

### 1.4 Some commitments are beyond ordinary amendment

A small set of the Standard's properties are *constitutional*: they may be changed only by the exceptional procedure of Section 2, which carries a burden far heavier than the ordinary amendment process. The constitutional commitments are the properties whose stability is so central to the Standard's meaning that an implementer, a user, or a regulator must be able to rely on them absolutely — and reliance that absolute requires that the properties be insulated from the ordinary ebb and flow of amendment.

### 1.5 Authority is designed to transfer

The Standard's governance is designed, from version 1.0.0, not to depend permanently on its founding maintainer. Section 6 defines a gated, three-phase path along which governing authority moves from the founding maintainer, through a technical steering committee, to a constituted Foundation. The path is defined now, at the beginning, precisely so that the transition is a planned and orderly execution of a pre-committed design rather than an improvised response to a future crisis.

---

## Section 2. The constitutional commitments

### 2.1 What the constitutional commitments are

`STANDARD.md` Section 28 names a small set of the Standard's properties as **constitutional commitments**. They are:

The **structural prohibition of the four neural-data categories** — raw neural signal, affective state, cognitive profile, biometric identity (`STANDARD.md` Section 13). No capability exposing any of these may exist.

The **evidence-taxonomy discipline** — the requirement that every quantitative claim under the AxonOS name carry an evidence level and an artefact, and the publishing rule that enforces it (`STANDARD.md` Section 22, `VALIDATION.md`).

The **open licensing of the Standard** — the release of the normative text under the Creative Commons Attribution-ShareAlike licence and the reference code under permissive licences, and the permission to fork (`STANDARD.md` Section 31, the legal material).

The **real-time guarantee discipline** — the requirement that every real-time bound carry an evidence level and that bounds may move only in the direction of tightening, never relaxation, within a major version (`STANDARD.md` Sections 9 and 28).

### 2.2 Why these are constitutional

These four are constitutional because each is a commitment on which a party outside the Project must be able to rely absolutely, and absolute reliance requires insulation from ordinary amendment.

A user must be able to rely, absolutely, on the privacy prohibitions: the entire proposition that a BCI can be used without one's neural interior becoming a profiled, surveilled, manipulable asset rests on those prohibitions holding, and a prohibition that could be removed by an ordinary minor revision is not a prohibition a user can rely on. A reviewer must be able to rely, absolutely, on the evidence discipline: the proposition that the Project's numbers are checkable rests on the discipline holding, and a discipline removable by ordinary amendment is not a discipline. An implementer who has forked the Standard must be able to rely, absolutely, on the open licence: the right to fork, once granted, cannot be revocable, or it was never a right. And a safety engineer must be able to rely, absolutely, on the real-time bounds not being quietly relaxed beneath a device already certified against them.

The constitutional status is the insulation. It places these four beyond the reach of the ordinary process, so that the reliance they invite is reliance the governance structurally supports.

### 2.3 The procedure for a constitutional change

A change to a constitutional commitment is possible — a standard that could never change even its deepest commitments would be unable to correct a genuine, demonstrated error in one of them — but it is made deliberately difficult. A constitutional change requires all of the following, and the absence of any one of them invalidates the change.

It requires a **major-version increment** of the Standard. A constitutional change can never be a minor or patch revision; it is, by definition, breaking.

It requires a **published harm analysis**: a document, public for the full notice period, that analyses, specifically and concretely, what harm the change could cause and to whom, and why the change is nonetheless warranted. For a proposal to weaken a privacy prohibition, the harm analysis must confront, directly, the harms the prohibition was enacted to prevent. The harm analysis is not a formality; it is the central document of a constitutional change, and a proposal whose harm analysis is evasive or incomplete is not accepted.

It requires a **notice period of at least ninety days**, during which the proposal, the harm analysis, and the full reasoning are public and open for comment, so that every affected party — users, implementers, reviewers, regulators — has genuine opportunity to respond before the change is decided.

It requires the **approval of the governing body in effect** at the time, under whatever phase of the Section 6 transition then obtains: the founding maintainer in the first phase, the technical steering committee in the second, the Foundation in the third.

### 2.4 The constitutional commitments bind every phase

The constitutional commitments, and the heavy procedure for changing them, bind the governing body in every phase of the Section 6 transition. The founding maintainer cannot weaken a privacy prohibition by ordinary amendment; neither can the technical steering committee; neither can the Foundation. The constitutional status is a property of the Standard, not a courtesy of the current governors, and it constrains whoever governs.

---

## Section 3. The Request-for-Comments process

### 3.1 What a Request for Comments is

Every substantive change to the Standard is made through a **Request for Comments**, abbreviated RFC: a numbered, public document that proposes a change, is reviewed in public, and is either accepted — in which case its proposed change is applied to the Standard — or rejected, or withdrawn.

The RFC is the unit of change. The Standard does not change except by an accepted RFC; the history of the Standard is the sequence of accepted RFCs; and the reasoning behind any part of the Standard is recoverable by finding the RFC that introduced it.

### 3.2 The anatomy of an RFC

An RFC is a document with seven required sections, and an RFC missing any of them is incomplete and is not accepted.

The **summary** states, in one paragraph, what the RFC proposes.

The **motivation** states the problem the RFC solves: what is wrong with the Standard as it stands, what goes wrong if nothing is done, why the current text is inadequate. The motivation must be concrete — it must point to specific requirements, specific implementer difficulties, specific real-world failures — because a vague motivation cannot be evaluated.

The **detailed design** states the proposed change in full: the exact new or amended normative text, shown as a difference against the current text where it amends an existing passage. If the RFC adds requirements, the detailed design states them with the precision the Standard's own requirements have. If the RFC affects the conformance suite, the detailed design states the new or changed tests.

The **drawbacks** section states, honestly, what the RFC makes worse: what cost it imposes, what complexity it adds, what it gives up. A serious RFC has drawbacks, and an RFC that claims none has not been thought through.

The **alternatives** section states what other designs were considered and why the proposed one was chosen.

The **unresolved questions** section states what the RFC's author has not settled and wishes reviewers to focus on.

The **migration** section, required for any breaking RFC, states how implementers move from the previous version to the version the RFC would produce.

### 3.3 Filing an RFC

An RFC is filed by adding it, as a numbered document, to the governance directory of the canonical repository, through the repository's ordinary contribution mechanism — a pull request. The act of filing makes the RFC public. Anyone may file an RFC; the process is not restricted to the maintainers, and an RFC from an independent implementer is reviewed by the same process and the same standard as an RFC from the founding maintainer.

### 3.4 The review period

A filed RFC is open for review for a defined minimum period. For an ordinary RFC — one that proposes a non-breaking change and touches no constitutional commitment — the minimum review period is **fourteen days**. For a breaking RFC, the minimum is the breaking-change notice period of Section 5. For an RFC touching a constitutional commitment, the minimum is the ninety-day constitutional notice period of Section 2.3.

The review period is a *minimum*. The clock does not begin until the RFC is complete — until all seven required sections are present — and it restarts if the RFC is substantively revised during review, because reviewers must have the full minimum period to consider the version that will actually be decided. An RFC under active substantive discussion is not decided merely because the minimum has elapsed; the minimum is a floor on deliberation, not a ceiling.

### 3.5 The decision

At the end of the review period, the RFC is decided by the governing body in effect under the current phase of the Section 6 transition. The decision is one of three.

**Accepted**: the RFC's reasoning is sound, its review surfaced no unresolved substantive objection, and the proposed change is warranted. An accepted RFC's change is applied to the Standard at the next release, and the RFC's status is recorded as accepted.

**Rejected**: the RFC's reasoning is unsound, or the review surfaced a substantive objection the RFC could not answer, or the change is not warranted. A rejected RFC is preserved, with its rejection and the reason recorded, in the governance archive, because a rejected proposal is part of the Standard's history and a future contributor must be able to see what was proposed and why it was declined.

**Withdrawn**: the RFC's author withdraws it. A withdrawn RFC is likewise preserved with its status recorded.

The decision, and its reasoning, are public. An acceptance states why the change is warranted; a rejection states why it is not. The governing body does not decide by unexplained fiat; the principle of reasoned change (Section 1.2) binds the decision as much as the proposal.

---

## Section 4. The review procedure in detail

### 4.1 What review consists of

The review of an RFC is the substantive examination of its proposal by whoever chooses to examine it. Review is public and open: anyone may review any RFC, and the review of an RFC from an independent contributor and the review of an RFC from a maintainer are conducted identically.

A reviewer examines the RFC against a set of questions. Is the motivation real — is the problem the RFC describes a genuine problem, and is the current Standard genuinely inadequate to it? Is the detailed design correct — would the proposed text actually solve the problem, and is it stated with the precision the Standard requires? Are the drawbacks complete — has the RFC honestly named what it makes worse, or has it concealed a cost? Were the alternatives genuinely considered — is the chosen design actually the best of the options, or merely the first the author thought of? Does the change interact with the rest of the Standard — does it contradict another requirement, void an evidence artefact, break a contract the RFC's author did not consider?

A review is recorded as public comment on the RFC. A review that raises a substantive objection obliges the RFC's author to respond — by amending the RFC to address the objection, by arguing that the objection is mistaken, or by accepting that the objection is fatal and withdrawing. An RFC cannot be accepted while a substantive objection stands unanswered.

### 4.2 Substantive and non-substantive objections

The review process distinguishes a substantive objection from a non-substantive one, because only a substantive objection blocks acceptance.

A **substantive objection** is an objection that, if correct, means the RFC should not be accepted in its current form: that its motivation is not real, that its design is incorrect, that it carries an unstated drawback that outweighs its benefit, that it contradicts another part of the Standard. A substantive objection must be answered before the RFC is accepted.

A **non-substantive objection** is a matter of preference, of style, of wording that does not affect the requirement, of a reviewer wishing the author had chosen differently among genuinely acceptable options. A non-substantive objection is recorded, is considered, and may improve the RFC, but it does not block acceptance: an RFC is not held hostage to a reviewer's preference among acceptable alternatives.

The distinction is itself sometimes contested — a reviewer may believe their objection substantive while the author believes it preference — and where the distinction is contested, the governing body of the current phase resolves it as part of the decision, stating, in the decision's reasoning, why the objection was treated as it was.

### 4.3 The maintainer's role in review

Under the first phase of the Section 6 transition, the founding maintainer is the governing body, and the maintainer both participates in review and renders the decision. This concentration of roles is a real limitation of the first phase, and the governance does not pretend otherwise; it is the reason the transition of Section 6 exists, and the reason the first phase is explicitly a phase to be moved on from rather than a permanent arrangement.

The first phase manages the limitation in two ways. First, the maintainer's decision, like every decision, is public and reasoned: the maintainer must state why an RFC was accepted or rejected, and a reasoned decision is reviewable by the community even when the decision itself rests with one person. Second, the constitutional commitments are beyond the maintainer's ordinary reach: the maintainer cannot, even as sole governing body of the first phase, weaken a privacy prohibition or the evidence discipline by ordinary amendment, because those require the constitutional procedure. The first phase concentrates the *ordinary* amendment authority in one person; it does not concentrate the *constitutional* authority, and the most consequential changes are insulated from the concentration.

---

## Section 5. Breaking changes

### 5.1 What makes a change breaking

A change to the Standard is **breaking** if an implementation conformant before the change could be non-conformant after it without any change to the implementation itself — that is, if the change alters what conformance requires in a way that an existing conformant implementation does not already satisfy.

`STANDARD.md` Section 26 enumerates the breaking changes: a change to a normative requirement, the addition or removal of a capability, a change to the wire format, a relaxation of a real-time bound. Each of these can render a previously conformant implementation non-conformant, and each therefore triggers the breaking-change procedure.

### 5.2 The breaking-change procedure

A breaking change requires everything an ordinary RFC requires, and three things more.

It requires a **major-version increment**: a breaking change can never be released as a minor or patch revision, because the version number is itself a promise — a promise that a minor or patch revision is safe to adopt without re-examination — and a breaking change in a minor revision would break that promise.

It requires a **migration document**: the RFC's migration section, elaborated into a complete, practical guide by which an implementer moves an implementation from conformance with the old version to conformance with the new. The migration document is not optional and not perfunctory; a breaking change without a usable migration path imposes its full cost on every implementer with no help, and the governance does not permit that.

It requires a **notice period of at least ninety days**: the breaking RFC, with its migration document, is public and open for comment for at least ninety days before the breaking change is released, so that every implementer has substantial, advance, certain knowledge of what is coming and substantial time to prepare.

### 5.3 The presumption against breaking changes

The governance carries a standing presumption against breaking changes. A breaking change imposes a cost on every existing implementer simultaneously, and the cost is involuntary — the implementer did not ask for the change and must nonetheless absorb it. The presumption against breaking changes means that a breaking RFC bears a heavier burden than a non-breaking one: it must show not only that it solves a real problem but that the problem cannot be solved in a non-breaking way, because if a non-breaking solution exists the non-breaking solution is to be preferred even if it is less elegant. Elegance is worth less than the avoidance of an involuntary cost imposed on every implementer.

### 5.4 Breaking changes and the stability commitments

`STANDARD.md` Section 28 states the stability commitments: within a major-version line, no normative requirement is removed, no defined term is removed or redefined, no wire-format field is removed or repurposed, no real-time bound is relaxed. These commitments mean that the breaking changes of Section 5.1 can occur only at a major-version boundary — they are precisely the changes a major version is permitted to make and a minor version is not. The stability commitments and the breaking-change procedure are two views of one discipline: the stability commitments state what a minor version may not do, and the breaking-change procedure states how a major version does the things a minor version may not.

---

## Section 6. The three-phase transition of authority

### 6.1 Why a transition is designed in advance

The AxonOS Standard begins under the stewardship of its founding maintainer. This is the natural and correct beginning for a standard — a standard begins as one person's or a small team's coherent design, and a coherent design requires, at the start, a coherent designer with the authority to keep it coherent. But a standard that remained permanently dependent on its founding maintainer would be a fragile standard: fragile against the maintainer's departure, the maintainer's error, the maintainer's eventual incapacity, and fragile against the reasonable reluctance of serious implementers and institutions to build long-term work on a contract governed in perpetuity by a single individual.

The governance therefore designs, at version 1.0.0, the path by which the founding stewardship becomes an institutional stewardship. The path is designed *now*, at the beginning, for a specific reason: a transition planned in advance, with its phases and its gates defined before any of them is reached, is an orderly execution of a pre-committed design, whereas a transition improvised later, under whatever pressure prompted it, is a crisis. The Project chooses the orderly path by committing to it before it is needed.

### 6.2 The three phases

The transition has three phases. Each phase is a configuration of governing authority; the movement from one phase to the next is gated by defined conditions.

**Phase A — the founding maintainer.** In Phase A, the founding maintainer is the sole governing body. The maintainer decides RFCs, renders the decisions, and bears the stewardship. Phase A is where the Standard begins, at version 1.0.0. Phase A's limitation — the concentration of ordinary amendment authority in one person — is real and is managed, as Section 4.3 describes, by the public-and-reasoned-decision requirement and by the insulation of the constitutional commitments. Phase A is explicitly a beginning, not a destination.

**Phase B — the technical steering committee.** In Phase B, governing authority rests with a technical steering committee: a small body of named individuals, including but not limited to the founding maintainer, who decide RFCs collectively. The committee decides by a defined procedure — a documented deliberation followed by a recorded vote — and its decisions, like all decisions, are public and reasoned. Phase B distributes the ordinary amendment authority that Phase A concentrated, so that no single person decides the Standard's ordinary evolution, while keeping the governing body small enough to remain coherent and decisive.

**Phase C — the Foundation.** In Phase C, governing authority rests with a constituted AxonOS Foundation: a legal entity, with a governing board, a defined membership, a constitution of its own, and an existence independent of any individual. The Foundation holds the Standard's trademark, stewards the Standard's evolution through the technical steering committee that becomes an organ of the Foundation, and provides the institutional permanence that lets the Standard be built upon for the long term. Phase C is the destination: a standard governed by an institution designed to outlast any individual.

### 6.3 The gates between the phases

The movement between phases is not automatic and not arbitrary; it is gated by defined conditions, so that a phase transition occurs when the Standard is genuinely ready for it and not before.

The gate from **Phase A to Phase B** is met when all of the following hold: the Standard has reached a stable version 1.0.0 or later that has been in force without a breaking change for a defined consolidation period; at least one conformant implementation independent of the founding maintainer exists; and a technical steering committee of qualified individuals, willing to serve, has been identified. The independent-implementation condition is significant: a standard with only its reference implementation has not yet proven it is a standard, and Phase B — distributed governance — is appropriate once the Standard has proven itself implementable by parties beyond its author.

The gate from **Phase B to Phase C** is met when all of the following hold: the technical steering committee has operated through Phase B for a defined period, demonstrating that distributed governance functions; the Standard has a community of implementers and users substantial enough to constitute a Foundation membership; and the legal and financial groundwork for constituting the Foundation — the entity, the constitution, the initial board, the trademark transfer — is complete. Phase C is the constitution of an institution, and an institution is constituted when there is a community for it to serve and the groundwork for it to stand on.

### 6.4 What does not change across the phases

The transition changes who governs. It does not change what governance may do. The constitutional commitments of Section 2 bind Phase A, Phase B, and Phase C identically. The Request-for-Comments process of Section 3 operates in every phase. The principle that every change is public, the principle of reasoned change, the presumption of stability, the breaking-change procedure — all bind every phase. The transition moves the authority along a path; it does not, at any point along the path, expand what the authority is permitted to do. An implementer building against the Standard in Phase A can rely on the constitutional commitments holding in Phase C, because the commitments are properties of the Standard and the transition does not touch them.

---

## Section 7. The AxonOS Foundation

### 7.1 What the Foundation will be

The AxonOS Foundation, constituted at Phase C, will be a legal entity whose purpose is the long-term stewardship of the AxonOS Standard and the reference implementation. It will have a governing board, a defined membership drawn from the Standard's community of implementers and users, a constitution defining its own governance, and the institutional and financial permanence to steward the Standard across a horizon longer than any individual's involvement.

### 7.2 What the Foundation will hold

The Foundation will hold the assets whose stewardship requires an institution rather than an individual. It will hold the **AxonOS trademark**, transferred from the founding maintainer, so that the right to say what may bear the AxonOS name rests with an accountable institution. It will hold the **governance of the Standard**, exercised through the technical steering committee operating as an organ of the Foundation. It will hold the **conformance-review function**, the Foundation review of `CONFORMANCE.md` Section 6, so that the independent confirmation of conformance is performed by an accountable institution.

### 7.3 What the Foundation will not do

The Foundation's purpose is stewardship of an open standard, and its constitution will constrain it accordingly. The Foundation will not be permitted to take the Standard closed — the open licensing is a constitutional commitment and binds the Foundation as it binds every governing body. The Foundation will not be permitted to weaken the privacy prohibitions or the evidence discipline by ordinary means, for the same reason. The Foundation will not be a vendor: it stewards the Standard and the reference implementation, and it does not compete with the implementers who build on the Standard. The Foundation is designed to be a steward, and its constitution will be written to keep it one.

### 7.4 The honest status at version 1.0.0

At version 1.0.0, the AxonOS Standard is in Phase A. The Foundation does not yet exist; the technical steering committee does not yet exist; the founding maintainer is the governing body. This document describes Phase B and Phase C, and the gates between the phases, as a *commitment* — a published, advance commitment to the path the governance will take — and not as a description of a present state. The honest status is that the transition is designed and committed, and that its first gate, the gate to Phase B, will be met when the Standard has stabilised and an independent implementation exists. The Project records this honestly, here, because a governance document that described an aspirational future as though it were a present fact would have failed, in its own first substantive section, the discipline of honest claims that the Standard exists to uphold.

---

---

## Section 8. Worked examples of the governance in operation

*Informative. The preceding sections defined the governance abstractly. This section traces three concrete scenarios through it, because the procedures are best understood in motion.*

### 8.1 An ordinary non-breaking RFC

Suppose an implementer, in the course of building a conformant kernel, discovers that the Standard's description of the admission-control procedure (Section 7.4 of `STANDARD.md`) is ambiguous: it does not state whether a task-set change that leaves utilisation exactly *at* the ceiling, rather than below it, is admitted. The implementer believes the intent is to admit it — the ceiling is a maximum, and a change to exactly the maximum does not exceed it — but the text does not say so, and two implementers could read it two ways.

The implementer files an RFC. Its summary proposes a one-sentence clarification: that a task-set change leaving utilisation equal to the ceiling is admitted. Its motivation states the ambiguity concretely, points to the exact sentence, and explains that two conformant implementations could diverge. Its detailed design gives the exact amended sentence as a difference against the current text. Its drawbacks section notes, honestly, that the clarification slightly reduces a future revision's freedom to reinterpret the boundary, though it judges this cost negligible. Its alternatives section notes the opposite clarification — that equality is refused — and explains why admission is the better reading. Its unresolved-questions section is empty. It has no migration section because it is non-breaking — no existing conformant implementation is rendered non-conformant, since the clarification only resolves an ambiguity in the implementation's favour.

The RFC is complete, so the fourteen-day review period begins. A reviewer comments that the clarification should also note the interaction with the configurable raised ceiling of Section 7.3; the RFC's author agrees, amends the RFC to add a clause, and — because the amendment is substantive — the fourteen-day clock restarts on the amended version. No further substantive objection arises. At the end of the period the governing body, in Phase A the founding maintainer, accepts the RFC, stating in the decision that the clarification resolves a genuine ambiguity and that the amended version addresses the reviewer's point. The clarification is applied to `STANDARD.md` at the next patch release, the version increments at the patch level, and the RFC is archived with status accepted.

This is the ordinary case, and it is deliberately undramatic: a real ambiguity, a complete proposal, a public review that improved it, a reasoned acceptance, a patch release. Most of the Standard's evolution will look like this.

### 8.2 A breaking RFC

Suppose, some years on, experience with deployed implementations reveals that the twenty-eight-byte intent-observation record's four-byte reserved field is insufficient for a genuinely needed extension — a second confidence value, say, that a substantial class of applications requires — and that the extension cannot be expressed within the existing reserved space.

The change is breaking: it alters the wire format, and a kernel and a software development kit built against the old format would not interoperate with counterparts built against the new one. The breaking-change procedure of Section 5 engages.

The RFC bears the ordinary seven sections, and its drawbacks section is substantial and honest: it states plainly that every existing conformant implementation must be revised, that the application-binary-interface version must increment, that there will be a period during which old and new implementations coexist and cannot interoperate. Its alternatives section must, under the presumption against breaking changes of Section 5.3, show genuinely that the extension cannot be achieved non-breakingly — it must demonstrate that the reserved space is truly insufficient and that no non-breaking encoding exists. Its migration section is a full, practical guide: how an implementer revises a kernel, how an implementer revises a software development kit, how a deployment transitions, how the coexistence period is managed.

The notice period is not fourteen days but at least ninety. For ninety days the RFC and its migration document are public, and every implementer of the Standard has certain, advance knowledge that the wire format will change and ninety days to prepare. At the end of the notice period the governing body decides; if it accepts, the change is released as a major-version increment of the Standard and an increment of the application-binary-interface version, and the migration document ships with it.

This is the breaking case, and it is deliberately heavy: a real and unavoidable need, a demonstration that nothing non-breaking suffices, an honest accounting of the cost, a full migration guide, ninety days of notice, a major version. The weight is the point — it ensures breaking changes are rare and, when they occur, well-prepared.

### 8.3 A proposed constitutional change

Suppose a party proposes that the workload-advisory capability's structural neighbour, a prohibited affective-state category, be partially un-prohibited — that a narrow, coarse affective-state capability be added, on the argument that some assistive application would benefit.

This touches a constitutional commitment: the structural prohibition of the four neural-data categories. The ordinary RFC process cannot make this change; the constitutional procedure of Section 2.3 engages.

The proposal requires a major-version increment — it is, necessarily, breaking and more. It requires a published harm analysis, and the harm analysis is the centre of the matter: it must confront, directly and concretely, the harms that the affective-state prohibition was enacted to prevent — the manipulation, the timing of persuasion and pricing to a user's vulnerability — and must argue, specifically, why the proposed narrow capability does not reopen those harms, or why, if it does reopen them partially, the benefit nonetheless warrants the cost. A harm analysis that is evasive about the manipulation risk, or that waves at "appropriate safeguards" without specifying them, is incomplete, and an incomplete harm analysis means the proposal is not accepted regardless of its other merits. The proposal requires a ninety-day notice period, during which users, implementers, reviewers, and any regulator who wishes may respond to the proposal and its harm analysis. And it requires the approval of the governing body in effect.

The weight here is the heaviest the governance imposes, and it is imposed precisely because the constitutional commitments are the properties on which parties outside the Project rely absolutely. The procedure does not make a constitutional change impossible — a genuine, demonstrated error in a constitutional commitment must be correctable — but it makes such a change an exceptional, deliberate, fully public, fully reasoned act, and it ensures that the affective-state prohibition cannot be eroded quietly, by increments, by ordinary RFCs each individually small. The constitutional procedure is the structural form of the Project's promise that the privacy prohibitions mean what they say.

---

---

## Section 9. The contribution process for non-RFC changes

*Normative.* Not every change to the repository is a Request for Comments. The RFC process governs substantive changes to the normative Standard. A large class of changes — corrections of typographical errors, repairs of broken cross-references, improvements to informative prose that change no requirement, additions to the architecture chapters' informative material, updates to the claims-catalogue links — are not substantive changes to normative text and do not require an RFC.

Such non-RFC changes are made through the repository's ordinary contribution mechanism: a pull request, reviewed by a maintainer, merged if it is correct. The dividing line is precise and is drawn at the word *normative*. A change that alters, adds, or removes a normative requirement — anything expressed with the requirement keywords, anything that alters what conformance demands — is substantive and requires an RFC. A change that touches only informative material, or only corrects an error without changing intent, is non-substantive and is an ordinary pull request.

A contributor uncertain which category a change falls into should treat it as substantive and file an RFC; the cost of an unnecessary RFC is a fourteen-day wait, while the cost of a substantive change slipping through as an ordinary pull request is an unreviewed alteration to the Standard's requirements, and the asymmetry of those costs means the uncertain case resolves toward the RFC.

A non-substantive change that, on review, turns out to alter a requirement is reverted, and the change is re-proposed as an RFC. The maintainer reviewing pull requests is responsible for catching this — for noticing that a change presented as a typographical correction in fact shifts a requirement — and a change that shifts a requirement does not become legitimate by having been mislabelled.

## Section 10. The repository as the governance record

*Normative.* The governance defined in this document is recorded, in its entirety, in the canonical repository. The Request-for-Comments archive is a directory of the repository; every RFC, accepted, rejected, or withdrawn, is a file in it. The Standard's history is the repository's commit history. The decisions, with their reasoning, are recorded with the RFCs. The claims catalogue, the remediation log, the changelog — all are files in the repository.

This is a deliberate consequence of the principle that every change is public (Section 1.1). The repository is not merely where the Standard's text lives; it is the complete and authoritative record of the Standard's governance. A party wishing to audit how the Standard came to be as it is — what was proposed, what was accepted and why, what was rejected and why, what was retracted — finds the complete answer in the repository, because the governance defines no other place an answer could be kept. There is no private minute-book, no decision recorded only in correspondence, no reasoning that exists only in a maintainer's memory. The repository is the governance record, and the governance record is complete.

This completeness has a cost and a benefit. The cost is discipline: every decision must be written down, every RFC must be archived rather than discarded, every retraction must be logged, and the writing-down is work. The benefit is that the Standard's governance is, in the most literal sense, auditable: not auditable in principle, by someone granted special access, but auditable in fact, by anyone, because the entire record is a public repository anyone may clone. For a Standard that asks implementers, users, and regulators to rely on it, the auditability of its governance is not a luxury; it is part of what makes the reliance reasonable, and the cost of the discipline is the price of that reasonableness.

---

## Section 11. Frequently raised questions about the governance

*Informative. The governance has been presented to implementers, prospective contributors, and institutional partners, and a recurring set of questions has emerged. Answering them in writing serves the reader.*

**"In Phase A, the founding maintainer decides every RFC. Is that not simply one-person rule?"**

In Phase A the founding maintainer holds the ordinary amendment authority, and the governance does not pretend otherwise — it names this as Phase A's central limitation and designs the Section 6 transition specifically to move beyond it. But two things make Phase A meaningfully different from unconstrained one-person rule. The constitutional commitments are beyond the maintainer's ordinary reach: the maintainer cannot, even as sole Phase-A governing body, weaken a privacy prohibition or the evidence discipline, because those changes require the constitutional procedure with its harm analysis and ninety-day notice. And every decision is public and reasoned: the maintainer must state why each RFC was accepted or rejected, and a reasoned public decision is open to community scrutiny in a way an unexplained fiat is not. Phase A is one person holding the *ordinary* amendment authority, transparently and under constitutional constraint, for a bounded time — not one person ruling without limit or accountability.

**"What stops the founding maintainer from simply never triggering the transition to Phase B?"**

The Phase-A-to-Phase-B gate is defined by objective conditions — a stabilised version, an independent implementation, an identified committee — and the governance commits, publicly and in this document, to the transition. A founding maintainer who met the gate conditions and refused to transition would be in visible breach of a published commitment, and the breach would be apparent to the entire community of implementers and users, whose continued participation is itself the thing the maintainer needs. The governance's protection here is not a mechanism that forces the maintainer's hand — no document can force a person — but the publication of the commitment, which converts a refusal from a private prerogative into a public default. A standard whose maintainer publicly breaks a published governance commitment is a standard implementers will leave, and that consequence is the real enforcement.

**"Can an outside party file an RFC, or is the process closed to the maintainers?"**

The process is open. Anyone may file an RFC, and an RFC from an independent implementer is reviewed by the same process, against the same standard, as an RFC from the founding maintainer. The seven required sections, the review period, the substantive-objection rule, the reasoned decision — all apply identically regardless of who filed. The governance is deliberately not a closed shop; a standard improves fastest when the implementers who hit its rough edges can propose the repairs, and the RFC process is the channel for exactly that.

**"What happens to the Standard if the founding maintainer departs before Phase B?"**

This is the scenario the transition design exists to guard against, and the honest answer is that an early departure would be a difficult moment — which is precisely why the governance commits, in advance, to the transition rather than leaving succession unplanned. If the founding maintainer departed during Phase A, the community of implementers and the open repository would remain: the Standard is openly licensed, its full history and governance record are in a repository anyone may clone, and a successor maintainer or an early-formed steering committee could continue the governance from the public record. The departure would be difficult but not fatal, because the governance has been designed, from version 1.0.0, so that nothing essential exists only in one person's keeping.

**"Why is the Foundation not constituted now, at version 1.0.0?"**

Because a foundation constituted before there is a community to serve and a body of proven practice to institutionalise would be a shell — a legal entity with a constitution but without the substance a constitution is meant to govern. The Phase-B-to-Phase-C gate requires a community of implementers and users substantial enough to constitute a membership, and a demonstrated period of functioning distributed governance, precisely because a foundation is constituted to institutionalise something real. The governance commits to the Foundation and defines the path to it; it declines to constitute it prematurely, and Section 7.4 records that honest status rather than dressing an intention as an accomplishment.

**"Does the open licence mean a hostile party could fork the Standard and take it in a bad direction?"**

A party can fork the Standard — the open licence permits it, and the permission is a constitutional commitment. But a fork is not the AxonOS Standard: the trademark provisions, in the Project's legal material, mean a divergent fork may not use the AxonOS name, and so a fork that took the Standard in a direction the Project rejects would have to do so under a different name, distinguishable from the AxonOS Standard. The open licence guarantees that the Standard's text is free; it does not guarantee that the AxonOS name attaches to every derivative, and the separation of the free text from the controlled name is what lets the licence be genuinely open without the name becoming meaningless.

---

## Section 12. The relationship between governance and the conformance regime

*Informative.* It is worth stating, in closing, how the governance defined in this document relates to the conformance regime of `CONFORMANCE.md`, because the two are easy to conflate and are in fact distinct.

The governance governs the **Standard**: it is the process by which the normative text changes. The conformance regime governs **implementations**: it is the process by which an implementation is tested against the normative text as it currently stands. The governance answers "how does the Standard evolve?"; the conformance regime answers "does this implementation meet the Standard?"

The two meet at exactly one point. An accepted RFC that changes a normative requirement also, through that same RFC's detailed-design section, changes the conformance suite, so that the suite remains the executable expression of the Standard after the change as before. An RFC that adds a requirement adds the test that checks it. An RFC that amends a requirement amends the corresponding test. An RFC that removes a requirement — possible only at a major version — removes its test. The governance process and the conformance suite move together, because an RFC's detailed design is required, by Section 3.2, to address both.

This coupling is why a conformance claim must always name a version: the suite is version-specific because the Standard is, and the governance is what keeps them synchronised. An implementer reading this governance document and the conformance document together should carry away one combined picture. The governance decides what the Standard requires. The conformance suite tests whether an implementation meets what the Standard requires. An accepted RFC updates both, in the same act, so that the requirement and its test never drift apart.

The Standard, the governance that evolves it, and the suite that tests against it are three aspects of one disciplined whole. The discipline is what an implementer ultimately relies on when they choose to build against the AxonOS Standard rather than against a private and unaccountable contract — and the governance is the part of that discipline which guarantees that the contract built against today will still be a recognisable, reasoned, and stably evolved contract for as long as the implementer needs it to be.

---

**End of GOVERNANCE.md.**

*This document is normative. A change to the Standard made otherwise than by the process defined here is not a valid change. The authoritative Standard is always the text this process produces, at the tagged commit it produces.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
