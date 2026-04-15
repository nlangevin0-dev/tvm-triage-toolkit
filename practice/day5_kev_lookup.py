import json

with open('findings_cves.json', 'r') as f:
    data = json.load(f)

with open('kev_list.json', 'r') as f:
    kev_data = json.load(f)

is_real = []

for finding in data:
    if finding['cve'] in kev_data:
        is_real.append(finding)
        print(f"True Finding", finding['hostname'], finding['cve'], finding['severity'])


with open('day5_output.json', 'w') as f:
    json.dump(is_real, f, indent=4)