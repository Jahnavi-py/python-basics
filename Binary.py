binary_numbers = input("Enter comma-separated binary numbers: ")
result = [num for num in binary_numbers.split(',') if int(num, 2) % 5 == 0]
print("Binary numbers divisible by 5:", ','.join(result))