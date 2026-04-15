import json
from datetime import datetime, timedelta

results = []

with open("step2_output.json", "r") as f:
    data = json.load(f) 

with open('remediation_guides.json', 'r') as f:
    rem = json.load(f)


for item in data:   
    plugin = str(item['plugin_id'])
    if plugin in rem:
        fix = rem[plugin]
    if item['exploitability'] in ["CRITICAL", "HIGH"]:
        deadline = (datetime.now() + timedelta(days = 30)).strftime("%Y-%m-%d")
    elif item['exploitability'] == "MEDIUM":
        deadline = (datetime.now() + timedelta(days = 60)).strftime("%Y-%m-%d")
    else:
        deadline = (datetime.now() + timedelta(days = 90)).strftime("%Y-%m-%d")
    results.append(f"Plugin ID: {plugin}\nHostname: {item['hostname']}\nSeverity: {item['exploitability']}\nDeadline: {deadline}\nFix: {fix['fix']}\n")
    print(f"Plugin ID: {plugin}\nHostname: {item['hostname']}\nSeverity: {item['exploitability']}\nDeadline: {deadline}\nRemediation Guide: {fix}\n")
    
with open('step3_output.json', 'w') as f:
    json.dump(results, f, indent=4)