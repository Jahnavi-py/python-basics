#Generate all possible combinations of a string (non-repeated).
'''import itertools
String= "Hello"
for i in range(1, len(elements) + 1):
    combination = itertools.combinations(elements, i)
#combination = itertools.combinations(elements, 3)
    for combs in combination:
        print(f"The combination from elements '{elements}' is '{''.join(combs)}' ")'''
import itertools
String = "Hello"
for i in range(1, len(String) + 1):
    combination = itertools.combinations(String, i)
    for comb in combination:
        print(f"Combination of string '{String}': '{''.join(comb)}'")