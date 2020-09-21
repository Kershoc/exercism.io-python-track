import string
import random

robots = []

class Robot:
    name = ''

    def __init__(self):
        self.reset()
        pass

    def genName(self):
        return ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))

    def reset(self):
        while self.name in robots:
            self.name = self.genName()
        robots.append(self.name)
        pass
