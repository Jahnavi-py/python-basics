tuplex = 4, 10, 16, 80, 75, 90
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
tuplex = tuplex[:5] +  (10, 30, 45) + tuplex[:5]
print(tuplex)
listx = list(tuplex)
listx.reverse(30)
tuplex=tuple(listx)
print(tuplex)
