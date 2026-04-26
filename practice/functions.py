# Test data for check_login and process_events
events = [
    {"username": "root", "source_ip": "10.0.0.1", "failed_count": 1},
    {"username": "admin", "source_ip": "10.0.0.5", "failed_count": 3},
    {"username": "admin", "source_ip": "10.0.0.1", "failed_count": 25},
    {"username": "jsmith", "source_ip": "203.0.113.47", "failed_count": 2},
    {"username": "deploy", "source_ip": "10.0.1.1", "failed_count": 1},
]

# Test data for classify_device_risk
devices = [
    {"hostname": "fw-edge-01", "device_type": "firewall", "zone": "perimeter", "internet_facing": True},
    {"hostname": "rtr-wan-01", "device_type": "router", "zone": "wan_edge", "internet_facing": True},
    {"hostname": "sw-ot-01", "device_type": "switch", "zone": "ot_network", "internet_facing": False},
    {"hostname": "sw-core-01", "device_type": "switch", "zone": "internal_core", "internet_facing": False},
    {"hostname": "fw-internal-01", "device_type": "firewall", "zone": "internal_core", "internet_facing": False},
]


def check_login(username, source_ip, failed_count):
    if username == "root":
        severity = "CRITICAL"
    elif failed_count > 10:
        severity = "HIGH"
    elif source_ip.startswith("203."):
        severity = "MEDIUM"
    else:
        severity = "LOW"
    return severity

def process_events(events):
    alerts = []
    for event in events:
        severity = check_login(event['username'], event['source_ip'], event['failed_count'])
        if severity != "LOW":
            alerts.append(event)
    return alerts

def classify_device_risk(hostname, device_type, zone, internet_facing):
    if internet_facing and device_type == "firewall":
        risk_level = "CRITICAL"
    elif internet_facing:
        risk_level = "HIGH"
    elif zone == "ot_network":
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    return risk_level

for event in events:
    print(check_login(event['username'], event['source_ip'], event['failed_count']))

results = process_events(events)
print(f"\n{len(results)} alerts found")

for device in devices:
    print(classify_device_risk(device['hostname'], device['device_type'], device['zone'], device['internet_facing']))