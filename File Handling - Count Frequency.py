#Write a program to count the frequency of a specific word in a text file.
from collections import Counter
word_to_find = "python"
with open("file_name.txt", "r") as file:
    words = file.read().lower().split()
word_counts = Counter(words)
frequency = word_counts[word_to_find]
print(f"The word '{word_to_find}' appears {frequency} times in the file.")

