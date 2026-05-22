# Architecture: The Consent Subsystem

*An architecture chapter of the AxonOS Standard. Informative throughout. This chapter elaborates the consent subsystem; the normative requirements are in `STANDARD.md` Sections 15 and 16. Where this chapter and the Standard differ, the Standard governs.*

---

## 1. Purpose of this chapter

The consent subsystem is the AxonOS Standard's mechanism for making a user's permission real. The capability system, the subject of the companion chapter, decides *which categories* of intent an application may receive. The consent subsystem decides something orthogonal and equally fundamental: *whether the user, right now, permits any intent to flow at all* — and, crucially, whether a user who has decided to stop the flow can make that decision *stick*.

The chapter argues that consent, for a brain-computer interface, must be three things that consent in most software is not. It must be **revocable in fact, not merely in principle**: a user who withdraws permission must see the data genuinely stop, within a short and bounded time, not merely see a setting change while the data continues. It must be **enforced below the application**, so that a misbehaving or malicious application cannot ignore or override the user's decision. And its strongest state — the withdrawal of consent — must be **terminal and uncoerceable**: once a user has withdrawn, no party, including the application, including a remote operator, including a future state of the system itself, may quietly turn the data back on.

This chapter explains the three-state consent finite-state machine that delivers these properties, the trusted path that protects the integrity of consent transitions, the timing bound on withdrawal and why it is bounded so tightly, the terminality of the withdrawn state and why terminality is the anti-coercion property, the interlock by which the kernel enforces consent on every observation, and the relationship between consent and the Cognitive Hypervisor on stimulation-driving deployments.

## 2. The problem: consent in most software is theatre

Begin with why the BCI domain needs a consent mechanism stronger than the conventional one.

In most software, "consent" is a setting. The user, at some point — at installation, at first run, in a dialog — agrees to something, a bit is set, and the agreement is thereafter a fact recorded in a configuration store. If the user later changes their mind, they find the setting and clear the bit. This is consent as most software implements it, and for most software it is adequate, because most software's data is not especially dangerous and the gap between the setting changing and the data actually stopping is not especially harmful.

For a brain-computer interface this conventional consent is inadequate, and the inadequacy has three parts.

First, conventional consent is often **revocable only in principle**. The user clears the bit, but the data does not necessarily stop — not promptly, not provably. The application may cache the permission; a background process may not re-check the bit for some time; the data may continue to flow through a pipeline that was started while consent held and is not re-evaluated. The setting says "no" while the data says "still going", and the user, seeing the setting, believes they have stopped something they have not stopped.

Second, conventional consent is often **enforced at the wrong layer**. The bit is checked, if it is checked, by the application itself, or by a library the application links. An application that wished to ignore the user's revocation — a malicious application, or merely a careless one — could simply not check the bit, or check it and proceed anyway, and nothing structural would prevent it. The user's "no" is enforced only by the good behaviour of the very software the user might be trying to say "no" to.

Third, conventional consent is **reversible without the user**. The bit can be set again — by the application, by an updater, by a remote operator, by any code with access to the configuration store — without a fresh, deliberate act by the user. A user who withdrew consent yesterday may find it quietly granted again today, by software acting on its own behalf, and conventional consent provides no mechanism that makes withdrawal *stay* withdrawn.

The consent subsystem is the AxonOS Standard's correction of all three inadequacies. It makes revocation a fact, not a principle, by bounding the time within which the data must stop. It enforces consent below the application, in the kernel, so that no application can ignore it. And it makes the withdrawn state terminal, so that withdrawal cannot be reversed without the user. Conventional consent is, the chapter contends, often theatre — a setting that gestures at control without delivering it — and the consent subsystem is built to make consent real.

## 3. The three-state finite-state machine

The consent subsystem models consent as a finite-state machine with exactly three states. This section defines the states, the transitions among them, and the reasoning behind having exactly three.

### 3.1 The three states

The **granted** state is the state in which the user permits intent observations to flow. In the granted state the consent interlock, described in Section 6, permits the kernel to publish observations normally. A freshly installed manifest places its consent machine in the granted state — installing a manifest is itself a deliberate user act of permission, and the granted state is its consequence.

The **suspended** state is the state in which the user has temporarily paused the flow. In the suspended state no observation flows; a consumer that requests observations receives the consent-suspended error. The suspended state is *resumable*: from it, the user may return to the granted state, and the flow resumes. The suspended state exists for the user who wants to stop the data now but intends to resume later — a user stepping away, a user who wants a private interval — and who should be able to do that without the heavier act of withdrawing and re-installing a manifest.

