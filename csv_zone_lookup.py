import json
import csv

with open('ip_addresses.csv') as f:
    rows = list(csv.DictReader(f))

with open('network_zones.json') as f:
    zones = json.load(f)

for row in rows:
    for zone in zones:
        if row['ip'] == zone['host']:
            print(f"IP: {row['ip']} | Hostname: {row['hostname']} | Zone: {zone['zone']} | Internet Facing: {zone['internet_facing']}")
