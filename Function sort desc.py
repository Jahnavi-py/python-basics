#Write a function to sort a list of numbers in descending order.
def sort_descending(numbers):
    return sorted(numbers, reverse=True)
numbers = [10, 5, 2, 8, 7, 3]
sorted_numbers = sort_descending(numbers)
print(sorted_numbers)