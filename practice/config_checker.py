import json
from collections import Counter

with open('data.json') as f:
    data = json.load(f)

for device in data:
    if device['telnet_enabled'] or device['snmp_community'] == 'public':
        print(device['hostname'])