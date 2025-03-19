import numpy as np

def get_key_matrix(key, size):
    """Convert the key string into a square matrix for encryption/decryption."""
    key_matrix = []
    k = 0
    for i in range(size):
        row = [ord(key[k + j]) % 65 for j in range(size)]  # Convert characters to numbers
        key_matrix.append(row)
        k += size
    return np.array(key_matrix)

def mod_inverse_matrix(matrix, mod):
    """Find the modular inverse of the key matrix in mod 26."""
    det = int(round(np.linalg.det(matrix)))  # Compute determinant
    try:
        det_inv = pow(det, -1, mod)  # Modular inverse of determinant
    except ValueError:
        raise ValueError("Key matrix is not invertible in mod 26.")
    
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Compute adjugate matrix
    return (det_inv * adjugate) % mod  # Compute modular inverse matrix

def hill_cipher_encrypt(plaintext, key, size):
    """Encrypt plaintext using the Hill cipher."""
    key_matrix = get_key_matrix(key, size)
    message_vector = np.array([[ord(char) % 65] for char in plaintext])  # Convert text to vector
    
    cipher_matrix = np.dot(key_matrix, message_vector) % 26  # Matrix multiplication and mod 26
    ciphertext = ''.join(chr(int(num) + 65) for num in cipher_matrix.flatten())
    return ciphertext

def hill_cipher_decrypt(ciphertext, key, size):
    """Decrypt ciphertext using the Hill cipher."""
    key_matrix = get_key_matrix(key, size)
    try:
        key_matrix_inverse = mod_inverse_matrix(key_matrix, 26)
    except ValueError as e:
        return f"Decryption not possible: {e}"
    
    cipher_vector = np.array([[ord(char) % 65] for char in ciphertext])  # Convert text to vector
    plain_matrix = np.dot(key_matrix_inverse, cipher_vector) % 26  # Matrix multiplication and mod 26
    plaintext = ''.join(chr(int(num) + 65) for num in plain_matrix.flatten())
    return plaintext

def main():
    """Main menu for Hill Cipher encryption and decryption."""
    while True:
        print("\n===== Hill Cipher Menu =====")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext (uppercase, length must match key size): ").upper()
            key = input("Enter the key (length must be a perfect square): ").upper()
            
            size = int(len(key) ** 0.5)
            if size * size != len(key) or len(plaintext) != size:
                print("Error: Key must be a square matrix (n^2 length), and plaintext must match matrix size!")
            else:
                ciphertext = hill_cipher_encrypt(plaintext, key, size)
                print("Encrypted Text:", ciphertext)
        
        elif choice == '2':
            ciphertext = input("Enter the ciphertext (uppercase, length must match key size): ").upper()
            key = input("Enter the key (length must be a perfect square): ").upper()
            
            size = int(len(key) ** 0.5)
            if size * size != len(key) or len(ciphertext) != size:
                print("Error: Key must be a square matrix (n^2 length), and ciphertext must match matrix size!")
            else:
                plaintext = hill_cipher_decrypt(ciphertext, key, size)
                print("Decrypted Text:", plaintext)
        
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
