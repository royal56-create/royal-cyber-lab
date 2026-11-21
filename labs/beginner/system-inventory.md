# Lab 01 — Local System Inventory

**Level:** Beginner  
**Target:** Your own Linux/Kali machine only  
**Impact:** Read-only inspection

## Goal
Collect a basic system snapshot without changing system configuration.

## Commands
```bash
whoami
hostname
uname -a
pwd
df -h
free -h
ps -eo pid,comm --sort=comm | head -n 20
```

## Expected learning
Identify the current account, host, kernel, storage, memory, and a sample of running processes.

## Safety and cleanup
These commands are intended for local inspection. Do not paste output publicly if it reveals usernames, hostnames, or other identifying details. No cleanup is required.
