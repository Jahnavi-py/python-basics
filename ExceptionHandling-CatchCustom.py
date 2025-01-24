#Implement a program to catch a custom exception for invalid bank account numbers
class InvalidAccountNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
def validate_account_number(account_number):
    if len(account_number) != 10 or not account_number.isdigit():
        raise InvalidAccountNumberError("Invalid bank account number! It must be a 10-digit number.")
    else:
        print(f"Bank account number '{account_number}' is valid.")
def main():
    account_number = input("Enter the bank account number: ")
    try:
        validate_account_number(account_number)
    except InvalidAccountNumberError as e:
        print(f"Error: {e}")
main()
