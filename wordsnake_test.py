__author__ = 'Bastiaan & Bob'

from bootstrap import get_game


class WordsnakeTester:

    def __init__(self):
        game = get_game()
        print(game.add_word('Kees', 'behaard'))
        print(game.start_game(['Jan', 'Jan']))
        print(game.start_game(['Jan', 'Piet']))
        print(game.add_word('Kees', 'behaard'))
        print(game.add_word('Jan', 'behaard'))
        print(game.add_word('Piet', 'behang'))
        print(game.add_word('Piet', 'behaarde'))
        print(game.add_word('Jan', 'haarzakje'))
        print(game.add_word('Jan', 'haardvuur'))
        print(game.start_game(['Kees', 'Anne']))
        print(game.add_word('Piet', 'vuurdoop'))
        print(game.add_word('Jan', 'doperwt'))
        print(game.add_word('Jan', None))
        print(game.add_word('Piet', 'uurdoopisgeenwoord'))
        print(game.add_word('Jan', 'opstaan'))
        print(game.add_word('Piet', 'aangaan'))
        print(game.add_word('Piet', 'aangaan'))
        print(game.add_word('Piet', 'aangaan'))
        print(game.add_word('Piet', 'aangaan'))
        # print(snake)

tester = WordsnakeTester()