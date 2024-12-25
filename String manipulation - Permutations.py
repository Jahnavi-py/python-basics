#Find all permutations of a string.
import itertools
elements = "Hello"
permutation = itertools.permutations(elements)
for perms in permutation:
    print(f"The permutations from elements '{elements}' is '{''.join(perms)}' ")