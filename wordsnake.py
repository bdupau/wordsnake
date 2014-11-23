__author__ = 'Bastiaan'


class Wordsnake:

    def __init__(self, fn_is_valid_word):
        self._snake = []
        self._is_valid_word = fn_is_valid_word

    # Checks if ending letters of word1 are starting letters of word2
    @staticmethod
    def overlap(word1, word2):
        size_overlap = 1
        max_overlap = len(word1) - 1
        # Start with one ending letter
        # Continue checking until the whole word minus one letter
        while size_overlap <= max_overlap:
            if word1[-size_overlap:] == word2[0:size_overlap]:
                return size_overlap
            size_overlap += 1
        return 0

    def _is_empty(self):
        if len(self._snake) == 0:
            return True
        return False

    def get_current_word(self):
        if self._is_empty():
            return None
        return self._snake[-1]

    def __str__(self):
        return str(self._snake)

    # Adds a word to the wordsnake, if it is valid
    def add_word(self, continuation='empty'):
        if not self._is_valid_word(continuation):
            return False
        if self._is_empty():
            self._snake.append(continuation)
            return True
        if self.overlap(self.get_current_word(), continuation) != 0:
            self._snake.append(continuation)
            return True
        return False
