#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
for d in ["architecture", "validation", "legal", "rfcs", "research"]:
    p = ROOT / d / "README.md"
    if not p.is_file():
        print(f"ERROR: {d}/README.md missing", file=sys.stderr)
        sys.exit(1)
    text = p.read_text(encoding="utf-8", errors="replace")
    if "not a separate standard" not in text:
        print(f"ERROR: {d}/README.md missing redirect disclaimer", file=sys.stderr)
        sys.exit(1)
print("legacy redirects: PASS")
