from src.const import ALPHABET


def vigenere_encrypt(plaintext: str, key: str) -> str:
    def format_cipher(text: str) -> str:
        return " ".join(text[i : i + 5] for i in range(0, len(text), 5))

    def encrypt_char(p: str, k: str) -> str:
        return chr(((ord(p) - ord("A")) + (ord(k) - ord("A"))) % 26 + ord("A"))

    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()

    key_length = len(key)
    cipher_text = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            cipher_text += encrypt_char(char, key[i % key_length])

    return format_cipher(cipher_text)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key_indices = [ALPHABET.index(k) for k in key.lower()]
    decrypted_text = ""

    for i, char in enumerate(ciphertext):
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            key_index = key_indices[i % len(key)]
            decrypted_char = ALPHABET[(char_index - key_index) % 26]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text