The **withdrawn** state is the state in which the user has permanently revoked permission. In the withdrawn state no observation flows; a consumer receives the consent-withdrawn error; and — this is the defining property — the withdrawn state is *terminal*. From the withdrawn state there is no transition back to granted and no transition to suspended. The flow does not resume. The only way the user receives observations again is to install a fresh manifest, which is a new, deliberate act of permission creating a new consent machine; the old machine, once withdrawn, stays withdrawn forever.

### 3.2 The transitions

The admissible transitions among the three states are exactly these. From **granted**, the machine may transition to **suspended** (the user pauses) or to **withdrawn** (the user revokes). From **suspended**, the machine may transition to **granted** (the user resumes) or to **withdrawn** (the user, having paused, decides to revoke outright). From **withdrawn**, the machine may transition nowhere: the withdrawn state has no outgoing transitions.

The two transitions that are *not* admissible, and that a conformant implementation must refuse, are the transition from withdrawn to granted and the transition from withdrawn to suspended. These two refusals are the terminality of the withdrawn state expressed as a property of the transition graph, and the conformance suite's test C3-T03 checks exactly that they are refused.

Additionally, a re-application of the machine's current state — a granted event applied to a machine already granted, a suspended event to a machine already suspended — is *idempotent*: it succeeds, leaves the state unchanged, and raises no error. Idempotency, the subject of Section 5.4, lets the trusted path recover cleanly from a lost or duplicated message.

### 3.3 Why exactly three states

Three states is the minimum that distinguishes the three things a user genuinely needs consent to express, and adding a fourth would add no genuine distinction.

The user needs to express *permission* — "the data may flow" — and that is the granted state. The user needs to express a *temporary stop* — "pause the data; I will resume" — and that is the suspended state, distinct from granted because the data is stopped and distinct from withdrawn because it is resumable. And the user needs to express a *permanent revocation* — "stop the data and do not let it resume without a fresh decision by me" — and that is the withdrawn state, distinct from suspended precisely in its terminality.

A two-state machine — on and off — could not distinguish the temporary pause from the permanent revocation, and the distinction matters enormously: a user who merely wanted to pause would, in a two-state machine, have no pause and would have to choose between leaving the data on and permanently revoking. A four-state machine would have to invent a fourth thing for the user to express, and there is no fourth thing: permission, temporary stop, and permanent revocation exhaust what consent is. Three states is the exact number, neither padded nor cramped, and the finite-state machine has exactly three.

## 4. The trusted path

A consent state machine is only as trustworthy as the channel by which its transitions are signalled. If an application could synthesise a consent event — could send the kernel a "transition to granted" message that the kernel could not distinguish from a genuine user act — then the consent machine would be worthless, because the application could grant itself consent the user never gave, or could prevent a withdrawal from registering. The integrity of the consent machine rests entirely on the integrity of the channel that carries its transition events, and that channel is the trusted path.

### 4.1 What the trusted path is

The trusted path is the input channel through which consent transitions are signalled, and its defining property is that the application layer **provably cannot synthesise an event on it**. A consent event that arrives over the trusted path is, by construction, a genuine user act; the application cannot forge one, because the application has no access to the channel.

### 4.2 The forms the trusted path may take

The Standard does not mandate a single physical realisation of the trusted path; it mandates the property — unforgeable by the application — and permits any realisation that genuinely delivers it. Three realisations are recognised.

The first is a **physical hardware control**: a button, a switch, wired directly to the kernel's hardware, whose state the kernel reads from a hardware register that no application-core software can write. A press of the button is a hardware event; application software, running on the application core, has no path by which to make the kernel's hardware register report a press that did not happen. The physical control is the simplest trusted path and the easiest to reason about: its unforgeability is a fact of the wiring.

The second is a **Secure-World user-interface partition**: on hardware with the ARM TrustZone-M security extension, a small user-interface component running in the Secure World, hardware-isolated from the Normal World where the application core's software runs. The user interacts with the Secure-World component to signal a consent transition; the Normal-World application cannot reach into the Secure World to synthesise that interaction. The Secure-World partition is the realisation used on deployments that already have TrustZone-M for the Cognitive Hypervisor, and it allows a richer consent interface than a single button while keeping the unforgeability.

The third is any **equivalent software-unforgeable channel** that an implementer can demonstrate genuinely delivers the property. The Standard leaves this category open because it cannot anticipate every hardware platform, but it places the burden of proof on the implementer: a channel claimed as a trusted path must be accompanied by a genuine argument that the application provably cannot synthesise an event on it, and a channel for which that argument cannot be made is not a trusted path, whatever else it is.

### 4.3 Why the trusted path is the most security-critical input

The chapter states plainly that the trusted path is the most security-critical input in the entire consent subsystem, and it is worth being explicit about why.

