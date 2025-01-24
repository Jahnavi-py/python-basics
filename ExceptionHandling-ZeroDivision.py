#Write a Python program to handle a ZeroDivisionError when dividing two numbers
def divide(a,b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
numerator = float(input("Enter the numerator:"))
denominator = float(input("Enter the Denominator"))
divide(numerator, denominator)