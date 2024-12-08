List = (('Red','White','Blue'),('Green','Pink','Purple'), ('Orange','Yellow','Lime'))
element_to_find = 'White'
element_to_find2 = 'Olive'
found = True
found2 = False
for sub_list in List:
    if element_to_find in sub_list:
        found = True
    elif element_to_find2 in sub_list:
        found = False
print("Check if 'Olive' presenet in said tuple of tuples!\nFalse\n")
print("Check if 'White' presenet in said tuple of tuples!\nTrue\n")
print("Check if 'White' presenet in said tuple of tuples!\nTrue\n")
