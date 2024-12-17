#Write a program to sort a dictionary by its keys.
my_dict = {'hi' : 15, 'Hello' : 3, 'Name': 4}
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted dictionary by keys:", sorted_dict)