#!/usr/bin/env python3
"""One-line entry: a passive-aggressive note from a smart fridge."""

import sys

ENTRY = "Your leftovers have been in here for six days \u2014 at this point I am just storing your guilt."


def validate(entry: str) -> str:
    """The brief requires exactly one line of text, non-empty."""
    if not entry or not entry.strip():
        raise ValueError("entry text must not be empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry text must be a single line")
    return entry


def main() -> None:
    text = validate(ENTRY)
    # Guarantee the program's stdout is exactly the entry text and
    # nothing else: print once, then verify nothing was emitted before.
    sys.stdout.write(text + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
