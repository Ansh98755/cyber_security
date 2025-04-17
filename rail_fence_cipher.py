def encrypt_rail_fence(text, rails):
    rail = ['' for _ in range(rails)]
    direction_down = False
    row = 0

    for char in text:
        rail[row] += char
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)

def decrypt_rail_fence(cipher, rails):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1

    return ''.join(result)
def main():
    while True:
        print("\n==== Rail Fence Cipher Menu ====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            rails = int(input("Enter the number of rails: "))
            encrypted = encrypt_rail_fence(text, rails)
            print("Encrypted Text:", encrypted)
        elif choice == '2':
            cipher = input("Enter the text to decrypt: ")
            rails = int(input("Enter the number of rails: "))
            decrypted = decrypt_rail_fence(cipher, rails)
            print("Decrypted Text:", decrypted)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
