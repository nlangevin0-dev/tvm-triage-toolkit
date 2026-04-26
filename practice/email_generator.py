import json
from datetime import datetime, timedelta

today = datetime.now().strftime("%Y-%m-%d")
sla = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
def main():
    try:
        with open('data/step2_output.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: 'data/step2_output.json' not found.")
        return
    
    for item in data:
       if item['severity'] == 'Critical':
            print(f"\n{'='*60}")
            print(f"To: Network Device Owner")
            print(f"Subject: [CRITICAL] {item['title']} on {item['hostname']}")
            print(f"Date: {today}")
            print(f"{'='*60}")
            print(f"\nA critical vulnerability has been identified:")
            print(f"\n  Host: {item['hostname']} ({item['host']})")
            print(f"  CVE: {item['cve']}")
            print(f"  Exploitability: {item['exploitability']}")
            print(f"  Zone: {item.get('zone', 'Unknown')}")
            print(f"\n  SLA Deadline: {sla}")
            print(f"\nPlease remediate by the deadline above.")
            print(f"{'='*60}")
if __name__ == "__main__":
    main()