#Create a program to check if a file exists in a directory
import os
def check_file_exists(filename, directory):
    filepath = os.path.join(directory, filename)
    return os.path.exists(filepath)
filename = "file_name.txt"
directory = "C:/Users/jahna/PycharmProjects/PythonProject/python-basics"
if check_file_exists(filename, directory):
    print(f"The file '{filename}' exists in '{directory}'.")
else:
    print(f"The file '{filename}' does not exist in '{directory}'.")
