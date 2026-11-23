#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is a fixed string. The program is deterministic: every run
writes the exact same bytes to /output/entry.txt (no randomness, no
network, no clock, pure standard library).
"""

import os

JOKE = (
    "My AI coding agent writes the code, I review the code, "
    "and then we both blame the demo \u2014 pair programming, "
    "but the pair is me and a very confident autocomplete."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
