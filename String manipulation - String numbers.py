#Check if a string contains only numbers.
string = input("Enter the string: ")
if string.isdigit():
    print(f"The string '{string}' contains only numbers '{string}'")
else:
    print(f"The string '{string}' doesn't contains only numbers '{string}'")