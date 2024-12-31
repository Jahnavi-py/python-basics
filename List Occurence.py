#Create a program to count the occurrences of each number in a list.
numbers = [1, 2, 3, 2, 1, 4, 5, 2, 3, 4, 4, 1]
count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print(f"The count the occurrences of each number in a list is {count}")