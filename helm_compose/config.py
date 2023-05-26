import json
import yaml


def load_config(file_path: str) -> dict:
    """
    Load and parse the configuration file.
    """
    try:
        with open(file_path, 'r') as file:
            if file_path.endswith('.json'):
                return json.load(file)
            elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Configuration file {file_path} not found.")
    except Exception as e:
        print(f"Error while loading configuration file: {e}")
