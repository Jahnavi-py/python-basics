#Use a loop to print all prime numbers between 1 and 50.
for num in range(2,51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"The prime numbers between 1 and 50 is : {num}")