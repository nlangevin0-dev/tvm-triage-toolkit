import json
from datetime import datetime, timedelta
from collections import Counter

# Load the open tickets data from the JSON file
with open('data/open_tickets.json') as f:
    data = json.load(f)

# Get today's date and the SLA date (30 days from now)
today = datetime.now().strftime('%Y-%m-%d')
sla = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

# Initialize counters for open and closed tickets
total_open_tickets = 0
total_closed = Counter()
overdue_tickets = []

# Process each ticket to calculate statistics
for info in data:
    if info['status'] == 'open':
        total_open_tickets += 1
    elif info['status'] == 'remediated':
        total_closed[info['ticket_id']] += 1

    # Convert today and deadline to datetime objects
    today_date = datetime.strptime(today, '%Y-%m-%d')
    deadline_date = datetime.strptime(info['deadline'], '%Y-%m-%d')

    # Check if the ticket is overdue
    if today_date > deadline_date:
        overdue_tickets.append(info['ticket_id'])

# Calculate SLA compliance percentage
total_tickets = len(data)
on_track = total_open_tickets
closed = len(total_closed)
sla_compliance_percentage = ((on_track + closed) / total_tickets) * 100

# Find the top 3 most urgent tickets (most days overdue)
# Calculate days overdue for each ticket
overdue_days = []
for info in data:
    if today_date > datetime.strptime(info['deadline'], '%Y-%m-%d'):
        days_overdue = (today_date - datetime.strptime(info['deadline'], '%Y-%m-%d')).days
        overdue_days.append((info['ticket_id'], days_overdue))

# Sort by days overdue (descending)
overdue_days.sort(key=lambda x: x[1], reverse=True)
top_urgent_tickets = [ticket_id for ticket_id, days in overdue_days[:3]]

# Generate the weekly email summary
email_summary = f"""
Subject: Weekly Email Summary - {today}

Dear Team,

Here is the weekly email summary for {today}:

- Total open tickets: {on_track}
- Overdue tickets: {len(overdue_tickets)}
- SLA compliance percentage: {sla_compliance_percentage:.2f}%
- Top 3 most urgent tickets: {', '.join(top_urgent_tickets)}

Best regards,
Your Team
"""

# Print the email summary
print(email_summary)