#.Create a program to read an encrypted file and decrypt it using a key.
from cryptography.fernet import Fernet
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)
    print(f"Key saved to file '{key_file}'.")
def load_key(key_file):
    try:
        with open(key_file, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Key file '{key_file}' not found.")
        return None
def write_encrypted_file(output_file, key, content):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(content.encode("utf-8"))
    with open(output_file, "wb") as file:
        file.write(encrypted_data)
    print(f"Encrypted data written to '{output_file}'.")
def read_decrypted_file(encrypted_file, key):
    try:
        with open(encrypted_file, "rb") as file:
            encrypted_data = file.read()
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
        return decrypted_data
    except FileNotFoundError:
        print(f"Error: File '{encrypted_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
key_file = "file_encryption_key.key"
encrypted_file = "file_encrypted.enc"
plaintext_content = "This is a secret message. Keep it safe!"
generate_key(key_file)
key = load_key(key_file)
if key:
    write_encrypted_file(encrypted_file, key, plaintext_content)
    decrypted_content = read_decrypted_file(encrypted_file, key)
    if decrypted_content:
        print(f"Decrypted content: {decrypted_content}")