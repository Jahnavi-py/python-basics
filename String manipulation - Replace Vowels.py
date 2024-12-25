#Replace all vowels in a string with a specific character
string = "Python Programming"
vowels = "aeiouAEIOU"
for vowel in vowels:
    string = string.replace("o","*")
print(string)