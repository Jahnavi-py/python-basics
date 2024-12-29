#Write a program to compress a text file using the zlib library.
import zlib
compressed_file = "file_compressed.txt"
with open("file_log.txt", "r") as file:
    content = file.read()
    compressed_data = zlib.compress(content.encode("utf-16"))
with open(compressed_file, "wb") as file:
    file.write(compressed_data)
    print(f"File '{"file_log.txt"}' compressed successfully to '{compressed_file}'.")