import json

with open('data/kev_list.json') as f:
    kev_list = json.load(f)
with open('data/false_positives.json') as f:
    false_positives = json.load(f)
with open('data/findings_20.json') as f:
    findings = json.load(f)

noise = []
actionable = []

for item in findings:
    is_fp = False
    for fp in false_positives:
        if item['plugin_id'] == fp['plugin_id'] and item['device_type'] == fp['device_type']:
            is_fp = True
    if is_fp:
        noise.append(item)
    else:
        if item['severity'] == 'Critical' or item['internet_facing'] or item['cve'] in kev_list:
            actionable.append(item)
        else:
            noise.append(item)

with open('data/actionable.json', 'w') as f:
    json.dump(actionable, f, indent=4)
with open('data/noise.json', 'w') as f:
    json.dump(noise, f, indent=4)

print(f"Total: {len(findings)}")
print(f"Actionable: {len(actionable)}")
print(f"Noise: {len(noise)}")