#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
license_path = ROOT / "LICENSE"

if not license_path.is_file():
    print("ERROR: LICENSE missing", file=sys.stderr)
    sys.exit(1)

text = license_path.read_text(encoding="utf-8", errors="replace")

required = [
    "MIT License",
    "Permission is hereby granted",
    "THE SOFTWARE IS PROVIDED",
]

for token in required:
    if token not in text:
        print(f"ERROR: LICENSE missing {token}", file=sys.stderr)
        sys.exit(1)

if len(text) < 900:
    print("ERROR: LICENSE too short", file=sys.stderr)
    sys.exit(1)

if (ROOT / "LICENSE.md").exists():
    print("ERROR: duplicate LICENSE.md should not exist; keep only canonical LICENSE", file=sys.stderr)
    sys.exit(1)

print("license policy: PASS")
