#Replace all vowels in a string with a specific character
string = "Python Programming"
print(f"The string is '{string}'")
vowels = "aeiouAEIOU"
for vowel in vowels:
    string = string.replace("o","*")
print(f"Replaced vowel with '{string}'")