#Write a function that takes a string and counts the vowels and consonants.
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
string = input("Enter the String :")
vowels, consonants = vowels_and_consonants(string)
print(f" for string {string} vowels count is : {vowels}, Consonants count is : {consonants}")