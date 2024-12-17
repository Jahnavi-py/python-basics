#Write a program to calculate the nth power of a number using a custom function.
def Custom_function(base, exponent):
    return base ** exponent
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = Custom_function(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")