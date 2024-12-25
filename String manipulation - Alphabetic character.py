#Extract only the alphabetic characters from a string.
string = "!!!@Python is a programming language, which is easy to read and write.!!!@"
print(f"The string is : {string}")
alphabetic_char = "".join(char for char in string if char.isalpha())
print(f"The string '{string}' Aplhabetic characters is : '{alphabetic_char}'")