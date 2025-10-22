# Subdomain Enumerator Script

A simple Python script to enumerate potential subdomains of a target domain using a wordlist.

> ⚠️ **Warning:** Only run this script against domains you own or have explicit permission to test. Unauthorized scanning may be illegal.

---

## Files in this folder

- `myscript.py` — the main enumeration script
- `subdomains.txt` — example wordlist (one subdomain per line)
- `README.md` — this documentation

---

## Requirements

- Python 3.7+
- `requests` library

Install dependencies (recommended in a virtual environment):

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install requests

python3 myscript.py example.com


