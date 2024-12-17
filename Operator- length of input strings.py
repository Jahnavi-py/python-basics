#Write a program to compare the lengths of two input strings.
string1 = "Jahnavi"
string2 = "Janu"
if len(string1) > len(string2):
    print(f"The length of string1 : {string1} is longer than the string2 : {string2}.")
elif len(string1) < len(string2):
    print(f"The length of string1 : {string1} is short than the string2 {string2}")
else:
    print("The string is Invalid")