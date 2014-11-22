__author__ = 'Bastiaan'

from dictionary import Dictionary


class Wordsnake:
    def __init__(self, fn_is_valid_word):
        self.__snake = []
        self.__is_valid_word = fn_is_valid_word

    # Checks if ending letters of word1 are starting letters of word2
    def __overlap(self, word1, word2):
        size_overlap = 1
        max_overlap = len(word1) - 1
        # Start with one ending letter
        # Continue checking until the whole word minus one letter
        while size_overlap <= max_overlap:
            if word1[-size_overlap:] == word2[0:size_overlap]:
                return True
            size_overlap += 1
        return False

    def __is_empty(self):
        if len(self.__snake) == 0:
            return True
        return False

    def get_current_word(self):
        return self.__snake[-1]

    def __str__(self):
        return str(self.__snake)

    # Adds a word to the wordsnake, if it is valid
    def add_word(self, continuation='empty'):
        if not self.__is_valid_word(continuation):
            return False
        if self.__is_empty():
            self.__snake.append(continuation)
            return True
        if self.__overlap(self.get_current_word(), continuation):
            self.__snake.append(continuation)
            return True
        return False


'''
    def get_overlap_size(self, word1, word2):
        size_overlap = 0
        max_overlap = len(word1) - 1

        # Start with one ending letter
        # Continue checking until the whole word minus one letter
        while size_overlap <= max_overlap:
            if word1[-size_overlap:] != word2[0:size_overlap]:
                break
            size_overlap += 1

        return size_overlap
'''

