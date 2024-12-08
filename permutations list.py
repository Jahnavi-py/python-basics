#print(list(itertools.permutations([4,5,6])))
import itertools
elements = (4,5,6,7,8)
perm = itertools.permutations(elements)
for perm in perm:
    print("the permutations are : ", perm)
combos = itertools.combinations(elements, 3)
combos = itertools.combinations(elements, 2)
combos = itertools.combinations(elements, 4)
for combos in combos:
    print("the Combinations are : ", combos)
