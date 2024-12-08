def common_data(list, list1):
    result = False
    for x in list:
        for y in list1:
            if x == y:
                result = True
                return result
print(common_data([1,2,3,4,5,],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))