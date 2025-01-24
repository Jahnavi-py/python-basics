#.Create a program that demonstrates the use of the else block in exception handling.
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    else:
        print(f"The result of {a} divided by {b} is: {result}")
print("Test 1: Division with a non-zero divisor")
divide_numbers(10, 2)
print("\nTest 2: Division with zero as the divisor")
divide_numbers(10, 0)