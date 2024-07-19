"""A module that loads a set of words from an online dictionary, filters
out the words that can be used to create palingrams, and saves a list of
palingrams to a file. This version is optimized because it uses a set to
store the words instead of a list. Thus lookup is O(1) and not O(n)."""

from typing import List, Set
from tqdm import tqdm

FILE_READ_ERROR_TEMPLATE = 'ERROR: {0}'
SOURCE_FILE = 'words_dict.txt'
WRITE_FILE = 'palingrams_faster.txt'
DEBUGG_STRING = 'added word {} - at index {} - resulting in {}\n'

def load_words(file_name : str) -> List[str]:
    """Function that loads the content of a file, line by line in a safe way 
    and cleans the extra spaces."""
    file_content = []
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            file_content = [x.strip() for x in file.readlines()]

    except (FileNotFoundError, IOError) as error:
        print(FILE_READ_ERROR_TEMPLATE.format(error))

    return file_content

def write_palingrams_list(palingrams_list : List[str], file_name : str = WRITE_FILE) -> None:
    """Function that, given a list of palingrams, writes them to a file."""
    with open(file_name, mode='w', encoding='utf-8') as file:
        for palingram in palingrams_list:
            file.write(palingram + '\n')

def is_palindrom(word : str) -> bool:
    """Function that takes as input a string an returns a string indicating
    if the string is a palindrom."""
    return word == word[::-1]

def compute_palingrams(words_set : Set[str]) -> List[str]:
    """Build all possible palingrams, given a list of words, an returns them
    as a list."""
    palingrams_list = []
    for word in tqdm(words_set):
        for idx in range(len(word) - 1):
            word_to_add = None
            word_first_part = word[0:idx+1]
            word_second_part = word[idx+1::]

            if is_palindrom(word_first_part) and word_second_part[::-1] in words_set:
                word_to_add = word_second_part[::-1] + ' ' + word

            elif word_first_part[::-1] in words_set and is_palindrom(word_second_part):
                word_to_add = word + ' ' + word_first_part[::-1]

            if word_to_add:
                palingrams_list.append(word_to_add)

    return palingrams_list

def main() -> None :
    """Loads a dictionary of words and retrieves and prints the palindroms."""
    words_set = set(load_words(SOURCE_FILE))
    palingrams_list = compute_palingrams(words_set)
    write_palingrams_list(palingrams_list)

if __name__ == '__main__':
    main()
