# Architecture: Real-Time Scheduling and Timing Analysis

**AxonOS Standard v1.0.1** · **Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

*An architecture chapter of the AxonOS Standard. Informative throughout. This chapter elaborates the scheduling discipline and the worst-case-timing analysis; the normative requirements are in `STANDARD.md` Sections 7 and 8. Where this chapter and the Standard differ, the Standard governs.*

---

## 1. Purpose of this chapter

The AxonOS kernel makes a promise that almost no general-purpose software makes: it promises an upper bound on how long its central computation can take, and it promises that bound not as a measured observation but as a proven fact about every possible execution. This chapter explains the machinery behind that promise. It explains the scheduling discipline that organises the kernel's work, the theory that tells us whether a given set of work can be scheduled at all, the analysis that turns a set of tasks into a number — the worst-case response time — and the conservatism that makes that number trustworthy.

The chapter is written for the implementer who must perform this analysis for a real kernel, and for the reviewer who must judge whether an analysis is sound. It assumes no prior background in real-time scheduling theory; it builds the theory from its foundations, because an implementer who applies the theory without understanding it will apply it wrongly at exactly the edge cases where it matters. But it does not stop at the foundations; it carries the theory through to the concrete, worked analysis of the reference task set, because the gap between knowing the theory and applying it correctly to a real system is itself substantial and is where most timing errors live.

## 2. The problem: what "schedulable" means

Begin with the question the whole chapter answers. The kernel has a set of tasks to perform, repeatedly, forever. Each task must be performed once per processing epoch — once every four milliseconds, in the reference configuration. Each task takes some amount of processor time. The tasks run on a single processor core, so they cannot all run at once; they must take turns. The question is: can the tasks be made to take turns in such a way that every task, every epoch, finishes before its deadline?

If the answer is yes, the task set is **schedulable**, and the kernel can make its timing promise. If the answer is no, the task set is **unschedulable**, no arrangement of turns will make every deadline, and the kernel cannot make its promise — the design must change, the task set must be made lighter, before the kernel is a hard-real-time system at all.

"Schedulable" is therefore the property the whole timing argument turns on, and it is worth being precise about what it asserts. It asserts that there *exists* a way of taking turns — a schedule — under which every task always meets its deadline. It does not assert that every way of taking turns works; most ways do not. It asserts that the scheduling discipline the kernel actually uses produces a working schedule, for this task set, under every admissible circumstance. Schedulability is always schedulability *of a particular task set, under a particular discipline*, and the analysis must name both.

## 3. The two disciplines

There are, broadly, two families of scheduling discipline for periodic real-time tasks on a single processor, and the AxonOS kernel's choice between them is a deliberate and consequential one.

### 3.1 Fixed-priority scheduling

In a fixed-priority discipline, each task is assigned a priority once, at design time, and that priority never changes. At every moment the processor runs the highest-priority task that is ready to run. The best-known fixed-priority discipline is Rate-Monotonic scheduling, in which the priority assignment follows a simple rule: the task with the shortest period gets the highest priority, the next-shortest the next-highest, and so on.

Rate-Monotonic scheduling has a great deal to recommend it. The priority assignment is simple and static; the runtime scheduler is trivial — it just runs the highest-ready-priority task; and the discipline has been used successfully in safety-critical systems for decades. Its schedulability, however, has a specific limitation, and the limitation is what steers the AxonOS kernel away from it.

### 3.2 Dynamic-priority scheduling

In a dynamic-priority discipline, a task's priority is not fixed but is recomputed continuously from the current situation. The dynamic-priority discipline the AxonOS kernel uses is Earliest-Deadline-First, in which a task's effective priority at any instant is determined by how close its deadline is: the ready task whose absolute deadline is nearest is the one the processor runs.

Earliest-Deadline-First requires slightly more of the runtime scheduler — at each scheduling decision it must compare deadlines rather than consult a static priority — but the cost is small for a small task set, and the discipline buys, in exchange, a schedulability property that fixed-priority scheduling cannot match.

## 4. The schedulability bounds

The difference between the two disciplines is captured precisely by a single foundational result, and understanding that result is understanding why the AxonOS kernel chooses as it does.

### 4.1 Utilisation

First, a definition. The **utilisation** of a single task is the fraction of the processor the task consumes: its worst-case execution time divided by its period. A task that takes 320 microseconds and runs every 4000 microseconds has a utilisation of 320 divided by 4000, which is 0.08 — it consumes eight per cent of the processor. The **total utilisation** of a task set is the sum of the individual utilisations. If the total utilisation exceeds 1.0, the task set asks for more than one processor's worth of work and is unschedulable on one processor by any discipline whatsoever; that much is simple arithmetic. The interesting question is what happens *below* 1.0.

### 4.2 The Liu and Layland result

The foundational result, due to Liu and Layland in a paper of 1973 that effectively founded the field of real-time scheduling analysis, gives the schedulability bound for each discipline.

