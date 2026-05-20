#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "validation" / "claims-register.md"
if not p.is_file():
    print("ERROR: claims-register missing", file=sys.stderr)
    sys.exit(1)
text = p.read_text(encoding="utf-8", errors="replace")
for token in ["AOS-0004", "AOS-0005", "AOS-0008", "AOS-0009", "0.1.1-draft"]:
    if token not in text:
        print(f"ERROR: claims register missing {token}", file=sys.stderr)
        sys.exit(1)
if "Standard repository created" in text:
    print("ERROR: claims register contains obsolete meta-claim", file=sys.stderr)
    sys.exit(1)
if text.count("|") < 35:
    print("ERROR: claims register table too thin", file=sys.stderr)
    sys.exit(1)
print("claims register: PASS")
