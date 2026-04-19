import json

try:
    with open("data/cisco.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found.")

misconfig = []

for info in data:
    if info['http_server'] == True:
        misconfig.append(info['hostname'])

print(f"\n{len(misconfig)} devices with HTTP server enabled")

with open("data/misconfig.json", "w") as f:
    json.dump(misconfig, f, indent=4)