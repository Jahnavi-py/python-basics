#Write a program to read a file and replace all occurrences of a specific word with another word.
input_file = "files.txt"
output_file = "file_occurence.txt"
old_word = "Python"
new_word = "Java"
try:
    with open(input_file, "r") as file:
        content = file.read()
        updated_content = content.replace(old_word,new_word)
    with open(output_file, "w") as file:
        file.write(updated_content)
    print(f"All occurrences of '{old_word}' have been replaced with '{new_word}' in '{output_file}'.")
except FileNotFoundError:
    print("Input file does not exists.")