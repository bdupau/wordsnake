__author__ = 'Bastiaan'


class Scorer:

    def __init__(self, fn_overlap):
        self._get_overlap = fn_overlap

    def score(self, word1, word2):
        if word1 is None:
            return 0
        return self._get_overlap(word1, word2) * 2