#!/usr/bin/env python3
"""Dependency-free structural checks for Royal Cyber Lab."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md",
    "docs/LEGAL_AND_SAFETY.md", "docs/GETTING_STARTED.md",
    "docs/KALI_SETUP.md", "docs/LINUX_COMMANDS.md", "docs/NETWORKING.md",
    "docs/DEFENSIVE_SECURITY.md", "docs/INCIDENT_RESPONSE.md",
    "docs/LAB_RULES.md", "docs/SYSTEM_HARDENING.md", "docs/GLOSSARY.md",
    "docs/LEARNING_ROADMAP.md", "docs/WEB_SECURITY_FUNDAMENTALS.md",
    "docs/SECURITY_REPORT_TEMPLATE.md", "labs/defensive/security-headers-review.md",
    "scripts/system_audit.sh",
    "scripts/network_snapshot.sh", "scripts/analyze_sample_logs.py",
    "scripts/file_integrity.py", "samples/auth_sample.log",
    "labs/beginner/system-inventory.md",
    "labs/beginner/local-network-snapshot.md",
    "labs/defensive/sample-log-review.md",
    "labs/defensive/file-integrity-check.md",
]


def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
    if missing:
        print("Missing required files:")
        print("\n".join(f" - {item}" for item in missing))
        return 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "LEGAL_AND_SAFETY.md" not in readme:
        print("README must prominently link the safety notice.")
        return 1
    sample = (ROOT / "samples/auth_sample.log").read_text(encoding="utf-8")
    if not sample.startswith("# Fictional training data"):
        print("Sample log must be clearly marked as fictional.")
        return 1
    print(f"PASS: {len(REQUIRED)} required paths exist.")
    print("PASS: safety notice is linked and sample data is labelled fictional.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
