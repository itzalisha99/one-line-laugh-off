#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
"""
import os

LINE = "I told my GPS I wanted the scenic route. It took me past my ex's house. Twice."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, UTF-8, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # round-trip check: what we wrote is exactly what we validated
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("written entry does not match validated entry")


if __name__ == "__main__":
    main()
