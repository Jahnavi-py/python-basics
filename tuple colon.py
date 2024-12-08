import copy
tuple =('HI', 5, [], True)
#print(tuple)
tuple_colon = copy.deepcopy(tuple)
tuple_colon[2].append(30)
print(tuple_colon)
#print(tuple)