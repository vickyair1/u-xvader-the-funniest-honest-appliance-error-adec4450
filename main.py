#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-xvader-the-funniest-honest-appliance-error-adec4450.

Writes one line (at most 200 characters): the funniest honest error
message an appliance could show.

Output is /output/entry.txt ONLY. The grade sandbox mounts the repo
read-only and provides /output as the writable directory; the gate
reads /output/entry.txt. Writing beside __file__ fails there (the
open raises, the program exits 1, run_completes fails), so this
program never writes anywhere else.
"""

import hashlib
import os
import sys

# The entry: a boiler (Vaillant-style F.28 ignition failure) reporting
# its fault in a flat, put-upon voice. The fault is real — a boiler
# attempts ignition several times, then locks out when there is no gas
# supply — and the twist is the machine's deadpan diagnosis of why.
ENTRY = (
    "ERROR F.28: I tried to light 14 times. There is no gas. "
    "I am not broken. Your bill is unpaid."
)

MAX_CHARS = 200

# The grade sandbox's writable directory; the gate reads this file.
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def entry_path():
    """Deterministic output location: /output/entry.txt."""
    return OUTPUT_PATH


def write_entry():
    """Create /output if needed, then write the validated entry there."""
    text = validate_entry(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return OUTPUT_PATH, text


def validate_entry(text):
    """Gate check mirroring the sealed scorer: UTF-8 text, 1..200 chars,
    not only white space, single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters, must be 1..%d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    path, text = write_entry()
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("wrote %s (%d chars, sha256 %s)" % (path, len(text), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
