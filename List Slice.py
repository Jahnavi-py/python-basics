#Use slicing to extract the first and last three elements of a list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_three = my_list[:3]
last_three = my_list[-3:]
result = first_three + last_three
print(f"slicing to extract the first and last three elements of a list from list {my_list} is {result}")