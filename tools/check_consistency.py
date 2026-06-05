#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
# AxonOS Standard consistency guard. Dependency-free (stdlib only).
# Usage: python tools/check_consistency.py <structure|version|attribution|license|sections|xref|links|all>
import re, sys, pathlib

ROOT = pathlib.Path(".")
NORMATIVE = ["STANDARD.md","GLOSSARY.md","CONFORMANCE.md","VALIDATION.md","GOVERNANCE.md"]
REQUIRED = NORMATIVE + ["CLAIMS.md","README.md","SECURITY.md","ROADMAP.md","CHANGELOG.md",
    "CITATION.cff","LICENSE","VERSION","architecture/kernel.md","architecture/scheduling.md",
    "architecture/capability-system.md","architecture/consent.md",
    ".github/workflows/ci.yml",".github/workflows/integrity.yml",
    "tools/check_integrity.py","tools/check_consistency.py"]

def md_files():
    return [p for p in sorted(ROOT.rglob("*.md")) if ".git" not in p.parts]

def fail(msg): print("  FAIL:", msg); return False
def header_version(text):
    m = re.search(r'Version (\d+\.\d+\.\d+)', text)  # case-sensitive: matches '**Version X**'/'…, Version X' headers
    return m.group(1) if m else None

def c_structure():
    missing=[f for f in REQUIRED if not (ROOT/f).exists()]
    return True if not missing else fail("missing files: "+", ".join(missing))

def c_version():
    v=(ROOT/"VERSION").read_text().strip()
    ok=True
    for f in NORMATIVE+["README.md"]:
        hv=header_version((ROOT/f).read_text(encoding='utf-8'))
        if hv!=v: ok=fail(f"{f} header version {hv} != VERSION {v}")
    cm=re.search(r'^version:\s*"([^"]+)"',(ROOT/"CITATION.cff").read_text(encoding='utf-8'),re.M)
    if not cm or cm.group(1)!=v: ok=fail(f"CITATION.cff version {cm and cm.group(1)} != {v}")
    return ok

def c_attribution():
    ok=True
    for p in md_files():
        if "Denis Yermakou" not in p.read_text(encoding='utf-8'): ok=fail(f"{p}: missing editor attribution")
    return ok

def c_license():
    lic=(ROOT/"LICENSE").read_text(encoding='utf-8')
    ok = True if "Creative Commons Attribution-ShareAlike 4.0" in lic else fail("LICENSE is not CC-BY-SA-4.0")
    for f in NORMATIVE:
        if "CC-BY-SA-4.0" not in (ROOT/f).read_text(encoding='utf-8'): ok=fail(f"{f}: no CC-BY-SA-4.0 notice")
    return ok

def section_set():
    return [int(m) for m in re.findall(r'^## Section (\d+)\.', (ROOT/"STANDARD.md").read_text(encoding='utf-8'), re.M)]

def c_sections():
    s=section_set()
    if len(s)!=len(set(s)): return fail(f"duplicate section numbers: {s}")
    if s!=sorted(s): return fail(f"section numbers out of order: {s}")
    # Gaps are tolerated (a number may be referenced before its heading exists); duplicates and disorder are not.
    return True

def c_xref():
    txt=(ROOT/"STANDARD.md").read_text(encoding='utf-8')
    defined=set(section_set()); mx=max(defined) if defined else 0
    refs=set(int(n) for n in re.findall(r'Sections?\s+(\d+)', txt))
    bad=sorted(n for n in refs if n>mx)
    return True if not bad else fail(f"cross-references to non-existent sections: {bad} (max {mx})")

def c_links():
    ok=True
    for p in md_files():
        for tgt in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if tgt.startswith(('http://','https://','mailto:','#')): continue
            path=tgt.split('#')[0]
            if not path: continue
            if not (p.parent/path).resolve().exists(): ok=fail(f"{p}: broken relative link -> {tgt}")
    return ok

CHECKS={"structure":c_structure,"version":c_version,"attribution":c_attribution,
        "license":c_license,"sections":c_sections,"xref":c_xref,"links":c_links}

def main(which):
    names=list(CHECKS) if which=="all" else [which]
    allok=True
    for n in names:
        r=CHECKS[n]()
        print(f"  [{'ok' if r else 'FAIL'}] {n}")
        allok = allok and r
    print("consistency guard:", "all checks passed." if allok else "FAILURES above.")
    return 0 if allok else 1

if __name__=="__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else "all"))
