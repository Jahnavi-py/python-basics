r_str = ""
for row in range(0,7):
    for column in range (0,7):
        if(((column == 0 or column == 5) and row != 2 ) or ((row == 0 or row == 6) and (column > 0 and column < 4))):
            r_str = r_str +  "*"
        else:
            r_str = r_str + "  "
    r_str = r_str +"\n"
print(r_str)