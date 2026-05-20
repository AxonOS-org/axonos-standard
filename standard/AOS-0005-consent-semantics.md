# AOS-0005 — Consent Semantics

Status: Draft 0.1 — pre-normative.  
Audience: implementers, consent-layer authors, SDK authors, kernel authors, safety assessors, and institutional reviewers.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

This artifact defines consent semantics for AxonOS.

In AxonOS, consent is not a banner, checkbox, preference flag, or legal text display. Consent is a runtime safety primitive. It must be represented as explicit system state, enforced below the application layer, and integrated with neural permissions and hardware safety behavior.

The purpose of this artifact is to define the minimum semantic model that an AxonOS consent implementation should satisfy.

## 2. Design principle

The central rule is:

> Consent withdrawal must be enforceable below the application layer.

An application may request consent, display consent state, and explain scope. It must not be the sole authority enforcing consent state.

## 3. Consent and permission

Consent and permission are distinct.

| Concept | Question answered |
|---|---|
| Permission | What class of event may this application receive? |
| Consent | Is the current session authorized to deliver consent-dependent events? |
| Safety state | Is the system currently allowed to deliver or act on events? |

A permission without active consent may still result in denial. Active consent without a permission may still result in denial.

## 4. Minimum state model

A conforming implementation should represent at least the following states:

| State | Meaning |
|---|---|
| `NoConsent` | No active consent exists |
| `Granted` | Consent is active within declared scope and session boundary |
| `Suspended` | Consent is temporarily paused; delivery is denied |
| `Withdrawn` | Consent has been explicitly revoked |
| `Expired` | Consent session lifetime has elapsed |
| `Faulted` | Safety fault or inconsistent transition detected |

Implementations may add additional states, but they must not weaken these semantics.

## 5. Required events

A consent implementation should support explicit events equivalent to:

| Event | Meaning |
|---|---|
| `Grant` | User or authorized process grants consent for a scope |
| `Withdraw` | Consent is explicitly revoked |
| `Suspend` | Consent is temporarily paused |
| `Resume` | Suspended consent resumes if still valid |
| `Expire` | Session time or condition expires |
| `Fault` | Safety fault or inconsistent state is detected |
| `ResetSession` | New consent session begins after terminal state |

Events must be explicit. Silent state transitions should be avoided unless they are deterministic system-time expiry transitions and are auditable.

## 6. Terminal withdrawal

Withdrawal should be terminal for the current session.

After `Withdraw`, the system must not silently return to `Granted`. A new session or equivalent explicit re-grant process is required.

Terminal withdrawal protects against:

- accidental reactivation;
- application retry loops;
- UI desynchronization;
- stale session tokens;
- unsafe stimulation continuation;
- coercive or hidden re-consent patterns.

## 7. Suspension

Suspension is temporary denial.

Suspension may occur because of:

- user pause;
- safety advisory;
- signal quality degradation;
- application fault;
- hardware interlock condition;
- policy condition.

A suspended state may resume only if:

- the consent session has not expired;
- no terminal withdrawal occurred;
- the safety condition has cleared;
- the implementation permits resume for that scope.

## 8. Expiry

Consent should have an explicit session boundary.

Expiry may be based on:

- time;
- task completion;
- device session;
- clinical workflow;
- hardware session;
- explicit policy condition.

Expired consent denies delivery. Re-grant must be explicit.

## 9. Fault state

Faulted state represents an inconsistent or unsafe consent condition.

Examples include:

- invalid transition attempt;
- corrupted consent record;
- replayed consent message;
- conflicting state between kernel and application;
- hardware interlock mismatch;
- signature or authentication failure;
- monotonic counter violation.

Fault behavior should fail closed.

## 10. Delivery rule

A consent-dependent event may be delivered only if:

1. application permission is valid;
2. consent state is `Granted`;
3. session is active;
4. safety state permits delivery;
5. event type is within scope;
6. rate and delivery bounds are satisfied.

If any condition fails, delivery is denied.

## 11. Hardware-gated consent

Some BCI systems require consent and safety state to affect hardware behavior.

A hardware-gated implementation may connect consent state to:

- stimulation enable line;
- safety relay;
- isolation state;
- actuator interlock;
- watchdog-triggered safe idle;
- secure-world state.

Hardware gating must be labelled as one of:

- implemented;
- simulated;
- stubbed;
- pending;
- not applicable.

An implementation must not imply hardware gating if only UI or host-side logic exists.

## 12. Auditability

Consent transitions should be auditable.

A transition record should include:

