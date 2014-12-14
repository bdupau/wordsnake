__author__ = 'Bastiaan'


class Game:

    def __init__(self, fn_get_current_word, fn_add_word, fn_score):
        self._players = {}
        self._get_current_word = fn_get_current_word
        self._add_word = fn_add_word
        self._score = fn_score

    def game_finished(self):
        if max(self._players.values()) > 25:
            return True
        return False

    def start_game(self, players):
        if self._players.__len__() > 0:
            return "Het is niet mogelijk het spel te starten. Het spel is al gestart."
        for player in players:
            if player in self._players:
                self._players.clear()
                return "Het is niet mogelijk een spel te starten. Er spelers zijn met dezelfde naam."
            self._players[player] = 0
        return "Nieuw spel is gestart."

    def add_word(self, player, word):
        if self._players.__len__() == 0:
            return "Het is niet mogelijk een woord toe te voegen. Het spel is nog niet begonnen."
        if self.game_finished():
            return "Het is niet mogelijk een woord toe te voegen. Het spel is al afgelopen."
        if player not in self._players:
            return "Het is niet mogelijk een woord toe te voegen. {} is geen deelnemer aan het spel.".format(player)
        current_word = self._get_current_word()
        if self._add_word(word):
            score = self._score(current_word, word)
            self._players[player] += score
            bot_text = "{0} heeft \'{1}\' aan de wordsnake toegevoegd voor {2} punten. {0} heeft nu {3} punten.".format(player, word, score, self._players[player])
            if self.game_finished():
                bot_text += " {} heeft het spel gewonnen !".format(player)
            return bot_text
        return "Het woord \'{}\' is niet valide.".format(word)