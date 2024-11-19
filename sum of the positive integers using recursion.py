def sum_intergers(n):
    if n <= 1:
        return 0
    else:
        return n + sum_intergers(n-2)
print(sum_intergers(6))
print(sum_intergers(10))