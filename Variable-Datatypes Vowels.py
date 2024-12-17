#Create a Python program to count the number of vowels and consonants in a string.
Name = input("Enter a string: ")
num_vowels = 0
num_consonants = 0
vowels = "aeiouAEIOU"
for char in Name:
    if char.isalpha():
        if char in vowels:
            num_vowels += 1
        else:
            num_consonants += 1
print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")