Every other part of the consent subsystem — the three-state machine, the timing bound, the terminality, the interlock — is logic that operates *on* consent events. The trusted path is the channel that *delivers* consent events, and it is therefore the foundation on which all that logic stands. If the trusted path is sound, the logic operates on genuine user acts and the whole subsystem is trustworthy. If the trusted path is compromised — if an application can synthesise an event on it — then the logic, however correct, is operating on forged inputs, and a perfectly correct three-state machine fed forged transitions produces a perfectly consistent but entirely false consent state. The trusted path is the single point on which the subsystem's trustworthiness most depends, and the conformance suite's test C3-T06 checks the property directly: it submits a consent event from an application-layer source and confirms the event is refused.

## 5. The withdrawal timing bound

The withdrawn state stops the data; the timing bound governs *how fast* it stops the data. This section explains the bound, its two components, and why it is bounded so tightly.

### 5.1 The two timescales of withdrawal

A withdrawal of consent has its effect across two distinct timescales, and the Standard bounds both.

The first is the **state-transition time**: the time for the consent machine itself to process a withdrawal event and move into the withdrawn state. This is a computation inside the kernel — receiving the event over the trusted path, executing the transition function, updating the state — and it is bounded, at evidence level L1, as a bounded number of processor cycles. The conformance suite's test C3-T02 proves this bound over the whole space of starting states and well-formed withdrawal events.

The second is the **end-to-end withdrawal time**: the wall-clock time from the user's act of withdrawal to the actual cessation of the observation stream that a consumer sees. This includes the state-transition time, plus the time for the next consent-interlock check to observe the new state, plus the propagation of the resulting consent-withdrawn error to the consumer. This end-to-end time is bounded at ten milliseconds, at evidence level L2, and the conformance suite's test C3-T05 measures it on the reference hardware.

### 5.2 Why ten milliseconds

The ten-millisecond end-to-end bound is not arbitrary. It is short enough to be, for the user, effectively immediate: a user who withdraws consent and sees the data stop within ten milliseconds experiences the withdrawal as instantaneous, because ten milliseconds is below the threshold of perceptible delay for an action of this kind. The bound is the operational meaning of the Standard's promise that withdrawal is "revocable in fact": the data does not merely eventually stop, it stops within a tenth of the time it takes to blink, and a user can therefore *trust* the withdrawal — can see, in the moment, that it worked.

The bound is also short enough to be a genuine safety property. On a stimulation-driving deployment, where withdrawal of consent must also disable stimulation, ten milliseconds is short enough that a user withdrawing consent because something is wrong — because the stimulation is uncomfortable, because something feels off — has the stimulation stopped before the next stimulation epoch could deliver another pulse. The bound is the difference between a withdrawal that protects the user in the moment of need and one that registers too slowly to matter.

### 5.3 Why the two components carry different evidence levels

The state-transition time is bounded at L1 — a formal proof — and the end-to-end time at L2 — a measurement. The asymmetry follows the validation discipline's general principle that each quantity carries the evidence appropriate to its kind. The state-transition time is a property of a piece of kernel code processing an input, and a bounded-model-checking proof can range over the whole input space and prove the cycle bound; it is exactly the kind of quantity L1 evidence suits. The end-to-end time additionally includes the interlock-check latency and the error-propagation latency, which involve the timing of the running system as a whole, and the appropriate evidence for that system-level wall-clock quantity is a measurement on the reference hardware. The Standard bounds the inner, purely computational component at L1 and the outer, system-level component at L2, each at the level its nature admits.

## 6. The consent interlock

The consent state machine holds the state; the consent interlock is the mechanism by which that state actually governs the flow of observations. This section describes the interlock.

### 6.1 The interlock check

Before the kernel publishes any intent observation, it consults the consent state. This consultation is the consent interlock, and it sits on the kernel's publication path: every observation, without exception, passes the interlock check before it is published.

If the consent state is granted, the interlock permits the publication, and the observation flows. If the consent state is suspended, the interlock suppresses the publication and causes the consumer to receive the consent-suspended error instead of an observation. If the consent state is withdrawn, the interlock suppresses the publication, causes the consumer to receive the consent-withdrawn error, and the stream terminates.

### 6.2 Why the interlock is in the kernel

The interlock is in the kernel — on the kernel's publication path, below the application — and this placement is the structural answer to the second inadequacy of conventional consent identified in Section 2: that conventional consent is enforced at the wrong layer.

Because the interlock is in the kernel, on the path every observation must traverse, an application cannot bypass it. There is no code path by which an observation reaches the application without passing the interlock, because the interlock is on the single path the kernel uses to publish, and the application receives observations only through that path. An application that wished to ignore the user's withdrawal — to keep receiving data after consent was withdrawn — has no mechanism to do so, because the data it would receive is data the kernel would have to publish, and the kernel will not publish past a withdrawn interlock. The user's "no", enforced in the kernel, is enforced against the application, not by the application; and that is exactly the property conventional application-layer consent enforcement lacks.

