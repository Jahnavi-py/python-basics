#Replace all vowels in a string with a specific character
my_string = "Python Programming"
print(f"The string is '{my_string}'")
vowels = "aeiouAEIOU"
for vowel in vowels:
    replaced_string = my_string.replace("o","*")
print(f"Replaced vowel with '{replaced_string}'")