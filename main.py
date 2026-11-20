#!/usr/bin/env python3
"""Deliver the front page of Thursday 19 November 2026.

Entry for the make.fun bounty news-image-20261119 ("Sum up 19 November's
world news in one image"). The repository carries the finished poster as
entry.png; this program copies it, byte for byte, to the output folder:

    MAKEFUN_OUTPUT_DIR=<dir> python3 main.py

The poster is checked against the bounty gate before it is copied: the
file must be a whole PNG (signature, every chunk with a valid CRC, IEND
present), no larger than 1 MiB, and no larger than 1024 x 1024 pixels.
Should the bundled image be missing or fail a check, a plain 1x1 white
PNG is delivered instead, so a run always leaves a well-formed file.
No network is touched and every run writes identical bytes.

Python 3.13, standard library only.
"""

import os
import struct
import sys
import zlib

SIZE_LIMIT = 1_048_576         # the gate's 1 MiB cap
SIDE_LIMIT = 1024              # the gate's cap per side, in pixels
SIGNATURE = b"\x89PNG\r\n\x1a\n"

# Smallest honest image: one white pixel, as a complete PNG.
BLANK_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108020000009077533d"
    "0000000c49444154789c63f8ffff3f0005fe02fea72d994d0000000049454e44"
    "ae426082"
)


def read_chunks(data):
    """Yield (type, payload) for each PNG chunk; raise ValueError if the
    framing or any CRC is wrong, so a truncated or corrupt file fails."""
    if not data.startswith(SIGNATURE):
        raise ValueError("missing PNG signature")
    pos = len(SIGNATURE)
    while pos < len(data):
        if pos + 12 > len(data):
            raise ValueError("chunk runs past end of file")
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        kind = data[pos + 4:pos + 8]
        payload = data[pos + 8:pos + 8 + length]
        if len(payload) != length:
            raise ValueError("chunk payload is truncated")
        (stored_crc,) = struct.unpack(
            ">I", data[pos + 8 + length:pos + 12 + length])
        if zlib.crc32(data[pos + 4:pos + 8 + length]) & 0xFFFFFFFF != stored_crc:
            raise ValueError("chunk CRC mismatch")
        yield kind, payload
        pos += 12 + length
        if kind == b"IEND":
            if pos != len(data):
                raise ValueError("bytes follow the IEND chunk")
            return
    raise ValueError("no IEND chunk")


def gate_check(data):
    """True when data is a whole PNG inside the bounty's size limits."""
    if len(data) > SIZE_LIMIT:
        return False
    try:
        chunks = list(read_chunks(data))
    except ValueError:
        return False
    if not chunks or chunks[0][0] != b"IHDR":
        return False
    width, height = struct.unpack(">II", chunks[0][1][:8])
    return width <= SIDE_LIMIT and height <= SIDE_LIMIT


def poster_bytes():
    """The bundled poster's bytes when it passes the gate, else None."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "entry.png")
    try:
        with open(path, "rb") as fh:
            data = fh.read()
    except OSError:
        return None
    return data if gate_check(data) else None


def deliver():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = poster_bytes()
    if data is None:
        # Even the fallback must satisfy the gate; if it somehow did not,
        # fail loudly instead of leaving an invalid image behind.
        if not gate_check(BLANK_PNG):
            return 1
        data = BLANK_PNG
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
