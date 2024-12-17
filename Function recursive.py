#Write a program with a recursive function to calculate the sum of digits of a number.
def sum_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_digits(number // 10)
number = int(input("Enter a number: "))
result = sum_digits(number)
print(f"The sum of the digits of {number} is {result}.")
