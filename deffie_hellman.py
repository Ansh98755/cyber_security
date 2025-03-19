def diffie_hellman():
    p = int(input("Enter the prime number for p: "))
    g = int(input("Enter the prime number for g: "))

    bob_private_no = int(input("Bob, enter your private number: "))
    alice_private_no = int(input("Alice, enter your private number: "))
    A_bob = pow(g, bob_private_no, p)
    B_alice = pow(g, alice_private_no, p)
    bob_private_key = pow(B_alice, bob_private_no, p)
    alice_private_key = pow(A_bob, alice_private_no, p)
    print(f"\nAlice's Public Key (A): {A_bob}")
    print(f"Bob's Public Key (B): {B_alice}")
    print(f"Bob's Private Key: {bob_private_key}")
    print(f"Alice's Private Key: {alice_private_key}\n")


def menu():
    while True:
        print("\nMenu:")
        print("1. Perform Diffie-Hellman Key Exchange")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            diffie_hellman()
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
