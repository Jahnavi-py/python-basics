number=int(input("Enter the Number : "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range (2, int(number ** 0.5 ) + 1):
        if number % i == 0:
            is_prime =False
print("Is the Prime Number?", is_prime)