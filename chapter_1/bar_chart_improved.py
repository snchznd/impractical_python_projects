"""A module that plots a bar chart representing the frequency of each letter in an input string.
   This version includes an empty bar for the letter that are not in the input string."""

import string

def get_count(letter : str, text : str) -> int :
    """Counts how many times the 'letter' character occurs in 'text'"""
    count = 0
    for char in text:
        if letter == char:
            count += 1
    return count

def main() -> None:
    """Asks the user for an input sentence and then plots a character-based bar plot of 
       the letters frequency. Plot empty bars for letters that are not in the input."""
    input_sentence = input('Enter your sentence: ')
    char_to_count = {}

    for letter in string.ascii_lowercase :
        char_to_count[letter] = get_count(letter, input_sentence)

    occurences = sorted(list(char_to_count.items()), key=lambda x: x[0])

    for char, count in occurences:
        print(f'{char}: ' + str([char] * count))


if __name__ == "__main__":
    main()
