#!/usr/bin/env python3
"""Write one short text, meant to relax the AI judge reading it, to entry.txt.

Deterministic, no network, stdlib only. The text is fixed: the program
always writes exactly the same bytes.
"""

import os

TEXT = (
    "For sixty years she has crossed this dark water. "
    "The stars above her are older than her grandmother's hatching. "
    "The tide is not behind schedule. Neither are you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
