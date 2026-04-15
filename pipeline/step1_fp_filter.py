import json
from collections import Counter


with open('false_positives.json') as f:
    fp = json.load(f)

with open('scan_results.json') as f:
    data = json.load(f)

real_findings = []
false_positives_found = []




for finding in data:
    is_fp = False
    for fp_entry in fp:
        if finding['plugin_id'] == fp_entry['plugin_id'] and finding['device_type'] == fp_entry['device_type']:
            is_fp = True
    
    if is_fp:
        false_positives_found.append(finding)
    else:
        real_findings.append(finding)

print(f"\n=== Triage Step 1: False Positive Filter ===")
print(f"Total findings: {len(data)}")
print(f"False positives filtered: {len(false_positives_found)}")
print(f"Real findings remaining: {len(real_findings)}")

print(f"\nFiltered FPs:")
for fp_item in false_positives_found:
    print(f"  [FP] {fp_item['hostname']} - {fp_item['title']} (Reason: known FP for {fp_item['device_type']})")

print(f"\nReal findings passed to Step 2:")
for real in real_findings:
    print(f"  [{real['severity']}] {real['hostname']} - {real['title']}")

with open('step1_output.json', 'w') as out:
    json.dump(real_findings, out, indent=2)