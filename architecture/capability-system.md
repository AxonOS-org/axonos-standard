# Architecture: The Capability System and Neural Permissions

*An architecture chapter of the AxonOS Standard. Informative throughout. This chapter elaborates the capability system; the normative requirements are in `STANDARD.md` Sections 12 through 14. Where this chapter and the Standard differ, the Standard governs.*

---

## 1. Purpose of this chapter

The capability system is the AxonOS Standard's privacy model. It is the answer to a question that every brain-computer interface must answer and that most answer badly: given that a BCI processes the most intimate data a human being generates, what mechanism decides which of that data an application is permitted to receive, and how strong is that mechanism?

The conventional answer — a runtime permission check, an access-control list, a settings toggle — is, this chapter will argue at length, structurally inadequate to the BCI domain. The AxonOS answer is different in kind: it makes the permission a property of the type system, enforced by the compiler before the system runs, rather than a property of a runtime check that executes while the system runs. The difference between those two — between a privacy guarantee that is *structural* and one that is *procedural* — is the subject of this chapter, and it is, the Project believes, the single most important idea in the Standard after the real-time guarantee itself.

This chapter explains the capability principle, contrasts it sharply with the conventional runtime-permission approach, walks through the four capabilities the Standard admits and the four categories it permanently prohibits, describes the manifest by which an application declares what it requests, and is frank about the boundaries of what the capability system does and does not protect against.

## 2. The problem: neural data is not application data

Begin with why the BCI domain needs a privacy model stronger than the conventional one.

Ordinary application data — a document, a photograph, a contact list — is data the user deliberately created or deliberately provided. It is sensitive, sometimes highly so, and it deserves protection, and the conventional mechanisms of access control are the appropriate protection for it. The user chose to write the document; the question is only who else may read it.

Neural data is different in a way that matters. The user did not deliberately create it. It is generated continuously, involuntarily, as a byproduct of the user simply being a thinking being with electrodes in contact with their nervous system. It is not a document the user chose to write; it is closer to a continuous, unfiltered transcript of the substrate of the user's mind, and the user has no more chosen its content than a person has chosen the rhythm of their heartbeat. This involuntary quality is what makes neural data more dangerous than ordinary application data: it is more revealing, because it was not curated by the user before it existed, and it is correspondingly more capable of being turned against the user, because it contains things the user would never have chosen to disclose.

A privacy model adequate to ordinary application data is therefore not adequate to neural data, because the conventional model's implicit assumption — that the data is a discrete, user-created artefact whose only question is its audience — does not hold. The neural data is a continuous involuntary stream, and the question is not merely who may read a chosen artefact but what categories of inference about the user may be drawn from the stream at all. The capability system is the AxonOS Standard's answer to that sharper question.

## 3. The capability principle

The capability system rests on a single principle, and the principle can be stated in one sentence: **the application receives typed intents, never neural data, and the set of intent types is closed.**

Unpack the sentence. The application does not receive the neural signal. It does not receive features extracted from the neural signal. It does not receive the classifier's internal state. It receives *intents*: typed values, each drawn from a small, fixed, closed set, each representing a single narrow conclusion — "the user expressed a leftward navigation intent", "the signal quality is currently 0.8", "an artefact was detected". The intent is the kernel's conclusion, radically narrower than the data the conclusion was drawn from, and the intent is all the application ever sees.

A **capability**, in this system, is a type-level token authorising the application to receive one specific category of intent. The navigation capability authorises navigation intents. The workload-advisory capability authorises workload-advisory intents. There are exactly four capabilities, the set is closed, and an intent whose category corresponds to no capability simply has no path to the application — not a path that is checked and blocked, but no path at all.

The phrase "type-level token" is the heart of it, and Section 4 is devoted to what it means. But the principle, stated plainly, is already most of the privacy model: the application's access to the user's neural interior is mediated entirely through a closed set of four narrow, typed intent categories, and everything else — the raw signal, the features, the affective inferences, the identifying patterns — is not access-controlled but absent from the interface entirely.

## 4. Capabilities as types, not flags

This section is the conceptual core of the chapter. It contrasts, as sharply as possible, the two ways a privacy mechanism can be built, and explains why the AxonOS Standard chooses the one it chooses.

### 4.1 The conventional way: the runtime permission flag

The conventional way to control access to a category of data is the runtime permission flag. The data exists in the system's memory. The code that could deliver it to the application exists. And between the data and the application stands a check — an `if` statement, testing a permission bit:

The structure is: *if the application holds the raw-signal permission, deliver the raw signal.* The permission bit is set or cleared by some configuration act; the check consults it; the data flows or does not according to the check's result.

This is how file-system permissions work. It is how the permission systems of mobile operating systems work — the dialog that asks whether an app may access the camera sets a bit, and a runtime check consults it. It is the overwhelmingly dominant pattern, and for ordinary application data it is appropriate.

