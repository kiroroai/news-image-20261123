#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123.

Copies the pre-rendered broadsheet image (entry.png, in this repository)
to /output/entry.png. Standard library only, no network, deterministic:
every run writes the same bytes.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    # The kit runs programs with MAKEFUN_OUTPUT_DIR set for local runs;
    # the grader writes to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy is byte for byte identical to the source.
    with open(src, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    assert src_hash == dst_hash, "entry.png copy mismatch"


if __name__ == "__main__":
    main()
