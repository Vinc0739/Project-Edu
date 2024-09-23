import base64
import os
from dotenv import dotenv_values
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

env = dotenv_values('./src/bot/.env')

class EncryptionManager:
    def __init__(self):
        self.master_key = self.get_master_key()
    
    # Master-Key aus .env bekommen
    def get_master_key(self):
        master_key = env['MASTER_KEY']
        if master_key is None:
            raise ValueError("Master key is not set in environment variables.")
        return master_key.encode('utf-8')
    
    # Salt generieren
    @staticmethod
    def generate_salt():
        return os.urandom(16)
    
    # User Schlüssel durch User-ID und Salt generieren
    def generate_user_key(self, user_id, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(self.master_key + user_id.encode()))
    
    # Verschlüsseln
    def encrypt(self, user_id, not_encrypted, salt):
        user_key = self.generate_user_key(str(user_id), salt)
        cipher_suite = Fernet(user_key)
        return cipher_suite.encrypt(not_encrypted.encode())
    
    # Entschlüsseln
    def decrypt(self, user_id, encrypted, salt):
        salt_bytes = base64.b64decode(salt)
        user_key = self.generate_user_key(str(user_id), salt_bytes)
        cipher_suite = Fernet(user_key)
        return cipher_suite.decrypt(encrypted).decode()