### 6.3 The interlock and the timing analysis

The interlock check is a small piece of computation on the publication path, and like everything on the signal-processing core's critical path it has a worst-case execution time that the kernel's timing analysis must account for. The interlock check is deliberately tiny — it reads the consent state, a single value, and branches — so that its contribution to the worst-case response time is negligible. The consent machine's state is held in a way the publication task can read without blocking and without allocation, consistent with the non-blocking producer discipline of the inter-process-communication channel, so that the interlock check, though it is on the critical path, does not threaten the dual-core contract's clause DC1.

## 7. The terminality of the withdrawn state

The terminality of the withdrawn state — the property that the withdrawn state has no outgoing transitions, that withdrawal cannot be reversed — is the consent subsystem's anti-coercion property, and it deserves a section of its own.

### 7.1 What terminality means precisely

Terminality means that no event, and no sequence of events, however long, drives the consent machine out of the withdrawn state. A withdrawal event applied to a granted or suspended machine moves it to withdrawn; thereafter, a granted event is refused, a suspended event is refused, and another withdrawal event is idempotent — the machine stays withdrawn. The conformance suite's test C3-T04 proves this by ranging over the entire space of event sequences applied to a withdrawn machine and confirming none escapes the withdrawn state.

### 7.2 Why terminality is the anti-coercion property

Consider what the absence of terminality would permit. If the withdrawn state could be left — if some event could transition the machine from withdrawn back to granted — then a withdrawal of consent would be reversible, and the question becomes: reversible by whom? The honest answer is: by whoever can deliver the transitioning event. And the parties who would have an interest in reversing a user's withdrawal are precisely the parties the user withdrew consent *from*: the application that wanted the data, the operator who deployed the application, anyone whose interest is in the data flowing and against the user's decision to stop it.

A reversible withdrawal is therefore a withdrawal subject to coercion. A user could be pressured — by an employer, by a service provider, by anyone with leverage — to allow their withdrawal to be reversed; or the reversal could be performed without the user's knowledge at all, by software acting on the interested party's behalf. The withdrawn state's terminality removes this entire class of pressure and concealment. Because the withdrawn state cannot be left, there is nothing for a coercing party to obtain: no event they could deliver, no pressure they could apply, that would turn the data back on. The only way data flows again is a fresh manifest — a new, deliberate, conspicuous act by the user, creating a new consent machine — and a fresh manifest is exactly the kind of deliberate user act that a user can refuse to perform under pressure and that cannot be performed without them. Terminality converts withdrawal from a setting that can be flipped back into a decision that, once made, stands until the user themselves makes a new and equally deliberate decision.

### 7.3 Terminality and the freshness of re-consent

It is worth being explicit that terminality does not trap the user. A user who withdrew consent and later genuinely wishes to use the BCI again is not prevented from doing so; they install a fresh manifest, and a fresh manifest creates a fresh consent machine in the granted state. What terminality ensures is that this re-consent is *fresh* — that it is a new, deliberate act, not the silent reversal of the old withdrawal. The user who returns does so by deciding, again, to permit; they do not return by having their previous "no" quietly overridden. Terminality is not a restriction on the user; it is a restriction on everyone *other* than the user, and what it restricts them from is reversing the user's decision without the user.

## 8. Consent and the Cognitive Hypervisor

On a stimulation-driving deployment — a deployment in which the BCI not only records but also delivers electrical stimulation to neural tissue — the consent subsystem has an additional and safety-critical relationship with the Cognitive Hypervisor.

### 8.1 The additional obligation of stimulation

A read-only BCI deployment, one that only records, carries the consent obligation this chapter has described: when consent is withdrawn, the observation stream stops. A stimulation-driving deployment carries that obligation and a further one: when consent is withdrawn, the *stimulation* must stop as well. A user who withdraws consent is withdrawing it from the whole interaction, and a deployment that stopped reading the user's neural activity but continued stimulating their neural tissue would have honoured consent in one direction and violated it in the other — and the direction it violated is the one with the direct physical safety stake.

### 8.2 The Cognitive Hypervisor interlock

The Cognitive Hypervisor, which runs in the Secure World and which enforces the neural-tissue charge-density limit on stimulation, also interlocks stimulation with the consent state. Before the Hypervisor permits any stimulation pulse, it consults the consent state — reading it across the Secure-World boundary through a Secure-Monitor call — and a suspended or withdrawn consent state disables stimulation exactly as it disables observation publication.

