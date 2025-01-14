#Write a script to use the math module to calculate the factorial of a number
import math
def factorial(number):
    if number < 0:
        print("Factorial is not defined for negative numbers")
    else:
        return math.factorial(number)
number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")