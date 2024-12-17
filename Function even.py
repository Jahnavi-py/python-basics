#Create a function to calculate the sum of all even numbers in a list.
def Even_number(number):
    return sum(num for num in number if num % 2 == 0)
numbers_list = [2,4,6,8,10]
result = Even_number(numbers_list)
print(f"The sum of all even numbers {numbers_list} in the list is {result}")