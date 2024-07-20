"""A module that takes an input from the user and returns corresponding
anagrams"""

from typing import List

SOURCE_FILE =  '..\\data\\words_dict.txt'
INPUT_MESSAGE = 'Enter your word: '
ERROR_MESSAGE = '/!\\ ERROR: '

def load_words(file_path : str) -> List[str]:
    """Loads a list of words."""
    words_list = []
    try:
        with open(file=file_path, mode='r', encoding='utf-8') as file:
            words_list = [x.strip() for x in file.readlines()]
    except (FileNotFoundError, IOError) as e:
        print(ERROR_MESSAGE.format(e))
    return words_list

def find_anagrams(words_list : List[str], word : str) -> List[str]:
    """Given a word and a list of known words (dictionary), finds all anagrams
    of the word in the list."""
    word = word.lower()
    word_sorted_letters : List[str] = sorted(word)
    anagrams_list : List[str] = []
    for dict_word in words_list:
        dict_word = dict_word.lower()
        if sorted(dict_word) == word_sorted_letters and dict_word != word:
            anagrams_list.append(dict_word)
    return anagrams_list


def main() -> None:
    """Asks the user for input and generates a word of corresponding anagrams."""
    words_list : List[str] = load_words(SOURCE_FILE)
    user_input : str = input(INPUT_MESSAGE)
    anagrams_list : List[str] = find_anagrams(words_list, user_input)
    if anagrams_list:
        print('List of anagrams:')
        for idx, anagram in enumerate(anagrams_list):
            print(f'{idx:>4}. {anagram}')
    else:
        print('No anagrams found.')

if __name__ == '__main__':
    main()
