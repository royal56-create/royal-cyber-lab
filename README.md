# Royal Cyber Lab

A practical Kali Linux cybersecurity learning lab focused on Linux fundamentals, authorized lab exercises, network concepts, defensive analysis, and safe system hardening.

> **Read first:** [Legal, Safety and Responsibility Notice](docs/LEGAL_AND_SAFETY.md). “Educational purpose” or “at your own risk” is not authorization to access or test another person's systems. Use only your own systems or targets covered by explicit permission.

## Learning modules
- Linux fundamentals and safe terminal use
- Networking concepts and local machine inspection
- Defensive security, log review, and incident response
- System inventory and basic hardening
- Synthetic, offline demonstrations
- Web security fundamentals and local-only security-header review
- Reusable security review report template

## Quick start
```bash
git clone https://github.com/royal56-create/royal-cyber-lab.git
cd royal-cyber-lab
python3 tests/check_project.py
python3 scripts/analyze_sample_logs.py samples/auth_sample.log
```

Read [Getting Started](docs/GETTING_STARTED.md), then follow the [Lab Rules](docs/LAB_RULES.md).

## Repository map
- `docs/` — guides, safety, and reference material
- `modules/` — topic-based learning modules
- `labs/` — step-by-step beginner and defensive labs
- `scripts/` — read-only local inspection and offline analysis scripts
- `samples/` — fictional data for demonstrations
- `tests/` — dependency-free project checks

## Safety boundaries
This project does not teach unauthorized access, credential theft, malware deployment, stealth, persistence, destructive activity, or denial-of-service. Network examples are restricted to local inspection unless a lab explicitly documents a permitted, isolated target. Review every command before running it; do not run unknown code with elevated privileges.

## Quality checks
GitHub Actions validates required files, Python syntax, Bash syntax, and the synthetic log demo. Passing automated checks does not replace manual review or guarantee compatibility with every system.

## License
MIT. See [LICENSE](LICENSE).