This means a withdrawal of consent, signalled over the trusted path, propagates to two interlocks: the kernel's consent interlock, which stops the observation stream, and the Cognitive Hypervisor's interlock, which stops the stimulation. Both are bound by the ten-millisecond end-to-end withdrawal bound; a user who withdraws consent on a stimulation-driving deployment sees both the recording and the stimulation cease within that bound. The terminality of the withdrawn state applies to both: once withdrawn, neither recording nor stimulation resumes without a fresh manifest. The consent subsystem and the Cognitive Hypervisor together ensure that a user's "no", on a stimulation-driving deployment, stops everything the BCI does to and with the user, promptly and terminally.

## 9. The boundaries of the consent subsystem

A chapter on a consent mechanism must be frank about its limits.

The consent subsystem ensures that, when the user signals a transition over the trusted path, the kernel honours it: a withdrawal stops the data, within the bound, terminally, enforced below the application. It does not, and cannot, ensure that the user's decision to withdraw is itself uncoerced — a user can be threatened or deceived into *not* withdrawing, or into installing a fresh manifest they would rather not, and no software mechanism can reach the social situation in which the user forms their decision. What the subsystem guarantees is that the decision the user does signal is honoured faithfully; the freedom of the decision itself is a matter beyond software.

The consent subsystem also does not defend against an adversary who can replace the kernel image or breach the Secure World. Its guarantees are guarantees about the behaviour of the genuine kernel and the genuine Hypervisor; an adversary who can substitute modified versions of either can make them do anything, and defending the integrity of the kernel and the Secure-World images is the job of a secure-boot mechanism, not the consent subsystem.

And the consent subsystem governs the flow of intent observations and of stimulation; it does not govern what an application does with observations it received while consent was granted. An application that received navigation intents legitimately, while consent was granted, and stored them, retains that stored data after a later withdrawal — withdrawal stops the *flow*, it does not reach back to *delete* what already legitimately flowed. Governing the retention and deletion of already-delivered data is an application-layer and data-governance concern, addressed by the deployment's data-handling policy, and it is outside the consent subsystem's scope.

Within those boundaries, the consent subsystem does exactly what `STANDARD.md` Sections 15 and 16 require: it makes consent revocable in fact through the ten-millisecond bound, enforced below the application through the kernel interlock, and terminal through the withdrawn state's lack of outgoing transitions. That is a strong and precisely defined guarantee, and the Project states it precisely and does not overstate it.

## 10. The consent finite-state machine as implemented

Sections 3 through 7 described the consent machine as a design; this section describes the reference kernel's implementation of it, because the implementation has properties an implementer must reproduce.

### 10.1 The state representation

The reference kernel represents the consent state as a single small atomic value — an atomic byte — holding one of three discriminant values for granted, suspended, and withdrawn. The state is atomic because it is written by the trusted-path handler and read by the consent interlock on the publication path, and those are different execution contexts; an atomic value can be read by the interlock without a lock and without the possibility of reading a torn, half-updated state. The atomic read is consistent with the non-blocking producer discipline of the inter-process-communication channel: the interlock, which is on the publication critical path, reads the consent state with a single atomic load, an operation whose worst-case time is a small fixed quantity that the timing analysis includes.

### 10.2 The transition function

The transition function takes the current state and an incoming event and produces the next state, or a refusal. It is a small, total, exhaustive function: for every one of the three current states and every kind of incoming event, the function's behaviour is explicitly defined — there is no combination of current state and event for which the function's behaviour is unspecified. This exhaustiveness is what test C3-T03 verifies, and it is what makes the transition function amenable to an L1 proof: a bounded model checker can range over the entire, small, finite space of state-and-event pairs and confirm the function behaves correctly on every one.

The transition function is also written so that the withdrawn state's terminality is structural rather than checked. In the function, the withdrawn state simply has no case that produces a non-withdrawn next state: a granted event applied to a withdrawn machine produces a refusal, a suspended event produces a refusal, a withdrawal event produces withdrawn again. The terminality is not a guard the function evaluates; it is the simple absence, in the function's definition, of any case that leaves the withdrawn state. This is the same structural discipline the capability system uses — a dangerous outcome is prevented by the absence of the code that would produce it, not by a check that forbids it — and it is what lets test C3-T04 prove terminality by exhaustion.

### 10.3 The idempotency of re-application

Section 3.2 noted that re-applying the machine's current state is idempotent. The implementation realises this in the transition function: a granted event applied to an already-granted machine produces granted, with no error and no side effect; likewise suspended applied to suspended. Idempotency matters because the trusted path, like any channel, can lose or duplicate a message, and the recovery from a lost or duplicated message must not produce a spurious state change. If the trusted path re-sends a transition event because it is unsure the first send arrived, the re-send, arriving at a machine already in the target state, must be a harmless no-operation — and idempotency is exactly that guarantee. Test C3-T07 verifies it.

## 11. A worked example: a withdrawal traced end to end

*Informative. The consent subsystem is best understood by tracing a single withdrawal through every component it touches.*

