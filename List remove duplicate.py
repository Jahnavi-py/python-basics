#Remove duplicate elements from a list.
my_list = [1, 2, 3, 2, 5]
#my_list.remove(2)
unique_list = list(set(my_list))
print(f"List after removing duplicates: {unique_list}")