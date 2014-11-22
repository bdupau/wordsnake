__author__ = 'Bastiaan'


class Dictionary:
    def __init__(self, language=None):
        self._language = language
        self._load_dictionary()

    def _load_dictionary(self):
        self._dictionary = []
        if self._language == 'dutch':
            file = open('OpenTaal-210G-basis-gekeurd.txt', 'r', encoding='utf-8')
            for line in file:
                self._dictionary.append(line.strip('\n'))

    def is_in_dictionary(self, word):
        return word in self._dictionary