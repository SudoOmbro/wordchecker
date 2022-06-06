def add_letter_to_dictionary(letter, dictionary):
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1