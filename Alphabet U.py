str = ""
for row in range(0,6):
    for column in range(0,6):
        #if(((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
        if (((column == 1 or column == 5) and row != 0) or (( row == 5) and (column > 1 and column < 5))):
            str = str +  "*"
        else:
            str = str + " "
    str = str + "\n"
print(str)