#A simple app to simulate rolling a pair of dice. Each time the program runs, it generates two random numbers between 1 and 6.
import random
dice_to_roll1 = random.randint(1,6)
dice_to_roll2 = random.randint(1,6)
dice1 = int(input("Enter a number to roll a dice1 : "))
dice2 = int(input("Enter a number to roll a dice2 : "))
if dice1 <= 6 and dice1 >= 1 and dice2 <= 6 and dice2 >= 1:
    print("Correctly Diced! Diced rolled is in between 1 and 6.")
#elif dice2 != 1 and dice2 != 2:
elif dice1 <= 6 and dice2 != 6 and dice1 >= 1 and dice2 !=1:
    print("Please roll the dice again!")
#elif dice1 != 1 and dice1 != 2:
elif dice1 != 6 and dice2 <= 6 and dice1 != 1 and dice2 >= 1:
    print("Please roll the dice again!")
print(f"The dice rolled number is between {dice1} and {dice2}")