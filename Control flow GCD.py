#Write a program to find the GCD of two numbers using loops.
num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
while num2 != 0:
    num1,num2 = num2, num1 % num2
print(f"The GCD of the two numbers is: {num1}")