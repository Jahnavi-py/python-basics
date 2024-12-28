#Write a program to read a binary file and display its content as a hexadecimal string.
binary_data = b'\x48\x65\x6C\x6C\x6F\x21'
file_path = "filebinary.bin"
with open(file_path, "wb") as file:
    file.write(binary_data)
    print(f"Binary file '{file_path}' created successfully.")
try:
    with open(file_path, "rb") as file:
        binary_content = file.read()
    hex_string = binary_content.hex()
    print("Hexadecimal content:")
    print(hex_string)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
