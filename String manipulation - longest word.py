#Find the longest word in a string
input_string = "Python is easy to read and write. I love programming in Python"
words = input_string.split()
longest = max(words, key=len)
print("The longest word is:", longest)