#Write a program to copy the contents of one file to another.
"""import shutil #Imports the shutil module, which provides functions for file operations.
source_filename = "files.txt"
destination_filename = "file_name.txt"
shutil.copyfile(source_filename, destination_filename)
"""
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line)
        print(f"File '{source_file}' copied successfully to '{destination_file}'")
    except FileNotFoundError:
            print(f"Error: Source file '{source_file}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
source_filename = "files.txt"
destination_filename = "file_name.txt"
copy_file(source_filename, destination_filename)