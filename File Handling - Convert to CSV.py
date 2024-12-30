#Write a program to read and parse a CSV file and convert it to JSON format.
import csv
import json
csv_file = "File.csv"
json_file = "File.json"
data = [
    ["Name", "Age", "City"],  # Header row
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "Chicago"]
]
try:
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"CSV file '{csv_file}' written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
try:
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    with open(json_file, "w") as file:
        json.dump(data, file, indent = 4)
    print(f"CSV data has been converted to JSON and saved to '{json_file}'.")
except FileNotFoundError:
    print(f"Error: The file '{csv_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")