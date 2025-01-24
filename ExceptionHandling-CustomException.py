#Create a custom exception class InvalidAgeError and write a program to validate user age input.
class InvalidAgeError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
def validate_age(age):
    if age <= 0:
        raise InvalidAgeError("Age cannot be zero or negative!")
    else:
        print(f"The age {age} is valid.")
try:
    user_age = int(input("Enter your age: "))  # Taking user input for age
    validate_age(user_age)
except InvalidAgeError as e:
    print(f"Custom Exception Caught: {e}")
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")