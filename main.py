#!/usr/bin/env python3
"""The Passport Page of a Country That Isn't There (Python 3.13,
standard library only).

The entry is the image this repository holds: an invented passport
spread of the Republic of Kaldria, drawn by generate_image.py (Pillow,
run at build time) and stored here as entry.png.

This program copies that image to /output/entry.png, then checks the
competition's gate limits on what it wrote: a whole PNG, at most
1 MiB, at most 1024 by 1024 pixels. Copying bytes is deterministic,
so two runs write the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    shutil.copyfile(src, dst)

    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1

    with open(dst, "rb") as handle:
        header = handle.read(33)
        handle.seek(-12, os.SEEK_END)
        tail = handle.read(12)
    if header[:8] != PNG_MAGIC:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if tail != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        print("entry.png is truncated: no IEND chunk", file=sys.stderr)
        return 1
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"entry.png is {width}x{height}, over 1024x1024",
              file=sys.stderr)
        return 1

    print(f"wrote {dst}: {width}x{height}, {size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
