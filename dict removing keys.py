#Write a program to remove all keys with even values from a dictionary.
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = {key: value for key, value in my_dict.items() if value % 2 != 0}
print(filtered_dict)