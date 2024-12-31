#Creating csv file
import csv
def create_csv_file(file_name, data):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"Created file: {file_name}")
data_file1 = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"]
]
data_file2 = [
    ["Name", "Age", "City"],
    ["Charlie", "35", "Chicago"],
    ["Diana", "28", "Houston"]
]
file1 = "file1.csv"
file2 = "file2.csv"
create_csv_file(file1, data_file1)
create_csv_file(file2, data_file2)