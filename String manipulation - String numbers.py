#Check if a string contains only numbers.
string = input("Enter the string: ")
if string.isdigit():
    print("The string contains only numbers:", string)
else:
    print("The string does not contain only numbers:", string)