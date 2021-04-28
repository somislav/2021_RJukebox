import json

def parse_json_config(config_path: str) -> dict:
    print(f"Parsing config file: [{config_path}]")

    try:
        with open(config_path, 'r') as configuration:
            config = json.load(configuration)

            print("--- CONFIGURATION ---")
            print(json.dumps(config, indent=4))

            return config
    except Exception as e:
        print(f"Error happened while parsing config file: {e}")
        return {}
