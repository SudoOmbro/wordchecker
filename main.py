from classes import ValidationContext, InputModes
from wordchecker import handle_input


def main():
    with open("test.txt", "r") as file:
        lines = file.readlines()
    context = ValidationContext()
    context.word_length = int(lines[0][:-1])
    context.input_mode = InputModes.ADD
    context.allowed_words = []
    for line in lines[1:]:
        return_value = handle_input(line[:-1], context)
        if return_value == 1:
            return 0


if __name__ == "__main__":
    main()
