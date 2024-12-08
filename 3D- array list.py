depth = 3
row =4
col = 6
array_3d = [[['*' for _ in range(col)] for _ in range(row)] for _ in range(depth)]
for depth in array_3d:
    for row in depth:
        print(row)
    print()