import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def derive_key(password: str, salt: bytes) -> bytes:
    # Derives a symmetric key from the password and salt.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def generate_salt() -> bytes:
    # Generates a new salt.
    return os.urandom(16)

def encrypt(data: bytes, password: str, salt: bytes) -> bytes:
    # Encrypts data using the password and salt.
    key = derive_key(password, salt)
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(token: bytes, password: str, salt: bytes) -> bytes:
    # Decrypts data using the password and salt.
    key = derive_key(password, salt)
    f = Fernet(key)
    return f.decrypt(token)