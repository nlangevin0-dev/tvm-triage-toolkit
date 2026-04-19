import json

try:
    with open('data/firewall_rules.json', 'r') as f:
        firewall_rules = json.load(f)
except FileNotFoundError:
    print("Firewall rules file not found. Starting with an empty list.")

rules_to_remove = []

for rule in firewall_rules:
    if rule['source'] == '0.0.0.0/0' and rule['port'] in [22, 23, 3389]:
        rules_to_remove.append(rule)
        print(f"[CRITICAL] Rule {rule['rule_id']} - {rule['source']} -> {rule['destination']} port {rule['port']} OPEN TO INTERNET")
print(f"Broken rules: {len(rules_to_remove)}")