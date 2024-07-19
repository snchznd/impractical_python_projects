"""A module that load a list of words, removes the one-letter words, and
writes the cleaned list to a new file."""

from typing import List

LOAD_FILE = 'words_dict.txt'
WRITE_FILE = 'words_dict_cleaned.txt'

def load_words_list(file_name : str) -> List[str]:
    """Function that loads a file containing one word per line and returns
    the words as a list"""
    words_list = []
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            words_list = [line.strip() for line in file.readlines()]

    except (FileNotFoundError, IOError) as e:
        print(f'/!\\ ERROR: {e}')

    return words_list

def write_words_list(file_name : str, words_list : List[str]) -> None:
    """Function that writes a list of words to a file."""
    with open(file=file_name, mode='w', encoding='utf-8') as file:
        for word in words_list:
            file.write(word + '\n')

def remove_single_letters(words_list : List[str]) -> List[str]:
    """Function that removes all single letter strings from a list of
    strings."""
    return [x for x in words_list if len(x) > 1]

def main() -> None:
    """Loads a list of words, removes the single letters, and writes the
    result to file."""
    words_list = load_words_list(LOAD_FILE)
    words_list = remove_single_letters(words_list)
    write_words_list(WRITE_FILE, words_list)

if __name__ == '__main__':
    main()
