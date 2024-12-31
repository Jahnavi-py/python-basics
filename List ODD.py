#Write a program to create a list of odd numbers from 1 to 50.
odd_numbers = []
for num in range (1,51):
        if num % 2 != 0:
            odd_numbers.append(num)
print("The odd numbers from 1 to 50 are:", odd_numbers)