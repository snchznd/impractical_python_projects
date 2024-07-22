"""A module that prompts the user for his name and iteratively builds a
sentence anagram based on it and on the user's input."""

from typing import List, Tuple
from collections import Counter

FILE_NAME = '..\\data\\words_dict.txt'
FINAL_PRINT = 'Anagram sentence: {}'
ERROR_MESSAGE = '/!\\ ERROR: '
INITIAL_PROMPT = ' --> Enter your name: '

def load_words_list(file_name : str) -> List[str]:
    """Loads a list of words from a file."""
    words_list = None
    try:
        with open(file=file_name, mode='r', encoding='utf-8') as file:
            words_list = [x.lower().strip() for x in file.readlines()]
    except (FileNotFoundError, IOError) as e:
        print(ERROR_MESSAGE.format(e))
        words_list = []
    return words_list

def get_user_name():
    """Prompts the user for his name and returns it."""
    return input(INITIAL_PROMPT)

def get_candidate_words(words_list : List[Tuple], letters_left : Counter) -> List[Tuple]:
    return [x for x in words_list if x[1] <= letters_left]

def build_anagram_sentence(words_list : List[Tuple], word : str) -> str:
    """Builds a sentence anagram based on a word, a list of words, and iterative
    prompts to the user."""
    letters_left = Counter(word)
    #print('letters left: ', letters_left)
    #print( words_list[:5], len(words_list))
    candidates = get_candidate_words(words_list, letters_left)
    if not candidates:
        print('No candidates for your name.')
    while candidates:
        print('\n CANDIDATES:')
        for idx, candidate in enumerate(candidates):
            print(' ' * 10 + f'{idx:<3}: {candidate[0]}')

        user_choice = -1
        while user_choice not in range(len(candidates)):
            user_choice = int(input(f' --> Choose a candidate in the set {{{0},..., {len(candidates)-1}}}: '))

        #place holder for now
        print('GOOD')
        break

def main() -> None:
    """Build a sentence anagram based on the user's input."""
    words_list = load_words_list(FILE_NAME)
    words_list = [(x, Counter(x)) for x in words_list]
    user_name = get_user_name()
    anagram_sentence = build_anagram_sentence(words_list, user_name)
    #print(FINAL_PRINT.format(anagram_sentence))



if __name__ == '__main__':
    main()
