# Ethical Hacking Starter — Server Repo

**Purpose:** safe, lab-only utilities and templates for our Discord community.  
**Rules:** All scripts and automation are for **lab environments only**. Do NOT use on external targets without written permission.

## Repo structure
- `README.md` - this file
- `scripts/scan_parser.py` - safe parser for nmap XML reports (lab usage)
- `scripts/sample_scan.xml` - example, sanitized nmap XML (for testing parser)
- `ansible/` - optional: lab provisioning playbooks (placeholders)

## How to use
1. Clone the repo.
2. Put your lab nmap XML in `scripts/` (or use the provided `sample_scan.xml`).
3. Run `python3 scripts/scan_parser.py --input sample_scan.xml --output summary.csv`
4. Review `summary.csv` in a spreadsheet.

## Contributing
- Open a PR and tag `Instructor` or `Lab-Runner` for review before adding tools that execute network actions.
