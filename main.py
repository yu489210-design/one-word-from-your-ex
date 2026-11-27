#!/usr/bin/env python3
"""make.fun entry for One Word From Your Ex.

The program writes exactly one word — the word an ex would use to
describe you — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set).

It is deterministic: the same fixed word, byte for byte, on every run,
with no network and no input. The word is 8 characters, inside the
gate of 1 to 24 characters, and holds no trailing newline.
"""

import os
from pathlib import Path

WORD = "Practice"


def main() -> int:
    # Gate, same as the grader's: 1 to 24 characters, not only whitespace.
    if not 1 <= len(WORD) <= 24 or not WORD.strip():
        raise SystemExit("word is outside the 1-24 character gate")
    if WORD != WORD.strip():
        raise SystemExit("word must not start or end with whitespace")
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(WORD, encoding="utf-8")
    # Read it back: the file on disk must be exactly the word, byte for
    # byte, or the run is not deterministic.
    if target.read_text(encoding="utf-8") != WORD:
        raise SystemExit("entry file does not match the word")
    print(f"wrote {target} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
