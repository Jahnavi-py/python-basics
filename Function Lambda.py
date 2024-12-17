# Create a lambda function to calculate the square of a number.
def square_number(n):
    return n
print(f"The square of a number {square_number(20)} is {(lambda n : n**2)(20)}")