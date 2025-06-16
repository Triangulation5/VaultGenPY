import json
import os
from typing import Optional, Dict
from crypto_utils import encrypt, decrypt, generate_salt

VAULT_FILE = "vault.bin"
SALT_FILE = "vault.salt"

class PasswordStorage:
    def __init__(self, master_password: str):
        self.master_password = master_password
        self.salt = self._load_or_create_salt()
        self.data = self._load_vault()

    def _load_or_create_salt(self) -> bytes:
        if os.path.exists(SALT_FILE):
            with open(SALT_FILE, "rb") as f:
                return f.read()
        else:
            salt = generate_salt()
            with open(SALT_FILE, "wb") as f:
                f.write(salt)
            return salt

    def _load_vault(self) -> Dict[str, Dict[str, str]]:
        if not os.path.exists(VAULT_FILE):
            return {}
        with open(VAULT_FILE, "rb") as f:
            encrypted = f.read()
        try:
            decrypted = decrypt(encrypted, self.master_password, self.salt)
            return json.loads(decrypted.decode())
        except Exception:
            print("Could not decrypt vault. Wrong master password or corrupted file.")
            exit(1)

    def _save_vault(self):
        data_bytes = json.dumps(self.data).encode()
        encrypted = encrypt(data_bytes, self.master_password, self.salt)
        with open(VAULT_FILE, "wb") as f:
            f.write(encrypted)

    def add_password(self, site: str, username: str, password: str):
        self.data[site] = {"username": username, "password": password}
        self._save_vault()

    def get_password(self, site: str) -> Optional[Dict[str, str]]:
        return self.data.get(site)

    def list_sites(self):
        return list(self.data.keys())