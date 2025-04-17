def ksa(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))  
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  
    return S

def prga(S):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4_encrypt_decrypt(data, key):
    """Encrypts or decrypts the input data using RC4"""
    key = [ord(c) for c in key]  
    S = ksa(key)
    keystream = prga(S)
    result = []

    for char in data:
        val = ord(char) ^ next(keystream)  
        result.append(chr(val))
    
    return ''.join(result)
def main():
    while True:
        print("\n==== RC4 Encryption/Decryption Menu ====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the text to encrypt: ")
            key = input("Enter the key: ")
            encrypted = rc4_encrypt_decrypt(plaintext, key)
            print("Encrypted Text (in hex):", encrypted.encode().hex())
        elif choice == '2':
            hex_data = input("Enter the hex-encoded encrypted text: ")
            key = input("Enter the key: ")
            encrypted_bytes = bytes.fromhex(hex_data)
            encrypted_text = ''.join([chr(b) for b in encrypted_bytes])
            decrypted = rc4_encrypt_decrypt(encrypted_text, key)
            print("Decrypted Text:", decrypted)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
