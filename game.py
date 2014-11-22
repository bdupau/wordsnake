__author__ = 'Bastiaan'

from bootstrap import get_wordsnake


class Game:

    def __init__(self):
        self._players = []
        self._snake = get_wordsnake()

    def start_game(self, players):
        self._players = players
        return "Starting a new game"

    def add_word(self, player, word):
        if player not in self._players:
            return "The word \'{}\' was not added to the wordsnake, because {} is not playing in this game".format(word, player)
        if self._snake.add_word(word):
            return "{} added the word \'{}\' to the wordsnake".format(player, word)
        return "The word \'{}\' was not added to the wordsnake, because it is not valid".format(word)

