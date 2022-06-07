from functools import cache
from typing import Dict


def add_letter_to_dictionary(letter, dictionary):
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1


LETTERS_VALUES: Dict[str, int] = {}  # implement in C as a giant switch

# generate dictionary
_value = 1
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz9876543210_-":
    LETTERS_VALUES[letter] = _value
    _value += 1


@cache
def get_word_hash(word: str, length: int):  # cache the result for this function (save it with the allowed word)
    # usa per salvare le parole le parole ammesse in ordine lessicografico
    value: int = 0
    for i in range(length):  # for (int i=0; i<length; i++)
        value += LETTERS_VALUES[word[i]] * (length - i)
    return value
