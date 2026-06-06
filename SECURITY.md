# Security Policy — The AxonOS Standard

**AxonOS Standard v1.1.0** · **Editor:** Denis Yermakou · **Project:** AxonOS · **Domicile:** Singapore

This document is the vulnerability-disclosure policy for the AxonOS
Standard and its reference implementation. It is distinct from the
**Security and Privacy Model** of the Standard itself, which is
defined normatively in Part III (Sections 12 through 16) of
`STANDARD.md`. This file governs how to *report* a security problem;
`STANDARD.md` Part III defines what the Standard *requires* of a
conformant implementation.

## Scope

This policy covers two kinds of security report.

A **specification defect** is a flaw in the AxonOS Standard itself —
a requirement that, if implemented exactly as written, would produce
an insecure system; an ambiguity that admits an insecure reading; a
missing requirement that leaves a real attack unaddressed. A
specification defect is a defect in the documents of this repository.

An **implementation vulnerability** is a flaw in the AxonOS reference
implementation — the openly licensed code repositories that constitute
one conformant implementation of the Standard. An implementation
vulnerability is a defect in code, not in the Standard.

Both kinds of report are in scope for this policy, and both are taken
seriously, because the AxonOS Standard governs software for
safety-relevant brain-computer-interface systems and a security flaw
in either the Standard or its reference implementation can propagate
into deployed devices.

## How to report

Report a suspected security problem by writing to
**security@axonos.org**. A report should describe the problem
concretely: which document or which repository, which section or which
code path, what an attacker could do, and — where the reporter can
provide it — how the problem could be reproduced or demonstrated.

A reporter who prefers not to use email may instead open a private
security advisory through the GitHub security-advisory mechanism on
the relevant repository. A reporter should **not** open an ordinary
public issue for a suspected security problem, because a public issue
discloses the problem before it can be addressed.

## What to expect

The Project acknowledges a security report within five business days.
The acknowledgement confirms receipt and states whether the report is
being treated as a specification defect, an implementation
vulnerability, or — after examination — not a security problem.

For a confirmed problem, the Project works with the reporter on a
remediation and a disclosure timeline. The default coordinated-
disclosure window is ninety days from acknowledgement to public
disclosure, shortened if a fix is ready sooner and extended only by
mutual agreement where the remediation is genuinely complex. The
Project credits the reporter in the public disclosure unless the
reporter asks to remain anonymous.

A confirmed specification defect is remediated through the Standard's
ordinary amendment process — a Request for Comments, as `GOVERNANCE.md`
defines — except that a security-motivated RFC may be expedited where
the defect is being actively exploited or the delay of the ordinary
review period would itself create risk.

## Supported versions

Security remediations are issued for the current major version of the
Standard. The current version is recorded in the `VERSION` file. Older
major versions, once superseded, do not receive security remediations;
a deployment on a superseded major version should plan its migration
to the current one.

## What this policy does not cover

This policy does not cover security problems in third-party
implementations of the AxonOS Standard that are not the reference
implementation. A security problem in an independent implementation
should be reported to that implementation's maintainers. If, however,
an independent implementation's security problem is in fact caused by
a defect in the Standard, that underlying specification defect is in
scope and should be reported here.

This policy does not constitute a warranty. The AxonOS Standard and
its reference implementation are provided under open licences whose
terms include the customary disclaimers; this policy is a statement of
the Project's disclosure practice, not an assumption of liability.

---

— The AxonOS Project · Singapore · Zurich · Berlin · Milano · San Mateo
