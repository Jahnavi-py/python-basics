#Write a program to demonstrate the use of the finally block in cleaning up resources after exception handling.
def read_file(file_name):
    file = None
    try:
        file = open(file_name, 'r')
        print(f"Reading contents of the file '{file_name}':")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file:
            file.close()
            print(f"File '{file_name}' has been closed.")
file_name = input("Enter the file name to read: ")
read_file(file_name)