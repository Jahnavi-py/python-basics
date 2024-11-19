import random
user = random.randint(1,9)
guess = None
while guess != user:
    guess = int(input("Enter number from 1 to 9 : "))
    if guess < user:
        print("Try again!")
    elif guess > user:
        print("Try again!")
    else:
        print("Well guessed!")
