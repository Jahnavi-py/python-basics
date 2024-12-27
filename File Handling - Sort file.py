#Sort the lines of a text file alphabetically and save the output to a new file.
input_file = "file_name.txt"
output_file = "file_sorted.txt"
with open (input_file, "r") as file:
    lines = file.readlines()
sorted_lines = sorted(lines)
with open(output_file, "w") as file:
    file.writelines(sorted_lines)
print(f"Lines have been sorted and saved to '{output_file}'.")