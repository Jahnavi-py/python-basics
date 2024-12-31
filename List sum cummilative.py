#Write a program to calculate the cumulative sum of a list.
def cumulative_sum(list):
    result = []
    total = 0
    for num in list:
        total += num
        result.append(total)
    return result
numbers = [10,50,3,4,7]
print(f"the cumulative sum of a list is {cumulative_sum(numbers)}")