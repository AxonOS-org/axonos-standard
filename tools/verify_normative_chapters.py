#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "standard/AOS-0001-system-boundary.md": [
        "Raw neural data must not cross into application space by default.",
        "Draft requirements",
        "Non-conformance examples",
    ],
    "standard/AOS-0004-neural-permissions.md": [
        "neural data is not application data",
        "Default denial",
        "Capability gate",
        "Prohibited default classes",
    ],
    "standard/AOS-0005-consent-semantics.md": [
        "withdrawal is terminal for the current session",
        "Terminal withdrawal",
        "Hardware-gated consent",
        "Draft requirements",
    ],
}

for path, tokens in checks.items():
    p = ROOT / path
    if not p.is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)
    text = p.read_text(encoding="utf-8", errors="replace")
    text_lc = text.lower()
    if len(text) < 3000:
        print(f"ERROR: {path} is too short for a normative chapter", file=sys.stderr)
        sys.exit(1)
    for token in tokens:
        haystack = text_lc if token.islower() else text
        if token not in haystack:
            print(f"ERROR: {path} missing token: {token}", file=sys.stderr)
            sys.exit(1)

print("AxonOS normative chapters: PASS")
