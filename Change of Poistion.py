list = (0,1,2,3,4,5)
n = 5
my_list=['{}{}'.format(x,y) for y in range(n,n+1) for x in list]
print(my_list)