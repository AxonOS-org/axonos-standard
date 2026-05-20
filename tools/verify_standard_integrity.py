#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "STANDARD.md", "STATUS.md", "VERSION", "CONFORMANCE.md",
    "VALIDATION.md", "GOVERNANCE.md", "SECURITY.md", "GLOSSARY.md",
    "ROADMAP.md", "REMEDIATION.md", "CHANGELOG.md", "LICENSE",
    "RELEASE_NOTES.md", "validation/claims-register.md",
    "legal/disambiguation.md", "standard/README.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        print(f"ERROR: missing {rel}", file=sys.stderr)
        sys.exit(1)
readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
if len(readme.splitlines()) < 60:
    print("ERROR: root README too short or collapsed", file=sys.stderr)
    sys.exit(1)
if "Draft 0.1.1" not in readme:
    print("ERROR: README missing Draft 0.1.1 status", file=sys.stderr)
    sys.exit(1)
print("standard integrity: PASS")
