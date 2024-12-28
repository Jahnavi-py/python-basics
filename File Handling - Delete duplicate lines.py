#Write a program to find and delete duplicate lines in a file.
with open("files_1.txt", "w") as file:
    file.write("Hi!")
    file.write('\n')
    file.write("Welcome to Python Programming.")
    file.write('\n')
    file.write("Welcome to python programming.")
    file.write('\n')
    file.write("Python is Dynamic Programming.")
print(f"File 'files_1.txt' is created.")
with open("files_1.txt", 'r') as file:
    lines = file.readlines()
    unique_lines = set(line.lower() for line in lines)
with open("files_1_DeletedDup.txt", "w") as file:
    for line in unique_lines:
        file.write(line)
print(f"Duplicates removed. The output is saved in 'files_1_DeletedDup.txt'.")