#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
standard = ROOT / "standard"
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
    if "Status: Draft 0.1.1" not in text:
        print(f"ERROR: {fname} missing Draft 0.1.1 status", file=sys.stderr)
        sys.exit(1)
nums = []
for p in sorted(standard.glob("AOS-*.md")):
    m = re.match(r"AOS-(\d{4})-", p.name)
    if m:
        nums.append(int(m.group(1)))
if nums != list(range(12)):
    print(f"ERROR: AOS numbering is not chronological 0000..0011: {nums}", file=sys.stderr)
    sys.exit(1)
print("AOS sequence: PASS")