### 4.2 The three structural weaknesses of the runtime flag

For neural data, the runtime permission flag has three structural weaknesses, and in the BCI domain each is serious enough on its own to disqualify the pattern.

The first weakness is that **the check can be wrong**. The check is a line of code — an `if` statement with a condition — and lines of code have bugs. The condition can be inverted, so that the check passes exactly when it should fail. The permission constant can be mistyped, so that the check consults the wrong bit. The check can be present on one code path that delivers the data and absent on a second path that also delivers it, so that the data flows unchecked through the path the developer forgot. None of these bugs announces itself; the system does not crash; it simply delivers data it should have withheld, silently, and the silence is what makes the weakness serious — a privacy failure that produced a crash would at least be noticed.

The second weakness is that **the check can be removed**. The check is a line of code, and lines of code are edited. A future maintainer, working under deadline pressure, merging a branch, refactoring a module, deletes the `if` statement — perhaps believing it redundant, perhaps not noticing it, perhaps merging carelessly — and a regression ships in which the data flows unconditionally. The check's protection lasts exactly as long as no one removes the check, and over a system's maintenance lifetime, across many maintainers and many revisions, "no one removes the check" is not a property anyone can guarantee.

The third weakness is the deepest: **the data exists**. Even when the check is correct, present on every path, and never removed, the sensitive data is still sitting in the system's memory, because the check controls only whether the data is *delivered*, not whether it *exists*. And data that exists in memory can leak by paths that have nothing to do with the check: a buffer over-read in an unrelated component, a use-after-free, an uninitialised-memory disclosure, any of the memory-safety bugs that afflict real systems can expose the data, because the data is there to be exposed. The runtime-flag pattern protects the front door and leaves the data sitting in the house.

### 4.3 The AxonOS way: the capability as type

The AxonOS capability system eliminates all three weaknesses by a single move: it makes the capability a type, and it makes a prohibited category of data a type that does not exist.

In the AxonOS kernel's interface, there is no type representing raw neural signal. There is no `RawNeuralSignal` type, no `EmotionEstimate` type, no `CognitiveProfile` type, no `BiometricIdentity` type. The intent observation that crosses the kernel boundary is a typed value, and its type permits it to carry one of exactly the four admitted intent categories and nothing else. A value carrying raw neural signal across the boundary would need a type to be a value *of*, and that type is not in the interface.

Consider what this does to each of the three weaknesses.

The check cannot be **wrong**, because there is no check. There is no `if` statement testing a raw-signal permission, because there is no raw-signal data path for an `if` statement to guard. The enforcement is the type system: a function that tried to return raw neural signal across the kernel boundary would have a return type that does not exist, and the code would not compile. A type error is not a runtime conditional that can be mis-written; it is a compile-time refusal, and the compiler does not have an off day.

The check cannot be **removed**, because there is nothing to remove. A future maintainer who wished to expose raw neural signal could not do it by deleting an `if` statement, because there is no `if` statement. They would have to *add* a type to the interface, add the functions that produce and consume values of that type, add the code paths that carry it — a substantial, conspicuous, reviewable construction, not a quiet deletion. The capability system converts the act of weakening privacy from an easy subtraction that can happen by accident into a hard addition that can happen only on purpose and in plain sight.

And the data does not **exist** as a boundary-crossing typed value. The kernel computes intents from neural data internally, and internally the neural data is of course present — it must be, for the kernel to do its work — but it is present *inside the kernel*, behind the kernel boundary, and it never becomes a typed value on the application's side of that boundary because no type for it exists there. A memory-disclosure bug in the application-facing interface has, among the types that interface defines, nothing of the prohibited categories to disclose, because those categories were never given a type to inhabit on that side of the boundary.

### 4.4 Why this is a structural guarantee

The phrase the chapter uses for the AxonOS privacy guarantee is that it is *structural*, and the word is precise. A structural guarantee is a guarantee that follows from the shape of the system — from what types exist, what functions can be written, what code can compile — rather than from the runtime behaviour of the system's code. A structural guarantee is checked by the compiler, before the system runs, and it holds for every execution because it is not a property of any execution; it is a property of the program's structure, which every execution shares.

The runtime-flag guarantee is, by contrast, *procedural*: it follows from the system's code behaving correctly at runtime — from the right `if` statement being present, correct, and reached. A procedural guarantee is only as good as the procedure, and the procedure is fallible code.

The AxonOS capability system is the deliberate choice of a structural guarantee over a procedural one for the most sensitive data the system handles. It is the same idea that underlies the capability-based operating systems of the research tradition and the capability-oriented sandboxing libraries of recent practice: authority is an unforgeable token, and the absence of the token is the absence of the authority, structurally, not the failure of a check. The AxonOS Standard adapts that idea to the BCI domain by fixing the closed set of exactly four capabilities, and by making the four prohibited categories not merely unauthorised but typeless.

## 5. The four admitted capabilities

