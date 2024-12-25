#Write a program to validate an email address format.
import re
def validate_address(address):
    address_regex = r'^\d+\s[A-Za-z]+\s[A-Za-z]+(\s[A-Za-z]+)?(\s\d{5})?$'
    if re.match(address_regex, address):
        return True
    else:
        return False
address = "10102 Old Carolina Dr 28214"
if validate_address(address):
    print(f"'{address}' is a valid address.")
else:
    print(f"'{address}' is not a valid address.")
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    else:
        return False
email = "bharadwajahnavi1005@gmail.com"
if validate_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is not a valid email address.")

