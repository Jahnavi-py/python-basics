#Use the os module to navigate directories and list all .txt files in a directory
import os
def list_txt_files(directory):
    try:
        files = os.listdir(directory)
        txt_files = [file for file in files if file.endswith('.txt')]
        return txt_files
    except FileNotFoundError:
        return f"Error: The directory '{directory}' does not exist."
    except PermissionError:
        return f"Error: Permission denied to access '{directory}'."
directory = "C:/Users/jahna/PycharmProjects/PythonProject/python-basics"
txt_files = list_txt_files(directory)
if isinstance(txt_files, list):
    print(f".txt files in '{directory}':")
    for txt_file in txt_files:
        print(txt_file)
else:
    print(txt_files)
