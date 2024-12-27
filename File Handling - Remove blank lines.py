#Write a program to remove all blank lines from a file.
input_file = "file_name.txt"
output_file = "file_name_cleaned.txt"
with open(input_file, "r") as file:
    lines = file.readlines()
    non_blank_lines = [line for line in lines if line.strip()]
with open(output_file, "w") as file:
    file.writelines(non_blank_lines)
print(f"Blank lines have been removed. The cleaned file is saved as '{output_file}'.")