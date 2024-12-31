#Write a program to split a list into two halves.
my_list = [1, 2, 3, 4, 5, 6]
midpoint = len(my_list) // 2
first_half = my_list[:midpoint]
second_half = my_list[midpoint:]
print(f"Original list: {my_list}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")