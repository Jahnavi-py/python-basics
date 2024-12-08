def list_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + list_sum(numbers[1:])

print(list_sum([2, 4, 5, 6, 7]))