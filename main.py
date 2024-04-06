from pathlib import Path

from src.const import ENGLISH_LETTER_FREQUENCIES
from src.frequency_analysis import key_frequency_analysis
from src.kasiski import kasiski_examination
from src.utils import read_file, normalize_text, save_text_to_file
from src.vigenere import vigenere_encrypt
from src.index_of_coincidence import index_of_coincidence

if __name__ == "__main__":
    plaintext = read_file(Path("data/great_gatsby.txt"))

    key = "KEY"
    ciphertext = vigenere_encrypt(plaintext, key)
    save_text_to_file(Path("data/great_gatsby_cipher.txt"), ciphertext)

    # ciphertext = read_file(Path("data/great_gatsby_cipher.txt"))
    ciphertext = normalize_text(ciphertext)
    # print(kasiski_examination(ciphertext=ciphertext))

    # print(key_frequency_analysis(ciphertext=ciphertext, key_length=5))

    print(index_of_coincidence(ciphertext=ciphertext, max_key_length=20))
