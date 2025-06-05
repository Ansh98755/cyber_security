from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import hashlib
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def sign_message(msg):
    h = hashlib.sha256(msg.encode()).digest()
    signature = private_key.sign(h, padding.PKCS1v15(), hashes.SHA256())
    return signature

def verify_signature(msg, sig):
    h = hashlib.sha256(msg.encode()).digest()
    try:
        public_key.verify(sig, h, padding.PKCS1v15(), hashes.SHA256())
        return True
    except:
        return False

while True:
    print("\n1. Sign Message\n2. Verify Signature\n3. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        msg = input("Enter message: ")
        sig = sign_message(msg)
        print("Signature (hex):", sig.hex())
    elif ch == '2':
        msg = input("Enter message: ")
        sig_hex = input("Enter signature (hex): ")
        sig = bytes.fromhex(sig_hex)
        if verify_signature(msg, sig):
            print("Signature Verified!")
        else:
            print("Invalid Signature!")
    elif ch == '3':
        break
