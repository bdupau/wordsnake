__author__ = 'Bastiaan & Bob'

from bootstrap import get_wordsnake

class WordsnakeTester:

    def __init__(self):
        snake = get_wordsnake()
        snake.init_word('strapless-beha')
        snake.add_word('behaard')
        snake.add_word('behang')
        snake.add_word('behaarde')
        snake.add_word('haarzakje')
        snake.add_word('haardvuur')
        snake.add_word('vuurdoop')
        snake.add_word('doperwt')
        snake.add_word('uurdoopisgeenwoord')
        snake.add_word('opstaan')
        print(snake)

tester = WordsnakeTester()


