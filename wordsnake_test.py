__author__ = 'Bastiaan & Bob'

from game import Game


class WordsnakeTester:

    def __init__(self):
        game = Game()
        print(game.start_game(['Jan', 'Piet']))
        print(game.add_word('Kees', 'behaard'))
        print(game.add_word('Jan', 'behaard'))
        print(game.add_word('Piet', 'behang'))
        print(game.add_word('Piet', 'behaarde'))
        print(game.add_word('Jan', 'haarzakje'))
        print(game.add_word('Jan', 'haardvuur'))
        print(game.add_word('Piet', 'vuurdoop'))
        print(game.add_word('Jan', 'doperwt'))
        print(game.add_word('Piet', 'uurdoopisgeenwoord'))
        print(game.add_word('Jan', 'opstaan'))
        # print(snake)

tester = WordsnakeTester()


