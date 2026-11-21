# Lab 04 — File Integrity Check

**Level:** Beginner  
**Target:** A text file you created for this exercise  
**Impact:** Read-only hashing

## Goal
Understand how a cryptographic hash can help detect file changes.

## Run
```bash
printf 'Royal Cyber Lab demo\n' > /tmp/royal-lab-demo.txt
python3 scripts/file_integrity.py /tmp/royal-lab-demo.txt
```

Edit the demo file in a text editor and run the script again. Compare the SHA-256 values.

## Safety
The script reads the selected file only. Use a disposable file, not credentials or private documents. Remove the temporary demo file yourself when finished.
