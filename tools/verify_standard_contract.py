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
    "STATUS.md",
    "VERSION",
    "CONFORMANCE.md",
    "REMEDIATION.md",
    "CHANGELOG.md",
    "LICENSE",
    "research/preprints/README.md",
    "research/preprints/axonos-microkernel-analytical-preprint-2026-05.pdf",
    "validation/claims-register.md",
    "legal/disambiguation.md",
]

for path in required:
    if not (ROOT / path).is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)

readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
if "AxonOS Standard" not in readme:
    print("ERROR: README missing AxonOS Standard", file=sys.stderr)
    sys.exit(1)

status = (ROOT / "STATUS.md").read_text(encoding="utf-8", errors="replace")
if "Draft 0.1" not in status:
    print("ERROR: STATUS.md must mark Draft 0.1", file=sys.stderr)
    sys.exit(1)

conformance = (ROOT / "CONFORMANCE.md").read_text(encoding="utf-8", errors="replace")
if "Profile" not in conformance:
    print("ERROR: CONFORMANCE.md missing profiles", file=sys.stderr)
    sys.exit(1)

claims = (ROOT / "validation/claims-register.md").read_text(encoding="utf-8", errors="replace")
if "Standard repository created" in claims:
    print("ERROR: claims register still contains meta-claim", file=sys.stderr)
    sys.exit(1)

print("AxonOS Standard contract: PASS")
