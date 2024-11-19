#A program that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
'''a = int(input("Enter the number for a :"))
b = int(input("Enter the number for b :"))
addition  = a + b
subtraction = a - b
multiplication = a * b
print ("Enter a number to arithemetic operation for sum : ", addition)
print("Enter a number to arithemetic operation for sub : ", subtraction)
print("Enter a number to arithemetic operation for multiply : ", multiplication)
def add(a, b):
    print("The addition of two numbers is:", a + b)

def subtract(a, b):
    print("The subtraction of two numbers is:", a - b)

def multiply(a, b):
    print("The multiplication of two numbers is:", a * b)

def divide(a, b):
    if b != 0:
        print("The division of two numbers is:", a / b)
    else:
        print("Division by zero is not allowed!")

print("Welcome to the basic arithmetic operations program!")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

if operation == "add":
    add(a, b)
elif operation == "subtract":
    subtract(a, b)
elif operation == "multiply":
    multiply(a, b)
elif operation == "divide":
    divide(a, b)
else:
    print("Invalid operation selected!")'''
a = int(input("Enter the number for a : "))
b = int(input("Enter the number for b : "))
def sum(a,b):
        add = a + b
        print("The addition for two numbers is : ", add)
sum (a,b)
def sub(a,b):
        subtract = a - b
        print("The subtraction for two numbers is : ", subtract)
sub(a,b)
def mul(a,b):
        multiply = a * b
        print("The multiplication for two numbers is : ", multiply)
mul(a,b)
def divide(a,b):
        divide = a % b
        print("The division of two numbers is :", divide)
divide(a,b)
