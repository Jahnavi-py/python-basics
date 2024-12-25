# Convert a string into a list of ASCII values of each character.
input_string = "Python Programming"
print(f"The string is : {input_string}")
ascii_values = [ord(char) for char in input_string]
print(f"The string '{input_string}' ascii value is '{ascii_values}'")