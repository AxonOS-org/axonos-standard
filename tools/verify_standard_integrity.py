#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
standard = ROOT / "standard"

required_root = [
    "README.md", "STANDARD.md", "STATUS.md", "VERSION", "CONFORMANCE.md",
    "VALIDATION.md", "GOVERNANCE.md", "SECURITY.md", "GLOSSARY.md",
    "ROADMAP.md", "REMEDIATION.md", "CHANGELOG.md", "LICENSE",
    "validation/claims-register.md", "legal/disambiguation.md",
]

for rel in required_root:
    if not (ROOT / rel).is_file():
        print(f"ERROR: missing {rel}", file=sys.stderr)
        sys.exit(1)

expected = [
    "AOS-0000-charter-and-scope.md",
    "AOS-0001-system-boundary.md",
    "AOS-0002-terminology.md",
    "AOS-0003-evidence-levels-and-claims.md",
    "AOS-0004-neural-permissions.md",
    "AOS-0005-consent-semantics.md",
    "AOS-0006-conformance-profiles.md",
    "AOS-0007-intent-event-model.md",
    "AOS-0008-ipc-and-timing-contract.md",
    "AOS-0009-security-and-privacy-threat-model.md",
    "AOS-0010-reference-implementation-mapping.md",
    "AOS-0011-governance-and-change-control.md",
]

for fname in expected:
    p = standard / fname
    if not p.is_file():
        print(f"ERROR: missing standard/{fname}", file=sys.stderr)
        sys.exit(1)
    text = p.read_text(encoding="utf-8", errors="replace")
    if "Status: Draft 0.1" not in text:
        print(f"ERROR: {fname} missing Draft 0.1 status", file=sys.stderr)
        sys.exit(1)
    if len(text.splitlines()) < 25:
        print(f"ERROR: {fname} appears one-line or too thin", file=sys.stderr)
        sys.exit(1)
    if "TODO" in text or "placeholder" in text.lower():
        print(f"ERROR: {fname} contains placeholder language", file=sys.stderr)
        sys.exit(1)

nums = []
for p in sorted(standard.glob("AOS-*.md")):
    m = re.match(r"AOS-(\d{4})-", p.name)
    if m:
        nums.append(int(m.group(1)))

if nums != list(range(12)):
    print(f"ERROR: AOS numbering is not chronological 0000..0011: {nums}", file=sys.stderr)
    sys.exit(1)

readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
if len(readme.splitlines()) < 45:
    print("ERROR: root README appears collapsed or too short", file=sys.stderr)
    sys.exit(1)
if readme.count("https://github.com/") > 3:
    print("ERROR: root README is overlinked", file=sys.stderr)
    sys.exit(1)

license_text = (ROOT / "LICENSE").read_text(encoding="utf-8", errors="replace")
if "MIT License" not in license_text or "Permission is hereby granted" not in license_text:
    print("ERROR: LICENSE is not full MIT text", file=sys.stderr)
    sys.exit(1)

claims = (ROOT / "validation/claims-register.md").read_text(encoding="utf-8", errors="replace")
if "Standard repository created" in claims:
    print("ERROR: claims register still contains meta-claim", file=sys.stderr)
    sys.exit(1)

print("AxonOS Standard integrity: PASS")