The closed set of capabilities at application-binary-interface version 1 has exactly four members. This section describes each: what intent it carries, why that intent is safe to admit, and why its rate ceiling is set where it is.

### 5.1 The navigation capability

The navigation capability authorises navigation intents: directional intentions — a leftward, rightward, upward, or downward intent — together with focus and scroll events. It is the capability an assistive cursor-control application holds; it is the capability that lets a user with motor impairment move a pointer and select.

Navigation is the highest-bandwidth of the four capabilities, with a rate ceiling of 50 hertz, because directional control is the use case that most needs responsiveness: a cursor that updates only a few times a second feels unusable, and 50 hertz is the rate at which directional control feels direct. Navigation is safe to admit at that rate because a stream of directional intents, however fast, reveals only the directions the user intended — it is the BCI equivalent of a stream of arrow-key presses, and a stream of arrow-key presses, while it reveals what the user is navigating, does not reveal the user's emotional state, does not build a cognitive fingerprint, does not identify the user. Navigation is the capability whose intent category is both most useful and least dangerous, and it is admitted at the highest rate for exactly that reason.

### 5.2 The workload-advisory capability

The workload-advisory capability authorises workload-advisory intents: a coarse, three-level estimate of the user's current cognitive load — low, medium, or high. It is the capability a workload-monitoring application holds; it is the capability that lets a tool advise a user, or a system, that the user is currently under heavy cognitive load and perhaps should not be interrupted.

Workload-advisory is the most sensitive of the four admitted capabilities, and its design reflects that. Its rate ceiling is 1 hertz — one estimate per second — and its values are quantised to just three coarse levels. Both of those are privacy controls, and they are deliberate. A cognitive-load estimate sampled at high rate and fine resolution would be a cognitive timeline: a detailed, continuous record of how the user's mental effort rose and fell through every moment of their day, and such a timeline is close to the prohibited cognitive-profile category. The 1-hertz ceiling and the three-level quantisation are what keep the capability *advisory* — a coarse, occasional hint — rather than a profiling instrument. Workload-advisory is admitted because the coarse hint is genuinely useful and, at one coarse sample per second, genuinely not a profile; the ceiling and the quantisation are the line between the two, and the Standard draws that line deliberately and holds it.

### 5.3 The session-quality capability

The session-quality capability authorises session-quality intents: a scalar quality metric, in the range zero to one, describing the current quality of the neural signal — how clean the recording is, how well the electrodes are making contact, how confident the system can be in its decoding. It is the capability that lets an application tell a user "the signal is poor, please adjust the headset" or adapt its own behaviour to degraded signal quality.

Session-quality has a rate ceiling of 2 hertz. It is safe to admit because the quality metric is a property of the *recording*, not of the user: it describes how good the signal is, which is a fact about electrode contact and noise, and it reveals nothing about the user's intentions, emotions, or identity. A stream of signal-quality scalars tells an eavesdropper how well the headset is working and nothing about the mind beneath it.

### 5.4 The artefact-events capability

The artefact-events capability authorises artefact-events intents: edge-triggered events signalling that a signal artefact — a muscle movement, an electrode disturbance — has been detected, or that a previously detected artefact has cleared. It is the capability that lets an application know that the current stretch of decoding is unreliable because the signal is contaminated, and discount it accordingly.

Artefact-events has a rate ceiling of 10 hertz. It is safe to admit because an artefact event reveals only that the signal was disturbed, not what disturbed it in any detail and certainly nothing about the user's cognition: it is a reliability flag, a "trust the next stretch less" signal, and a stream of such flags carries no inference about the user's interior.

### 5.5 Why exactly these four, and why closed

The four capabilities are the four intent categories that the Project's analysis found to be simultaneously *useful* — each enables a real and valuable class of application — and *safe* — each, at its specified rate and resolution, reveals only its narrow intended conclusion and does not compose into one of the prohibited categories. The set is closed, fixed at the application-binary-interface version, because closure is what makes an application's possible accesses enumerable and bounded: a user, a reviewer, or a regulator examining an AxonOS deployment can know that the application's entire access to the user's neural interior is some subset of these four narrow categories, and that knowledge — the completeness of the enumeration — is itself a privacy property. An open, extensible capability set would mean the enumeration was never complete, and the assurance the closure provides would be lost.

## 6. The four prohibited categories

Against the four admitted capabilities stand four prohibited categories: categories of neural data that the Standard does not merely leave unauthorised but structurally prohibits, in the sense of Section 4 — no type for them exists in the interface, and so no capability for them can be held and no value of them can cross the kernel boundary.

### 6.1 Raw neural signal

