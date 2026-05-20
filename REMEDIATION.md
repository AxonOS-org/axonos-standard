# AxonOS Standard Hardening Plan

This repository was created as the canonical entry point for the AxonOS Standard.
External review correctly identified that the first public version was a skeleton
and should not present itself as a mature conformance standard.

This remediation plan upgrades the repository from a draft skeleton to a
pre-normative Draft 0.1 standard hub.

## Accepted findings

The following findings are accepted:

1. The initial repository structure contained placeholder files.
2. The standard lacked a root `LICENSE`.
3. The standard lacked explicit versioning.
4. The claims register did not yet record technical claims.
5. Conformance profiles were not defined.
6. Governance was described but not yet instantiated.
7. Security reporting lacked operational details.
8. Research artifacts were not separated from normative text.

## Remediation actions

| Area | Action | Status |
|---|---|---|
| Licensing | Add root `LICENSE` for standard documentation | In progress |
| Versioning | Add `VERSION` and draft status | In progress |
| Status | Add `STATUS.md` with Draft 0.1 pre-normative state | In progress |
| Conformance | Add `CONFORMANCE.md` with draft profiles | In progress |
| Claims | Replace meta-claim with technical claims register | In progress |
| Research | Add `research/preprints/` for non-normative papers | In progress |
| Governance | Expand governance and maintainer process | Pending |
| Security | Add PGP/security key process | Pending |
| Architecture | Expand placeholder chapters into normative sections | Pending |
| RFC linkage | Pin standard sections to RFC versions and implementation commits | Pending |

## Principle

The repository remains the canonical AxonOS Standard entry point, but it must
state its maturity honestly.

A weak standard should not pretend to be mature. A draft standard should expose
its gaps and close them through an auditable process.
