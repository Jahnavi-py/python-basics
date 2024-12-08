#flatten_list = ([2,4,3],[1,5,6],[9],[7,9,0])
#chunksize = 4
#shallow_list = [flatten_list[i:i + chunksize] for i in range(0, len(flatten_list), chunksize)]
#print(shallow_list)
import itertools
flatten_list = [[2,4,3],[1,5,6],[9],[7,9,0]]
shallowlist = list(itertools.chain(*flatten_list))
print(shallowlist)