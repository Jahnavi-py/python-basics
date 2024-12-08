Tuples = (('333','33'),('1416','55'))
converted_tuple = tuple(tuple(int(item) for item in inner_tuple) for inner_tuple in Tuples)
#str = tuple((int(item) for item in Tuples))
print(converted_tuple)