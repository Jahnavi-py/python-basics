'''number = int(input("Enter the Fibonacci Numbers :"))
a, b = 0,1
for _ in range(number):
        a, b = b, a + b

for i in range(50):
    print((i))'''
def fibonacci_recursive(number):
    if number <= 1:
        return number
    else:
        return fibonacci_recursive(number-1) + fibonacci_recursive(number-2)

# Print Fibonacci series up to the 10th term
for i in range(10):
    print(fibonacci_recursive(i), end=" ")
