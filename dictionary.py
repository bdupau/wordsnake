__author__ = 'Bastiaan'


class Dictionary:
    def __init__(self, language=None):
        self.__language = language
        self.__load_dictionary()

    def __load_dictionary(self):
        self.__dictionary = []
        if self.__language == 'dutch':
            file = open('OpenTaal-210G-basis-gekeurd.txt', 'r', encoding='utf-8')
            for line in file:
                self.__dictionary.append(line.strip('\n'))

    def is_in_dictionary(self, word):
        return word in self.__dictionary