Raw neural signal — the unprocessed or lightly processed sample stream from the acquisition layer — is prohibited because it is the universal solvent. From the raw signal, given sufficient computation, every other inference can in principle be derived: the affective state, the cognitive profile, the biometric identity are all latent in the raw signal, waiting for an algorithm to extract them. To expose the raw signal would be to expose, implicitly, everything the other prohibitions forbid, and so the raw-signal prohibition is the keystone: it is prohibited so that the other three prohibitions can be meaningful, because a system that handed out the raw signal would have made the other three prohibitions empty.

### 6.2 Affective state

Affective state — any representation of the user's emotional condition — is prohibited because a continuously available emotion estimate is an instrument of manipulation. A party that knows the user's emotional state, and whose interests diverge from the user's, can time its persuasion, its pricing, its demands, to the user's moments of greatest vulnerability — the moments of anxiety, of fatigue, of low resistance. The Project's analysis, recorded in `STANDARD.md` Section 13.3, found no use of a continuously available affective-state estimate that is reliably in the user's interest and many that are reliably against it, and the category is therefore prohibited outright rather than access-controlled.

### 6.3 Cognitive profile

Cognitive profile — any persistent, identifying representation of the user's cognitive characteristics, accumulable across sessions into a stable fingerprint of how a particular mind works — is prohibited because such a fingerprint is an instrument of discrimination. A profile of a mind's speed, its lapses, its characteristic patterns is exactly the data that, in the hands of an employer screening candidates, an insurer pricing risk, or a credentialing body gating access, becomes a basis for exclusion. The prohibition exists so that the use of a brain-computer interface cannot become the mechanism by which a person is cognitively profiled and then, on the basis of the profile, excluded.

### 6.4 Biometric identity

Biometric identity — any representation of neural activity usable to identify the user as a specific individual — is prohibited because neural-pattern identification is an instrument of surveillance. A BCI that could identify its user from their neural activity could be made to report who is using it; a population of such BCIs could be made into an identification network that tracked individuals by the signature of their own nervous systems. The prohibition keeps the BCI an instrument the user wields rather than an instrument that watches and identifies the user.

### 6.5 The cost of reversal

The four prohibitions are constitutional commitments, in the sense of `STANDARD.md` Section 28 and the governance document. They cannot be reversed by an ordinary minor or patch revision. Adding a capability that exposed any prohibited category would require a major-version increment, a published harm analysis that confronted directly the harms the prohibition was enacted to prevent, a ninety-day notice period, and the approval of the governing body. The cost of reversal is set deliberately high, because a prohibition that could be cheaply reversed would not be a prohibition a user could rely on, and the entire value of the prohibitions is that a user can rely on them.

## 7. The manifest

An application declares which capabilities it requests through a manifest: a signed, structured record the kernel verifies and installs before the application receives any observation.

### 7.1 The manifest's four fields

The manifest is a Concise Binary Object Representation map with four fields. The application identifier is a reverse-DNS-form string, at most 64 bytes, naming the application. The capability set is a 32-bit field in which each of the low four bits requests one of the four capabilities; the admissible mask is the constant value with exactly those four bits available, and a manifest with any higher bit set is refused. The maximum rate is a 16-bit field giving the observation rate the application requests, which must not exceed the smallest rate ceiling among the capabilities the application declares. The signature is a 64-byte Edwards-curve digital signature, computed by the application developer's signing key over the other three fields.

### 7.2 Manifest verification

At installation the kernel verifies the manifest and refuses it if any check fails. The signature must verify against the developer's published key — an invalidly signed manifest is refused with the signature-invalid error. The application identifier must not exceed 64 bytes. The capability set must have no bit set outside the admissible mask. The maximum rate must not exceed the smallest ceiling among the declared capabilities. A manifest passing every check is installed, and the application thereafter receives observations of exactly the capabilities it declared, at no more than the rate it declared; a manifest failing any check is refused, and the application does not start.

### 7.3 What the manifest accomplishes

The manifest makes an application's capability requests explicit, signed, and verifiable. Explicit, because the application must declare, in a structured field, exactly which of the four capabilities it wants — there is no way for an application to receive a capability it did not declare. Signed, because the manifest's signature binds the declaration to the developer's identity, so that a manifest cannot be forged or altered after signing. And verifiable, because the kernel checks every field against the Standard's bounds before installation, so that a manifest requesting more than the Standard permits — a reserved bit, an over-ceiling rate — is caught and refused. The manifest is the application's contract with the kernel about access, and the verification is the kernel's enforcement of that contract's bounds.

## 8. The boundaries of the capability system

A chapter on a privacy mechanism must be frank about what the mechanism does not do, because a mechanism over-trusted is a mechanism that lulls.

The capability system protects against three things, precisely. It protects against an application-layer code path that attempts to receive a capability the application did not declare — such a path cannot be constructed, because the type for the undeclared capability's observation is not available to that application. It protects against a future maintainer of the kernel weakening the privacy model by deletion — there is no check to delete, and weakening the model requires conspicuous addition. And it protects against a memory-disclosure bug in the application-facing interface exposing a prohibited category — the prohibited categories have no type on that side of the boundary, so there is nothing of them there to disclose.

