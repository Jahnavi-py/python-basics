import random
number_to_guess = random.randint(5, 20)
user_guess =int(input("Guess the number between 5 and 20:"))
if user_guess == number_to_guess:
    print("Congo! You guessed it Correct.")
elif user_guess > 20 or user_guess < 5:
    print("You guessed out of range")
else:
    print("Sorry! The correct number is:", number_to_guess)
