import json
from collections import Counter

with open('scan_results.json') as f:
    result = json.load(f)

with open('false_positives.json') as f:
    false_positives = json.load(f)

false = []
real = []


for finding in result:
    is_fp = False
    for fp in false_positives:
        if finding['plugin_id'] == fp['plugin_id'] and finding['device_type'] == fp['device_type']:
            is_fp = True
            break
    if is_fp:
        false.append(finding)
    else:
        real.append(finding)    

with open('day4_out.json', 'w') as f:
    json.dump(real, f , indent=4)