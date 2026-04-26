import json

with open('data/scan_results.json') as f:
    scan_results = json.load(f)
with open('data/false_positives.json') as f:
    false_positives = json.load(f)

real = []
fp = []

for data in scan_results:
    is_fp = False
    for i in false_positives:
        if data['plugin_id'] == i ['plugin_id']:
            is_fp = True
            break
    if not is_fp:
        real.append(data)
    else:
        fp.append(data)

with open('data/step_1-output.json', 'w') as f:
    json.dump(real, f, indent=4)

