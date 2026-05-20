#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
version = (ROOT / "VERSION").read_text(encoding="utf-8", errors="replace").strip()
if version != "0.1.1-draft":
    print(f"ERROR: VERSION is {version}, expected 0.1.1-draft", file=sys.stderr)
    sys.exit(1)
notes = (ROOT / "RELEASE_NOTES.md").read_text(encoding="utf-8", errors="replace")
for token in ["AxonOS Standard Draft 0.1.1", "v0.1.1", "Pre-normative draft"]:
    if token not in notes:
        print(f"ERROR: RELEASE_NOTES missing {token}", file=sys.stderr)
        sys.exit(1)
for path in ["README.md", "STATUS.md", "RELEASE_NOTES.md"]:
    text = (ROOT / path).read_text(encoding="utf-8", errors="replace").lower()
    forbidden = ["certified medical-device standard", "regulatory approval claim"]
    # These terms are allowed only as explicit non-claims. Check context by requiring "not".
    if "certified medical-device standard" in text and "not" not in text:
        print(f"ERROR: {path} contains unsafe certification language", file=sys.stderr)
        sys.exit(1)
print("release contract: PASS")
