tuple = [(1,2),(2,3),(3,4)]
sum_list = []
for tup in tuple:
    sum_list.append(sum(tup))
print("sum of all the elements of each tuple stored inside a list of tuples : ", sum_list)
tuple2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
sum_list2 = []
for element in tuple2:
    sum_list2.append(sum(element))
print("sum of all the elements of each tuple2 stored inside a list of tuples : ", sum_list2)