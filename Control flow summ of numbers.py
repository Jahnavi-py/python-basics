#Write a program to sum all numbers in a list using a loop.
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 2, 3, 4, 5]
result = sum_numbers(numbers)
print(f"Sum of all numbers in the list {numbers} is {result}")