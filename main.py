from pathlib import Path

from src.frequency_analysis import decrypt_key
from src.kasiski import kasiski_examination
from src.utils import read_file, normalize_text, save_text_to_file
from src.vigenere import vigenere_encrypt, vigenere_decrypt
from src.index_of_coincidence import index_of_coincidence


if __name__ == "__main__":
    # plaintext = read_file(Path("data/frankenstein.txt"))

    # key = "KEYLA"
    # ciphertext = vigenere_encrypt(plaintext, key)
    # save_text_to_file(Path("data/frankenstein_cipher.txt"), ciphertext)

    ciphertext = read_file(Path("data/vigenere_cipher_2.txt"))
    ciphertext = normalize_text(ciphertext)

    estimated_key_length, _ = kasiski_examination(ciphertext=ciphertext)
    # print(index_of_coincidence(ciphertext=ciphertext, max_key_length=20))

    decrypted_key = decrypt_key(ciphertext, estimated_key_length)
    print(decrypted_key)

    print(vigenere_decrypt(ciphertext=ciphertext, key=decrypted_key))