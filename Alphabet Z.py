e_str = ''
for row in range(0,7):
    for column in range(0,7):
        if(((column <= 0 or column <= 5) or row != 1 ) and ((row == 0 or row == 6 ) and (column >= 0  or column <= 5) or row + column == 6)):
        #if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row + column == 6):
            e_str = e_str + "*"
        else:
            e_str = e_str + " "
    e_str = e_str + "\n"
print(e_str)