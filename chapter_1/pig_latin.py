"""A module that tranlates english words to their Pig Latin equivalent."""

import sys

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def input_is_valid(word : str) -> str:
    """Check the validity of the input word for translatin to Pig Lating."""
    return isinstance(word, str) and len(word) > 0 and len(word.split(' ')) == 1

def translate(word : str) -> str:
    """Translates a word from english to Pig Latin."""
    head, tail = word[0], word[1::]
    if head in CONSONANTS:
        return tail + head + 'ay'
    return word + 'way'

def main():
    """Asks user for english words to translate to Pig Latin and translates them 
       until the user quits."""
    while True :
        user_input = input('\nTranslate additional word to Pig Latin? [y/n]: ')
        if user_input.lower() in ('no', 'n') :
            break
        input_word = input('English word to translate: ')
        if not input_is_valid(input_word) :
            print('Error: input must be a single word.',
                  file=sys.stderr)
            continue
        pig_latin_word = translate(input_word)

        print(f'Translation: {input_word} --> {pig_latin_word}')

if __name__ == '__main__':
    main()
