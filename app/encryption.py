from cryptography.fernet import Fernet
from .config import ENCRYPTED_FILES_PATH

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('secret.key', 'rb').read()

def encrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)
    
    with open(file_path, 'rb') as file:
        original = file.read()
    
    encrypted = cipher.encrypt(original)
    
    encrypted_file_path = ENCRYPTED_FILES_PATH + '\\' + file_path.split('\\')[-1] + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    return encrypted_file_path

def decrypt_file(encrypted_file_path):
    key = load_key()
    cipher = Fernet(key)
    
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = cipher.decrypt(encrypted)
    
    decrypted_file_path = encrypted_file_path.replace('.encrypted', '')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    return decrypted_file_path
