#Write a program to calculate the size of a file in bytes, kilobytes, and megabytes.
import os
file_path = "file_name.txt"
file_size = os.path.getsize(file_path)
print(f"The size of the file '{file_path}' is {file_size} bytes.")
kb_size = file_size / 1024
print(f"The size of the file '{file_path}' in kilobytes : {kb_size:.2f}KB")
mb_size = kb_size / 1024
print(f"The size of the file '{file_path}' in megabytes : {mb_size:.2f} MB")
gb_size = mb_size / 1024
print(f"The size of the file '{file_path}' in gigabytes : {gb_size:.5f}GB")