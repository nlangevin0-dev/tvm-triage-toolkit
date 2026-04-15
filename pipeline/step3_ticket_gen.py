import json
from datetime import datetime, timedelta

with open('step2_output.json', 'r') as f:
    data = json.load(f)

with open('remeditation_guides.json', 'r') as f:
    remediation = json.load(f)
    
results = []

for finding in data:
    # lookup remediation
    plugin = str(finding['plugin_id'])
    if plugin in remediation:
        fix = remediation[plugin]
    
    # set deadline
    if finding['exploitability'] in ['CRITICAL', 'HIGH']:
        deadline = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    elif finding['exploitability'] == 'MEDIUM':
        deadline = (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d")
    else:
        deadline = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")

    finding['deadline'] = deadline
    finding['fix'] = fix

    # print ticket
    print(f"\n{'='*60}")
    print(f"TICKET: {finding['hostname']} - {finding['title']}")
    print(f"Severity: {finding['exploitability']} | CVE: {finding['cve']}")
    print(f"Host: {finding['host']} | Zone: {finding['zone']}")
    print(f"Fix: {fix['fix']}")
    print(f"Downtime Required: {fix['downtime_required']}")
    print(f"Deadline: {deadline}")
    print(f"{'='*60}")

    results.append(finding)

with open('step3_output.json', 'w') as out:
        json.dump(results, out, indent=2)