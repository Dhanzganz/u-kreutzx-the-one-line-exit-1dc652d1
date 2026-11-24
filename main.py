#!/usr/bin/env python3
"""The One-Line Exit - make.fun entry.

Writes a single funny one-line resignation letter to /output/entry.txt.
No network, deterministic, python3.13.
"""

import os

ENTRY = "I hereby resign: HR's 'we're a family' speech finally convinced me to disown you all."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate check (competition.yaml): /output/entry.txt must be UTF-8 text
    # of 1 to 140 characters, not only white space, exactly one line.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
