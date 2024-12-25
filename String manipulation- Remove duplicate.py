#Remove duplicate characters from a string.
'''input_string = "aabbccddeeff"
unique_string = list(set(input_string))
print(unique_string)'''
def remove_duplicates(string):
    return ''.join(dict.fromkeys(string))
string = "aabbccddeeff"
print(f"The string is : {string} and removed duplicates from the string is : {remove_duplicates(string)}")
