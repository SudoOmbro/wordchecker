from typing import List, Dict


class InputModes:

    ADD: int = 0
    GET_REFERENCE: int = 1
    GET_WORD_NUMBER: int = 2
    PLAY: int = 3


class ValidationContext:

    # globals
    word_length: int
    input_mode: int
    allowed_words: List[str]  # I would implement this as a tree

    # game locals
    reference_word: str
    reference_word_letters: Dict[str, int]  # stores the occurrences of every letter in the reference word
    word_number: int
    word_count: int
