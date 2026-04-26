import json
from datetime import datetime, timedelta

with open('data/step2_output.json', 'r') as f:
    data = json.load(f)
with open('data/remediation_guides.json', 'r') as f:
    remediation_guides = json.load(f)

results = []

for finding in data:
    plugin = str(finding['plugin_id'])
    if plugin in remediation_guides:
        guide = remediation_guides[plugin]
    
    if finding['exploitability'] in ['CRITICAL', 'HIGH']:
        deadline = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
    elif finding['exploitability'] == 'MEDIUM':
        deadline = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d')
    else:
        deadline = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')
    
    finding['deadline'] = deadline
    finding['fix'] = guide['fix']
    results.append(finding)

with open('data/step3_output.json', 'w') as f:
    json.dump(results, f, indent=4)