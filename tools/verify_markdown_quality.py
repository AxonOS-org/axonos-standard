#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
paths = list(ROOT.glob("*.md")) + list((ROOT / "standard").glob("*.md"))
for p in paths:
    text = p.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if len(lines) < 8 and p.name not in {"VERSION"}:
        print(f"ERROR: {p.relative_to(ROOT)} is too short/collapsed", file=sys.stderr)
        sys.exit(1)
    too_long = [i for i, line in enumerate(lines, 1) if len(line) > 220]
    if too_long:
        print(f"ERROR: {p.relative_to(ROOT)} has very long line(s): {too_long[:5]}", file=sys.stderr)
        sys.exit(1)
    lower = text.lower()
    for bad in ["todo", "placeholder", "lorem ipsum"]:
        if bad in lower:
            print(f"ERROR: {p.relative_to(ROOT)} contains {bad}", file=sys.stderr)
            sys.exit(1)
readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
if readme.count("http://") + readme.count("https://") > 3:
    print("ERROR: root README has too many external links", file=sys.stderr)
    sys.exit(1)
print("markdown quality: PASS")
