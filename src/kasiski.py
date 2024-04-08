from math import gcd
from functools import reduce
from typing import Dict, List, Tuple, Set
from collections import defaultdict, Counter


def find_repeated_sequences(
    ciphertext: str, min_seq_length: int = 3
) -> Dict[str, List[int]]:
    sequences = defaultdict(list)
    for i in range(len(ciphertext) - min_seq_length + 1):
        seq = ciphertext[i : i + min_seq_length]
        if seq not in sequences:
            for j in range(i, len(ciphertext) - min_seq_length + 1):
                if ciphertext[j : j + min_seq_length] == seq:
                    sequences[seq].append(j)

    sequences = {
        seq: positions for seq, positions in sequences.items() if len(positions) > 1
    }
    return sequences


def calculate_distances(sequences: Dict[str, List[int]]) -> Dict[str, List[int]]:
    distances = {}
    for seq, positions in sequences.items():
        distances[seq] = [
            positions[i] - positions[i - 1] for i in range(1, len(positions))
        ]
    return distances


def find_gcd_and_factors(distances_by_seq: Dict[str, List[int]]) -> Dict[str, Set[int]]:
    gcd_and_factors = {}
    for seq, distances in distances_by_seq.items():
        if distances:
            overall_gcd = reduce(gcd, distances)
            factors = {i for i in range(1, overall_gcd + 1) if overall_gcd % i == 0}
            gcd_and_factors[seq] = factors
    return gcd_and_factors


def pick_possible_keys(
    factors_by_seq: Dict[str, Set[int]], max_key_length: int
) -> Dict[int, int]:
    key_length_counts = {}
    for factors in factors_by_seq.values():
        for factor in factors:
            if factor > 2 and factor <= max_key_length:
                if factor not in key_length_counts:
                    key_length_counts[factor] = 1
                else:
                    key_length_counts[factor] += 1
    return dict(
        sorted(key_length_counts.items(), key=lambda item: item[1], reverse=True)
    )


def kasiski_examination(ciphertext: str, max_sequence_len: int = 7) -> Tuple[int, int]:
    possible_keys = {}
    for seq_length in range(3, max_sequence_len):
        sequences_positions = find_repeated_sequences(
            ciphertext=ciphertext, min_seq_length=seq_length
        )
        distances = calculate_distances(sequences_positions)
        factors = find_gcd_and_factors(distances)
        possible_keys_per_seq = pick_possible_keys(
            factors_by_seq=factors, max_key_length=10
        )
        if possible_keys_per_seq:
            if not possible_keys:
                possible_keys = possible_keys_per_seq
            else:
                for key, value in possible_keys_per_seq.items():
                    possible_keys[key] += value 

    most_common_key, most_common_count = Counter(possible_keys).most_common(1)[0]
    return most_common_key, most_common_count
