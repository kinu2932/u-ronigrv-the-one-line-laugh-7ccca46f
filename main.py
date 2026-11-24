#!/usr/bin/env python3
"""The One-Line Laugh: write one funny line to /output/entry.txt.

Stdlib only. The entry is a single sentence of at most 200 characters.
"""

import os

LINE = "I set four alarms every night, and every morning all five of us hit snooze."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert text.isascii(), "entry must be ASCII so bytes equal characters"
    assert "  " not in text, "entry must not contain double spaces"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
