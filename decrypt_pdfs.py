import os
from cryptography.fernet import Fernet
import time

def load_key():
    """Load the previously generated encryption key."""
    return open("secret.key", "rb").read()

def decrypt_file(file_path, key):
    """Decrypt a single file using the provided key."""
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"Decrypted: {file_path}")

def decrypt_pdfs_in_os(root_directory):
    """Decrypt all encrypted PDF files in the entire OS by searching recursively."""
    # Load the encryption key
    key = load_key()

    # Walk through all directories and decrypt PDFs
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.pdf'):
                try:
                    file_path = os.path.join(foldername, filename)
                    decrypt_file(file_path, key)
                    time.sleep(0.5)  # Slow down the process for better simulation feel
                except Exception as e:
                    print(f"Failed to decrypt {filename}: {e}")

if __name__ == "__main__":
    # Get the root directory based on OS
    if os.name == "nt":  # Windows
        root_directory = "C:\\"
    else:  # Linux/Mac
        root_directory = "/"

    decrypt_pdfs_in_os(root_directory)
