import json
from datetime import datetime, timedelta
from collections import Counter

owner_count = Counter()
owner_overdue = Counter()

with open('../data/open_tickets.json', 'r') as f:
    data = json.load(f)

for ticket in data:
    if ticket['status'] == 'remediated':
        sla = 'CLOSED'
    else:
        deadline = datetime.strptime(ticket['deadline'], "%Y-%m-%d")
        days_remaining = (deadline - datetime.now()).days
        if days_remaining < 0:
            sla = 'OVERDUE'
        elif days_remaining < 7:
            sla = 'AT RISK'
        else:
            sla = 'ON TRACK'
    owner = ticket.get('owner', 'Unknown')
    owner_count[owner] += 1
    if sla == 'OVERDUE':
        owner_overdue[owner] += 1
    ticket['sla_status'] = sla
    if sla != 'CLOSED':
        ticket['days_remaining'] = days_remaining
    print(f"[{sla}] {ticket['ticket_id']} - {ticket['hostname']} - {ticket['title']} | Owner: {owner}")

print(f"\nTotal: {len(data)} tickets")
print(f"Overdue: {sum(owner_overdue.values())}")
print(f"Open: {len([t for t in data if t.get('sla_status') != 'CLOSED'])}")
print(f"Closed: {len([t for t in data if t.get('sla_status') == 'CLOSED'])}")

with open('../data/step4_output.json', 'w') as out:
    json.dump(data, out, indent=2)