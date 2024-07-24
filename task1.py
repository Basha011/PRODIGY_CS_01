def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice not in ('e', 'd'):
        print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")
        return

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print("Encrypted message:", encrypted_text)
    else:
        decrypted_text = decrypt(text, shift)
        print("Decrypted message:", decrypted_text)


if __name__ == "__main__":
    main()
