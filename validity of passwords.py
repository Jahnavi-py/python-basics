import re
def validate(password):
    if len (password) < 6:
        print("Password must atleast be min 6 and max 16 characters long.")
    elif not re.search("[A-z]", password):
        print("Password must contain atleast one upper case.")
    elif not re.search("[a-z]", password):
        print("Password must contain atleast one smaller case")
    elif not re.search("[0-9]", password):
        print("Password must contain atleast one number")
    elif not re.search("[$#@]", password):
        print("Password must contain a special symbol")
    else:
        print("Password valid!")
password = input("Enter password : ")
print(validate(password))