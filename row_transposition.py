# def validate_key(key):  
#     """  
#     Validate the key to ensure it is a valid permutation of numbers from 1 to N.  
#     """  
#     n = len(key)  
#     expected = set(range(1, n + 1))  
#     actual = set(key)  
#     return actual == expected  

# def encrypt_row_transposition(plaintext, key):  
#     """  
#     Encrypt the plaintext using the row transposition cipher.  
#     """  
#     # Validate the key  
#     if not validate_key(key):  
#         raise ValueError("Invalid key. Key must be a permutation of numbers from 1 to N.")  

#     # Remove spaces and non-alphabet characters  
#     plaintext = ''.join(filter(str.isalpha, plaintext.upper()))  

#     # Pad the plaintext if necessary  
#     padding_length = len(key) - (len(plaintext) % len(key))  
#     if padding_length != len(key):  
#         plaintext += 'X' * padding_length  

#     # Arrange plaintext into rows  
#     rows = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]  

#     # Reorder columns based on the key  
#     ciphertext = ''  
#     for row in rows:  
#         for col_index in key:  
#             ciphertext += row[col_index - 1]  

#     return ciphertext  

# def main():  
#     while True:  
#         print("\n--- Row Transposition Cipher Menu ---")  
#         print("1. Encrypt a message")  
#         print("2. Validate a key")  
#         print("3. Exit")  
#         choice = input("Enter your choice (1/2/3): ")  

#         if choice == '1':  
#             # Encrypt a message  
#             plaintext = input("Enter the plaintext: ")  
#             key_input = input("Enter the key as comma-separated numbers (e.g., 3,1,4,2): ")  
#             try:  
#                 key = list(map(int, key_input.split(',')))  
#                 ciphertext = encrypt_row_transposition(plaintext, key)  
#                 print("Ciphertext:", ciphertext)  
#             except ValueError as e:  
#                 print("Error:", e)  

#         elif choice == '2':  
#             # Validate a key  
#             key_input = input("Enter the key as comma-separated numbers (e.g., 3,1,4,2): ")  
#             try:  
#                 key = list(map(int, key_input.split(',')))  
#                 if validate_key(key):  
#                     print("The key is valid.")  
#                 else:  
#                     print("The key is invalid. It must be a permutation of numbers from 1 to N.")  
#             except ValueError:  
#                 print("Invalid input. Please enter numbers only.")  

#         elif choice == '3':  
#             # Exit the program  
#             print("Exiting the program. Goodbye!")  
#             break  

#         else:  
#             print("Invalid choice. Please select 1, 2, or 3.")  

# if __name__ == "__main__":  
#     main()  


def validate_key(key):  
    """  
    Check if the key is valid.  
    A valid key must have numbers from 1 to N without duplicates.  
    Example: For N=4, key can be [3,1,4,2].  
    """  
    n = len(key)  
    expected = set(range(1, n + 1))  # Expected numbers: 1, 2, ..., N  
    actual = set(key)  # Actual numbers in the key  
    return actual == expected  # Check if they match  

def encrypt_row_transposition(plaintext, key):  
    """  
    Encrypt the plaintext using the row transposition cipher.  
    """  
    # Remove spaces and non-alphabet characters  
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))  

    # Pad the plaintext if its length is not a multiple of the key length  
    padding_length = len(key) - (len(plaintext) % len(key))  
    if padding_length != len(key):  
        plaintext += 'X' * padding_length  

    # Arrange plaintext into rows  
    rows = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]  

    # Reorder columns based on the key  
    ciphertext = ''  
    for row in rows:  
        for col_index in key:  
            ciphertext += row[col_index - 1]  

    return ciphertext  

def main():  
    while True:  
        print("\n--- Row Transposition Cipher ---")  
        print("1. Encrypt a message")  
        print("2. Exit")  
        choice = input("Enter your choice (1/2): ")  

        if choice == '1':  
            # Encrypt a message  
            plaintext = input("Enter the plaintext: ")  
            key_input = input("Enter the key as comma-separated numbers (e.g., 3,1,4,2): ")  

            try:  
                # Convert key input to a list of integers  
                key = list(map(int, key_input.split(',')))  

                # Validate the key  
                if not validate_key(key):  
                    print("Invalid key. It must contain numbers from 1 to N without duplicates.")  
                    continue  

                # Encrypt the plaintext  
                ciphertext = encrypt_row_transposition(plaintext, key)  
                print("Ciphertext:", ciphertext)  

            except ValueError:  
                print("Invalid input. Please enter numbers only.")  

        elif choice == '2':  
            # Exit the program  
            print("Exiting the program. Goodbye!")  
            break  

        else:  
            print("Invalid choice. Please select 1 or 2.")  

if __name__ == "__main__":  
    main()  