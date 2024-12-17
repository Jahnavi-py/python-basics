#Merge two dictionaries and handle duplicate keys by adding their values.
dict1 = {'a': 1, 'b': 3, 'c': 4}
dict2 = {'b': 5, 'c': 6, 'd': 45}
merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value
print(merged_dict)