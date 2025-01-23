#Create a package for basic arithmetic operations (addition, subtraction, multiplication, division) and import it into another script.
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide( a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b