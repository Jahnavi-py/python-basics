#Write a Python program to display the first 5 lines of a file
with open("file_name.txt", 'r') as file:
    for i in range(5):
        line = file.readline()
        if not line:
            break
        print(line.strip())