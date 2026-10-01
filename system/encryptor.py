
def encryptor_func():
    while True:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                    "k", "l", "m", "n", "o", "p", "q", "r",
                    "s", "t", "u", "v", "w", "x", "y", "z"]
        mode_choice_encryptor = input("Choose mode: letter/word/exit: ").lower()
        if mode_choice_encryptor == "exit":
                print("Exiting encryptor.")
                break
        elif mode_choice_encryptor == "letter":
            while True:
                enter_letter = input("Enter letter to encrypt: ").lower()
                if enter_letter in alphabet:
                    index = alphabet.index(enter_letter)
                    encrypted_index = (index + 3) % len(alphabet)
                    encrypted_letter = alphabet[encrypted_index]
                    print(f"Encrypted letter: {encrypted_letter}")
                elif enter_letter=="exit":
                    print("Exiting encryptor.")
                else:
                    print("Letter not in alphabet.")
        elif mode_choice_encryptor == "word":
            # print("Word encryption mode is currently unavailable.")
            print("Word encryption mode activated. Enter '!exit' or '/exit' to quit.")
            enter_word = input("Enter word to encrypt: ").lower()
            encrypted_word = ""
            for letter in enter_word:
                if letter in alphabet:
                    index = alphabet.index(letter)
                    encrypted_index = (index + 3) % len(alphabet)
                    encrypted_letter = alphabet[encrypted_index]
                    encrypted_word += encrypted_letter
                elif letter == " ":
                    encrypted_word += " "  # Preserve spaces
                elif letter == "!" or letter == "/":
                    print("Exiting encryptor.")
                    return
                else:
                    encrypted_word += letter  # Non-alphabet characters remain unchanged
            print(f"Encrypted word: {encrypted_word}")
        else:
            print("Invalid mode choice.")

if __name__ == "__main__":
    encryptor_func()