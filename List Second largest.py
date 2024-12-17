#Create a program to find the second largest element in a list.
numbers = [10,15,20,30,45,5,6]
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print(f"The second largest element is: {second_largest}")

