import json

try:
    with open('data/device_firmware.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found.")

try:
    with open('data/vulnerable_firmware.json', 'r') as f:
        vulnerable = json.load(f)
except FileNotFoundError:
    print("File not found.")

firmware_list = []

for info in data:
    for vuln in vulnerable:
        if info['vendor'] == vuln['vendor'] and info['model'] == vuln['model'] and info['firmware'] == vuln['firmware']:
            firmware_list.append(info['hostname'])
            print(f"[{vuln['severity']}] {info['hostname']} - {vuln['cve']} - {info['vendor']} {info['model']} firmware {info['firmware']}")
with open('data/vulnerable_devices.json', 'w') as f:
    json.dump(firmware_list, f, indent=4)