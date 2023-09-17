ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sanitize_input(text):
    return text.replace(" ", "").upper()

def validate_text(text):
    for char in text:
        if char not in ALPHABET:
            raise ValueError(f"Caracterul '{char}' nu aparține alfabetului.")
    return text

def validate_key2(key2):
    if len(key2) < 7:
        raise ValueError("Cheia 2 trebuie să aibă o lungime de cel puțin 7 caractere.")
    for char in key2:
        if char not in ALPHABET:
            raise ValueError("Cheia 2 trebuie să conțină doar litere ale alfabetului latin.")
    return key2

def generate_shifted_alphabet(key2):
    # First, remove duplicate characters from key2
    unique_chars = ""
    for char in key2:
        if char not in unique_chars:
            unique_chars += char

    # Next, generate the permuted alphabet
    shifted = unique_chars
    for char in ALPHABET:
        if char not in unique_chars:
            shifted += char

    return shifted

def cezar_encrypt(text, key):
    source_alphabet = ALPHABET
    result = ""
    for char in text:
        idx = source_alphabet.index(char)
        result += source_alphabet[(idx + key) % 26]
    return result

def cezar_decrypt(text, key):
    source_alphabet = ALPHABET
    result = ""
    for char in text:
        idx = source_alphabet.index(char)
        result += source_alphabet[(idx - key) % 26]
    return result

def cezar_encrypt_2keys(text, key1, key2):
    encrypted_text = cezar_encrypt(text, key1)
    result = ""
    source_alphabet = ALPHABET
    key2_alphabet = generate_shifted_alphabet(key2)
    for char in encrypted_text:
        idx = source_alphabet.index(char)
        result += key2_alphabet[idx]
    return result

def cezar_decrypt_2keys(text, key1, key2):
    source_alphabet = ALPHABET
    key2_alphabet = generate_shifted_alphabet(key2)
    intermediate_text = ""
    for char in text:
        idx = key2_alphabet.index(char)
        intermediate_text += source_alphabet[idx]
    return cezar_decrypt(intermediate_text, key1)

def main():
    global ENCRYPTED_MESSAGE

    while True:
        print("Alegeți operația:")
        print("1 - Criptare")
        print("2 - Decriptare")
        print("3 - Criptare cu 2 chei")
        print("4 - Decriptare cu 2 chei")
        print("0 - Ieșire")

        choice = input("Selectați opțiunea: ")

        if choice == '0':
            break

        if choice in ['1', '3']:
            mesaj = input("Introduceți mesajul pentru criptare: ")
            mesaj_curatit = sanitize_input(mesaj)

            try:
                validate_text(mesaj_curatit)
            except ValueError as e:
                print(e)
                continue

            cheie1 = int(input("Introduceți cheia 1 (între 1 și 25 inclusiv): "))
            if not 1 <= cheie1 <= 25:
                print("Cheia 1 incorectă. Introduceți o valoare între 1 și 25.")
                continue

            if choice == '1':
                ENCRYPTED_MESSAGE = cezar_encrypt(mesaj_curatit, cheie1)
                print("Mesajul criptat este:", ENCRYPTED_MESSAGE)
            else:
                cheie2 = input("Introduceți cheia 2 (minim 7 caractere): ")
                try:
                    cheie2 = validate_key2(sanitize_input(cheie2))
                except ValueError as e:
                    print(e)
                    continue

                ENCRYPTED_MESSAGE = cezar_encrypt_2keys(mesaj_curatit, cheie1, cheie2)
                print("Alfabetul permutat pe baza cheii 2 este:", generate_shifted_alphabet(cheie2))
                print("Mesajul criptat cu 2 chei este:", ENCRYPTED_MESSAGE)

        elif choice in ['2', '4']:
            mesaj_criptat = input("Introduceți mesajul criptat pentru decriptare: ")
            mesaj_curatit = sanitize_input(mesaj_criptat)

            try:
                validate_text(mesaj_curatit)
            except ValueError as e:
                print(e)
                continue

            cheie1 = int(input("Introduceți cheia 1 (între 1 și 25 inclusiv): "))
            if not 1 <= cheie1 <= 25:
                print("Cheia 1 incorectă. Introduceți o valoare între 1 și 25.")
                continue

            if choice == '2':
                mesaj_decriptat = cezar_decrypt(mesaj_curatit, cheie1)
                print("Mesajul decriptat este:", mesaj_decriptat)
            else:
                cheie2 = input("Introduceți cheia 2: ")
                try:
                    cheie2 = validate_key2(sanitize_input(cheie2))
                except ValueError as e:
                    print(e)
                    continue

                mesaj_decriptat = cezar_decrypt_2keys(mesaj_curatit, cheie1, cheie2)
                print("Mesajul decriptat cu 2 chei este:", mesaj_decriptat)

        else:
            print("Opțiune invalidă. Încercați din nou.")

if __name__ == "__main__":
    ENCRYPTED_MESSAGE = ""
    main()
