#Create a program to count how many numbers between 1 and 100 are divisible by 7.
count = 0
for number in range(1, 101):
    if number % 7 == 0:
        print("The numbers are: ", number)
        count += 1
print(f"There are {count} numbers between 1 and 100 that are divisible by 7.")
