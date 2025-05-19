import random

def get_random_color():
    r = round(random.uniform(0, 1), 2)
    g = round(random.uniform(0, 1), 2)
    b = round(random.uniform(0, 1), 2)
    return r, g, b