Consider a user, mid-session, who decides to withdraw consent. The user's deployment is a stimulation-driving one, so the withdrawal must stop both recording and stimulation.

The user performs the withdrawal act. On this deployment the trusted path is a physical hardware button wired to the kernel; the user presses it in the manner the deployment defines for withdrawal — say, a long press, distinguishing withdrawal from the short press that suspends. The button press is a hardware event, registered in a hardware register that no application-core software can write.

The kernel's trusted-path handler reads the hardware register, recognises the long press as a withdrawal event, and invokes the consent transition function. The machine is currently in the granted state; the transition function, given granted and a withdrawal event, produces the withdrawn state. The kernel writes the withdrawn discriminant into the atomic consent-state value. This is the state-transition time, bounded at L1 as a bounded number of processor cycles, and test C3-T02's proof covers it.

The next processing epoch's pipeline runs, as every epoch's does, and reaches its publication task. The publication task performs the consent interlock check: it reads the atomic consent state. It reads withdrawn. The interlock therefore suppresses the publication: no observation is written to the inter-process-communication channel, and the consumer, polling the channel, receives the consent-withdrawn error, error code 0x06. The observation stream has terminated.

In the same span, the Cognitive Hypervisor, in the Secure World, performs its own interlock before the next stimulation pulse. It reads the consent state across the Secure-World boundary through a Secure-Monitor call. It reads withdrawn. It disables stimulation: no pulse is delivered.

From the user's button press to the cessation of both the observation stream and the stimulation, the elapsed wall-clock time is within the ten-millisecond end-to-end bound, and test C3-T05's measurement on the reference hardware confirms it. The user, having pressed the button, sees the BCI stop — both halves of it — within a tenth of a second, effectively immediately.

Now the terminality takes effect. Suppose the application, which wanted the data, attempts to restore the flow: it sends, somehow, a granted event toward the kernel. But the application has no access to the trusted path — the trusted path is a hardware button and a hardware register the application cannot write — so the application's attempt is not a trusted-path event at all, and test C3-T06's property ensures a non-trusted-path consent event is refused. Suppose, alternatively, a genuine trusted-path granted event somehow reached the machine — perhaps the user, pressured, pressed the button again. The machine is in the withdrawn state; the transition function, given withdrawn and a granted event, produces a refusal; the machine stays withdrawn. There is no event, from any source, that returns this machine to granted. The only path by which this user receives observations again is the installation of a fresh manifest — a new, deliberate act creating a new consent machine — and that fresh act is one the user performs, or does not, of their own volition.

The trace shows every component doing its defined job: the trusted path delivering a genuine event, the transition function moving to the terminal state, the two interlocks stopping recording and stimulation within the bound, and the terminality refusing every attempt to reverse the withdrawal. The user's "no" was prompt, was complete, was enforced beneath the application, and stands.

## 12. Common objections to the consent subsystem

*Informative.*

**"The terminality of the withdrawn state is harsh. A user who withdraws by accident, or who changes their mind a minute later, must re-install a whole manifest. Why not allow a brief grace period for reversal?"**

The objection proposes a grace period — an interval after withdrawal during which the user could reverse it without the full re-consent. The chapter rejects the grace period, and the reason is precisely the anti-coercion property of Section 7.2. A grace period is, by definition, an interval during which the withdrawn state is *not* terminal — during which an event can return the machine to granted — and an interval during which the withdrawn state is not terminal is an interval during which a coercing party can obtain a reversal. The grace period would be a window of vulnerability, and a coercing party would simply apply their pressure within the window. The cost of terminality without a grace period is real — an accidental withdrawal does require re-installing a manifest — but re-installing a manifest is not an enormous burden, and it is a burden the chapter judges far smaller than the alternative cost of a reversal window that coercion could exploit. The terminality is harsh by design, and the harshness is the protection.

**"Ten milliseconds is an eternity in computing. Why not bound the withdrawal at microseconds, like the response time?"**

The ten-millisecond bound is an end-to-end, system-level, wall-clock bound, and it is not the same kind of quantity as the microsecond-scale worst-case response time. The response time is a property of one epoch's pipeline computation; the end-to-end withdrawal time spans a state transition, the *next* epoch's interlock check, and the propagation of an error to a consumer on the non-deterministic application core. Bounding it at the microsecond scale would require the application-core propagation itself to be microsecond-bounded, and the application core is, by the architecture's design, non-deterministic. Ten milliseconds is the bound that is both *achievable* given the application core's nature and *short enough* to make withdrawal perceptibly immediate and operationally safe. A tighter bound would either be unachievable or would require making the application core deterministic, which the architecture deliberately does not do. Ten milliseconds is the right bound for the kind of quantity this is.

**"If the trusted path is just a hardware button, a malicious actor with physical access could press it — or prevent the user from pressing it. The trusted path is not so trustworthy."**

