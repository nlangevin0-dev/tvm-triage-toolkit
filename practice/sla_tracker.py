import json
from collections import Counter
from datetime import datetime

with open('data/open_tickets.json') as f:
    data = json.load(f)

owner_count = Counter()
today = datetime.now().date()   # Use .date() to ignore time component

print("Ticket Analysis:")
print("=" * 50)

for ticket in data:
    owner = ticket['owner']
    owner_count[owner] += 1
    
    if ticket['status'] == 'remediated':
        ticket_status = "CLOSED"
        days_remaining = None
    elif ticket['status'] == 'open':
        try:
            deadline = datetime.strptime(ticket['deadline'], "%Y-%m-%d").date()
            days_remaining = (deadline - today).days
            
            if days_remaining >= 7:
                ticket_status = "ON TRACK"
            elif days_remaining >= 0:
                ticket_status = "AT RISK"
            else:
                ticket_status = "OVERDUE"
        except (KeyError, ValueError, TypeError):
            ticket_status = "INVALID DATA"
            days_remaining = None
    else:
        ticket_status = "UNKNOWN STATUS"
        days_remaining = None

    # Print for this ticket
    days_str = f"{days_remaining} days" if days_remaining is not None else "N/A"
    print(f"Ticket Status: {ticket_status:8} | Days: {days_str:>8} | Owner: {owner}")

print("\n" + "=" * 50)
print("Owner Summary:")
for owner, count in owner_count.most_common():
    print(f"{owner}: {count} tickets")

