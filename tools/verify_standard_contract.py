#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "STANDARD.md",
    "GOVERNANCE.md",
    "VALIDATION.md",
    "SECURITY.md",
    "GLOSSARY.md",
    "ROADMAP.md",
    "legal/disambiguation.md",
    "legal/attribution.md",
    "architecture/overview.md",
    "architecture/kernel.md",
    "architecture/neural-permissions.md",
    "architecture/consent.md",
    "architecture/gateway.md",
    "architecture/swarm.md",
    "validation/evidence-levels.md",
    "validation/claims-register.md",
    "validation/falsifiable-predictions.md",
    "rfcs/README.md",
]

for path in required:
    if not (ROOT / path).is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if "AxonOS Standard" not in readme:
    print("ERROR: README missing AxonOS Standard", file=sys.stderr)
    sys.exit(1)

if "Neural data is not application data" not in readme:
    print("ERROR: README missing core principle", file=sys.stderr)
    sys.exit(1)

ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
if "\n" not in ci or "standard-contract" not in ci:
    print("ERROR: CI workflow malformed", file=sys.stderr)
    sys.exit(1)

disamb = (ROOT / "legal/disambiguation.md").read_text(encoding="utf-8")
if "AxonDAO" not in disamb:
    print("ERROR: disambiguation missing AxonDAO", file=sys.stderr)
    sys.exit(1)

print("AxonOS Standard contract: PASS")
