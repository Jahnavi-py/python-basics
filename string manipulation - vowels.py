#Count the number of vowels in a string.
def vowels_and_consonants(n):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    for char in n:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count
string = "Python is easy to read and write."
vowels, consonants = vowels_and_consonants(string)
print(f" For string '{string}' vowels count is : {vowels}, Consonants count is : {consonants}")