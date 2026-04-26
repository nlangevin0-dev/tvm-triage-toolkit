import json

with open('data/step_1-output.json', 'r') as f:
    data = json.load(f)
with open('data/network_zones.json', 'r') as f:
    network_zones = json.load(f)
with open('data/kev_list.json', 'r') as f:
    kev_list = json.load(f)

output = []

for info in data:
    zone_info = None
    for zone in network_zones:
        if info['host'] == zone['host']:
            zone_info = zone
            break
        if zone_info is None:
            continue

    on_kev = info['cve'] in kev_list

    if zone_info['internet_facing'] and on_kev:
        rating = "CRITICAL"
    elif zone_info['internet_facing'] or on_kev:
        rating = "HIGH"
    elif zone_info['firewalls_between'] < 2:
        rating = "MEDIUM"
    else:
        rating = "LOW"

    info['exploitability'] = rating
    output.append(info)

with open('data/step2_output.json', 'w') as f:
    json.dump(output, f, indent=4)