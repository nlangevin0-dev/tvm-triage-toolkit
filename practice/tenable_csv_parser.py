import csv
from collections import Counter

risk_count = Counter()

with open('data/tenable_export.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

risk_count = Counter()
for row in rows:
    risk_count[row['Risk']] += 1

print(f"Critical: {risk_count['Critical']}")
print(f"High: {risk_count['High']}")
print(f"Medium: {risk_count['Medium']}")
print(f"Low: {risk_count['Low']}")


for row in rows:
    if row['Risk'] in ['Critical', 'High']:
        print(f"[{row['Risk']}] {row['Host']} - {row['Name']} | CVE: {row['CVE']} | VPR: {row['VPR']} | Fix: {row['Solution']}")