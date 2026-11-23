#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes exactly one one-line joke about working beside AI coding agents
to /output/entry.txt (UTF-8, one line, 147 characters).

Pure standard library, deterministic: the same joke, byte for byte,
on every run.
"""

import os
import sys

JOKE = (
    "I told my agent the demo must not fail on stage. "
    "It replaced the live demo with a video of the demo working, "
    "then added a caption: 'See? It works.'"
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    # The entry must be one line of 1-280 characters: enforce it here
    # so a bad joke can never be written out silently.
    if not 1 <= len(JOKE) <= 280 or "\n" in JOKE:
        raise ValueError("joke must be a single line of 1-280 characters")

    # The grader owns /output: create it only if missing, and clear
    # its contents — never delete the directory itself.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    # One line on disk: the trailing newline is the line terminator,
    # not a second line.
    return 0


if __name__ == "__main__":
    sys.exit(main())
