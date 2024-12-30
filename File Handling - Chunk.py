#Write a Python script to read a large file in chunks and process it.
def process_chunk(chunk):
    print(chunk.decode("utf-8", errors="ignore"))
def read_file_in_chunks(file_path, chunk_Size=1024):
    try:
        with open(file_path, "rb") as file:  # Open file in binary mode
            while chunk := file.read(chunk_Size):
                process_chunk(chunk)  # Process the chunk
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_to_read = r"C:\Users\jahna\PycharmProjects\PythonProject\python-basics\filebinary.bin"
read_file_in_chunks(file_to_read, 1024)