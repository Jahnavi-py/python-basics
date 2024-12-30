#Write a program to calculate the MD5 checksum of a file.
import hashlib
def calculate_md5(file_path):
    try:
        with open(file_path, "rb") as file:
            md5_hash = hashlib.md5()
            while chunk := file.read(8192):  # Read 8 KB at a time
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
file_to_check = r"/C:\Users\jahna\PycharmProjects\PythonProject\python-basics\files.txt"
md5_checksum = calculate_md5(file_to_check)
print(f"MD5 Checksum: {md5_checksum}")