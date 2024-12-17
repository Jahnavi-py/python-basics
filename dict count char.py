#Write a program to count the frequency of characters in a string using a dictionary.
string = "Hello World"
Char_frequency = {}
for char in string:
    if char in Char_frequency:
        Char_frequency[char] += 1
    else:
        Char_frequency[char] = 1
print("Character frequencies:")
for char, count in Char_frequency.items():
    print(f"'{char}': {count}")