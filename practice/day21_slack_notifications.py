import json
from datetime import datetime

def main():
    try:
        with open('data/open_tickets.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: 'data/open_tickets.json' not found.")
        return
    
    current_time = datetime.now().strftime("%Y-%m-%d")
    #deadline = datetime.strptime(['deadline'], '%Y-%m-%d')

    for i in data:
        deadline = datetime.strptime(i['deadline'], '%Y-%m-%d')
        days_overdue = (datetime.now() - deadline).days
        if days_overdue > 0 and i['status'] == 'open':
            print(f"Overdue: {i['ticket_id']} - {i['hostname']}")
            print(f"Owner: {i['owner']}")
            print(f"Days Overdue: {days_overdue}")
            print(f"Original Deadline: {i['deadline']}")


if __name__ == "__main__":
    main()

