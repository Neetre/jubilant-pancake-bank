'''
Neetre 2024
'''

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import numpy as np

class Security:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate(password):
        key = Security.generate_key()
        Security.save_key(key)
        
        enc_pwd = Security.encrypt_password(password, key)
        
        return enc_pwd
    
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_password(password, key):
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode("utf-8"))
        return encrypted_password
    
    @staticmethod
    def decrypt_password(password, key):
        f = Fernet(key)
        dec_password = f.decrypt(password).decode("utf-8")
        return dec_password
    
    @staticmethod
    def save_key(key):
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
            
    @staticmethod
    def load_key():
        return open('secret.key', 'rb').read()
    
    @staticmethod
    def generate_key_pair(password):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode('utf-8'))
        )
        
        return pem, public_key

    @staticmethod
    def decode_pem(pem_data, password):
        private_key = serialization.load_pem_private_key(
            pem_data,
            password=password.encode("utf-8"),
            backend=default_backend()
        )
        return private_key
    
    @staticmethod
    def generate_2FA_code():
        # 6 cifers, random
        code = np.random.randint(100000, 999999)
        return code
