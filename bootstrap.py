__author__ = 'Bastiaan & Bob'

from dictionary import Dictionary
from wordsnake import Wordsnake

def get_wordsnake():
    dutch_dictionary = Dictionary('dutch')
    wordsnake = Wordsnake(dutch_dictionary.is_in_dictionary)
    return wordsnake

