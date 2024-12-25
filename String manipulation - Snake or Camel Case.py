#Convert a given string to snake_case or camelCase.
import re
input_string = "This is Snake_Case"
string = re.sub(r'[-\s]+', '_', input_string).lower()
print(f"The given string '{input_string}' converted to snake case is '{string}'")
#camelCase
input_string1 = "This String is camelcase"
words = re.split(r'[-_\s]+', input_string1)
camel_case_string = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
print(f"The given string '{input_string1}' converted to camel case is '{camel_case_string}'")