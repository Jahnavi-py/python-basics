#row = 5
#for i in range(row):
    #for j in range(row, 0 - 1):
        #print("", end ="")
   # print('')
   # for k in range(2 * i +1):
      #  print("*", end = "")
    #print('')
row = 5
for i in range(row):
    for j in range(i):
        print("* ", end = "")
    print('')
for i in range(row, 0, -1):
    for j in range(i):
        print("* ", end="")
    print('')