The objection conflates two threat models. The trusted path's job is to ensure that a consent event is unforgeable *by software* — that the application, the remote operator, the code, cannot synthesise a consent transition. It is not, and does not claim to be, a defence against an adversary with physical control of the device and of the user. An adversary who can physically press the user's withdrawal button, or physically restrain the user from pressing it, has physical coercive control of the situation, and physical coercive control is beyond what any software or hardware consent mechanism can remedy — it is the social-coercion limit the chapter acknowledges in Section 9. What the trusted path guarantees is the software-unforgeability property, and that property is exactly the one that matters against the realistic threat: not an adversary physically present at the device, but an application or an operator, remote or local, trying to override the user's consent through software. Against that threat the hardware button is genuinely trustworthy, because software cannot press it.

## 13. A note to the independent implementer

This chapter exists so that an independent implementer can build a conformant consent subsystem. Three points of guidance.

Build the terminality structurally, not as a check. The withdrawn state must be terminal because the transition function contains no case that leaves it — not because a guard forbids leaving it. An implementer who writes a check "if the state is withdrawn, reject the transition" has built the terminality as a procedural guard, and a procedural guard can be mis-written or removed. The conformant construction is a transition function whose withdrawn cases simply all produce withdrawn or a refusal; the terminality is then a property of the function's shape, and test C3-T04 proves it by exhaustion over the function's whole domain.

Treat the trusted path's unforgeability as a property you must *demonstrate*, not assume. If the implementer's deployment uses a hardware button, the unforgeability is a fact of the wiring and is easy to argue. If it uses a Secure-World partition, the unforgeability rests on the TrustZone-M isolation and must be argued from that. If it uses some other channel, the implementer bears the burden of a genuine argument that the application provably cannot synthesise an event on it. An implementer who simply asserts a channel is trusted, without the argument, has not built a trusted path; test C3-T06 checks the property, but the implementer should be able to argue it independently of the test.

Keep the interlock check tiny and non-blocking. The interlock is on the publication critical path, and the dual-core contract's clause DC1 bounds that path. The interlock check must therefore be a single atomic read of the consent state and a branch — nothing more. An interlock that did more, that took a lock, that allocated, would threaten the timing guarantee. The conformant interlock reads one atomic value and branches, and its tiny worst-case cost is included in the timing analysis without strain.

## 14. Consent in relation to the capability system

*Informative. The consent subsystem and the capability system are the two halves of the AxonOS privacy model, and a reader who has the companion capability-system chapter in mind benefits from seeing precisely how the two relate.*

The capability system and the consent subsystem answer two different questions, and the difference is worth stating sharply because the two are easy to conflate.

The capability system answers a *static, structural* question: of all the categories of neural-derived data, which may this application ever, in principle, receive? Its answer is fixed at the time the application's manifest is installed: the application may receive the closed set of capabilities its manifest declared, and nothing else, ever. The capability system's guarantee does not change moment to moment; it is a property of what types exist and what the manifest granted, and it holds for the application's whole life.

The consent subsystem answers a *dynamic, temporal* question: right now, at this moment, does the user permit any of that to flow at all? Its answer changes moment to moment as the user grants, suspends, and withdraws. The consent subsystem's guarantee is not about *which categories* but about *whether, now*.

The two compose, and the composition is the full privacy model. An observation reaches an application only if *both* gates are open: the capability gate, which requires the observation's category to be one the application's manifest declared, and the consent gate, which requires the user's consent state to be granted. The capability system bounds the *worst case* of what an application could ever see; the consent subsystem gives the user *live, revocable control* within that bound. An application restricted by the capability system to navigation intents alone still receives nothing if the user has suspended or withdrawn consent; a user who has granted consent still has their application restricted to the categories the capability system allows. Neither subsystem substitutes for the other: the capability system without consent would give the user no live control, only a fixed bound; consent without the capability system would give the user an on-off switch over an unbounded firehose. Together they give what the privacy model intends — a tightly bounded set of categories, and live, revocable, terminal user control over the flow within that set.

An implementer building a complete AxonOS deployment implements both, and implements them as the two distinct subsystems they are: the capability system enforced structurally at the application binary interface through the type system and the manifest, the consent subsystem enforced through the three-state machine and the kernel interlock. The conformance suite tests them in separate categories — C2 for the capability system, C3 for consent — because they are separate guarantees, and a deployment is conformant only when both are present and both pass.

## 15. Consent across the application binary interface

*Informative. The consent subsystem's effects reach the application through the application binary interface, and this section describes that crossing precisely, because an implementer of the software development kit must reproduce it.*

