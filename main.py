from pathlib import Path
from src.encryption import vigenere_encrypt
from src.utils import read_file, normalize_text, save_text_to_file
from src.const import ENGLISH_LETTER_FREQUENCIES
from src.kasiski import kasiski_examination

if __name__ == "__main__":
    frank = read_file(Path("data/frankenstein.txt"))

    key = "KATERI"
    ciphertext = vigenere_encrypt(frank, key)
    # print(f"Ciphertext: {ciphertext}")
    # save_text_to_file(Path("data/frankenstein_cipher.txt"), ciphertext)

    # ciphertext = read_file(Path("data/frankenstein_cipher.txt"))
    ciphertext = normalize_text(ciphertext)
    print(kasiski_examination(ciphertext=ciphertext))
