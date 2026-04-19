import random
import time
from collections import Counter

hostnames = ["fw-edge-01", "rtr-core-02", "sw-access-01", "rtr-wan-01", "sw-ot-01", "sw-dist-01", "fw-internal-01", "rtr-edge-02"]
severities = ["Critical", "Critical", "High", "High", "High", "Medium", "Medium", "Medium", "Low", "Low"]
cves = ["CVE-2024-5678", "CVE-2024-1234", "CVE-2024-9012", "CVE-2023-4455", "CVE-2024-3333", "CVE-2025-1111", "CVE-2025-2222", "N/A"]
zones = ["perimeter", "internal_core", "wan_edge", "internal_access", "ot_network", "distribution"]
plugin_ids = [10407, 42263, 65821, 55902, 78432, 91345, 88001, 77002, 33445]
fp_plugins = [10407, 42263, 65821]
kev_list = ["CVE-2024-5678", "CVE-2024-3333"]


stats = Counter()

while True:
    finding = {
        "plugin_id": random.choice(plugin_ids),
        "hostname": random.choice(hostnames),
        "severity": random.choice(severities),
        "cve": random.choice(cves),
        "zone": random.choice(zones)
    }

    # Triage
    if finding['plugin_id'] in fp_plugins:
        status = "FP FILTERED"
        stats['fp'] += 1
    elif finding['cve'] in kev_list:
        status = "KEV MATCH - CRITICAL"
        stats['kev'] += 1
    elif finding['severity'] in ['Critical', 'High']:
        status = "ACTIONABLE"
        stats['actionable'] += 1
    else:
        status = "LOW PRIORITY"
        stats['low'] += 1

    print(f"[{status}] {finding['hostname']} | {finding['severity']} | {finding['cve']} | {finding['zone']}")

    time.sleep(1)

    total = sum(stats.values())
    if total % 10 == 0:
        print(f"\n--- STATS: Total={total} | FP={stats['fp']} | KEV={stats['kev']} | Actionable={stats['actionable']} | Low={stats['low']} ---\n")