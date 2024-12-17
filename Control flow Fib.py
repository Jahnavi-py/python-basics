#Write a program to print the Fibonacci series up to n terms.
n = int(input("Enter the number:"))
fib = [0, 1]
for i in range (2,n):
     fib.append(fib[i-1] + fib[i-2])
print("Fibonacci Series:",fib)