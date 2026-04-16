import csv
import re
from collections import Counter

failed = Counter()

with open('../data/auth.log', 'r') as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r'from (\S+)', line)
            if match:
                ip = match.group(1)
                failed[ip] += 1

with open('failed_logins.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ip', 'count', 'flagged'])
    for ip, count in failed.items():
        flagged = 'yes' if count > 10 else 'no'
        writer.writerow([ip, count, flagged])