# TVM Triage Toolkit

Python scripts I built to automate vulnerability management triage. The idea is simple — vulnerability scanners like Tenable generate thousands of findings and most of them are noise. These scripts filter the noise so only real, actionable stuff gets sent to the people who fix things.

## What it does

Five scripts that run in order like a pipeline:

1. **False positive filter** — checks findings against a database of known false positives and removes them
2. **Exploitability checker** — looks at where each device sits in the network and whether the CVE is on the CISA KEV list, then assigns a real-world risk rating (not just CVSS)
3. **Ticket generator** — creates remediation tickets with the actual fix, whether downtime is needed, and an SLA deadline
4. **SLA tracker** — monitors open tickets and flags anything overdue or at risk
5. **Report generator** — builds an HTML dashboard showing ticket status and SLA compliance for leadership

## How the triage logic works

Not every Critical finding is actually critical. A CVSS 9.8 on a switch behind three firewalls with no public exploit is way less urgent than a CVSS 7.0 on an internet-facing firewall that's on the CISA KEV list.

**Exploitability ratings:**
- CRITICAL — internet-facing AND on CISA KEV list
- HIGH — internet-facing OR on CISA KEV list  
- MEDIUM — internal with fewer than 2 firewalls
- LOW — behind 2+ firewalls, not on KEV

**SLA deadlines:**
- Critical/High: 30 days
- Medium: 60 days
- Low: 90 days

## Project structure

```
pipeline/          — the 5 main scripts
practice/          — daily practice scripts I wrote while learning
data/              — sample JSON data files for testing
```

## Running it

```bash
cd pipeline
python3 step1_fp_filter.py
python3 step2_exploitability.py
python3 step3_ticket_gen.py
python3 step4_sla_tracker.py
python3 step5_report.py
open report.html
```

## Practice scripts

The `practice/` folder has individual scripts I built while learning Python for security automation. Things like log parsers, config checkers, firmware auditors, inventory counters, and rebuilds of the pipeline scripts from memory.

## What I'd add next

- Hook into the Tenable API instead of reading JSON files
- Auto-create tickets in ServiceNow or Jira
- Auto-download the CISA KEV list daily
- Send Slack notifications for overdue tickets
- Replace JSON files with a database

## Built with

Python, json, csv, datetime, collections.Counter, re

## Author

Nick Langevin — [github.com/nlangevin0-dev](https://github.com/nlangevin0-dev)