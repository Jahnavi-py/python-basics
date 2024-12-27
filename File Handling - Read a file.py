#Read the contents of a text file and print it line by line.
with open("files.txt", "r") as file:
   # content = file.read() # used for reading file directly
    #print(content)
    for line in file:
        print(line, end = "")