For **Rate-Monotonic** scheduling, a task set of *n* tasks is guaranteed schedulable if its total utilisation does not exceed *n* times the quantity two-to-the-one-over-*n*-power minus one. This expression is a little awkward, but its behaviour is simple to describe. For one task it is 1.0. For two tasks it is about 0.83. For three, about 0.78. As *n* grows, the bound decreases, and in the limit, for many tasks, it approaches the natural logarithm of two, which is about 0.693. So Rate-Monotonic scheduling can *guarantee* schedulability only up to a utilisation of roughly sixty-nine per cent for a task set with many tasks. A task set above that bound *might* still be schedulable — the bound is sufficient, not necessary — but it is not *guaranteed* to be, and a guarantee is exactly what a hard-real-time system needs.

For **Earliest-Deadline-First** scheduling, the result is dramatically cleaner. A task set is schedulable under Earliest-Deadline-First if and only if its total utilisation does not exceed 1.0. Not "guaranteed schedulable up to a bound that depends on the task count"; schedulable, if and only if, up to a single clean threshold of 1.0, for any number of tasks. The Earliest-Deadline-First condition is both sufficient and necessary, and it is a single inequality with no dependence on how many tasks there are.

### 4.3 What the difference means

The gap between the two bounds — roughly 0.69 for Rate-Monotonic with many tasks, exactly 1.0 for Earliest-Deadline-First — is the central reason the AxonOS kernel uses Earliest-Deadline-First. But the raw efficiency gain is not, in fact, the most important part of the difference, because the AxonOS task set is light — about 0.16 utilisation — and would fit comfortably under either bound. The more important part of the difference is the *shape* of the two conditions.

The Rate-Monotonic condition depends on the task count and is only sufficient, not necessary. This means that every time the task set changes — and the pipeline will change, across the life of the Standard — the schedulability must be re-examined with care: the bound itself shifts as the task count changes, and a task set near the bound requires the exact, more complex response-time analysis rather than the simple utilisation test. The Earliest-Deadline-First condition is a single inequality, exact, with no task-count dependence. When the task set changes, re-checking schedulability under Earliest-Deadline-First is the recomputation of one sum and one comparison. For a Standard whose pipeline will be revised many times, by many implementers, the discipline whose schedulability check is a single stable inequality is the discipline whose check will actually be performed correctly every time, and that reliability of the check, more than the raw efficiency, is why the kernel chooses Earliest-Deadline-First.

## 5. From utilisation to response time

The utilisation test answers the yes-or-no question — is the task set schedulable? — but it does not answer the question the dual-core contract actually asks, which is quantitative: *what is the worst-case response time?* A task set can be schedulable, every deadline always met, and still the implementer needs to know the actual worst-case time from epoch start to observation delivery, because clause DC1 bounds that specific number. The utilisation test does not yield it. A different analysis does: the response-time analysis.

### 5.1 Why response time exceeds execution time

The first thing to understand about response time is why it is not simply the sum of the tasks' execution times. In a preemptive system — and the AxonOS kernel is preemptive, because Earliest-Deadline-First preempts a running task when a nearer-deadline task becomes ready — a task's response time is the time from when it becomes ready to when it completes, and that interval includes not only the task's own execution but also every interval during which the task was preempted by some other task with a nearer deadline.

So the response time of a task is its own worst-case execution time, plus the *interference* it suffers: the total time, during its response-time window, that the processor spends running other tasks instead of it. And the interference is not a fixed quantity; it depends on how many times each higher-priority task can be released during the window, which depends on the window's length, which depends on the interference — the quantity is defined in terms of itself.

### 5.2 The response-time recurrence

This circularity is resolved by a recurrence. The response time is computed iteratively. One starts with an initial estimate of the response time — the task's own execution time, with no interference. One then computes, for that estimated window length, how much interference the task would suffer: for each task that can preempt it, the number of times that task could be released within the window, multiplied by that task's worst-case execution time. Adding that interference to the task's own execution time gives a new, longer estimate of the response time. One then recomputes the interference for the new, longer window — a longer window admits more releases of the preempting tasks, hence more interference — giving a longer estimate still. One repeats.

The iteration has one of two outcomes. Either the estimate stops growing — two successive iterations give the same value — in which case that value is the worst-case response time, the fixed point of the recurrence. Or the estimate grows past the task's deadline, in which case the task is not schedulable and there is no finite response time to report. For a schedulable task set the iteration always converges, and the value it converges to is the number the analysis was after.

### 5.3 The recurrence for the whole pipeline

The response-time recurrence as just described computes the response time of a single task. The dual-core contract's clause DC1 is about the response time of the *whole pipeline* — from epoch start to the publication of the intent observation. For the AxonOS pipeline this whole-pipeline response time is governed by the last task to complete in the epoch, the inter-process-communication publication task, whose completion marks the observation's delivery. The whole-pipeline analysis is therefore the response-time analysis of the publication task, accounting for the interference of every pipeline stage that must complete before it and every interrupt that can intervene. The number that analysis converges to, bounded conservatively, is the worst-case response time that clause DC1 caps at 1000 microseconds.

## 6. The worked analysis of the reference task set

The preceding sections gave the theory. This section applies it, concretely, to the reference task set of `STANDARD.md` Appendix D, because the application is where understanding is tested.

