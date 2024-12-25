#Write a program to find the first non-repeating character in a string.
def find_non_repeating_characters(string):
    string = string.replace(" ", "").lower()
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    non_repeating = [char for char, count in char_count.items() if count == 1]
    return non_repeating
string = "Python is easy to read and write"
result = find_non_repeating_characters(string)
print(f"Non-repeating characters in '{string}': {result}")
