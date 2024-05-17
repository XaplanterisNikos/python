def decrypt_message(message):
    decrypted_message = ""
    for char in message:
        if not char.isnumeric():
            decrypted_message += char
    return decrypted_message


def main():
    strange_message = "432H3525el523l52o5 523C532F52"
    decrypted_message = decrypt_message(strange_message)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == '__main__':
    main()
