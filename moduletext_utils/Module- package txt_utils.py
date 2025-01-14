#Create a package text_utils with the following modules:
#.string_operations.py: Functions to count vowels and reverse a string.
#.file_operations.py: Functions to read and write to a file.
from moduletext_utils import string_operations, file_operation
string =  "Welcome to Python Programming"
print(f"Original String: {string}")
print(f"Reversed String: {string_operations.reverse_string(string)}")
print(f"Vowel Count: {string_operations.count_vowels(string)}")
filename = "modulesample.txt"
content = "Welcome to Python Programming."
file_operation.write_file(filename, content)
print(f"Content of '{filename}': {file_operation.read_file(filename)}")