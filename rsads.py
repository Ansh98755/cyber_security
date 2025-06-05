import random
import hashlib

def hash_function(pt):
    pt = hashlib.sha256(pt.encode('utf-8')).hexdigest()
    return pt

def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys(p, q):
    if not (checkPrime(p) and checkPrime(q)):
        raise ValueError("Invalid Prime Numbers")
    
    n = p * q
    fi = (p - 1) * (q - 1)
    
    e = random.choice([i for i in range(2, fi) if gcd(i, fi) == 1])
    
    def mod_inverse(e, fi):
        for d in range(2, fi):
            if (d * e) % fi == 1:
                return d
        return None
    
    d = mod_inverse(e, fi)
    if d is None:
        raise ValueError("Failed to find modular inverse")
    
    return ((e, n), (d, n))  


def generate_signature(msg, private_key):
    d, n = private_key
    digest = hash_function(msg)
    digest_int = int(digest, 16) % n 
    print("Sender's Message Digest :", digest_int)
    signature = pow(digest_int, d, n)  
    print("Sender's Signature (Encrypted Hash):", signature)
    return signature

def verify_signature(msg, signature, public_key):
    e, n = public_key
    digest = hash_function(msg)
    digest_int = int(digest, 16) % n
    print("Receiver's Message Digest :", digest_int)
    decrypted_hash = pow(signature, e, n)  
    print("Receiver's Unpacked Hash :", decrypted_hash)
    return digest_int == decrypted_hash
  
def main():
    msg = input("Enter a Message :")
    print("Enter Two Prime Numbers:")
    p = int(input())
    q = int(input())
    
    public_key, private_key = generate_keys(p, q)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    signature = generate_signature(msg, private_key)
    # msg += 'F'
    if verify_signature(msg, signature, public_key):
        print("Signature Verified Successfully!")
    else:
        print("Signature Verification Failed!")

if __name__ == "__main__":
    main()