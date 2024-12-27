#Append a new line to an existing file without overwriting it.
with open("files.txt", "a") as file:
    file.write("Python is easy to read and write. - Appending the new line\n")