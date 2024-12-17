#Write a program to find the key with the maximum value in a dictionary.
my_dict = {
    'a': 10,
    'b': 20,
    'c': 15,
    'd': 30
}
max_key = max(my_dict, key=my_dict.get)
max_value = my_dict[max_key]
print(f"The key:'{max_key}' with the maximum value is: {max_value}")