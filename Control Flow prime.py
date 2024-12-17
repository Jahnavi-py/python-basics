#Write a program to check if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number : "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not prime.")