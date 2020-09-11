import hashlib
from random import randint

def hash_colour(data):
    return (
        randint(126, 255),
        randint(126, 255),
        randint(126, 255)
    )
