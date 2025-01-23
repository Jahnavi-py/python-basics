#Create a package data_processing with modules:
#.csv_handler.py: Functions to read and write CSV files.
#.json_handler.py: Functions to parse and write JSON files.
#.data_cleaner.py: Functions to remove duplicates and handle missing values.
from Dataprocessing.CSV_handler import read_csv, write_csv
from Dataprocessing.JSON_handler import read_json, write_json
from Dataprocessing.data_cleaner import remove_duplicates, handle_missing_values


def main():
    # CSV Example
    csv_file = "example.csv"
    csv_data = [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": None, "City": "San Francisco"},
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Charlie", "Age": 35, "City": None}
    ]

    # Write to CSV
    write_csv(csv_file, csv_data, fieldnames=["Name", "Age", "City"])
    print("CSV Read:", read_csv(csv_file))

    # JSON Example
    json_file = "example.json"
    json_data = {"Name": "Charlie", "Age": 35, "City": "Los Angeles"}

    # Write to JSON
    write_json(json_file, json_data)
    print("JSON Read:", read_json(json_file))

    # Data Cleaning Example
    print("\nOriginal Data:", csv_data)

    # Remove Duplicates
    deduplicated_data = remove_duplicates(csv_data)
    print("\nData after removing duplicates:", deduplicated_data)

    # Handle Missing Values
    filled_data = handle_missing_values(deduplicated_data, fill_value="Unknown")
    print("\nData after handling missing values (fill_value='Unknown'):", filled_data)

    numeric_filled_data = handle_missing_values(deduplicated_data, method="mean")
    print("\nData after handling missing values (method='mean'):", numeric_filled_data)

if __name__ == "__main__":
    main()
