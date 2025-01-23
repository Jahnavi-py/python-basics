#.json_handler.py: Functions to parse and write JSON files.
import json
def read_json(file_path):
    try:
        with open(file_path, mode="r") as jsonfile:
            return json.load(jsonfile)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}
def write_json(file_path, data):
    try:
        with open(file_path, mode="w") as jsonfile:
            json.dump(data, jsonfile, indent=4)
            print(f"Data successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")
