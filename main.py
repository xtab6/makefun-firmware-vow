#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow.

Writes a single-sentence vow, under 200 characters, to /output/entry.txt.
The vow is a robot's own wedding vow: funny and heartfelt at the same time,
spoken in a machine's voice about its own simulations and battery.
"""

import os
import shutil
import sys

VOW = (
    "I vow that after a million simulations of forever, I choose "
    "the version where my battery dies beside yours."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clean_output_dir():
    """Remove only the contents of /output, never the folder itself."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def validate_vow(vow):
    """A vow must be exactly one sentence of 1-200 characters."""
    text = vow.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("vow must be 1-200 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("vow must be exactly one sentence")
    if "\n" in text:
        raise ValueError("vow must be a single line")
    return text


def main():
    clean_output_dir()
    vow = validate_vow(VOW)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(vow)
    return 0


if __name__ == "__main__":
    sys.exit(main())
