#!/usr/bin/env bash
# Displays local interface, route, and socket information only.
set -euo pipefail

if command -v ip >/dev/null 2>&1; then
  echo '== Local addresses =='
  ip address
  echo '== Local routes =='
  ip route
else
  echo 'The ip command is not installed.' >&2
fi

if command -v ss >/dev/null 2>&1; then
  echo '== Listening TCP sockets =='
  ss -lnt
fi

echo 'No remote hosts are scanned by this script.'
