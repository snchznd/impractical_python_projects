"""A module that prompts the user for his name and iteratively builds a
sentence anagram based on it and on the user's input."""

from typing import List, Tuple
from collections import Counter

FILE_NAME = '..\\data\\words_dict.txt'
FINAL_PRINT = '\n --> Final anagram sentence: {}'
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
    """Returns only the elements of the list whose set of letters are a subset of the 
    letters of letters_left"""
    return [x for x in words_list if x[1] <= letters_left]

def build_anagram_sentence(words_list : List[Tuple], word : str) -> str | None:
    """Builds a sentence anagram based on a word, a list of words, and iterative
    prompts to the user."""
    reset = False
    letters_left = Counter(word)
    candidates = get_candidate_words(words_list, letters_left)
    if not candidates:
        print('No candidates found for your name.')
    anagram_sentence_list = []
    anagram_sentence = ''

    while candidates:
        print('\n Candidates:')
        for idx, candidate in enumerate(candidates):
            print(' ' * 5 + f'{idx:<3}: {candidate[0]}')

        user_choice = -1
        acc = 0
        valid_choices = range(len(candidates))
        choice_message = f' --> Choose a candidate in the set {{{0},..., {len(candidates)-1}}}: '
        while user_choice not in valid_choices:
            if acc >= 1:
                print('[enter "RESET" to start over]')

            user_choice = input(choice_message)
            if user_choice.lower() != 'reset':
                user_choice = int(user_choice)
            else:
                reset = True
                break
            acc += 1

        if reset:
            return None

        chosen_word, chosen_word_counter = candidates[user_choice]
        print(f' --> You selected: {chosen_word}')
        anagram_sentence_list.append(chosen_word)
        anagram_sentence = ' '.join(anagram_sentence_list)

        letters_left -= chosen_word_counter
        candidates = get_candidate_words(words_list, letters_left)

        if candidates:
            print(f' --> Anagram sentece so far: {anagram_sentence}')
    return anagram_sentence

def main() -> None:
    """Build a sentence anagram based on the user's input."""
    words_list = load_words_list(FILE_NAME)
    words_list_complete = [(x, Counter(x)) for x in words_list]
    user_name = get_user_name()
    anagram_sentence = None
    while not anagram_sentence:
        anagram_sentence = build_anagram_sentence(words_list_complete, user_name)
        if not anagram_sentence:
            print('\nReseting Game...\nStarting again with empty sentence.')
    print(FINAL_PRINT.format(anagram_sentence))



if __name__ == '__main__':
    main()
