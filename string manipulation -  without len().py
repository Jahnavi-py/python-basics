#Write a function to find the length of a string without using len().
def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count

string = "Python is easy to read and write."
print(f"The length of the string is: '{string_length(string)}'")