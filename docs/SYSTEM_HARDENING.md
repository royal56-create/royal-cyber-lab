# Local System Hardening Checklist

Use this checklist only on a machine you own or administer. Changes can affect availability; make a backup and understand rollback steps first.

- [ ] Install security updates from trusted distribution repositories.
- [ ] Remove unused packages only after checking dependencies.
- [ ] Review enabled services and their business purpose.
- [ ] Use standard accounts for daily work; elevate privileges only when necessary.
- [ ] Apply least-privilege permissions to files and directories.
- [ ] Use a host firewall policy appropriate to the machine's role.
- [ ] Enable screen locking and device encryption where appropriate.
- [ ] Configure reliable backups and test restoration.
- [ ] Review authentication logs and investigate anomalies.
- [ ] Document every configuration change and its rollback.

This document is a review checklist, not an automated hardening script. It deliberately does not change firewall, account, or service settings.
