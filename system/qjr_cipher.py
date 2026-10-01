
# TODO: QJRcipher

from random import randint

def qjr_cipher_encrypt(plaintext: str, key: int):
    encrypted = []
    # key_change = []
    for char in plaintext:
        if char.isalpha():
            if char == char.lower():
                encrypted.append(str(int(ord(char.upper()))+int(key)))

            elif char == char.upper():
                encrypted.append(str(int(ord(char.lower()))+int(key)))

        else:
            encrypted.append(str(int(ord(char))+key))


    return " ".join(encrypted)

def qjr_cipher_decrypt(encrypted: list, key: int):
    decrypted = []
    # key_change = []
    for char in plaintext:
        if char.isalpha():
            if char == char.lower():
                decrypted.append(str(chr(char.upper())+int(key)))

            elif char == char.upper():
                encrypted.append(str(int(ord(char.lower()))+int(key)))

        else:
            encrypted.append(str(int(ord(char))+key))


    return " ".join(encrypted)


if __name__ == "__main__":
    text = "Hello, World!!! 1"
    print(qjr_cipher_encrypt(text, 0))
    print(qjr_cipher_encrypt(text, 1))
    print(qjr_cipher_encrypt(text, 2))
    print(qjr_cipher_encrypt(text, 3))
    print(qjr_cipher_encrypt(text, 4))
    print(qjr_cipher_encrypt(text, 5))
    print(qjr_cipher_encrypt(text, 10))
    print(qjr_cipher_encrypt(text, 15))
    print(qjr_cipher_encrypt(text, 20))
    print(qjr_cipher_encrypt(text, 25))
    print(qjr_cipher_encrypt(text, 50))
    print(qjr_cipher_encrypt(text, 75))
    print(qjr_cipher_encrypt(text, 80))
    print(qjr_cipher_encrypt(text, 100))
    print(qjr_cipher_encrypt(text, 1024))
