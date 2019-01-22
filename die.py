import random


class Die():

    def __init__(self):
        self.value = None
        self.state = None
        self.roll()

    def roll(self):
        self.value = random.randrange(1,7)