The capability system does not protect against four things, and the chapter states them plainly. It does not protect against a user who installs a genuinely malicious application that declares legitimate capabilities and then misuses the observations it legitimately receives — the capability system gates *which* categories an application receives, not *what the application does* with the categories it is entitled to, and what an application does with legitimately received navigation intents is the application's responsibility and the user's choice of what to install. It does not protect against an adversary who can replace the kernel image — such an adversary can make the kernel do anything, and defending the kernel image's integrity is the job of a secure-boot mechanism, not the capability system. It does not protect against side-channel inference — a malicious application with a legitimate capability could, in principle, infer something about the user from the *timing* of their intents rather than the intents' content, and that is an application-layer attack outside the capability system's scope. And it does not, by itself, defend a stimulation-driving deployment's safety — that is the Cognitive Hypervisor's job.

The capability system does exactly what Sections 4 through 7 describe and exactly what `STANDARD.md` Sections 12 and 13 require: it makes the four prohibited categories structurally absent, and it confines the application to a closed set of four narrow, typed, rate-limited intent categories. That is a strong and precisely defined guarantee, and the Project states it precisely and does not overstate it. The capability system is the privacy model; it is not the whole of security; and a complete AxonOS deployment composes it with secure boot, with the consent subsystem, and, where there is stimulation, with the Cognitive Hypervisor.

## 9. A worked example: building a conformant assistive application

*Informative. The capability system is best understood by tracing a real application through it. This section follows a hypothetical but representative application — an assistive communication tool — from its design through its manifest to its runtime behaviour.*

### 9.1 The application

The application is an assistive communication tool for a user with severe motor impairment. It presents an on-screen keyboard; the user moves a cursor over the keyboard by intending directional movements, and dwells on a key to select it. It additionally dims its interface and pauses, rather than demanding interaction, when it detects the user is under heavy cognitive load, and it warns the user when the signal quality has degraded enough that its decoding is unreliable.

### 9.2 Determining the capabilities the application needs

The application's developer works through the four capabilities and determines which the application genuinely needs.

The cursor control needs **navigation**: the directional intents are exactly navigation intents, and without the navigation capability the application's core function is impossible. The load-sensitive dimming needs **workload-advisory**: the three-level cognitive-load estimate is what tells the application the user is under heavy load. The signal-quality warning needs **session-quality**: the scalar quality metric is what the warning is based on. The application does not need **artefact-events**: it does not do anything specific when an artefact is detected, beyond what the session-quality metric already conveys, and so it does not request that capability.

The developer has thus determined that the application needs three of the four capabilities and not the fourth. This determination is itself a small privacy act: the developer requests exactly what the application needs and no more, and the capability system, by requiring an explicit declaration, makes that minimalism natural — there is no reason to declare a capability the application will not use, and a manifest that declared all four when only three were needed would be a manifest that asked the user to grant more than the application required.

### 9.3 Writing the manifest

The developer writes the manifest. The application identifier is the reverse-DNS-form string naming the application. The capability set is the 32-bit field with the navigation, workload-advisory, and session-quality bits set and the artefact-events bit clear — three of the low four bits set, the rest zero. The maximum rate is the rate the application requests; the application's cursor control wants to be responsive, so it would like a high rate, but the maximum-rate field is bounded by the *smallest* ceiling among the declared capabilities, and the workload-advisory capability's ceiling is 1 hertz. The developer therefore faces a design consequence of the capability system: an application that declares workload-advisory cannot also receive navigation at 50 hertz through the same manifest's single rate field.

### 9.4 A design consequence the developer must confront

This is a genuine and instructive consequence, and the chapter does not paper over it. The manifest has a single maximum-rate field, and that field is bounded by the smallest ceiling among the declared capabilities. An application that declares both navigation, ceiling 50 hertz, and workload-advisory, ceiling 1 hertz, has a manifest whose maximum rate cannot exceed 1 hertz — which would cripple the cursor control.

The conformant resolution, and the one the Standard's design intends, is that such an application is built as two cooperating components, each with its own manifest. One component holds the navigation capability and runs at 50 hertz, doing the cursor control. A second component holds the workload-advisory and session-quality capabilities and runs at 1 hertz, doing the load-sensitive dimming and the quality warning. The two components are separate manifests, separate capability declarations, separate observation streams, and the application as a whole is their composition.

This is not an awkward workaround; it is the capability system working as designed. The system's discipline is that an application receives exactly the capabilities it declares at exactly the rate appropriate to them, and the two-component structure is the honest expression of an application that genuinely has a high-rate concern and a low-rate concern. The single-manifest, single-rate constraint pushes the developer toward separating those concerns, and the separation is good design: the high-rate cursor-control component and the low-rate advisory component are genuinely different in their needs, and building them as separate components with separate capability grants is more honest, and more privacy-respecting, than building them as one component that holds everything at once. The capability system's apparent inconvenience is, on examination, the system steering the developer toward the better structure.

