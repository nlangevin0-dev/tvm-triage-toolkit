import json

with open('data/step2_output.json', 'r') as f:
    data = json.load(f)
with open('data/remediation_guides.json', 'r') as f:
    remediation_guides = json.load(f)

for i in data:
    for j in remediation_guides:
        if i['plugin_id'] == j[str('plugin_id')]:
            print(i)