import json
from collections import Counter
fail_count = Counter()

with open('data/switch_configs.json', 'r') as f:
    switch_configs = json.load(f)

for config in switch_configs:
    failures = []
    if config['http_server']:
        failures.append("HTTP server enabled")
    if config['ssh_version'] == 1:
        failures.append("SSH version 1")
    if config['telnet']:
        failures.append("Telnet enabled")
    if config['snmp_version'] in ['v1', 'v2c']:
        failures.append("SNMP not v3")
    if not config['banner']:
        failures.append("No login banner")
    if not config['ntp_configured']:
        failures.append("NTP not configured")
    
    for f in failures:
        print(f"[FAIL] {config['hostname']} - {f}")
        fail_count[f] += 1
        print(fail_count)
        
with open('data/switch_configs_output.json', 'w') as f:
    json.dump(failures, f, indent=4)