#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "standard/AOS-0001-system-boundary.md": [
        "Raw neural data must not cross into application space by default.",
        "Boundary conformance requirements",
        "Non-conformance examples",
    ],
    "standard/AOS-0004-neural-permissions.md": [
        "Neural data is not application data.",
        "Default denial",
        "Capability gate",
        "Prohibited default classes",
    ],
    "standard/AOS-0005-consent-semantics.md": [
        "Consent withdrawal must be enforceable below the application layer.",
        "Terminal withdrawal",
        "Hardware-gated consent",
        "Conformance requirements",
    ],
}

for path, tokens in checks.items():
    p = ROOT / path
    if not p.is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)
    text = p.read_text(encoding="utf-8", errors="replace")
    if len(text) < 9000:
        print(f"ERROR: {path} is too short for a normative chapter", file=sys.stderr)
        sys.exit(1)
    for token in tokens:
        if token not in text:
            print(f"ERROR: {path} missing token: {token}", file=sys.stderr)
            sys.exit(1)

print("AxonOS normative chapters: PASS")
