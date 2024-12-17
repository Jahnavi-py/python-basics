#Create a function to check if a number is an Armstrong number.
def armstrong_number(number):
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number
num = int(input("Enter a number: "))
if armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")