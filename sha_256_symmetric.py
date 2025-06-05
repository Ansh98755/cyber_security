from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

key = os.urandom(32)

def encrypt_message(msg):
    iv = os.urandom(12)  
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    ciphertext = encryptor.update(msg.encode()) + encryptor.finalize()
    return base64.b64encode(iv + encryptor.tag + ciphertext).decode()

def decrypt_message(token):
    raw = base64.b64decode(token)
    iv = raw[:12]
    tag = raw[12:28]
    ciphertext = raw[28:]

    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    try:
        decrypted = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted.decode()
    except:
        return None

while True:
    print("\n1. Encrypt Message\n2. Decrypt Message\n3. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        msg = input("Enter message: ")
        token = encrypt_message(msg)
        print("Encrypted (base64):", token)
    elif ch == '2':
        token = input("Enter encrypted message (base64): ")
        decrypted = decrypt_message(token)
        if decrypted is not None:
            print("Decrypted Message:", decrypted)
        else:
            print("Decryption failed or invalid key!")
    elif ch == '3':
        break
