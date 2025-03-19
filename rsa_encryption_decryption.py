import random
import sympy

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keypair():
    p = sympy.randprime(100, 500)
    q = sympy.randprime(100, 500)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

def main():
    public, private = generate_keypair()
    while True:
        print("\nRSA Encryption Menu:")
        print("1. View Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Public Key:", public)
            print("Private Key:", private)
        elif choice == "2":
            message = input("Enter message to encrypt: ")
            encrypted_msg = encrypt(public, message)
            print("Encrypted Message:", encrypted_msg)
        elif choice == "3":
            ciphertext = input("Enter space-separated encrypted values: ")
            ciphertext = list(map(int, ciphertext.split()))
            decrypted_msg = decrypt(private, ciphertext)
            print("Decrypted Message:", decrypted_msg)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
