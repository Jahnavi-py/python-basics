#Write a program to find the factorial of a number using a loop.
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")
