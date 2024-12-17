#Write a program to print the ASCII value of a given character. AMERICAN STANDARAD CODE FOR INFORMATION INTERCHANGE
char = input("Enter a character: ")
if len(char)==1:
    print(ord(char))
else:
    print("Please enter only a single character.")