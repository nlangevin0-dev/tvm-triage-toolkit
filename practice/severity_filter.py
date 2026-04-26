import json

with open('findings.json', 'r') as f:
    data = json.load(f)

for finding in data['findings']:
    sev = finding['severity']
    if sev in ("Critical", "High"): 
        print(f"[{sev}] Plugin {finding['plugin_id']} - {finding['plugin_name']}")