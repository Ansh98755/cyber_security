def validate_key(key):
    n = len(key)
    return set(key) == set(range(1, n + 1))

def encrypt_row_transposition(plaintext, key):
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
    key_length = len(key)
    padding_length = (key_length - (len(plaintext) % key_length)) % key_length
    plaintext += 'X' * padding_length
    rows = [plaintext[i:i + key_length] for i in range(0, len(plaintext), key_length)]
    ciphertext = ''
    for k in sorted((val, idx) for idx, val in enumerate(key)):
        col_index = k[1]
        for row in rows:
            ciphertext += row[col_index]
    return ciphertext

def decrypt_row_transposition(ciphertext, key):
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    grid = [['' for _ in range(key_length)] for _ in range(num_rows)]
    sorted_key = sorted((val, idx) for idx, val in enumerate(key))
    index = 0
    for _, col_index in sorted_key:
        for row in range(num_rows):
            grid[row][col_index] = ciphertext[index]
            index += 1
    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext

def main():
    while True:
        print("\n--- Row Transposition Cipher ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key_input = input("Enter the key as comma-separated numbers (e.g., 3,1,4,2): ")

            try:
                key = list(map(int, key_input.strip().split(',')))
                if not validate_key(key):
                    print("Invalid key. It must be a permutation of 1 to N.")
                    continue

                ciphertext = encrypt_row_transposition(plaintext, key)
                print("Ciphertext:", ciphertext)

            except ValueError:
                print("Invalid input. Use numbers like 3,1,4,2")

        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            key_input = input("Enter the key as comma-separated numbers (e.g., 3,1,4,2): ")

            try:
                key = list(map(int, key_input.strip().split(',')))
                if not validate_key(key):
                    print("Invalid key. It must be a permutation of 1 to N.")
                    continue

                plaintext = decrypt_row_transposition(ciphertext, key)
                print("Decrypted Plaintext:", plaintext)

            except ValueError:
                print("Invalid input. Use numbers like 3,1,4,2")

        elif choice == '3':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
