from cryptography.fernet import Fernet
import os

class TokenGetter:
    def __init__(self):
        key = os.environ.get('key')
        enc_token = os.environ.get('enc_token')
        self.dec_token = Fernet(key).decrypt(enc_token).decode()

    def get_token(self):
        return self.dec_token

    def encrypt_token(self, token):
        key = os.environ.get('key')
        return Fernet(key).encrypt(token.encode()).decode()

        