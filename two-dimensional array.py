row = 3
col = 4
array_2D = [[0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    for j in range(col):
        array_2D[i][j] = i * j
print(array_2D)