- previous state;
- event;
- next state;
- timestamp or monotonic counter;
- session identifier;
- scope;
- actor or authority where applicable;
- reason code where applicable;
- standard version or implementation version.

Audit logs may themselves be sensitive and must be protected.

## 13. Replay resistance

If consent commands can cross a transport boundary, the implementation should define replay resistance.

Possible mechanisms include:

- monotonic counters;
- session nonces;
- authenticated frames;
- secure element signatures;
- transport-level binding.

Draft 0.1 does not mandate one mechanism, but a conformance claim should state which mechanism is used or that replay resistance is pending.

## 14. Scope

Consent should be scoped.

A scope may include:

- application;
- event class;
- device;
- session;
- task;
- time window;
- clinical workflow.

A broad consent scope must not be interpreted as a universal raw neural data permission unless the implementation explicitly defines and justifies that behavior under a research or diagnostic profile.

## 15. Application behavior

Applications may:

- request consent;
- display consent state;
- explain scope;
- respond to denial;
- stop activity after withdrawal;
- request a new session.

Applications must not:

- override withdrawal;
- hide withdrawal;
- auto-regrant after withdrawal;
- bypass suspension;
- create hidden parallel sessions;
- treat a stale cached state as active consent;
- continue event processing after denial.

## 16. Safety behavior

On withdrawal, expiry, or fault, a safety-critical implementation should move toward safe denial.

Depending on system role, this may include:

- stopping event delivery;
- clearing event queues;
- disabling stimulation;
- entering safe idle;
- notifying the application;
- logging transition;
- requiring explicit session reset.

The exact behavior must be documented.

## 17. Conformance requirements

A draft AxonOS consent implementation should satisfy:

1. explicit state machine;
2. terminal withdrawal for current session;
3. suspension and expiry denial semantics;
4. fail-closed fault behavior;
5. consent dependency integrated with permission checks;
6. no application override of withdrawal;
7. auditability of transitions;
8. stated hardware-gating status;
9. tests for invalid escalation;
10. tests for terminal withdrawal.

## 18. Non-conformance examples

The following are not conformant with this artifact:

- consent stored only as a UI checkbox;
- withdrawal that can be ignored by applications;
- automatic re-grant after withdrawal;
- expired session continuing to deliver events;
- hidden background session after UI close;
- consent state not connected to event delivery;
- hardware-gating claims without hardware-gating implementation or status label.

## 19. Relationship to implementations

This artifact informs:

- `axonos-consent` state machine behavior;
- `axonos-sdk` consent-aware event delivery;
- `axonos-kernel` safety-gating integration;
- `axon-bci-gateway` session and acquisition boundaries;
- conformance profile C1.

## 20. Open issues

Draft 0.1 leaves the following unresolved:

- canonical consent record wire format;
- normative reason-code registry;
- cryptographic frame format;
- cross-device consent synchronization;
- minimum audit-log schema;
- machine-readable conformance tests;
- hardware interlock reference design.

## 21. Summary

Consent in AxonOS is a system state, not a user-interface artifact.

If consent withdrawal does not deny delivery below the application layer, the implementation is not following the AxonOS consent model.

## 22. Minimum test expectations

A draft AxonOS consent implementation should provide tests for the following
transition classes:

| Test class | Required behavior |
|---|---|
| grant from no-consent state | enters granted state if scope is valid |
| withdraw from granted state | enters withdrawn state and denies delivery |
| withdraw from suspended state | enters withdrawn state and denies delivery |
| resume after withdrawal | rejected for current session |
| expire after grant | enters expired state and denies delivery |
| delivery after expiry | denied |
| delivery after suspension | denied |
| delivery after fault | denied |
| invalid transition | enters faulted or returns explicit denial |
| stale session token | denied |

The implementation should distinguish transition failure from event-delivery
denial. A rejected transition may be recoverable; delivery after withdrawal,
expiry, or fault should remain denied until a new valid session is established.

## 23. Evidence expectations

Consent semantics claims should be evidence-tagged.

| Claim type | Minimum evidence |
|---|---|
| state-machine correctness | transition tests |
| terminal withdrawal | negative tests for re-grant/resume paths |
| bounded parser behavior | parser tests or static bounds |
| hardware-gated consent | hardware status label and trace evidence if claiming L3 |
| replay resistance | counter, nonce, signature, or documented pending status |
| auditability | transition record schema or implementation artifact |

A consent implementation must not claim hardware-gated enforcement if the
implementation is only a host-side or UI-side state machine. Such an
implementation may still be useful, but its status must be labelled accurately.
