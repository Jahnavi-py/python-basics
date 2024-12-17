#Write a program to input a list of numbers (comma-separated) and print them as a Python list.
numbers_input = input("Enter numbers separated by commas: ")
numbers_list = [int(num) for num in numbers_input.split(',')]
print(f"The list of numbers is {numbers_list}")
