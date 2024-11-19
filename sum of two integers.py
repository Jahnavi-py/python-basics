a = 15
b = 20
sum = a + b
#print(sum)
if sum <= b:
#if sum == b:
    print(b)
else:
    print("the sum of integer doesn't lie in between 15 & 20.",sum)


#other code
def sum(x,y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
print(sum(10,6))
print(sum(10, 2))
print(sum(10,12))