### 9.5 Runtime behaviour

The two manifests are installed; the kernel verifies each, finds each well-formed and validly signed, and installs both. The navigation component thereafter receives navigation intents at up to 50 hertz; the advisory component receives workload-advisory and session-quality intents at up to 1 hertz. Neither component can receive an intent of a category it did not declare — the type for such an intent is not available to it. If either component requests observations faster than its declared rate, it receives the rate-exceeded error. If the user suspends consent, both components' streams stop and both receive the consent-suspended error; if the user withdraws consent, both streams terminate and both receive the consent-withdrawn error. The application, composed of its two components, does its assistive work entirely through the closed, typed, rate-limited intent categories the capability system admits, and the user's raw neural signal, their affective state, their cognitive profile, and their biometric identity never had a type by which they could have reached the application at all.

## 10. The capability system compared with prior access-control models

*Informative. The capability system did not arise in a vacuum; it stands in a tradition, and understanding its relationship to prior models sharpens what is and is not novel about it.*

### 10.1 Relationship to capability-based operating systems

The AxonOS capability is a direct descendant of the capability concept of the capability-based operating-systems tradition — the tradition of the research operating systems that, decades ago, explored building an entire system around unforgeable tokens of authority rather than around access-control lists. In that tradition, a capability is a token that both designates a resource and authorises a specific access to it; holding the token is having the authority, and not holding it is not having the authority, with no separate check.

The AxonOS capability inherits exactly this idea: the capability is the authority, its absence is the absence of the authority, and the enforcement is structural rather than a runtime check against a list. What the AxonOS Standard adds to the inherited idea is domain specialisation: where a general capability-based operating system has an open, unbounded universe of capabilities — one per resource, and resources are created freely — the AxonOS Standard fixes a *closed set of exactly four*, because the four correspond to the four intent categories the Project's privacy analysis admitted. The closure is the AxonOS contribution: it converts the general capability mechanism, which gates access to an open universe of resources, into a privacy model, which gates access to a deliberately tiny and fixed set of neural-data categories and structurally excludes everything else.

### 10.2 Relationship to mobile-platform permission models

The capability system is most usefully contrasted with the permission models of contemporary mobile platforms, because those models are what most readers will instinctively compare it to, and the contrast is instructive.

A mobile permission model is a runtime-flag model in the sense of Section 4.1. The data — the location, the camera feed, the contacts — exists; the platform mediates access with a runtime check against a permission the user granted through a dialog. The model has improved over its history — permissions have become more granular, more revocable, more visible to the user — but every improvement has been an improvement *within* the runtime-flag paradigm: a better dialog, a finer-grained flag, a check that runs at more moments. The paradigm itself, data-that-exists plus a check-that-guards-it, has not changed.

The AxonOS capability system is not an improvement within that paradigm; it is a different paradigm. It does not improve the dialog or refine the flag; it removes the flag, by removing the type, so that the prohibited categories are not better-guarded but absent. A reviewer who reads the capability system as "a permission model, like a phone's, but for a BCI" has missed the point. The phone's model and the AxonOS model answer the same question — which sensitive data may an application receive — but they answer it with mechanisms of different *kinds*: one procedural, one structural. The AxonOS Standard chose the structural mechanism deliberately, because for data as sensitive and as involuntary as neural data, the procedural mechanism's three structural weaknesses are not acceptable, and no refinement of the procedural mechanism removes them — only a change of kind does.

### 10.3 Relationship to type-driven security in programming languages

The capability system also stands in a more recent tradition: the use of a programming language's type system as a security mechanism, the tradition in which a sensitive value is given a type that constrains what can be done with it, and the compiler enforces the constraint. Capability-oriented sandboxing libraries, information-flow type systems, and the broad practice of "making illegal states unrepresentable" all belong to this tradition.

The AxonOS capability system is an application of exactly this tradition to the BCI privacy problem. The prohibited categories are made unrepresentable — they are illegal states, and the type system makes them unrepresentable by simply not providing their types. The admitted categories are made representable but constrained — their types exist, but only at the kernel boundary, and only carrying the narrow intents the capabilities authorise. The enforcement is the compiler's, at build time, which is the tradition's defining move. What the AxonOS Standard contributes is the recognition that this tradition — usually applied to prevent, say, an unsanitised string reaching a database query — is exactly the right tradition for the BCI privacy problem, and the working out of the closed four-capability set that applies it.

## 11. Implementer guidance for the capability system

*Informative. This section distils the chapter into guidance for the implementer building a conformant capability system.*

Make the prohibited categories typeless, not flagged. The single most important implementation decision is that the four prohibited categories must have no type at the application-facing boundary. An implementer who builds the prohibited categories as types that exist but are guarded by a check has built a runtime-flag system and has not built the AxonOS capability system, whatever the implementer calls it. The conformance suite's test C2-T07 checks exactly this: it enumerates the implementation's types and interfaces and confirms that none exposes a prohibited category. Build so that test passes by construction — by there being no such type — not by a check.

