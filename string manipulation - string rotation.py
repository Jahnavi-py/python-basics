#Check if one string is a rotation of another string.
def string_rotation(string1, string2):
    if len(string1) != len(string2) or not string1 or not string2:
        return False
    return string2 in string1 + string2
string1 = "abcd"
string2 = "dabc"
result = string_rotation(string1, string2)
print(f"Is string2 '{string2}' rotation of string1 '{string1}'? '{result}'")