### 6.1 The reference task set restated

The reference task set comprises seven tasks, each with a worst-case execution time and a period. The six signal-processing tasks and the one publication task, with their worst-case execution times in microseconds, are: the Kalman-filter state update at 80; the finite-impulse-response filter at 320; the notch filter at 40; the artefact-rejection stage at 15; the common-spatial-pattern feature extractor at 160; the linear-discriminant classifier at 25; and the inter-process-communication publication task at 0.2. Every task has the same period, 4000 microseconds, because every task runs exactly once per processing epoch.

### 6.2 The utilisation check

The first analysis is the utilisation check, and it is arithmetic. Each task's utilisation is its execution time divided by its period. The Kalman update: 80 over 4000, which is 0.020. The finite-impulse-response filter: 320 over 4000, 0.080. The notch filter: 40 over 4000, 0.010. The artefact-rejection stage: 15 over 4000, 0.00375. The common-spatial-pattern extractor: 160 over 4000, 0.040. The linear-discriminant classifier: 25 over 4000, 0.00625. The publication task: 0.2 over 4000, which is 0.00005, negligible.

The total utilisation is the sum: 0.020 plus 0.080 plus 0.010 plus 0.00375 plus 0.040 plus 0.00625 plus 0.00005, which is 0.16005, conventionally rounded to 0.160.

The Earliest-Deadline-First schedulability condition is that total utilisation not exceed 1.0. The reference task set's 0.160 is far below 1.0, so the task set is schedulable under Earliest-Deadline-First. It is also far below the kernel's configured utilisation ceiling of 0.25, so it is admissible. The utilisation check passes with a wide margin: the task set uses 16 per cent of the processor against a theoretical limit of 100 per cent and an administrative ceiling of 25 per cent.

### 6.3 The response-time analysis

The utilisation check confirms schedulability; the response-time analysis yields the actual worst-case response time. For the reference task set the analysis is, in fact, simpler than the general recurrence of Section 5.2, and the reason it is simpler is itself instructive.

All seven tasks share the same period, 4000 microseconds, and all seven must complete once within each 4000-microsecond epoch. Because they share a period, no task is released a second time before all tasks have had their first release of the epoch; the interference term of the recurrence — which counts *repeated* releases of preempting tasks within a window — does not produce multiple releases, because within a single epoch each task is released exactly once. The pipeline within an epoch is therefore, in effect, a straight-line sequence: the seven tasks execute, in their pipeline order, one after another, each once, and the worst-case response time of the whole pipeline is, to first approximation, simply the sum of the seven worst-case execution times.

That sum is: 80 plus 320 plus 40 plus 15 plus 160 plus 25 plus 0.2, which is 640.2 microseconds.

### 6.4 From the straight-line sum to the conservative bound

The 640.2-microsecond figure is the pipeline's worst-case execution time — the processor time the seven tasks themselves consume. It is not yet the worst-case *response* time, because the response time must also account for everything that can intervene *between* and *during* the tasks: the interrupts, the micro-architectural effects, the conservative allowances.

The reference analysis adds, on top of the 640.2-microsecond straight-line sum, the following conservative allowances. It adds the worst-case interrupt interference: the analog-to-digital converter's sample-ready interrupt, the inter-core bridge's interrupt, and the radio's interrupt can each fire during the epoch, and each steals cycles for its handler; the analysis assumes each fires at its maximum admissible rate and each handler takes its maximum duration. It adds the worst-case micro-architectural penalty: as the kernel architecture chapter's Section 7.3 describes, the verification harness assumes every memory access is a cache miss and every branch is mispredicted, and the response-time analysis carries the same conservative assumption, inflating each task's effective execution time to its cache-cold, misprediction-laden worst case. It adds a margin for the imprecision inherent in the worst-case-execution-time estimates themselves.

When these conservative allowances are added to the 640.2-microsecond straight-line sum, the analysis yields a worst-case response time below the 1000-microsecond bound of clause DC1, and the bounded model checker, ranging over the entire admissible input and machine-state space with all these conservative assumptions built in, confirms it: the proven upper bound is 1000 microseconds, and the L1 evidence is the checker's transcript.

### 6.5 The measured value and the margin

The L2 soak, on the reference hardware, measures a worst observed response time of 972 microseconds over twelve hours and roughly 10.8 million epochs, with zero deadline misses. The measured 972 sits below the proven 1000, and the gap between them — 28 microseconds — together with the much larger gap between the 972 measured worst and the 640.2 straight-line sum, is the conservatism made visible.

It is worth dwelling on the two gaps, because they answer two different questions. The gap between the 640.2-microsecond straight-line sum and the 972-microsecond measured worst — about 332 microseconds — is the real cost of the interrupts and the micro-architectural effects: it is how much, on the worst real epoch of a twelve-hour soak, the intervening interrupts and the cache and pipeline effects actually added to the bare task execution. The gap between the 972-microsecond measured worst and the 1000-microsecond proven bound — 28 microseconds — is the headroom of the proof over reality: it is the amount by which the conservatively proven bound exceeds the worst the real system, over a long soak, was observed to do. The first gap is the cost of the real world; the second is the safety margin of the proof. Both are healthy, and a kernel for which either gap were near zero would be a kernel one small change away from trouble.

