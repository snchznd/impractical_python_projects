"""A module that plots a bar chart representing the frequency of each letter in an input string."""

import string

def main() -> None:
    """Asks the user for an input sentence and then plots a character-based bar plot of 
       the characters frequency."""
    input_sentence = input('Enter your sentence: ')
    char_to_count = {}
    for char in input_sentence :
        char = char.lower()
        if char not in string.ascii_lowercase :
            continue
        if char in char_to_count:
            char_to_count[char] += 1
        else :
            char_to_count[char] = 1

    occurences = sorted(list(char_to_count.items()), key=lambda x: x[0])

    for char, count in occurences:
        print(f'{char}: ' + str([char] * count))


if __name__ == "__main__":
    main()
