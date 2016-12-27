from collections import Counter
from base_numeral_system import base_ns
import math


def fix_zeros(code: list, size: int):
    return code + ([0] * (size - len(code)))


def encode(text: str):
    # Generate codes for letters in sentence
    codes = {}

    letters = []
    amount = len(text)
    for letter, frequency in Counter(text).most_common():
        probability = frequency/amount
        letters.append((letter, probability))
    letters.reverse()

    q = 0
    previous_probability = 0

    while len(letters) > 0:
        letter, probability = letters.pop()
        q += previous_probability

        previous_probability = probability

        size = 1 + math.ceil(-math.log(probability, 2))
        code = base_ns.convert((q + probability / 2), 2, size).fraction[:size]
        codes[letter] = fix_zeros(code, size)

    # Encode phrase
    result = []
    for letter in text:
        result += codes[letter]

    return codes, result


def decode(codes: dict, encoded_text: list):
    result = ""
    i = 0
    while len(encoded_text) >= i:
        for letter, code in codes.items():
            if encoded_text[:i] == code:
                encoded_text = encoded_text[i:]
                result += letter
                i = 0
        i += 1
    return result
