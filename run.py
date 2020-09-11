from snakegame.engines.pyglet import PygletEngine
from matt_bot import unionfind_bot
from old_matt import matt_old_bot, safe_bot
from sample_bots import random_avoid_bot, manual_bot
n=5
engine = PygletEngine(n, n, 3)
engine.add_bot(safe_bot)
engine.add_bot(manual_bot)

for i in range(10):
    #engine.add_bot(random_avoid_bot)
    #engine.add_bot(random_bot)
    #engine.add_bot(safe_bot)
    #engine.add_bot(unionfind_bot)
    #engine.add_bot(matt_old_bot)
    continue
engine.run()