## 7. Admission control as the analysis made continuous

The response-time analysis of Section 6 is performed once, at design time, for a fixed task set. But the Standard permits the task set to change at runtime, through the admission-control procedure of `STANDARD.md` Section 7.4. Admission control is, conceptually, the schedulability analysis made continuous: it is the utilisation check of Section 6.2, performed afresh every time a task-set change is proposed, before the change is allowed to take effect.

When a component proposes adding a task, or changing a task's execution time or period, admission control computes what the total utilisation *would be* after the change. If that prospective utilisation stays within the configured ceiling — 0.25 by default — the change is admitted, because a task set within the ceiling is, by the Earliest-Deadline-First condition and the ceiling's conservative margin, schedulable. If the prospective utilisation would exceed the ceiling, the change is refused, with the admission-refused error, because admitting it would produce a task set whose schedulability the analysis can no longer conservatively guarantee.

Admission control is, in other words, the mechanism that extends the design-time schedulability guarantee across runtime changes. The design-time analysis proves the *initial* task set schedulable; admission control ensures that every *subsequent* task set, every configuration the kernel ever actually runs, has also passed the schedulability check before it became the running configuration. The combination — the design-time response-time analysis plus the runtime admission-control check — is what makes the timing guarantee hold not just for the kernel as shipped but for the kernel as it evolves through its operating life.

## 8. The limits of the analysis

A chapter on timing analysis must be honest about what the analysis does not deliver, because an analysis over-trusted is more dangerous than an analysis understood.

The response-time analysis delivers a worst-case response time *for the model it is given*: for the stated task set, with the stated worst-case execution times, under the stated assumptions about interrupts and micro-architecture. It does not deliver a worst-case response time for a system that differs from the model. If a task's true worst-case execution time exceeds the figure the analysis was given — because the figure was an underestimate, because a later code change lengthened the task — then the analysis's conclusion, though validly derived, is a conclusion about a system that is not the one running, and the real system has no proven bound. The analysis is only as sound as the worst-case execution times it is given, and obtaining sound worst-case execution times for the individual tasks is itself a substantial analysis problem, addressed by the bounded-model-checking methodology that the validation document describes.

The analysis also assumes the model of interference is complete — that the interrupts it accounts for are all the interrupts, that no source of processor contention has been omitted. An omitted interference source is an unsound analysis, and the completeness of the interference model is something the implementer is responsible for and the analysis itself cannot check. This is the deepest reason the dual-core contract pairs the L1 proof of clause DC1 with the L2 soak measurement: the soak runs the *real* system, with *all* its real interference, and a soak whose measured worst stays below the proven bound is corroborating evidence that the proof's model did not omit anything large. A divergence — a measured worst that approached or exceeded the proven bound — would be the signal that the model and the reality had parted company, and the soak exists, in part, to detect exactly that.

## 9. Jitter: the second timing quantity

Clause DC1 of the dual-core contract bounds the worst-case response time; clause DC2 bounds the jitter. The two are distinct quantities, they answer distinct questions, and an implementer who understands only the first has understood only half of what the user actually experiences.

### 9.1 What jitter is and is not

The worst-case response time answers the question "how long, at most, can one observation take?" Jitter answers a different question: "how regular is the spacing between observations?" Jitter is the standard deviation of the interval between successive intent observations. A system with low jitter delivers observations at a metronome-steady cadence; a system with high jitter delivers them irregularly — now slightly early, now slightly late — even if every observation individually meets its deadline and even if the average cadence is exactly correct.

It is essential to see that low worst-case response time and low jitter are independent properties, neither implying the other. A system could have an excellent worst-case response time — every observation delivered well within its deadline — and yet have poor jitter, if the observations, though all on time, arrived at irregular moments within their windows. Conversely a system could have steady jitter around a cadence that was itself too slow. The dual-core contract bounds both because the user's experience depends on both: the worst-case response time governs whether the interface ever feels laggy, and the jitter governs whether the interface feels *steady* — whether it has the metronomic regularity that lets the user form a stable, trusting mental model of its behaviour.

### 9.2 Why jitter matters to a brain-computer interface

For a brain-computer interface specifically, jitter has a significance beyond the general one. The neural decoding the kernel performs is, in part, a temporal inference: the pipeline's filters and its classifier reason about how the signal evolves over time, and that reasoning implicitly assumes the samples arrive on a known, regular schedule. Jitter in the observation cadence is, propagated backward, a sign of jitter in the processing schedule, and jitter in the processing schedule degrades the temporal inference. A steady cadence is therefore not merely a matter of the interface feeling smooth; it is a matter of the decoding being accurate, because the decoding's temporal model assumes the steadiness. This is part of why the contract bounds jitter tightly — at 10 microseconds at the three-sigma envelope — and why the reference implementation's measured jitter of 2.1 microseconds at one sigma is reported as a headline figure rather than an afterthought.

### 9.3 Why the contract requires jitter at L2, not L1

