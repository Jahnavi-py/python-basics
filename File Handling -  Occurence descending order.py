#Count the number of occurrences of each word in a file and display the results in descending order.
from collections import Counter
input_file = "file_name.txt"
with open(input_file, "r") as file:
    content = file.read()
words = content.lower().split()
word_counts = Counter(words)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print("Word Frequencies (Descending Order):")
for word, count in sorted_word_counts:
    print(f"{word}: {count}")