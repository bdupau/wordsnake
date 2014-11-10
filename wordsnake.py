__author__ = 'Bastiaan'


class Wordsnake:
    def __init__(self, word=None):
        self.__snake = []
        self.__snake.append(word)
        self.__load_dictionary()

    def __load_dictionary(self):
        self.__dictionary = []
        file = open('OpenTaal-210G-basis-gekeurd.txt', 'r', encoding='utf-8')
        for line in file:
            self.__dictionary.append(line.strip('\n'))

    def __is_in_dictionary(self, word):
        return word in self.__dictionary

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

    def __is_valid_continuation(self, current_word, continuation):
        if self.__is_in_dictionary(continuation):
            if self.__overlap(current_word, continuation):
                return True
        return False

    def get_current_word(self):
        return self.__snake[-1]

    def __str__(self):
        return str(self.__snake)

    # Adds a word to the wordsnake, if it is valid
    def add_word(self, continuation='empty'):
        if self.__is_valid_continuation(self.get_current_word(), continuation):
            self.__snake.append(continuation)

    def get_dictionary(self):
        self.add_word()
        return self.__dictionary


class WordsnakeTester:

    if __name__ == "__main__":
        snake = Wordsnake('behaard')
        snake.add_word('behang')
        snake.add_word('behaarde')
        snake.add_word('haarzakje')
        snake.add_word('haardvuur')
        snake.add_word('vuurdoop')
        snake.add_word('doperwt')
        snake.add_word('uurdoopisgeenwoord')
        snake.add_word('opstaan')
        print(snake)
