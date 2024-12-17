#Write a function that takes two numbers as input and returns their greatest common divisor (GCD).
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input("Enter the number1 : "))
b = int(input("Enter the number2 : "))
print(f"The GCD of two numbers is {gcd(a, b)}")