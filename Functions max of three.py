def max_num(x,y):
    if x > y:
        return y
    else:
        return x
def max_three(x,y,z):
    return max_num(x, max_num(y,z))

print(max_three(4, 8, 12))