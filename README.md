# CyberWolf CTF #028 — The Broken Archive

Category: FORENSIC
Difficulty: EASY
Points: 50

Flag: `CYBERWOLF{archive_recovered}`

## Intended solve

1. Open the challenge website.
2. Download `recovered_archive.zip`.
3. Extract the archive.
4. Inspect every entry, including hidden directories/files.
5. Find `.recovery/.case_note.txt`.
6. Open the recovered note and retrieve the flag.

The important file is deliberately stored in a hidden directory.
No brute force is required.
