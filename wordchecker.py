from copy import copy
from typing import Dict, Callable, List

from classes import ValidationContext, InputModes
from commands import handle_command
from utils import add_letter_to_dictionary, get_word_hash


def add_word(word: str, context: ValidationContext) -> int:
    context.allowed_words.append(word)
    context.allowed_words.sort(key=lambda w: get_word_hash(w, context.word_length))  # in C I would use a binary tree
    return 0


def get_reference_word(word: str, context: ValidationContext) -> int:
    context.reference_word = word
    context.reference_word_letters = {}
    for letter in word:
        add_letter_to_dictionary(letter, context.reference_word_letters)
    context.input_mode = InputModes.GET_WORD_NUMBER
    return 0


def get_word_number(num: str, context: ValidationContext) -> int:
    context.word_number = int(num)
    context.input_mode = InputModes.PLAY
    return 0


def check_word(word: str, context: ValidationContext) -> int:
    if word not in context.allowed_words:
        print("not_exists")
        return 0
    result: List[str] = []  # I'm using a list here to make working with the result easier, in C it's just a string
    correct_letters: Dict[str, int] = {}  # stores the occurrences of letters in correct positions in the current word
    wrong_letters: Dict[str, int] = {} # stores the occurrences of letters in wrong positions in the current word
    sub_letters: Dict[str, int] = {}  # n - c
    marked_positions: List[int] = []  # positions that require a second checking pass
    word_states: Dict[int, Dict[str, int]] = {}  # stores the state of the word up until a certain position
    equalities: int = 0  # used to check if the 2 words are the same
    # find occurrences of correct letters in current word
    for i in range(context.word_length):
        if word[i] == context.reference_word[i]:
            add_letter_to_dictionary(word[i], correct_letters)  # this would be int(letter) - 45
            result.append("+")
            equalities += 1
        elif word[i] not in context.reference_word:
            result.append("/")
        else:
            result.append("|")
            word_states[i] = copy(wrong_letters)
            add_letter_to_dictionary(word[i], wrong_letters)
            marked_positions.append(i)
    # if the words are the same, print "ok" and finish the game
    if equalities == context.word_length:
        print("ok")
        return 1
    # calculate sub letters
    for letter in context.reference_word_letters:
        sub_letters[letter] = context.reference_word_letters[letter] - correct_letters.get(letter, 0)
    # check marked positions
    for position in marked_positions:
        letter = word[position]
        if word_states[position].get(letter, 0) >= sub_letters.get(letter, 0):
            result[position] = "/"
    # print results
    print("".join(result))
    # TODO print constraints? What the fuck are those
    # increase word count and end game if necessary
    context.word_count += 1
    if context.word_count == context.word_number:
        print("ko")
        context.input_mode = InputModes.ADD
    return 0


INPUT_HANDLERS: Dict[int, Callable[[str, ValidationContext], int]] = {
    InputModes.ADD: add_word,
    InputModes.GET_REFERENCE: get_reference_word,
    InputModes.GET_WORD_NUMBER: get_word_number,
    InputModes.PLAY: check_word
}


def handle_input(input_string: str, context: ValidationContext):
    if input_string[0] == "+":
        return handle_command(input_string[1:], context)
    function = INPUT_HANDLERS[context.input_mode]
    return function(input_string, context)
