def non_intergers(n):
    if n == 0:
        return 0
    else:
        return n % 10 + non_intergers(n // 10)
print(non_intergers(345))
print(non_intergers(45))
