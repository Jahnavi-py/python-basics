#Write a program to rotate a list by k positions to the left.
my_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = my_list[k:] + my_list[:k]
print(f"Original list: {my_list}")
print(f"List after left rotation by {k} positions: {rotated_list}")