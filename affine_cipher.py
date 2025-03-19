import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None
def affine_cipher(text, a, b, mode):
    if gcd(a, 26) != 1:
        print("Key 'a' must be coprime with 26.")
        return ""

    result = ""
    text = text.lower() 

    if mode == 'encrypt':
        for char in text:
            if char.isalpha():
                encrypted_char = chr(((a * (ord(char) - 97) + b) % 26) + 97)
                result += encrypted_char
            else:
                result += char  

    elif mode == 'decrypt':
        a_inv = mod_inverse(a, 26)
        if a_inv is None:
            print("Modular inverse does not exist for the given 'a'.")
            return ""

        for char in text:
            if char.isalpha():
                decrypted_char = chr(((a_inv * ((ord(char) - 97 - b)) % 26 + 26) % 26) + 97)
                result += decrypted_char
            else:
                result += char  

    return result
def main():
    while True:
        print("\n===== Affine Cipher Menu =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice in ['1', '2']:
            text = input("Enter text: ")
            a = int(input("Enter key 'a' (coprime with 26 and in range 1-25): "))
            b = int(input("Enter key 'b' (0-25): "))

            if not (1 <= a <= 25 and 0 <= b <= 25 and gcd(a, 26) == 1):
                print("Invalid keys! 'a' must be coprime with 26, and both keys should be in the correct range.")
                continue

            mode = 'encrypt' if choice == '1' else 'decrypt'
            print("Result:", affine_cipher(text, a, b, mode))

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()
