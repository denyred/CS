# Playfair Cipher Implementation

**By: Spataru Dionisie**

**Course: Cryptography and Programming Security**

**Assistant Professor: Catalin Mitu**
## Introduction
<div style="text-align:justify">
The Playfair cipher is a manual symmetric encryption technique invented in 1854 by Charles Wheatstone, but was named after Lord Playfair who promoted the use of the cipher. It was used mainly to encrypt tactical communications by the British forces in World War I and for the protection of commercial flag communications.

The Playfair cipher encrypts pairs of letters (digraphs) instead of single letters, making frequency analysis more difficult. The key is a 5x5 matrix of letters generated from a keyword, where each letter occurs only once. The letters 'I' and 'J' are combined into one location. The rest of the positions are filled with the remaining letters in alphabetical order. 
</div>
## Algorithm Description

The algorithm works as follows:

1. The key is used to generate a 5x5 matrix of unique letters. 'I' and 'J' share a location.

2. The plaintext message is converted to digraphs (pairs of letters) by adding 'X' if needed to complete the pair. 

3. For each pair of letters:

   - If they are in the same row of the matrix, each is shifted to the right cyclically.

   - If they are in the same column, each is shifted down cyclically. 

   - Otherwise, each letter is swapped with the one in the other letter's row, while keeping the column the same.

4. The ciphertext is generated from the encrypted digraphs.
<div style="text-align:justify">
To decrypt, the inverse mappings are applied to convert the ciphertext back to the plaintext digraphs and message.
</div>

## Implementation 

The Python implementation has the following key functions:

- `create_matrix()` - Generates the 5x5 key matrix from the keyword

- `find_position()` - Finds the row and column of a letter in the matrix  

- `encrypt_pair()` - Encrypts a pair of letters based on their positions

- `decrypt_pair()` - Decrypts a pair of letters based on their positions  

- `playfair_cipher()` - Implements the full Playfair encryption/decryption algorithm

The driver code allows the user to choose to encrypt or decrypt a message using a provided key.

##Code snippet

```python
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
```




## Conclusion
<div style="text-align:justify">
The Playfair cipher was an influential development in the field of cryptography when it was invented in 1854. At the time, most ciphers were easily broken using frequency analysis of single letters. By encrypting pairs of letters, the Playfair cipher eliminated much of the letter frequency information that cryptanalysts relied on to crack monoalphabetic substitution ciphers.
While the Playfair cipher is no longer secure compared to modern algorithms, it still holds historical significance as one of the early polyalphabetic ciphers. When it was introduced, the Playfair cipher was considered very difficult to break without knowing the secret key. It remained in active use for several decades, especially by the British military.
This Python implementation of the Playfair cipher serves as a good educational example. It illustrates classical encryption concepts like using a key square matrix, encrypting letter pairs, and applying simple substitution rules. Recreating historical ciphers helps provide insight into the evolution of cryptographic techniques over time.
Studying the Playfair cipher also highlights the "arms race" between cryptographers trying to hide information, and cryptanalysts trying to reveal it. As ciphers become more advanced, codebreaking techniques also progress. This back-and-forth continues to this day, with cryptographers trying to stay one step ahead of adversaries. While the Playfair cipher is obsolete today, it represented an creative innovation in its time period.
In summary, this Playfair cipher implementation exemplifies the ingenuity of early cryptographers like Wheatstone and Playfair. It provides a glimpse into the origins of polyalphabetic substitution ciphers that paved the way for more advanced algorithms used in modern encryption. Recreating historical ciphers can be an enlightening educational experience for aspiring cryptographers.
</div>

## Repository link
