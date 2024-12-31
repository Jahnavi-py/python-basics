#Write a program to merge multiple CSV files into a single CSV file.
import os
import csv
def merge_csv_files(input_directory, output_file):
    try:
        # Verify the input directory exists
        if not os.path.exists(input_directory):
            print(f"Error: The directory '{input_directory}' does not exist.")
            return

        # List all CSV files in the directory
        csv_files = [file for file in os.listdir(input_directory) if file.endswith(".csv")]
        if not csv_files:
            print("No CSV files found in the specified directory.")
            return

        print(f"Merging {len(csv_files)} files...")

        # Open the output file for writing
        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = None  # CSV writer object

            # Iterate over all CSV files
            for file in csv_files:
                file_path = os.path.join(input_directory, file)
                with open(file_path, "r", encoding="utf-8") as infile:
                    reader = csv.reader(infile)
                    headers = next(reader, None)  # Get headers from the first row

                    # Write headers only once
                    if writer is None:
                        writer = csv.writer(outfile)
                        if headers:
                            writer.writerow(headers)

                    # Write the remaining rows
                    for row in reader:
                        writer.writerow(row)

        print(f"Files merged successfully into '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Directory containing the input CSV files
input_directory = r"C:\Users\jahna\PycharmProjects\PythonProject\python-basics"

# Path to save the merged output file
output_file = r"C:\Users\jahna\PycharmProjects\PythonProject\python-basics\file_merged.csv"

merge_csv_files(input_directory, output_file)