#Create a program to recursively list all files in a directory and its subdirectories.
import os
def list_files(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
directory_to_list = r"C:\Users\jahna\PycharmProjects\PythonProject\TestFile3"
list_files(directory_to_list)