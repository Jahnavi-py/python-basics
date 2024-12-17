#Write a function that takes a list of numbers and returns the largest number.
def largest_numbers(number):
    if not number:
        return None
    return max(number)
numbers = [10,2,4,50,7]
largest = largest_numbers(numbers)
print(f"The list of numbers is {numbers} and returns the largest number from the list is {largest}")