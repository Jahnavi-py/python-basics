text = input("Enter a sentence")
vowels = "aeiouAEIOU"
vowels_count = 0
constant_count = 0
for char in text:
    if char in vowels:
        vowels_count +=1
    elif char.isalpha():
        constant_count += 1
print("Vowels", vowels_count)
print("constant", constant_count)
