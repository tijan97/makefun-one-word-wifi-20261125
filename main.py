#!/usr/bin/env python3
"""One Word for Your Wi-Fi — writes the entry word to entry.txt.

The grader runs this program in a sandbox and reads the single word
from <output dir>/entry.txt.
"""

import os

ENTRY_WORD = "Princess"


def validate(word):
    """The sealed gate accepts UTF-8 text of 1 to 20 characters, not only
    whitespace, and this competition takes exactly one word."""
    if not isinstance(word, str):
        raise ValueError("entry word must be text")
    if not 1 <= len(word) <= 20:
        raise ValueError("entry word must be 1 to 20 characters")
    if not word.strip():
        raise ValueError("entry word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main():
    validate(ENTRY_WORD)
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)
    # Confirm the file on disk is byte-identical to the entry word.
    with open(entry_path, "rb") as f:
        written = f.read()
    if written != ENTRY_WORD.encode("utf-8"):
        raise ValueError("entry.txt does not match the entry word")


if __name__ == "__main__":
    main()
