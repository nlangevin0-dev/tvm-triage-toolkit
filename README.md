# TVM Triage Toolkit

Automated vulnerability management triage pipeline built in Python. Reduces noise from enterprise vulnerability scanners by filtering false positives, assessing exploitability based on network context, generating remediation tickets, tracking SLA compliance, and producing leadership reports.

## The Problem

Enterprise vulnerability scanners generate thousands of findings per cycle. Most are noise — false positives, unexploitable findings behind multiple firewalls, or low-risk issues on non-critical assets. Sending raw scan output to remediation teams creates friction and erodes trust. This pipeline automates triage so only actionable, contextualized findings reach the people who fix them.

## Pipeline Architecture

```
Tenable Scan Results
        │
        ▼
┌─────────────────────────┐
│ Step 1: FP Filter       │ ── Removes known false positives
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Step 2: Exploitability  │ ── Assesses risk via network position + CISA KEV
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Step 3: Ticket Gen      │ ── Creates tickets with fix steps + SLA deadlines
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Step 4: SLA Tracker     │ ── Monitors tickets against deadlines
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Step 5: Report          │ ── Generates HTML leadership dashboard
└─────────────────────────┘
```

## Project Structure

```
tvm-triage-toolkit/
├── README.md
├── pipeline/
│   ├── step1_fp_filter.py
│   ├── step2_exploitability.py
│   ├── step3_ticket_gen.py
│   ├── step4_sla_tracker.py
│   └── step5_report.py
├── practice/
│   ├── day1_severity_filter.py
│   ├── day2_severity_counter.py
│   ├── day3_config_checker.py
│   ├── day4_fp_filter_rebuild.py
│   ├── day5_kev_lookup.py
│   ├── day6_exploitability_rebuild.py
│   ├── day7_owner_grouping.py
│   ├── day8_ticket_gen_rebuild.py
│   ├── day11_avg_remediation.py
│   ├── csv_zone_lookup.py
│   └── sla_tracker.py
└── data/
    ├── scan_results.json
    ├── false_positives.json
    ├── network_zones.json
    ├── kev_list.json
    ├── remediation_guides.json
    ├── open_tickets.json
    ├── findings.json
    ├── findings_cves.json
    ├── findings_with_owners.json
    ├── device_configs.json
    └── ip_addresses.csv
```

## Pipeline Scripts

| Script | Input | Output | Purpose |
|--------|-------|--------|---------|
| `step1_fp_filter.py` | `scan_results.json`, `false_positives.json` | `step1_output.json` | Filters known false positives by plugin ID and device type |
| `step2_exploitability.py` | `step1_output.json`, `network_zones.json`, `kev_list.json` | `step2_output.json` | Rates exploitability (CRITICAL/HIGH/MEDIUM/LOW) using network position and CISA KEV |
| `step3_ticket_gen.py` | `step2_output.json`, `remediation_guides.json` | `step3_output.json` | Generates tickets with fix instructions, downtime flags, and SLA deadlines |
| `step4_sla_tracker.py` | `open_tickets.json` | `step4_output.json` | Classifies tickets as OVERDUE/AT RISK/ON TRACK/CLOSED and counts by owner |
| `step5_report.py` | `step4_output.json` | `report.html` | HTML dashboard with SLA compliance metrics and ticket details |

## Triage Decision Logic

### Step 1: False Positive Filtering
Matches findings against a confirmed FP database by plugin ID and device type. The FP database starts empty and grows as the operator confirms false positives during manual review.

### Step 2: Exploitability Rating
- **CRITICAL** — Internet-facing AND on CISA KEV list
- **HIGH** — Internet-facing OR on CISA KEV list
- **MEDIUM** — Internal, fewer than 2 firewalls between device and attack surface
- **LOW** — Behind 2+ firewalls, not on KEV

### Step 3: SLA Deadlines
- Critical/High exploitability: 30-day remediation SLA
- Medium exploitability: 60-day remediation SLA
- Low exploitability: 90-day remediation SLA

### Step 4: SLA Status
- **OVERDUE** — Past deadline
- **AT RISK** — Less than 7 days remaining
- **ON TRACK** — 7+ days remaining
- **CLOSED** — Remediated

## Practice Scripts

Individual scripts built during a 28-day learning program focused on security automation fundamentals. Each script reinforces a core pattern used in the pipeline: file I/O, JSON parsing, filtering, counting, datetime operations, CSV handling, and report generation.

## Compliance Mapping

| NIST Control | How This Pipeline Addresses It |
|-------------|-------------------------------|
| RA-5 (Vulnerability Scanning) | Automated triage of scan results |
| SI-2 (Flaw Remediation) | Ticket generation, SLA tracking, remediation verification |
| CM-6 (Configuration Settings) | Remediation guides enforce secure configurations |
| CM-7 (Least Functionality) | Findings flag unnecessary services |

## Usage

Run the pipeline sequentially:

```bash
cd pipeline
python3 step1_fp_filter.py
python3 step2_exploitability.py
python3 step3_ticket_gen.py
python3 step4_sla_tracker.py
python3 step5_report.py
open report.html
```

## Future Enhancements

- Tenable API integration for automated finding ingestion
- ServiceNow/Jira API integration for automated ticket creation
- CISA KEV auto-download and cross-reference
- Email delivery of HTML reports to leadership
- Slack/Teams notifications for overdue tickets
- SQLite database replacing JSON files for scalable tracking
- Automated rescanning and ticket closure on verified remediation

## Author

Nick Langevin — [github.com/nlangevin0-dev](https://github.com/nlangevin0-dev)
