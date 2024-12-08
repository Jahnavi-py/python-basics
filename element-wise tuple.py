Tuple1 = (1,2,3,4)
Tuple2 = (3,5,2,1)
Tuple3 = (2,2,3,1)
#Element_wiselists = ( )
#for sums in Tuple:
    #Element_wiselists.append(sum(sums))
#print("The element-wise sum of the give tuples : ", Element_wiselists)
element_wise = tuple(a + b + c for a,b,c in zip(Tuple1, Tuple2, Tuple3))
print("The element-wise sum of the give tuples : ", element_wise)