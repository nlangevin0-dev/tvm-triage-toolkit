import json

with open('../../data/scan_results.json', 'r') as f:
    data = json.load(f)

with open('../../data/false_positives.json', 'r') as f:
    false_positives = json.load(f)

results_with_fp = []
results_without_fp = []   

for result in data:
    is_fp = False
    for fp in false_positives:
        if result['plugin_id'] == fp['plugin_id'] and result['device_type'] == fp['device_type']:
            is_fp = True
    
    if is_fp:
        results_with_fp.append(result)
    else:
        results_without_fp.append(result)

with open('../../data/step1_output.json', 'w') as f:
    json.dump(results_without_fp, f, indent=4)