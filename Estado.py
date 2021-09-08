import math

class Estado():
    parente = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = math.inf
        self.h = math.inf
        self.f = math.inf
        