Make the admitted capabilities' types available only where the manifest authorises them. The four admitted capabilities' observation types must be structured so that an application receives the type for a capability only if its manifest declared that capability. An implementer's language will offer mechanisms for this — a generic parameterised by the capability, a module structure that exposes a capability's type only behind the manifest grant — and the implementer should use whichever mechanism their language makes most robust. The goal is that an application's code that tried to handle an undeclared capability's observation would not compile.

Enforce the rate ceilings at manifest installation and at runtime both. The rate ceilings are enforced in two places: at manifest installation, where a manifest declaring a rate above the smallest ceiling of its capabilities is refused, and at runtime, where a request for observations faster than the declared rate yields the rate-exceeded error. An implementer must build both enforcement points; the conformance suite tests both, in C2-T03 through C2-T06.

Verify the manifest completely before installing it. The manifest verification has four checks — signature, identifier length, capability-set mask, rate ceiling — and all four must pass before the manifest is installed. An implementer must build all four and must build them so that a failure of any one refuses the manifest; a partial verification that installed a manifest failing one check is a non-conformance, tested by C2-T08 and C2-T09.

Treat the closed set as genuinely closed. The capability set has exactly four members, and an implementer must not add a fifth, however tempting a fifth might seem for some particular application. The closure is a privacy property — it is what makes an application's possible accesses enumerable — and an implementation that added a capability would have broken the closure and would fail conformance test C2-T01. A genuine need for a fifth capability is a matter for the Request-for-Comments process and a future version of the Standard, not for a local extension.

## 12. Common objections to the capability system

*Informative. The capability system, presented to reviewers, draws a recurring set of objections. Answering them sharpens the design.*

**"A determined implementer can always add a type. The 'no type exists' guarantee is only as strong as the implementers' discipline not to add one — which is just the runtime-flag problem moved one level up."**

The objection is partly right and the chapter should concede the part that is right: yes, an implementer of the kernel itself could add a type for a prohibited category, just as, in a runtime-flag system, a maintainer could add a check. The capability system does not make weakening the privacy model *impossible*; nothing short of physics makes anything impossible. What it does is change the *character* of the act required to weaken it. In a runtime-flag system, weakening privacy is a *deletion* — removing an `if` — and deletions are small, easy, and can happen by accident, through a careless merge or a refactor. In the capability system, weakening privacy is an *addition* — adding a type, adding the functions that produce and consume it, adding the code paths that carry it — and additions of that size are conspicuous, reviewable, and cannot happen by accident. The objection is right that discipline is still required; it is wrong that the situation is unchanged, because the capability system converts the dangerous act from an easy accidental subtraction into a hard deliberate construction, and that conversion is exactly the safety margin. Moreover the conformance suite's test C2-T07 enumerates the implementation's types and would *detect* such an addition — so the addition is not only conspicuous in review but caught by the conformance regime.

**"Four capabilities is too few. Real applications will need intent categories you have not anticipated, and the closed set will become a straitjacket."**

It may, and if it does, the Request-for-Comments process exists precisely to address it: a genuine, demonstrated need for a fifth capability is exactly the kind of thing an RFC proposes, and a future minor version of the Standard could add a fifth capability if the RFC showed the need and showed the fifth category to be safe. What the Standard will not do is leave the set *open*, so that capabilities can be added locally and ad hoc, because the closure is itself the privacy property — it is what lets a user or a regulator know that an application's access is some subset of an enumerable set. The straitjacket, if it is one, is deliberate: it is tight enough to be a guarantee, and it is loosened, when loosening is genuinely warranted, only through the deliberate and public RFC process. A set that could be loosened ad hoc would not be a guarantee at all.

**"The workload-advisory capability already sounds like the thin end of a wedge. A coarse cognitive-load estimate is still a cognitive signal. Why is it admitted when cognitive profile is prohibited?"**

The objection identifies the genuine tension, and the answer is in the rate ceiling and the quantisation. The prohibited cognitive-profile category is a *persistent, fine-grained, accumulable* representation — a fingerprint built up across sessions. The workload-advisory capability is a *coarse, three-level, one-hertz, non-accumulated* hint. The difference is not a difference of topic — both concern cognition — but a difference of resolution and persistence, and the Standard's claim is that the difference of resolution and persistence is the difference between a profiling instrument and an advisory hint. A three-level estimate sampled once per second cannot be assembled into the fine cognitive timeline that profiling needs; the ceiling and the quantisation are the wall between the advisory hint and the profile. The objection is right that the wall must be *held* — that a future RFC raising the workload-advisory rate ceiling would be eroding the wall and should be scrutinised as a near-constitutional matter — and the chapter agrees: the ceiling is load-bearing, and its erosion would be a serious matter. But a coarse hint, held coarse, is not a profile, and the Standard admits the hint while prohibiting the profile because, held to its ceiling, the hint is genuinely useful and genuinely not a profile.

