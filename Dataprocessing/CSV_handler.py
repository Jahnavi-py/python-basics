#Create a package data_processing with modules: .csv_handler.py: Functions to read and write CSV files.
import csv
def read_csv(filepath):
    try:
        with open(filepath, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
def write_csv(file_path, data, fieldnames):
    try:
        with open(file_path, mode="w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            print(f"Data successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")