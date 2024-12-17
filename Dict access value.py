#Access the value associated with a specific key in a dictionary
my_dict = {'name': 1, 'age': 25, 'color': 5}
value = my_dict["name"]
print(f"the value associated with a specific key in a dictionary {my_dict} is {value}")
key = my_dict.get("age")
print(f"the value associated with a specific key in a dictionary {my_dict} is {key}")