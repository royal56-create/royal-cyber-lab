#!/usr/bin/env bash
# Read-only local system snapshot. No configuration is changed.
set -euo pipefail

printf '%s\n' '== Identity =='
whoami
hostname

printf '%s\n' '== Kernel =='
uname -a

printf '%s\n' '== Storage =='
df -h

printf '%s\n' '== Memory =='
if command -v free >/dev/null 2>&1; then free -h; else echo 'free command unavailable'; fi

printf '%s\n' '== Listening TCP sockets =='
if command -v ss >/dev/null 2>&1; then ss -lnt; else echo 'ss command unavailable'; fi

printf '%s\n' 'Read-only snapshot complete. Review output before sharing; it may contain identifying details.'
