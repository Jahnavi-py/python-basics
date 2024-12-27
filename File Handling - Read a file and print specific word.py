#Read a file and print only lines that contain a specific word.
word_to_find = "Python"
with open("file_name.txt", "r") as file :
    for line in file:
        if word_to_find in line:
            print(line, end = "")