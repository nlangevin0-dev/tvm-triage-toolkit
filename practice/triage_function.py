import json

with open('data/network_zones.json') as f:
    zones = json.load(f)
with open('data/kev_list.json') as f:
    kev_list = json.load(f)

test_findings = [
    {"host": "10.0.3.1", "hostname": "fw-edge-01", "cve": "CVE-2024-5678", "severity": "Critical"},
    {"host": "10.0.1.2", "hostname": "rtr-core-02", "cve": "CVE-2024-1234", "severity": "Critical"},
    {"host": "10.0.5.1", "hostname": "rtr-wan-01", "cve": "CVE-2024-9012", "severity": "High"},
    {"host": "10.0.2.1", "hostname": "sw-access-01", "cve": "CVE-2024-3333", "severity": "Medium"},
    {"host": "10.0.4.1", "hostname": "sw-ot-01", "cve": "CVE-2023-4455", "severity": "Low"}
]

def triage_finding(finding, zones, kev_list):
    zone_info = None
    for zone in zones:
        if finding['host'] == zone['host']:
            zone_info = zone
    if zone_info is None:
        return {"rating": "UNKNOWN", "zone": "Unknown", "kev": False}
    on_kev = finding['cve'] in kev_list
    if zone_info['internet_facing'] and on_kev:
        rating = "CRITICAL"
    elif zone_info['internet_facing'] or on_kev:
        rating = "HIGH"
    elif zone_info['firewalls_between'] < 2:
        rating = "MEDIUM"
    else:
        rating = "LOW"
    return {"rating": rating, "zone": zone_info['zone'], "kev": on_kev}

for finding in test_findings:
    result = triage_finding(finding, zones, kev_list)
    print(f"{finding['hostname']}: {result}")