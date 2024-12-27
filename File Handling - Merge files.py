#Write a program to merge the contents of two files into a third file.
file_merge = ["files.txt", "file_name.txt"]
output_file = "file_merge.txt"
with open(output_file,"w") as outfile:
    for file in file_merge:
        with open(file,"r") as infile:
            outfile.write(infile.read())
print(f"File merged successfully.!! {output_file}")