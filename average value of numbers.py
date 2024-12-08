# calculates the average of each individual tuple in the list.
'''tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
avg_list = []
for tup in tuple:
        avg_list.append(sum(tup) / len(tup))
print("Avg of all the elements of each tuple stored inside a list of tuples : ", avg_list)
tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
avg_list2 = []
for element in tuple2:
    avg_list2.append(sum(element) / len(element))
print("avg of all the elements of each tuple2 stored inside a list of tuples : ", avg_list2)'''

#calculates the average for each position across all tuples.
tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
def avg_col(tuples):
    return[sum(col) / len(col) for col in zip (*tuples)]
avg_tuple = avg_col(tuple)
avg_tuple2 = avg_col(tuple2)
print("Avg of all the elements of each tuple stored inside a list of tuples : ", avg_tuple)
print("Avg of all the elements of each tuple stored inside a list of tuples : ", avg_tuple2)
