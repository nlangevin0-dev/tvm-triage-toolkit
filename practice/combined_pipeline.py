import json
from datetime import datetime, timedelta

def main():
    with open('data/scan_results.json') as f:
        scan_results = json.load(f)
    with open('data/false_positives.json') as f:
        false_positives = json.load(f)
    with open('data/network_zones.json') as f:
        zones = json.load(f)
    with open('data/kev_list.json') as f:
        kev_list = json.load(f)
    with open('data/remediation_guides.json') as f:
        remediation = json.load(f)

    # Step 1: Filter false positives
    real_findings = []
    for finding in scan_results:
        is_fp = False
        for fp in false_positives:
            if finding['plugin_id'] == fp['plugin_id'] and finding['device_type'] == fp['device_type']:
                is_fp = True
        if not is_fp:
            real_findings.append(finding)

    print(f"Step 1: {len(scan_results)} total findings, {len(scan_results) - len(real_findings)} false positives filtered, {len(real_findings)} real findings")

    # Step 2: Exploitability rating
    for finding in real_findings:
        zone_info = None
        for zone in zones:
            if finding['host'] == zone['host']:
                zone_info = zone
                break

        if zone_info is None:
            finding['exploitability'] = 'UNKNOWN'
            finding['zone'] = 'Unknown'
            continue

        on_kev = finding['cve'] in kev_list

        if zone_info['internet_facing'] and on_kev:
            rating = "CRITICAL"
        elif zone_info['internet_facing'] or on_kev:
            rating = "HIGH"
        elif zone_info['firewalls_between'] < 2:
            rating = "MEDIUM"
        else:
            rating = "LOW"

        finding['exploitability'] = rating
        finding['zone'] = zone_info['zone']

    print(f"Step 2: Exploitability ratings assigned")
    for f in real_findings:
        print(f"  [{f['exploitability']}] {f['hostname']} - {f['title']}")

    # Step 3: Ticket generation
    tickets = []
    for finding in real_findings:
        plugin = str(finding['plugin_id'])
        fix = remediation.get(plugin, {'fix': 'No remediation guide available', 'downtime_required': 'Unknown'})

        if finding['exploitability'] in ['CRITICAL', 'HIGH']:
            deadline = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        elif finding['exploitability'] == 'MEDIUM':
            deadline = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d')
        else:
            deadline = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')

        ticket = {
            'hostname': finding['hostname'],
            'title': finding['title'],
            'cve': finding['cve'],
            'exploitability': finding['exploitability'],
            'zone': finding['zone'],
            'fix': fix['fix'],
            'deadline': deadline
        }
        tickets.append(ticket)

    print(f"\nStep 3: {len(tickets)} tickets generated")
    for t in tickets:
        print(f"\n  {'='*50}")
        print(f"  TICKET: {t['hostname']} - {t['title']}")
        print(f"  Severity: {t['exploitability']} | CVE: {t['cve']}")
        print(f"  Zone: {t['zone']}")
        print(f"  Fix: {t['fix']}")
        print(f"  Deadline: {t['deadline']}")
        print(f"  {'='*50}")

if __name__ == "__main__":
    main()