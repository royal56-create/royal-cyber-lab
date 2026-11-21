#!/usr/bin/env python3
"""Print a SHA-256 digest for a user-selected file; read-only, no network access."""
import hashlib
from pathlib import Path
import sys


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} FILE", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print("Input file not found or is not a regular file.", file=sys.stderr)
        return 2
    print(f"SHA-256  {sha256_file(path)}  {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
