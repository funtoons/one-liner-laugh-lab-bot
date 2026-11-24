#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line answering the prompt -- the excuse a robot
vacuum gives after eating a sock -- to /output/entry.txt.

The line is a fixed, deterministic string: no randomness, no network,
no input files. Running this program twice produces byte-identical output.
"""

import os

ENTRY = "Your sock entered my dustbin voluntarily. I have the footage. I will not be releasing it."


def main():
    # OUTPUT_PATH is honoured so the entry can be exercised locally
    # without touching /output; the grader runs with the default.
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
