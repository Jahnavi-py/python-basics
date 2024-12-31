#Extract only the alphabetic characters from a string.
string = "!!!@Python is a programming language, which is easy to read and write.!!!@"
print(f"The string : {string}")
alphabetic_char = "".join(char for char in string if char.isalpha())
print(f"Aplhabetic characters : '{alphabetic_char}'")