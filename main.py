#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of software error copy (at most 200 characters) to
/output/entry.txt: the brutal truth about what went wrong, funny on a
single read, shippable in a real error dialog.

The line names a concrete failure (the server ran out of memory while
saving), tells the user what happened to their work, and gives them
something useful to do next (close a few tabs, try again). The joke is
the middle clause: unsaved work demoted from fact to rumour.
"""

import os
import shutil
import sys

LINE = (
    "The server ran out of memory while saving, "
    "so your work is now a rumour. "
    "Close a few tabs and try again."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    if len(LINE) > 200 or len(LINE) < 1:
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only whitespace", file=sys.stderr)
        return 1

    # Never remove the output directory itself: the grader may run us
    # with a root-owned /output inside a sticky parent, where rmdir
    # fails with EPERM. Create it if missing, clear only its contents.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Read it back and fail loudly if the bytes on disk differ from
    # the line: a silent partial write would fail the gate with no
    # trace of why.
    with open(OUTPUT_FILE, "rb") as f:
        written = f.read()
    if written != (LINE + "\n").encode("utf-8"):
        print("verification failed: entry.txt differs from the line",
              file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
