import json
from datetime import datetime


with open('data/open_tickets.json', 'r') as f:
    data = json.load(f)

remediation_days = []

for line in data:
    if line['status'] == 'remediated':
        created_at = datetime.strptime(line['opened'], '%Y-%m-%d')
        deadline = datetime.strptime(line['deadline'], '%Y-%m-%d')
        days_to_fix = (deadline - created_at).days
        remediation_days.append(days_to_fix)

average = sum(remediation_days) / len(remediation_days)
print(f"Average remediation time: {average} days")