tuple =(( ),( ), (''), ('a', 'b'), ('a','b','c'), ('d'))
print("The given tuples are : " , tuple)
filtered_tuple = [t for t in tuple if t]
print("List after removing empty tuples : " , filtered_tuple)