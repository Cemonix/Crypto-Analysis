from collections import Counter
from typing import List


def calculate_ioc(ciphertext: str) -> float:
    n = len(ciphertext)
    if n <= 1:
        return 0

    letter_frequencies = Counter(ciphertext)
    ioc = sum(freq * (freq - 1) for freq in letter_frequencies.values()) / (n * (n - 1))
    return ioc


def average_ioc(ciphertext: str, key_length: int) -> float:
    ioc_sum = 0
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        ioc_sum += calculate_ioc(segment)
    average_ioc = ioc_sum / key_length
    return average_ioc


def index_of_coincidence(ciphertext: str, max_key_length: int) -> List[float]:
    return [average_ioc(ciphertext, key_length) for key_length in range(1, max_key_length + 1)]
