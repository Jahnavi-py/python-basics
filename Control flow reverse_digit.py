# Write a program to reverse the digits of a number using a while loop.
number = int(input("Enter an integer: "))
reversed_num= 0
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10
print(f"The sum of the digits is: {reversed_num}")