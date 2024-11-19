def GCD(a, b):
    low = min(a,b)
    high = max(a,b)
    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return GCD(low, high % low)
print(GCD(15,18))