Clause DC1, the worst-case response time, is required at evidence level L1 — a formal proof. Clause DC2, the jitter, is required at L2 — a measurement. The asymmetry is deliberate and worth understanding.

A worst-case response time is an upper bound, and an upper bound is the kind of claim a formal proof is suited to: the proof ranges over the input space and confirms no input exceeds the bound. Jitter is not an upper bound; it is a statistical property — a standard deviation — of the distribution of inter-observation intervals over a long run. A standard deviation is not naturally the subject of a bounded-model-checking proof, because it is not a property of a single execution that the checker can range over; it is an aggregate of many executions. The appropriate evidence for a statistical aggregate is a measurement of that aggregate over a long, representative run — which is exactly what an L2 soak provides. The contract requires each clause at the evidence level appropriate to the kind of quantity the clause bounds: L1 for the worst-case bound, because a proof suits a bound; L2 for the jitter, because a measurement suits a statistical aggregate.

### 9.4 Where jitter comes from, and how the kernel minimises it

If the kernel's schedule were perfectly deterministic — if every epoch's pipeline executed in exactly the same time — the jitter would be zero, because every observation would be delivered at exactly the same offset within its epoch. Real jitter is the variation in that offset from epoch to epoch, and that variation comes from the same sources the worst-case analysis's conservative allowances cover: the interrupts, which fire at moments not synchronised to the epoch and so perturb different epochs differently; the micro-architectural effects, which make a cache-cold epoch run a little longer than a cache-warm one. Jitter is, in a sense, the *statistical shadow* of the same interference whose *worst case* the response-time analysis bounds.

The kernel minimises jitter by the same disciplines that bound the worst case. The fixed task set means every epoch runs the same work, so the only epoch-to-epoch variation is the interference, not the work itself. The Earliest-Deadline-First schedule is deterministic given the releases, so it adds no variation of its own. The lock-free, never-blocking inter-process-communication channel means the publication task's timing does not vary with the consumer's behaviour. What variation remains is the interrupt timing and the micro-architecture, and the reference implementation's 2.1-microsecond measured jitter is the residue of those, after the disciplines have removed everything else. The disciplines that make the worst case provable are, not coincidentally, the disciplines that make the cadence steady; determinism serves both.

## 10. The interrupt analysis in detail

The conservative allowance for interrupt interference, mentioned in Section 6.4 as one of the additions to the straight-line task sum, deserves a section of its own, because it is the part of the timing analysis most often done carelessly and the part where a careless analysis most often becomes unsound.

### 10.1 Why interrupts are the hard part

The tasks of the pipeline are, from the analysis's point of view, well-behaved: they are released on a known schedule, once per epoch, and their worst-case execution times are established by their own bounded-model-checking analysis. Interrupts are not so well-behaved. An interrupt fires when its hardware source decides it fires — when a sample is ready, when the bridge has activity, when the radio needs service — and those moments are not synchronised to the epoch. An interrupt can fire at any point during the pipeline's execution, it preempts whatever task is running, it runs its handler, and only then does the preempted task resume. The interrupt is, in effect, a task with the highest priority of all and an irregular release pattern, and the analysis must bound the interference it inflicts.

### 10.2 The two quantities the analysis needs

To bound an interrupt source's interference, the analysis needs two quantities: the maximum rate at which the interrupt can fire, and the maximum duration of its handler.

The maximum rate is a property of the hardware source. The analog-to-digital converter's sample-ready interrupt fires once per sample; at the reference sampling rate, that is a known, fixed maximum rate. The bridge interrupt's maximum rate is bounded by the bridge's protocol. The radio interrupt's maximum rate is bounded by the radio's configuration. Each of these maxima is established from the hardware's documentation and, where the documentation is insufficient, from measurement, and each is taken at its conservative maximum — the analysis assumes the interrupt fires as often as it possibly could.

The maximum handler duration is a property of the handler's code, and it is established the same way the tasks' worst-case execution times are: by analysis of the handler code, conservatively, assuming cache-cold execution. The interrupt handlers are deliberately kept short — an interrupt handler does the minimum necessary to service its source and defers everything else — precisely so that this maximum duration is small, because the handler's duration enters the interference bound and a long handler would inflate it.

### 10.3 Composing the interrupt interference

With the maximum rate and maximum handler duration of each interrupt source known, the interference from that source over a window of a given length is bounded by the number of times the interrupt could fire within the window — the window length divided by the minimum inter-arrival time, rounded up — multiplied by the maximum handler duration. This is the same form as the task-interference term of the response-time recurrence, and it enters the recurrence the same way: it is part of the interference that lengthens the response-time window, and because lengthening the window admits more interrupt firings, the interrupt interference participates in the recurrence's iteration toward its fixed point exactly as task interference does.

The reference analysis includes the interference of all three interrupt sources — the converter, the bridge, the radio — at their conservative maxima, and the sum of that interference is part of the gap, identified in Section 6.5, between the 640.2-microsecond straight-line task sum and the measured worst of 972. The interrupts are real, they are accounted for conservatively, and the accounting is part of what makes the 1000-microsecond proven bound a sound bound rather than an optimistic one.

