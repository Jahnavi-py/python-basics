#Write a program to calculate the square of a number using a function.
def square(number):
    return number ** 2
num = float(input("Enter a number: "))
result = square(num)
print(f"The square of {num} is {result}")