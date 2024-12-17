#Write a program to calculate the factorial of a number using recursion.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")