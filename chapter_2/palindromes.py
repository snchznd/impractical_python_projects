"""A module that loads a list of words from an online dictionary and filters
out the words that are not palindromes."""

from typing import List

FILE_READ_ERROR_TEMPLATE = 'ERROR: {0}'
SOURCE_FILE = '..\\data\\words_dict.txt'

def load_words(file_name : str) -> List[str]:
    """Function that loads the content of a file, line by line in a safe way 
    and cleans the extra spaces."""
    file_content = []
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            file_content = [x.strip() for x in file.readlines()]

    except (FileNotFoundError, IOError) as error:
        print(FILE_READ_ERROR_TEMPLATE.format(error, file_name))

    return file_content

def keep_only_palindroms(words_list : List[str]) -> List[str]:
    """Function that takes as input a list of strings and filters out the 
    strings that are not palindroms."""
    return [x for x in words_list if x == x[::-1]]

def main() -> None :
    """Loads a dictionary of words and retrieves and prints the palindroms."""
    words_list = load_words(SOURCE_FILE)
    palindroms = keep_only_palindroms(words_list)
    for idx, word in enumerate(palindroms):
        print(f'---> {idx}: {word}')

if __name__ == '__main__':
    main()
