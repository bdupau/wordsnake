__author__ = 'Bastiaan'


class Game:

    def __init__(self, fn_get_current_word, fn_add_word, fn_score):
        self._scores_per_player = {}
        self._get_current_word = fn_get_current_word
        self._add_word = fn_add_word
        self._score = fn_score
        self._is_started = False

    def game_finished(self):
        if max(self._scores_per_player.values()) > 25:
            return True
        return False

    def start_game(self, players):
        if len(self._scores_per_player) > 0:
            return "Het is niet mogelijk het spel te starten. Het spel is al gestart."
        if len(set(players)) < len(players):
            return "Het is niet mogelijk een spel te starten. Er spelers zijn met dezelfde naam."

        self._scores_per_player = { player : 0 for player in players }
        self._is_started = True
        return "Nieuw spel is gestart."

    def add_word(self, player, word):
        if not self._is_started:
            return "Het is niet mogelijk een woord toe te voegen. Het spel is nog niet begonnen."
        if self.game_finished():
            return "Het is niet mogelijk een woord toe te voegen. Het spel is al afgelopen."
        if player not in self._scores_per_player:
            return "Het is niet mogelijk een woord toe te voegen. {} is geen deelnemer aan het spel.".format(player)
        
        current_word = self._get_current_word()
        if self._add_word(word):
            score = self._score(current_word, word)
            self._scores_per_player[player] += score
            bot_text = "{0} heeft \'{1}\' aan de wordsnake toegevoegd voor {2} punten. {0} heeft nu {3} punten.".format(player, word, score, self._scores_per_player[player])
            if self.game_finished():
                bot_text += " {} heeft het spel gewonnen !".format(player)
            return bot_text
        return "Het woord \'{}\' is niet valide.".format(word)