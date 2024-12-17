#Use a while loop to reverse a given number.
num = 12345
reversed_number = 0
while num > 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10
print(f"Reversed number: {reversed_number}")