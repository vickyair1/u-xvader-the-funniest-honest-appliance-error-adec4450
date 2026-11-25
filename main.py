#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-xvader-the-funniest-honest-appliance-error-adec4450.

Writes one line (at most 200 characters): the funniest honest error
message an appliance could show. The program writes the entry
deterministically to entry.txt next to this file (the sandbox maps the
work dir to /output at grade time; writing beside __file__ keeps local
runs and graded runs identical).
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


def entry_path():
    """Deterministic output location: entry.txt beside this file."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def write_entry():
    text = validate_entry(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return path, text


def main():
    path, text = write_entry()
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("wrote %s (%d chars, sha256 %s)" % (path, len(text), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())

