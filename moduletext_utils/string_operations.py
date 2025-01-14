#Create a package text_utils with the following modules:
#.string_operations.py: Functions to count vowels and reverse a string.
#.file_operations.py: Functions to read and write to a file.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
def reverse_string(s):
    return s[::-1]