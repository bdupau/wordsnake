__author__ = 'Bastiaan & Bob'

from dictionary import Dictionary
from wordsnake import Wordsnake
from scorer import Scorer
from game import Game


def get_game():
    dutch_dictionary = Dictionary('dutch')
    wordsnake = Wordsnake(dutch_dictionary.is_in_dictionary)
    scorer = Scorer(wordsnake.overlap)
    game = Game(wordsnake.get_current_word, wordsnake.add_word, scorer.score)
    return game

