#Use a dictionary comprehension to create a dictionary of squares for numbers 1 to 5.
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict)