# Validation Policy

AxonOS uses evidence levels to prevent ambiguity between analytical claims, runtime measurements, and externally validated results.

## Evidence levels

| Level | Name | Meaning |
|---|---|---|
| L0 | Design intent | Architecture intent, not yet validated |
| L1 | Analytical / code-level | Static analysis, unit tests, model checks, instruction counts |
| L2 | Runtime measured | Measured on development hardware or controlled harness |
| L3 | Externally instrumented | GPIO, oscilloscope, logic analyzer, independent trace capture |
| L4 | Independent review | External technical review or reproducibility check |
| L5 | Regulatory / certified | Formal regulatory or certification evidence |

## Claim rules

A claim must state:

- value;
- evidence level;
- artifact;
- date or commit;
- limitations;
- falsification threshold where applicable.

## Prohibited claim patterns

Avoid:

- "real-time" without deadline and bound;
- "verified" without verification scope;
- "safe" without hazard context;
- "private" without threat model;
- "clinical" without clinical evidence.
