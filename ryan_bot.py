from snakegame.common import *
from random import choice


def ryan_bot(board, pos):
        x, y = pos
        directions = [
            ['U', (0, -1)],
            #['D', (0, 1)],
            ['L', (-1, 0)],
            ['R', (1, 0)],
        ]
        for direction, (dx, dy) in directions:
                if is_apple(get_cell(board, x + dx, y + dy)):
                        return direction
        for direction, (dx, dy) in directions:
                if is_empty(get_cell(board, x + dx, y + dy)):
                        return direction
        #rip
        return "D"
        
# Test code to run the snake game.
# Leave the if statement as is, otherwise I won't be able to run your bot with
# the other bots.
if __name__ == '__main__':
        from snakegame.engines.pyglet import PygletEngine
        p = PygletEngine(25, 25, 50, wrap=True)
        for i in range(10):
                p.add_bot(ryan_bot)
        p.run()
