# Implement a program to flatten a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for inner_list in nested_list for item in inner_list]
print(f"The flattened nested list is {flattened}")