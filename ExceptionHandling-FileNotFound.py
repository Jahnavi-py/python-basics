#Write a Python program to open a file, handle the FileNotFoundError, and display an appropriate message if the file does not exist.
def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"File '{file_name}' opened successfully.")
            content = file.read()
            print("File contents:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found!")
file_name = input("Enter the file name to open: ")
open_file(file_name)