### 10.4 The discipline of short handlers

A theme running through this section is that the interrupt handlers are kept short, and it is worth making the discipline explicit because it is a design rule an implementer must follow. Every microsecond of an interrupt handler's worst-case duration is a microsecond that, multiplied by the handler's maximum firing count, inflates the interference bound and pushes the worst-case response time up. An interrupt handler that did substantial work — that ran a filter, that touched a complex data structure, that, worst of all, contained a loop whose bound depended on runtime data — would inflate the interference bound badly and might, on its own, push the response time past the deadline.

The discipline is therefore that an interrupt handler does the irreducible minimum: it acknowledges the hardware, it moves the smallest possible amount of data, it sets a flag or advances an index, and it returns. Everything else — the actual processing of whatever the interrupt signalled — is done by a pipeline task, on the pipeline task's schedule, under the pipeline task's analysed worst-case execution time. The interrupt handler is a doorbell, not a workshop: it announces that something has arrived and returns immediately, and the work the arrival implies is done by the scheduled tasks. This discipline keeps the handler durations small, keeps the interrupt interference bounded tightly, and is one of the design rules that the difference between a schedulable AxonOS kernel and an unschedulable one can come down to.

## 11. The Earliest-Deadline-First scheduler as implemented

Sections 3 and 4 described Earliest-Deadline-First as a discipline; this section describes the discipline as the reference kernel actually implements it, because the gap between the abstract discipline and a sound implementation of it is real.

### 11.1 The data the scheduler keeps

The reference scheduler keeps, for each task in the fixed task set, a small record: the task's relative deadline, its current absolute deadline, and its current state — ready, running, or completed-for-this-epoch. Because the task set is fixed and small, these records live in a fixed-size array, indexed by a fixed task identifier; the scheduler uses no dynamic data structure, allocates nothing, and grows nothing.

### 11.2 The scheduling decision

At each scheduling decision — each scheduler tick, each task release, each task completion — the scheduler performs one operation: it scans the fixed array, finds the task whose state is ready and whose absolute deadline is nearest, and runs it, preempting the currently running task if the found task differs from it. The scan is a bounded loop over the fixed array; its worst-case duration is a fixed, known quantity; and that quantity is included in the scheduler's own worst-case-execution-time accounting, because the scheduler, too, is code that runs on the signal-processing core and consumes its cycles.

### 11.3 Why not a faster data structure

A reader familiar with scheduling implementations might note that a priority heap, or a balanced search tree, would make the "find the nearest deadline" operation asymptotically faster than a linear scan of an array — logarithmic in the task count rather than linear. The reference kernel deliberately does not use one, and the reason connects back to the chapter's central theme.

The task set is small and fixed — seven tasks. For seven tasks, a linear scan is not slow; it is seven comparisons, a handful of microseconds at most, and its worst-case duration is trivial to compute exactly. A priority heap would make the operation asymptotically faster, but "asymptotically faster" is a statement about behaviour as the task count grows large, and the task count does not grow large; it is seven. What the priority heap would cost is analysability: a heap's operations have a worst-case duration that depends on the heap's current shape, and bounding that worst case exactly is more work than bounding the linear scan's, which is simply seven comparisons. The reference kernel chooses the linear scan because, for a small fixed task set, the linear scan is fast enough and its worst-case duration is trivially exact, and trivially-exact worst-case duration is worth more to this kernel than an asymptotic speed-up that the small task count makes irrelevant. This is, once more, the kernel's recurring trade: it declines an optimisation that improves a case it does not care about — large task counts — in exchange for keeping the worst-case analysis simple, and the simplicity of the analysis is the product.

## 12. A worked iteration of the response-time recurrence

Section 6.3 noted that the reference task set's analysis is simpler than the general recurrence, because the shared period collapses the recurrence into a straight-line sum. An implementer whose task set does *not* share a single period — a plausible future configuration — will need the general recurrence, and this section works one through, on a small illustrative example, so that the recurrence is concrete rather than abstract.

### 12.1 The illustrative task set

Consider a task set of three tasks, deliberately chosen to have distinct periods so that the recurrence does real work. Task one has a worst-case execution time of 100 microseconds and a period of 400 microseconds. Task two has a worst-case execution time of 150 microseconds and a period of 800 microseconds. Task three has a worst-case execution time of 200 microseconds and a period of 1600 microseconds. The total utilisation is 100 over 400 plus 150 over 800 plus 200 over 1600, which is 0.25 plus 0.1875 plus 0.125, totalling 0.5625 — schedulable under Earliest-Deadline-First, since it is below 1.0.

We compute the worst-case response time of task three, the task with the latest deadline, which under Earliest-Deadline-First is the task most subject to interference.

### 12.2 The iteration

The recurrence begins with the initial estimate equal to task three's own execution time: 200 microseconds.

The first iteration computes the interference within a 200-microsecond window. Task one, period 400, can be released at most once in a 200-microsecond window — 200 divided by 400, rounded up, is 1 — contributing 1 times 100, which is 100 microseconds of interference. Task two, period 800, can be released at most once in a 200-microsecond window — 200 over 800 rounded up is 1 — contributing 1 times 150, which is 150 microseconds. The new estimate is task three's own 200 plus 100 plus 150, totalling 450 microseconds.

