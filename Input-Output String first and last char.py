#Take a string input and display its first and last characters
string = input("Enter the string ")
if len(string) > 0:
    print("First character:", string[0])
    print("Last character:", string[-1])
else:
    print("Invalid String")
