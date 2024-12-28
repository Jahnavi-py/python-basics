#Create a program to reverse the contents of a file line by line.
input_file = "file_name.txt"
output_file = "file_reversed.txt"
with open(input_file, "r") as file:
    lines = file.readlines()
with open(output_file, "w") as file:
        for line in lines:
            file.write(line.strip()[::-1] + "\n")
print(f"Reversed content has been written to '{output_file}'.")