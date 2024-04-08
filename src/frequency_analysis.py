from typing import Dict

from src.const import ALPHABET, CZECH_LETTER_FREQUENCIES


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


def create_frequency_mapping(
    language_frequencies: Dict[str, float], ciphertext_frequencies: Dict[str, float]
) -> Dict[str, str]:
    """
    Creates a letter mapping based on the frequency analysis of a language and a ciphertext.

    Parameters:
    - language_frequencies: A dictionary of letter frequencies for the language.
    - ciphertext_frequencies: A dictionary of letter frequencies for the ciphertext.

    Returns:
    - A dictionary mapping from ciphertext letters to language letters based on frequency analysis.
    """
    if len(language_frequencies) != len(ciphertext_frequencies):
        raise Exception(
            f"Given dictionaries language_frequencies \
            and ciphertext_frequencies does not have the same length!"
        )

    sorted_language_ngrams = sorted(language_frequencies.values(), key=lambda val: val)
    sorted_ciphertext_ngrams = sorted(
        ciphertext_frequencies.values(), key=lambda val: val
    )

    mapping = {}
    for ciphertext_ngram, language_ngram in zip(
        sorted_ciphertext_ngrams, sorted_language_ngrams
    ):
        mapping[ciphertext_ngram] = language_ngram

    return mapping


def map_segment(ciphertext_segment: str, mapping: Dict[str, str]) -> str:
    """
    Maps each letter in the ciphertext segment to a new letter based on the provided mapping.

    Parameters:
    - ciphertext_segment: A string representing a segment of the ciphertext.
    - mapping: A dictionary mapping each letter in the ciphertext to a corresponding plaintext letter.

    Returns:
    - A string representing the decrypted segment of the ciphertext.
    """
    mapped_text = ""
    for char in ciphertext_segment:
        if char in mapping:
            mapped_text += mapping[char]
        else:
            mapped_text += char
    return mapped_text


def calculate_chi_square(
    observed_frequencies: Dict[str, int],
    expected_frequencies: Dict[str, float],
    shift: int,
) -> float:
    chi_square = 0
    total_letters = sum(observed_frequencies.values())

    adjusted_observed = {
        letter: observed_frequencies.get(letter, 0) / total_letters
        for letter in ALPHABET
    }

    for letter, observed in adjusted_observed.items():
        shifted_letter = ALPHABET[(ALPHABET.index(letter) - shift) % len(ALPHABET)]
        expected = expected_frequencies.get(shifted_letter, 0)
        if expected > 0:
            chi_square += ((observed - expected) ** 2) / expected

    return chi_square


def find_best_shift_for_segment(
    ciphertext_segment: str, expected_frequencies: Dict[str, float]
) -> int:
    observed_frequencies = analyze_single_char_frequencies(ciphertext_segment)

    chi_square_result = {}
    for shift in range(len(ALPHABET)):
        chi_square = calculate_chi_square(
            observed_frequencies, expected_frequencies, shift
        )
        chi_square_result[shift] = chi_square

    return min(chi_square_result.items(), key=lambda v: v[1])[0]


def decrypt_key(ciphertext:str, key_length: int) -> str:
    shifts = []
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        shifts.append(
            find_best_shift_for_segment(
                ciphertext_segment=segment, expected_frequencies=CZECH_LETTER_FREQUENCIES,
            )
        )

    key = "".join(ALPHABET[shift] for shift in shifts)
    return key