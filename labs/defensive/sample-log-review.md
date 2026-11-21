# Lab 03 — Synthetic Authentication Log Review

**Level:** Beginner  
**Target:** The synthetic file at `samples/auth_sample.log`  
**Impact:** Offline file analysis only

## Run
```bash
python3 scripts/analyze_sample_logs.py samples/auth_sample.log
```

## Tasks
- Count successful and failed sample events.
- Identify repeated source labels in the synthetic data.
- Explain why a failed login alone does not prove compromise.

## Safety
The sample is fictional. Do not substitute real authentication logs unless you have authorization and have removed sensitive information. The script does not connect to a network or attempt authentication.
