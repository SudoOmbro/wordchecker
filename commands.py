from typing import Callable, Dict

from classes import ValidationContext, InputModes


def start_new_game(context: ValidationContext) -> int:
    context.input_mode = InputModes.GET_REFERENCE
    context.word_count = 0
    return 0


def print_filtered(context: ValidationContext) -> int:
    # TODO i don't understand what i'm supposed to print here
    print(context.allowed_words)
    return 0


def insert_start(context: ValidationContext) -> int:
    context.input_mode = InputModes.ADD
    return 0


def insert_end(context: ValidationContext) -> int:
    context.input_mode = InputModes.PLAY
    return 0


COMMANDS_SWITCH: Dict[str, Callable[[ValidationContext], int]] = {
    "nuova_partita": start_new_game,
    "stampa_filtrate": print_filtered,
    "inserisci_inizio": insert_start,
    "inserisci_fine": insert_end
}


def handle_command(command: str, context: ValidationContext) -> int:
    return COMMANDS_SWITCH[command](context)