**"The two-component workaround in the worked example is clumsy. A real developer will resent it."**

A developer encountering it for the first time may well resent it, and the chapter does not dismiss that reaction. But Section 9.4 argued, and the chapter maintains, that the two-component structure is not a workaround but the honest expression of an application with a genuine high-rate concern and a genuine low-rate concern, and that building those as separate components with separate capability grants is better design — more honest about what each part needs, more privacy-respecting in what each part is granted — than building them as one component holding everything. The single-manifest single-rate constraint is the capability system declining to let a high-rate component silently also hold a sensitive low-rate capability, and that declining is a feature. A developer who internalises the reason tends, in the Project's experience, to stop resenting it: the constraint is not arbitrary friction but the system steering toward the structure the developer would, on reflection, have chosen anyway.

## 13. A note to the independent implementer

This chapter, and the Standard it accompanies, exist so that an independent implementer can build a conformant capability system. This closing note is addressed to that implementer.

The capability system is, of the AxonOS subsystems, the one where an implementer is most likely to build something that looks conformant, passes a casual inspection, and is in fact a runtime-flag system wearing the capability system's vocabulary. The trap is subtle. An implementer can name four types `Navigation`, `WorkloadAdvisory`, `SessionQuality`, `ArtefactEvents`, can call them "capabilities", can gate them with the manifest — and can, alongside them, have a `RawSignal` type that exists in the interface and is merely guarded by a check that the manifest does not grant raw-signal access. Such an implementation has the capability system's words and the runtime-flag system's structure, and it would fail conformance test C2-T07, which enumerates the types and finds the `RawSignal` type that should not exist.

The discipline that avoids the trap is simple to state and requires real care to apply: the prohibited categories must have *no type* at the application-facing boundary. Not a type that is never granted; not a type behind a check; no type. If an implementer finds themselves writing a check that tests whether raw-signal access is granted, the implementer has already gone wrong, because the existence of the check implies the existence of the thing checked, and the thing should not exist to be checked. The correct implementation has nothing to check, because the prohibited category was never given a type, never given a producing function, never given a code path. The compiler enforces the prohibition by the simple fact that code referring to a non-existent type does not compile.

Build the prohibited categories as absences, not as guarded presences. That single discipline is the difference between an implementation that has the AxonOS capability system and one that has a runtime-flag system with AxonOS labels, and the conformance suite is built to tell the two apart.

## 14. Summary

The capability system is the AxonOS Standard's privacy model, and its central idea is the choice of a structural guarantee over a procedural one. A capability is a type, not a runtime flag; a prohibited category is a type that does not exist, not a category guarded by a check. This choice eliminates the three structural weaknesses of the conventional runtime-permission pattern — the check that can be wrong, the check that can be removed, the data that exists to be leaked — by ensuring there is no check to be wrong or removed and no boundary-crossing typed value to leak. The closed set of four admitted capabilities — navigation, workload-advisory, session-quality, artefact-events — comprises the intent categories the Project found simultaneously useful and safe, each at a rate ceiling chosen so the category cannot compose into something dangerous, with the workload-advisory ceiling and quantisation drawn deliberately to keep that capability advisory rather than a profiling instrument. The four prohibited categories — raw neural signal, affective state, cognitive profile, biometric identity — are structurally absent, prohibited because each is an instrument of a specific harm, and their prohibition is a constitutional commitment whose reversal carries a deliberately high cost. The manifest makes an application's capability requests explicit, signed, and verifiable, and the worked example shows the manifest's single-rate constraint steering a developer toward the better, more privacy-respecting two-component structure. The system stands in the tradition of capability-based operating systems and of type-driven security, contributing the closed four-capability specialisation for the BCI privacy problem, and it differs in kind, not degree, from the runtime-flag permission models of contemporary mobile platforms. The recurring objections — that a determined implementer could still add a type, that four capabilities is too few, that workload-advisory is a wedge, that the two-component structure is clumsy — each identify a genuine tension and each is answered: the dangerous act is converted from an easy subtraction to a hard reviewable addition and is caught by conformance test C2-T07; the set is loosened only through the deliberate RFC process; the workload-advisory wall is the rate ceiling and the quantisation, and it is load-bearing; and the two-component structure is honest design rather than a workaround. The system's boundaries are stated frankly: it gates which categories an application receives, not what the application does with them, and it composes with, rather than replacing, secure boot, consent, and the Cognitive Hypervisor. The capability system is the structural reason a user can use an AxonOS deployment without their neural interior becoming a profiled, surveilled, manipulable asset — not because a check protects them, but because the dangerous categories have no type to inhabit.

---

*End of the capability-system architecture chapter.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
