#Write a function to calculate the nth Fibonacci number.
def fibonacci(n):
    fib = [0, 1]
    for i in range (2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
n = 15
fib_sequence = fibonacci(n)
print(fib_sequence)