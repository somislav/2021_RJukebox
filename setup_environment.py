import os
import sys
import json


print("Setting up an environment")
config_path = "environment.ini"

try:
    with open(config_path, 'r') as configuration:
        env_config = json.load(configuration)

    for env_name, env_value in env_config.items():
        os.environ[env_name] = env_value
except Exception as e:
    pass

print("Adding current working directory to PYTHONPATH")
sys.path.append(os.getcwd())
