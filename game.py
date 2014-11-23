__author__ = 'Bastiaan'


class Game:

    def __init__(self, fn_get_current_word, fn_add_word, fn_score):
        self._players = {}
        self._get_current_word = fn_get_current_word
        self._add_word = fn_add_word
        self._score = fn_score

    def start_game(self, players):
        if self._players.__len__() > 0:
            return "Cannot start a game while game is in progress."
        for player in players:
            if player in self._players:
                self._players.clear()
                return "Cannot start a game with identical players."
            self._players[player] = 0
        return "Starting a new game."

    def add_word(self, player, word):
        if player not in self._players:
            return "The word \'{}\' was not added to the wordsnake, because {} is not playing in this game.".format(word, player)
        current_word = self._get_current_word()
        if self._add_word(word):
            score = self._score(current_word, word)
            self._players[player] += score
            return "{0} added the word \'{1}\' to the wordsnake for {2} points. {0} now has {3} points.".format(player, word, score, self._players[player])
        return "The word \'{}\' was not added to the wordsnake, because it is invalid.".format(word)