#!/usr/bin/env python3
"""Entry for make.fun bounty u-deranalabs-invent-a-word-we-need-17a020e0.

Coins one new English word and defines it in a single line.
Writes the entry text to /output/entry.txt FIRST, then attempts a
repo-root copy of entry.txt inside try/except (the grader sandbox is
read-only, so a failed repo-root write must never crash the run).
Deterministic, no network, no secrets.
"""

import os

ENTRY = "percentghost (n.) The last 1% of your phone battery that refuses to die, haunting your screen for three more hours."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass

if __name__ == "__main__":
    main()
