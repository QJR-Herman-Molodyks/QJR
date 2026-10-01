latine_lowercase = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
     "w", "x", "y", "z"]

latine_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                    "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]

cyrillic_lowercase = ["а", "б", "в", "г", "ґ", "д", "е", "є",
                      "ж", "з", "и", "і", "ї", "й",
                      "к", "л", "м", "н", "о", "п", "р", "с",
                      "т", "у", "ф", "х", "ц", "ч", "ш", "щ",
                      "ь", "ю", "я"]

cyrillic_uppercase = ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є",
                      "Ж", "З", "И", "І", "Ї", "Й",
                      "К", "Л", "М", "Н", "О", "П", "Р", "С",
                      "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ",
                      "Ь", "Ю", "Я"]



cymbols_table = [" ", ".", ",", ";", ":", "'", '"', "/",
                 "-", "=", "+", "_", "!", "@", "#", "$",
                 "%", "^", "&", "*", "(", ")", "`", "~",

                 ""]

def cesar_encode(text, shift=3):
    result = []
    text = list(text)
    for letter in text:
        if letter in latine_lowercase:
            index = (latine_lowercase.index(letter) + shift) % len(latine_lowercase)
            result.append(latine_lowercase[index])

        elif letter in latine_uppercase:
            index = (latine_uppercase.index(letter) + shift) % len(latine_uppercase)
            result.append(latine_uppercase[index])

        elif letter in cyrillic_lowercase:
            index = (cyrillic_lowercase.index(letter) + shift) % len(cyrillic_lowercase)
            result.append(cyrillic_lowercase[index])

        elif letter in cyrillic_uppercase:
            index = (cyrillic_uppercase.index(letter) + shift) % len(cyrillic_uppercase)
            result.append(cyrillic_uppercase[index])

        else:
            # Keep symbols and other characters as-is
            result.append(letter)

    result = "".join(result)
    # print(result)
    return result

def cesar_decode(text, shift=3):
    result = []
    text = list(text)
    for letter in text:
        if letter in latine_lowercase:
            index = (latine_lowercase.index(letter) - shift) % len(latine_lowercase)
            result.append(latine_lowercase[index])

        elif letter in latine_uppercase:
            index = (latine_uppercase.index(letter) - shift) % len(latine_uppercase)
            result.append(latine_uppercase[index])

        elif letter in cyrillic_lowercase:
            index = (cyrillic_lowercase.index(letter) - shift) % len(cyrillic_lowercase)
            result.append(cyrillic_lowercase[index])

        elif letter in cyrillic_uppercase:
            index = (cyrillic_uppercase.index(letter) - shift) % len(cyrillic_uppercase)
            result.append(cyrillic_uppercase[index])

        else:
            # Keep symbols and other characters as-is
            result.append(letter)

    result_decode = "".join(result)
    # print(result)
    return result_decode

if __name__ == "__main__":
    while True:
        print(cesar_encode(input("Enter a text: ")))
        print(cesar_decode(input("Enter a text: ")))