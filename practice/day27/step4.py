import json
from datetime import datetime
from collections import Counter

with open('data/open_tickets.json') as f:
    data = json.load(f)

owner_count = Counter()

for ticket in data:
    if ticket['status'] == 'remediated':
        sla = 'CLOSED'
    else:
        deadline = datetime.strptime(ticket['deadline'], '%Y-%m-%d')
        days_remaining = (deadline - datetime.now()).days
        if days_remaining < 0:
            sla = 'OVERDUE'
        elif days_remaining < 7:
            sla = 'AT RISK'
        else:
            sla = 'ON TRACK'
    
    ticket['sla_status'] = sla
    owner_count[ticket['owner']] += 1

with open('data/step4_output.json', 'w') as f:
    json.dump(data, f, indent=4)

print(owner_count)