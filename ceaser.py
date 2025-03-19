def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == 'decrypt':
                shift_amount = -shift_amount
            if char.islower():
                start = ord('a')
                
            else:
                start = ord('A')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += new_char
        else:
            result += char
    return result

def main():
    while True:
        print("\nMenu:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice in ('1', '2'):
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value (1-25): "))
            if  shift<1 or shift>25:
                        print("Shift value must be between 1 and 25.")
                        continue
                   
            else:
                        mode = 'encrypt' if choice == '1' else 'decrypt'
                        result_text = caesar_cipher(text, shift, mode)
                        print("Result:", result_text)
        elif choice == '3':
            print("Exiting the program")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()