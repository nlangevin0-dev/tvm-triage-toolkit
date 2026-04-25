import json
from datetime import datetime, timedelta

with open('data/open_tickets.json') as f:
    data = json.load(f)


#overdue =     

for info in data:
    open_ticket = None
    if info['status'] =='open':
        open_ticket = len(data['status'] == 'open')
        print(open_ticket)