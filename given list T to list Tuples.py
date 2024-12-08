list1 = [(1,2), (2,3),(3,4)]
print("Orginal list1 of tuples : ", list1)
Convert_lists = []
for item in list1:
    Convert_lists.append(list(item))
print("The given list1 of tuples to a list of lists : ", Convert_lists)
list2 = [(1,2),(2,3,5),(3,4), (2,3,4,2)]
print("orginal list2 of tuples : ", list2)
Convert_lists2 = []
for item in list2:
    Convert_lists2.append(list(item))
print("The given list2 of tuples to a list of lists : ",Convert_lists2)