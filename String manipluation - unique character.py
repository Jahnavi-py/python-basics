#Check if a string contains only unique characters.
'''string = "Python is easy to read and write"
if string.find("a"):
    print(f"{string} : unique character exists.")
else:
    print("Unique character does not exists.")'''
string = "Python is easy to read and write"
string = string.replace(" ", "").lower()
if len(set(string)) == len(string):
    print(f"The string '{string}' contains only unique characters.")
else:
    print(f"The string '{string}' does not contain only unique characters.")
string1 = "Flower"
string1 = string1.replace(" ", "").lower()
if len(set(string1)) == len(string1):
    print(f"The string1 '{string1}' contains only unique characters.")
else:
    print(f"The string1 '{string1}' does not contain only unique characters.")