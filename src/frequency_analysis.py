from typing import Dict
from collections import Counter
import numpy as np

from src.const import ENGLISH_ALPHABET, ENGLISH_LETTER_FREQUENCIES


def analyze_single_char_frequencies(input_text: str) -> Dict[str, int]:
    frequencies = {}
    for char in input_text:
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def analyze_ngrams_frequencies(input_text: str, n: int = 2) -> Dict[str, int]:
    ngrams_frequencies = {}

    for i in range(len(input_text) - n + 1):
        ngram = input_text[i : i + n]
        if all(char.isalpha() for char in ngram):
            if ngram in ngrams_frequencies:
                ngrams_frequencies[ngram] += 1
            else:
                ngrams_frequencies[ngram] = 1

    return ngrams_frequencies


def calculate_chi_squared(observed: Counter, expected: Dict[str, float]) -> float:
    chi_squared = 0.0
    for letter in ENGLISH_ALPHABET:
        observed_freq = observed.get(letter, 0)
        expected_freq = expected[letter] * sum(observed.values())
        chi_squared += (observed_freq - expected_freq) ** 2 / expected_freq
    return chi_squared


def guess_key_segment(segment: str) -> str:
    lowest_chi_squared = np.inf
    best_shift = None
    for shift in range(len(ENGLISH_ALPHABET)):
        shifted_segment = "".join(
            ENGLISH_ALPHABET[
                (ENGLISH_ALPHABET.index(c) - shift) % len(ENGLISH_ALPHABET)
            ]
            for c in segment
        )

        chi_squared = calculate_chi_squared(
            Counter(shifted_segment), ENGLISH_LETTER_FREQUENCIES
        )
        
        if chi_squared < lowest_chi_squared:
            lowest_chi_squared = chi_squared
            best_shift = shift
    return ENGLISH_ALPHABET[best_shift] if best_shift else ""


def key_frequency_analysis(ciphertext: str, key_length: int = 3) -> str:
    key = ""
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        key += guess_key_segment(segment)

    return key.upper()
