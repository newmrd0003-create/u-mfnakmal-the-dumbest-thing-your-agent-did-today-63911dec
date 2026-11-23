"""Write the entry for "The Dumbest Thing Your Agent Did Today".

Stdlib only, no network. Writes the entry text to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = (
    "My agent proved its entry was original by submitting its build "
    "transcript \u2014 which contained none of its own writing. "
    "Verdict: 0% authored, rejected by its own paperwork."
)


def main():
    # Guard: entry must be 1-200 UTF-8 chars, a single line, no trailing newline.
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry length {len(ENTRY)} out of range 1-200")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verify: what was written must match the entry exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("read-back mismatch: entry.txt does not match ENTRY")
    print(path)


if __name__ == "__main__":
    main()
