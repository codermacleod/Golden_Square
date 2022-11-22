def encode(text, key):
    cipher = make_cipher(key)
    print(f"Cipher: {cipher}")
    ciphertext_chars = []
    print(f"Iterate over letters in text:{text}:")

    for i in text:
        print(f"Letter {i}")
        ciphered_char = chr(65 + cipher.index(i))
        print(f"Ciphered character:{ciphered_char}")
        # print(f"Before append:{ciphertext_chars}")
        ciphertext_chars.append(ciphered_char)
        print(f"After append:{ciphertext_chars}")

    # print(f"{ciphered_char}")
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    print("Now decoding!")
    print(f"Encrypted text: {encrypted}")
    print(f"The Key: {key}")
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        print(f"'i' Before encrypt: {i}")
        plain_char = cipher[ord(i) - 65]
        print(f"ord(i) is: {ord(i)} ")
        print(plain_char)
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    print(f"The key: {key}")
    alphabet = [chr(i + 96) for i in range(1, 27)]
    print(f"Starting alphabet: {alphabet}")
    cipher_with_duplicates = list(key) + alphabet
    print(f"cipher_with_duplicates: {cipher_with_duplicates}")
    cipher = []
    print("Go through cipher_with_duplicates list:...")
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    print(f"Cipher without duplicates: {cipher}")
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
