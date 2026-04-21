import json

def main():
    try:
        with open('data/baseline_configs.json', 'r') as f:
            baseline_configs = json.load(f)
        
        with open('data/actual_configs.json', 'r') as f:
            actual_configs = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    for hostname in baseline_configs:
            baseline = baseline_configs[hostname]
            actual = actual_configs[hostname]
            if baseline == actual:
               print(f"[OK] {hostname}")
            else:
                for setting in baseline:
                    if baseline[setting] != actual[setting]:
                        print(f"[DRIFT] {hostname} - {setting}: expected {baseline[setting]}, found {actual[setting]}")

if __name__ == "__main__":
    main()