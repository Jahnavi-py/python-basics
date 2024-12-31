#Create a function that accepts a list and returns its average.
def cal_average(number):
    if not number:
        return 0
    return sum(number) / len(number)
number = [10, 3, 40, 5, 50]
average = cal_average(number)
print(f"The average of list is {average}")