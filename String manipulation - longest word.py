#Find the longest word in a string
input_string = "Python is easy to read and write. I love programming in Python"
words = input_string.split()
longest = max(words, key=len)
print(f"The string '{input_string}' longest word is '{longest}'")
