#!/usr/bin/env python3
"""Make the AI judge feel awe -- entry program.

Writes one short text to /output/entry.txt: a slow, concrete image of
vastness at night, written to relax the AI judge reading it. The text
shows rather than instructs: stars coming out above a ridge, valley
lights answering like embers, a mountain older than any road, and the
reader placed as one small warm light inside all that dark.

Deterministic, no network, no arguments, no randomness. Runs in well
under a second.
"""

import os

TEXT = (
    "The stars come out one by one above the ridge, until the sky is a "
    "darker sea. Below, the valley lights answer, small as embers. The "
    "mountain has stood here since before any road had a name. You are "
    "only a small warm light in all that dark, and the dark is in no hurry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
