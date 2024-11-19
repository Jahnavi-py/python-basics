i = 'jahnavi'
vowels = ['a','e','i','o','u']
vowels_count = 0
for char in i:
    if char in vowels:
        vowels_count += 1
    elif vowels_count > 0:
        print("The vowles are : ", vowels_count)
else:
    print("none")

#if vowels == 'aeiouAEIOU':
    #print(vowels)
#elif list == vowels:
    #print("The vowles in the list are : ",vowels)
#else:
   # print(None)

