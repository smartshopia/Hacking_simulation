import base64

def decrypt_data(encrypted_data):
    """Simulate file decryption by base64 decoding the content."""
    return base64.b64decode(encrypted_data).decode('utf-8')

def read_and_decrypt_file(file_name):
    """Read the encrypted file, decrypt it, and display the contents."""
    with open(file_name, 'r') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_data(encrypted_data)
    print(f"Decrypted file contents of {file_name}:\n{decrypted_data}")

# Example usage to decrypt one file
read_and_decrypt_file('encrypted_files/encrypted_file_1.txt')
