import json
from collections import Counter

severity_count = Counter()

with open('findings.json') as f:
    data = json.load(f)

for finding in data['findings']:
    severity_count[finding['severity']] += 1

print("Severity Counts:", severity_count)



