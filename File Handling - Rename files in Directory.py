#Implement a program to rename all files in a directory based on a specific pattern (e.g., add a timestamp).
import os
from datetime import datetime
def rename_file_directory(directory, pattern="%Y%m%d_%H%M%S"):
    try:
        if not os.path.exists(directory):
            print(f"Error: The directory '{directory}' does not exist.")
            return
        timestamp = datetime.now().strftime(pattern)
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                name, ext = os.path.splitext(filename)
                new_name = f"{name}_{timestamp}{ext}"
                new_path = os.path.join(directory, new_name)
                os.rename(file_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_name}'")
        print("Renaming completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
directory_to_rename = r"C:\Users\jahna\PycharmProjects\first_lecture"
rename_file_directory(directory_to_rename)