The consent state lives in the kernel; the application lives above the software development kit; and the consent subsystem's effects therefore travel from the kernel, across the application binary interface, through the software development kit, to the application. The crossing uses no special channel — it uses the ordinary application-binary-interface error mechanism.

When the consent interlock suppresses an observation because the state is suspended, the consumer — the software development kit — receives, in place of an observation, the consent-suspended error, error code 0x05. When the interlock suppresses because the state is withdrawn, the consumer receives the consent-withdrawn error, error code 0x06. These are two of the closed enumeration of error codes the application binary interface defines, and the consent subsystem's communication with the application layer is entirely through them: the consent state itself never crosses the interface as a queryable value; what crosses is the *effect* of the state, expressed as the appropriate error in place of a suppressed observation.

The software development kit, on receiving error code 0x05 or 0x06, propagates it to the application as a typed error, as it propagates every application-binary-interface error. The application thus learns of the consent state's effect in the same way it learns of any other condition that stops observations — as a typed error delivered where an observation would have been. The application is *required*, by `STANDARD.md`'s constraint on the application layer, to behave correctly on receipt of these two error codes: on consent-suspended, an application should cease acting as though it were receiving live intent and should be prepared for observations to resume; on consent-withdrawn, an application should cease acting on intent entirely and should understand that the stream has terminated and will not resume without a fresh manifest. An application that ignored these errors — that continued to behave as though intent were flowing — would be misbehaving, though the consent subsystem's guarantee holds regardless: the kernel has stopped publishing, so an application ignoring the error simply receives nothing, and its misbehaviour harms only its own correctness, not the user's privacy.

The distinction between the suspended error and the withdrawn error matters to the application and the software development kit must preserve it. The suspended error signals a *resumable* condition: the application should expect that observations may begin again, and should hold itself ready. The withdrawn error signals a *terminal* condition: the application should expect nothing further from this stream, ever, and a software development kit that presented the withdrawn error to the application as though it were merely another transient interruption would mislead the application about the finality of what had happened. The two error codes are distinct because the two consent states they reflect are distinct in exactly the property — resumability versus terminality — that the application most needs to know, and the application binary interface carries that distinction faithfully from the kernel's consent machine to the application's error handler.

This crossing is why the conformance suite tests the consent subsystem partly through the error-taxonomy category: tests C5-T05 and C5-T06 check that the consent-suspended and consent-withdrawn errors are emitted in the right circumstances, and test C3-T08 checks that the suspended state produces the suppression and the error together. The consent subsystem and the application binary interface are not separate concerns at this point; the interface is the medium through which consent's effect reaches the application, and an implementer must build the consent subsystem and the software development kit's error handling as the two ends of one path.

## 16. Summary

The consent subsystem is the AxonOS Standard's mechanism for making a user's permission real, correcting the three inadequacies of conventional software consent: that it is revocable only in principle, enforced at the wrong layer, and reversible without the user. The three-state finite-state machine — granted, suspended, withdrawn — gives the user exactly the three things consent must express: permission, a resumable temporary stop, and a terminal permanent revocation, and the implementation realises the machine as a small atomic state and an exhaustive, total transition function whose withdrawn cases structurally never leave the withdrawn state. The trusted path, unforgeable by the application and realised as a hardware control, a Secure-World partition, or a demonstrably equivalent channel, is the most security-critical input, because every part of the consent logic stands on the genuineness of the events it delivers. The withdrawal timing bound has two components — an L1-proven bound on the state-transition computation and an L2-measured ten-millisecond bound on end-to-end cessation — the ten milliseconds being short enough that withdrawal is perceptibly immediate and operationally safe. The consent interlock, on the kernel's publication path below the application, makes consent enforced against the application rather than by it, and is kept tiny and non-blocking. The terminality of the withdrawn state is the anti-coercion property: because the withdrawn state has no outgoing transitions, there is nothing a coercing party could obtain that would reverse a user's withdrawal, and the only return is a fresh, deliberate manifest. On stimulation-driving deployments the consent state additionally interlocks the Cognitive Hypervisor. The consent subsystem and the capability system together constitute the full privacy model — the capability system bounding which categories an application could ever receive, the consent subsystem giving live revocable control over whether anything flows within that bound — and an observation reaches an application only when both gates are open. The consent state's effect reaches the application across the application binary interface as the consent-suspended and consent-withdrawn error codes, the distinction between which carries the crucial resumable-versus-terminal information faithfully to the application's error handler. The subsystem's boundaries are stated frankly: it honours the decision the user signals, not the social freedom of the decision; it guards the genuine kernel and Hypervisor, not a substituted image; and it governs the flow of data, not the retention of data that already flowed. The consent subsystem is the structural reason a user's "no", in an AxonOS deployment, is real — prompt, enforced beneath the application, and, once given as a withdrawal, terminal.

---

*End of the consent-subsystem architecture chapter.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
