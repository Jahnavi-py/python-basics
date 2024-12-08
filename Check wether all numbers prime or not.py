def test(num):
    return all(is_prime(i) for i in num)
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                return False
        return True
num = [2,3,9,11]
print("Original list")
print(num)
print("Check if each number is prime in the said list of numbers:")
print(test(num))
num = [3, 5, 7, 13]
print("Original list of numbers:")
print(num)
print("Check if each number is prime in the said list of numbers:")
print(test(num))
num = [1, 5, 3]
print("Original list of numbers:")
print(num)
print("Check if each number is prime in the said list of numbers:")
print(test(num))