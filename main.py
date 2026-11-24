#!/usr/bin/env python3
"""One Word from Grandma — make.fun entry.

Writes exactly one word to entry.txt: the single word our grandma would
text about AI.

The word is "Al". Grandma reads "AI" and is quite sure it is a nice young
man called Al who answers all her questions — warm, a little baffled, and
convinced the robot is a person. The joke is the letters themselves: A-I
misread as a name. No caption needed, no explanation, one word.
"""

import os

WORD = "Al"

MAX_CHARS = 30


def validate(word):
    """A valid entry: exactly one word, 1-30 chars, not only whitespace.

    The word must also be printable text with at least one letter: a bare
    digit or punctuation mark is not a word a grandma would text.
    """
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word or not word.strip():
        raise ValueError("word must not be empty or only whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError("word must be at most 30 characters")
    if len(word.split()) != 1:
        raise ValueError("word must be a single word")
    if not word.isprintable():
        raise ValueError("word must be printable text")
    if not any(ch.isalpha() for ch in word):
        raise ValueError("word must contain at least one letter")
    return word


def main():
    word = validate(WORD)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Write via a fixed temp name, then atomically replace. Never use
    # tempfile.mkstemp here: it would leave a hidden file in the output
    # directory and the output folder must contain ONLY entry.txt.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word)
    os.replace(tmp_path, path)
    # This shell's umask is 007, so set the mode explicitly after replace.
    os.chmod(path, 0o644)

    # Read it back and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != word:
        raise ValueError("verification failed: entry.txt does not match")
    validate(written)
    print("wrote entry.txt: %r (%d chars)" % (written, len(written)))


if __name__ == "__main__":
    main()
