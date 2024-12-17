#Write a function to remove duplicates from a list.
def remove_list(list1):
    return list(set(list1))
my_list = [1, 2, 3, 2, 5]
unique_list = remove_list(my_list)
print(f"The original list is {my_list}\n")
print(f"list after removing duplicates: {unique_list}")