The second iteration computes the interference within the now-longer 450-microsecond window. Task one, period 400, can be released at most twice in a 450-microsecond window — 450 over 400 rounded up is 2 — contributing 2 times 100, which is 200 microseconds. Task two, period 800, still at most once — 450 over 800 rounded up is 1 — contributing 150 microseconds. The new estimate is 200 plus 200 plus 150, totalling 550 microseconds.

The third iteration computes the interference within 550 microseconds. Task one, period 400: 550 over 400 rounded up is 2, contributing 200 microseconds. Task two, period 800: 550 over 800 rounded up is 1, contributing 150 microseconds. The new estimate is 200 plus 200 plus 150, totalling 550 microseconds.

The third iteration produced the same value as the second: 550 microseconds. The recurrence has reached its fixed point. The worst-case response time of task three is 550 microseconds, and since 550 is less than task three's period of 1600 — and a fortiori less than its deadline — task three is schedulable, with substantial room to spare.

### 12.3 What the worked iteration shows

The worked iteration makes several things concrete that the abstract description of Section 5.2 left implicit.

It shows that the recurrence genuinely iterates: the estimate grew from 200 to 450 to 550 before stabilising, and an analysis that stopped at the first estimate would have badly underestimated the response time. The growth happens because a longer window admits more releases of the interfering tasks — task one went from one release to two as the window grew past 400 microseconds — and the recurrence must keep growing the window until the interference it computes stops increasing.

It shows that the recurrence terminates: for a schedulable task set the estimate stops growing at a fixed point, and the fixed point is the answer. For an unschedulable task set the estimate would instead grow without bound, past the deadline, and that unbounded growth is the analysis's way of reporting unschedulability.

And it shows why the reference task set's analysis was simpler. The reference task set's seven tasks all share the period 4000 microseconds; in a 4000-microsecond epoch, each task is released exactly once, the "rounded up" release counts are all exactly 1, and the recurrence's interference term never grows on a second iteration because no second release occurs within the epoch. The recurrence, for the reference task set, reaches its fixed point on the first iteration, and that first-iteration fixed point is exactly the straight-line sum of Section 6.3. The shared period is what collapses the general recurrence into the simple sum, and an implementer who introduces tasks of differing periods reintroduces the full iterative recurrence and must perform it as worked here.

## 13. Practical guidance for the implementer performing this analysis

This closing section distils the chapter into practical guidance for the implementer who must perform the timing analysis for a real conformant kernel.

Establish the worst-case execution times first, and establish them soundly. Every subsequent step of the analysis takes the per-task worst-case execution times as input, and an analysis built on underestimated execution times is unsound regardless of how carefully the later steps are performed. The worst-case execution times are established by the bounded-model-checking methodology of the validation document, conservatively, assuming cache-cold execution; do not shortcut this with a measured typical value.

Perform the utilisation check before the response-time analysis. The utilisation check is cheap — a sum and a comparison — and it answers the yes-or-no schedulability question immediately. If the utilisation check fails, the task set is unschedulable and no response-time analysis is needed; the task set must be lightened first. Only a task set that passes the utilisation check is worth the response-time analysis.

Perform the response-time analysis with the full recurrence unless the shared-period simplification provably applies. If every task shares a single period, the recurrence collapses to the straight-line sum, and the implementer may use the sum — but only after confirming the shared period genuinely holds for every task. If any task has a different period, the full iterative recurrence of Section 12 is required, and the implementer must iterate it to its fixed point, not stop early.

Account for the interrupts explicitly and conservatively. The interrupt interference is the most commonly under-counted part of the analysis. Enumerate every interrupt source, establish each source's conservative maximum rate and maximum handler duration, and include each source's interference in the recurrence. An analysis that omits an interrupt source is unsound, and the omission will not announce itself — it will simply produce a bound lower than the truth.

Pair the proof with a soak. The L1 proof establishes the bound over the model; the L2 soak runs the real system and is the standing check on whether the model has stayed faithful. Run the soak, publish its trace, and treat any approach of the measured worst toward the proven bound as a signal — not necessarily of a violated bound, but of a model and a reality that have drifted closer than the analysis assumed, and that drift is worth investigating before it becomes a violation.

Re-run the whole analysis on every task-set change. The fixed-task-set discipline and admission control exist precisely because the analysis is valid only for the task set it was performed on. Every change to the task set — every revision of the pipeline, every adjustment of a worst-case execution time — invalidates the prior analysis and requires a fresh one. Build the re-analysis into the development process so that it happens automatically on every change, because an analysis that is performed only when someone remembers to perform it is an analysis that will, eventually, not be performed when it was needed.

## 14. Common objections to the scheduling design

*Informative. The scheduling design, like the kernel design, has drawn a recurring set of objections from reviewers. Answering them sharpens the design's rationale.*

**"Earliest-Deadline-First has a reputation for poor behaviour under overload — when a task set is briefly pushed past full utilisation, EDF can cascade into a state where many tasks miss deadlines, whereas a fixed-priority scheme degrades more gracefully."**

