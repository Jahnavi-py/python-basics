#Write a program to create a dictionary with keys as numbers and values as their squares.
n =int(input("Enter the number for which we want to be squares: "))
squares_dict = {i: i**2 for i in range(1, n+1)}
print("The squares of numbers are :", squares_dict)