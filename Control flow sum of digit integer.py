# Write a program to find the sum of the digits of an integer.
number = int(input("Enter an integer: "))
digit_sum = 0
while number > 0:
    digit = number % 10
    digit_sum += digit
    number = number // 10
print(f"The sum of the digits is: {digit_sum}")
