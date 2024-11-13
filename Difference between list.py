list1 = (1,2,3,4,5,6,7,8,9)
list2 = (10,11,12,13,14,15)
diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
total = diff1 + diff2
print(total)