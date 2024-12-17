#Input a list of integers from the user and find their average.
numbers = input("Enter the list of integers separated by spaces: ")
numbers_list = list(map(int, numbers.split()))
average = sum(numbers_list) / len(numbers_list)
print("The average of the list of integers is:", average)