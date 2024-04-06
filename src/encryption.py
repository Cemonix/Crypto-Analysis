def vigenere_encrypt(plaintext: str, key: str) -> str:
    def format_cipher(text: str) -> str:
        return ' '.join(text[i:i+5] for i in range(0, len(text), 5))

    def encrypt_char(p: str, k: str) -> str:
        return chr(((ord(p) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
    
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()

    key_length = len(key)
    cipher_text = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            cipher_text += encrypt_char(char, key[i % key_length])
    
    return format_cipher(cipher_text)