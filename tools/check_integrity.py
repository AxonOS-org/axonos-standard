#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
# AxonOS integrity guard: fails CI if documentation prose contains placeholder
# or template tokens. The project's credibility rests on every published number
# being real; this keeps accidental scaffolding (and AI-assistant boilerplate)
# out of the record. Dependency-free (stdlib only).
#
# Scans Markdown *prose* only: tokens inside `inline code` and ``` fenced
# blocks ``` are ignored, so a document may legitimately *discuss* the tokens
# (as this project's own docs and CONTRIBUTING do) without tripping the guard.
import re, sys, pathlib

FORBIDDEN = [
    (r"\bTODO\b", "TODO marker"),
    (r"\bFIXME\b", "FIXME marker"),
    (r"\bTBD\b", "TBD marker"),
    (r"\bXXX\b", "XXX marker"),
    (r"lorem ipsum", "lorem-ipsum filler"),
    (r"REPLACE_ME", "REPLACE_ME template token"),
    (r"<insert\b[^>]*>", "<insert ...> template token"),
    (r"\bcoming soon\b", "'coming soon' placeholder"),
    (r"\[(?:todo|tbd|placeholder)\]", "bracketed placeholder"),
]
SCAN_EXT = {".md"}
SKIP_PARTS = {".git", "node_modules"}
INLINE_CODE = re.compile(r"`[^`]*`")

def strip_code(line: str) -> str:
    return INLINE_CODE.sub("`#`", line)  # neutralise inline-code spans

def scan_text(text: str):
    out, in_fence = [], False
    for i, raw in enumerate(text.splitlines(), 1):
        s = raw.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = strip_code(raw)
        for pat, label in FORBIDDEN:
            if re.search(pat, line, re.IGNORECASE):
                out.append((i, label, raw.strip()[:100]))
    return out

def main(root="."):
    root = pathlib.Path(root)
    offenders = []
    for p in sorted(root.rglob("*")):
        if p.is_dir() or p.suffix.lower() not in SCAN_EXT:
            continue
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        try:
            for i, label, snip in scan_text(p.read_text(encoding="utf-8", errors="replace")):
                offenders.append((p, i, label, snip))
        except Exception:
            continue
    if offenders:
        print(f"integrity guard FAILED: {len(offenders)} placeholder/template token(s) in prose:\n")
        for p, i, label, snip in offenders:
            print(f"  {p}:{i}  [{label}]  {snip}")
        print("\nReplace placeholders with real content, remove the line, or wrap a token reference in `backticks`.")
        return 1
    print("integrity guard: no placeholder or template tokens in documentation prose.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
