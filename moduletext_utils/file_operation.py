#Create a package text_utils with the following modules:
#.string_operations.py: Functions to count vowels and reverse a string.
#.file_operations.py: Functions to read and write to a file.
def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()