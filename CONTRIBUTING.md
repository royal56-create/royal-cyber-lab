# Contributing

Thanks for helping improve Royal Cyber Lab.

## Contribution rules
- Keep all exercises legal, defensive, and safe by default.
- Use localhost, synthetic data, or a lab machine you own or are explicitly authorized to test.
- Never submit real credentials, personal data, malware, persistence mechanisms, stealth/evasion instructions, or destructive payloads.
- Explain prerequisites, expected output, cleanup, and safety boundaries.
- Prefer read-only commands and standard-library scripts.
- Do not describe a disclaimer as permission to test third-party systems.

## Before opening a pull request
1. Run `python tests/check_project.py`.
2. Run `bash -n scripts/*.sh` where Bash is available.
3. Run `python -m py_compile scripts/*.py`.
4. Review every command for unintended network or system changes.