The objection describes a real property of Earliest-Deadline-First, and it would matter for a system that operated near full utilisation and risked transient overload. The AxonOS kernel does not. It operates at a measured utilisation of 0.160 against an administrative ceiling of 0.25 and a theoretical bound of 1.0; it is nowhere near the overload regime, and the admission-control procedure structurally prevents the task set from ever reaching it. The overload pathology of Earliest-Deadline-First is a pathology of EDF *near saturation*, and the AxonOS kernel is, by deliberate design and enforced ceiling, never near saturation. The objection identifies a real weakness of the discipline in an operating regime the kernel is constructed never to enter.

**"The shared-period simplification feels like a trick. A real pipeline will eventually have tasks of differing periods, and then the simple sum is wrong."**

It is not a trick; it is an honest consequence of the current reference pipeline's structure, and the chapter is explicit, in Sections 6.3 and 12.3, that the simplification holds only because every reference task shares the 4000-microsecond period, and that a task set with differing periods reintroduces the full recurrence. The reference pipeline shares a period because every stage runs once per epoch, which is the natural structure for a pipeline that produces one observation per epoch. If a future pipeline introduces a task that runs, say, only every fourth epoch, the analysis for that pipeline uses the full recurrence of Section 12, and the chapter provides exactly that recurrence, worked through, for precisely that eventuality. The simplification is not hidden and not relied upon beyond its stated validity; it is used where it provably applies and abandoned where it does not.

**"A 0.16 utilisation is absurdly low. The kernel is using one-sixth of its processor. Either the processor is wildly overspecified or the analysis is wildly conservative."**

Both halves of the dilemma are, in a sense, true, and both are deliberate. The processor is specified with headroom because the headroom costs little — a commodity Cortex-M4F is inexpensive — and buys both the utilisation margin and the freedom for the pipeline to grow across the Standard's life without a hardware change. And the analysis is conservative because conservatism is the price of a sound proof: the worst-case execution times are cache-cold worst cases, the interrupt allowances are maximum-rate maximum-duration, and every one of those conservatisms inflates the analysed utilisation above the typical-case reality. The 0.16 figure is the analysed, conservative utilisation; the typical-case utilisation is lower still. A reviewer who finds 0.16 absurdly low has correctly noticed that the kernel is not short of processor — and being not short of processor is exactly the comfortable position a hard-real-time system wants to be in, because the discomfort of a hard-real-time system near its limit is the discomfort the whole design exists to avoid.

**"Why prove the worst-case response time at all? A twelve-hour soak with zero misses over ten million epochs is surely convincing enough."**

It is convincing, and the kernel runs exactly that soak and publishes its trace as the L2 evidence. But "convincing" is not "proven", and the gap between them is the gap the whole validation discipline exists to close. A twelve-hour soak exercises the inputs and machine states that twelve hours of operation happened to produce; the worst-case input might be one the soak never generated, lying in the vast unsampled remainder of the input space. The L1 proof ranges over that entire space, including the unsampled remainder, and confirms the bound holds there too. The soak tells the implementer the kernel is fast on the inputs it tried; the proof tells the implementer the kernel is fast on every input it could ever meet. For a safety-relevant system the difference is not academic, and the kernel does both: the proof for the universal guarantee, the soak as the standing corroboration that the proof's model matches reality.

## 15. Summary

The AxonOS kernel's timing guarantee rests on a chain of reasoning this chapter has followed link by link. The kernel's work is a fixed set of periodic tasks. The Earliest-Deadline-First discipline schedules them, chosen because its schedulability condition — total utilisation at most 1.0 — is a single, exact, task-count-independent inequality, stable under the revisions the pipeline will undergo, and because the kernel operates so far below saturation that the discipline's near-saturation weaknesses never arise. The utilisation check confirms the reference task set, at 0.160 utilisation, is both schedulable and within the 0.25 ceiling. The response-time analysis, simplified for the reference task set by the tasks' shared period into a straight-line sum of 640.2 microseconds plus conservative allowances for interrupt interference and micro-architectural effects, yields a worst-case response time the bounded model checker proves does not exceed 1000 microseconds and a twelve-hour soak measures at a worst of 972 with zero misses. Jitter is bounded by clause DC2 at evidence level L2, and the reference implementation's 2.1-microsecond measured jitter is the residue of interrupt and micro-architectural variation after the determinism disciplines have removed everything else. The interrupt analysis bounds each source's interference conservatively, and the discipline of short handlers keeps that interference small. The general response-time recurrence, worked through on a three-task example, iterates a window estimate to its fixed point and is required whenever tasks do not share a single period. Admission control extends the design-time guarantee across runtime task-set changes. The honest limits of the analysis are guarded by the pairing of the L1 proof with the L2 soak.

That chain is the machinery behind the kernel's unusual promise: not a measured observation that the kernel is usually fast, but a proven fact that the kernel is, on every admissible execution, fast enough — and a steady measured cadence that the kernel is, observation after observation, regular enough for the user to trust.

---

*End of the scheduling and timing-analysis chapter.*

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
