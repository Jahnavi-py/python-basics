#Use a dictionary to count the frequency of each word in a sentence
sentence = ("Python is easy to read, easy write and dynamic. "
            "It is versitle language. Python has in-bulit functions.")
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)