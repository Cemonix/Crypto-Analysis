from typing import Dict


def analyze_single_char_frequencies(input_text: str) -> Dict[str, int]:
    frequencies = {}
    for char in input_text:
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def analyze_ngrams_frequencies(input_text: str, n: int = 2) -> Dict[str, int]:
    ngrams_frequencies = {}

    for i in range(len(input_text) - n + 1):
        ngram = input_text[i:i+n]
        if all(char.isalpha() for char in ngram):
            if ngram in ngrams_frequencies:
                ngrams_frequencies[ngram] += 1
            else:
                ngrams_frequencies[ngram] = 1

    return ngrams_frequencies