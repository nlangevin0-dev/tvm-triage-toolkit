import json
from collections import Counter

with open('fidnings_with_owners.json') as f:
    data = json.load(f)

owners = Counter()

for finding in data:
    owner = finding['owner']
    if owner:
        owners[owner] += 1

print("Owners and their finding counts:")
for owner, count in owners.items():
    print(f"{owner}: {count}")