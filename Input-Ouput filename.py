#Write a program to ask the user for a filename and then print its extension.
import os
filename = input("Enter the filename: ")
file_extension = os.path.splitext(filename)[1]
if file_extension:
  print("The extension of the file is:", file_extension)
else:
  print("The file does not have an extension.")