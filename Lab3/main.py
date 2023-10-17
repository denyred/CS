# Creates the 5x5 key matrix from the encryption key
def create_matrix(key):
    # Implementation details
    matrix = []
    key = key.upper().replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZȘȚĂÎÂ'
    for char in key:
        if char in alphabet and char not in matrix:
            matrix.append(char)
            alphabet = alphabet.replace(char, '')
    matrix.extend(list(alphabet))
    matrix = [matrix[i:i+6] for i in range(0, len(matrix), 6)]
    return matrix

# Finds the position of a character in the key matrix
def find_position(matrix, char):
    # Implementation details
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == char:
                return i, j

# Encrypts a pair of characters based on their positions in the key matrix
def encrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)


    if row1 == row2:
        return matrix[row1][(col1 + 1) % 6], matrix[row2][(col2 + 1) % 6]
    elif col1 == col2:
        return matrix[(row1 + 1) % 6][col1], matrix[(row2 + 1) % 6][col2]
    else:
        return matrix[row1][col2], matrix[row2][col1]

# Decrypts a pair of characters based on their positions in the key matrix
def decrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 6], matrix[row2][(col2 - 1) % 6]
    elif col1 == col2:
        return matrix[(row1 - 1) % 6][col1], matrix[(row2 - 1) % 6][col2]
    else:
        return matrix[row1][col2], matrix[row2][col1]

# Implements the full Playfair cipher encryption/decryption algorithm
def playfair_cipher(key, text, mode='encrypt', original_length=None):
    # Generate the key matrix
    matrix = create_matrix(key)
    # Prepare the plaintext by converting to uppercase and
    # removing 'J' characters
    text = text.upper().replace('J', 'I')
    # Split text into digraph pairs
    pairs = []

    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        if len(pair) < 2:
            # Padd lone characters with 'X'
            pair += 'X'
        pairs.append(pair)

    # Encrypt/decrypt each pair of characters
    result = []
    for pair in pairs:
        if mode == 'encrypt':
            # Encrypt the digraph
            encrypted_pair = encrypt_pair(matrix, pair[0], pair[1])
        else:
            # Decrypt the digraph
            encrypted_pair = decrypt_pair(matrix, pair[0], pair[1])
        result.append(encrypted_pair[0] + encrypted_pair[1])

    # For decryption, may need to trim last 'X' padding
    if mode == 'decrypt' and original_length is not None and original_length % 2 != 0:

        return ''.join(result)[:-1]

    return ''.join(result)


# Driver code
if __name__ == "__main__":
    operation = input("Operation 1-Enc/2-Dec: ").strip().lower()
    key = input("Key : ")

    while len(key) < 7:
        key = input("Key should be 7+ characters")

    if operation == "1":
        message = input("Message: ")
        while len(message) % 2 != 0:
            message += "X"
        print("Encrypted message:", playfair_cipher(key, message))
    elif operation == "2":
        cryptogram = input("Enter the cryptogram to decrypt: ")
        original_length = len(cryptogram)
        while len(cryptogram) % 2 != 0:
            cryptogram += "X"
        print("Decrypted message:", playfair_cipher(key, cryptogram, mode='decrypt', original_length=original_length))
    else:
        print("Invalid operation chosen.")
