#!/usr/bin/env python3
"""Emit a single quiet text to entry.txt.

The program takes no input, makes no network calls, and always produces
the same bytes. It exists to give the reader one image to return to: a
sea turtle crossing dark water she has crossed for sixty years.
"""

import os
from pathlib import Path

SENTENCES = (
    "For sixty years she has crossed this dark water.",
    "The stars above her are older than her grandmother's hatching.",
    "The tide is not behind schedule. Neither are you.",
)


def build_text() -> str:
    return " ".join(SENTENCES)


def entry_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_text(), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
