#!/usr/bin/env python3
"""Summarize a deliberately synthetic authentication log; offline and read-only."""
from collections import Counter
from pathlib import Path
import re
import sys

EVENT = re.compile(r"^(?P<timestamp>\S+)\s+(?P<status>SUCCESS|FAILED)\s+user=(?P<user>[\w-]+)\s+source=(?P<source>[\w.:-]+)$")


def analyze(path: Path) -> int:
    counts = Counter()
    sources = Counter()
    malformed = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = EVENT.fullmatch(line)
        if not match:
            malformed += 1
            continue
        counts[match.group("status")] += 1
        if match.group("status") == "FAILED":
            sources[match.group("source")] += 1

    print(f"Successful events: {counts['SUCCESS']}")
    print(f"Failed events: {counts['FAILED']}")
    print(f"Malformed/ignored lines: {malformed}")
    print("Most common synthetic sources for failed events:")
    for source, count in sources.most_common(5):
        print(f"  {source}: {count}")
    print("Reminder: a failed event alone is not proof of compromise.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} PATH_TO_SYNTHETIC_LOG", file=sys.stderr)
        raise SystemExit(2)
    log_path = Path(sys.argv[1])
    if not log_path.is_file():
        print("Input file not found.", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(analyze(log_path))
