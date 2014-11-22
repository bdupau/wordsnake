__author__ = 'Bastiaan'

from bootstrap import get_wordsnake


class Game:

    def __init__(self):
        self.__players = []
        self.__snake = get_wordsnake()

    def start_game(self, players):
        self.__players = players
        return "Starting a new game"

    def add_word(self, player, word):
        if player not in self.__players:
            return "The word \'{}\' was not added to the wordsnake, because {} is not playing in this game".format(word, player)
        if self.__snake.add_word(word):
            return "{} added the word \'{}\' to the wordsnake".format(player, word)
        return "The word \'{}\' was not added to the wordsnake, because it is not valid".format(word)

