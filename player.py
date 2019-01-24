from die import *


class Player:

    def __init__(self):
        self.dice = []
        self.qualifiers = []

    def add_die(self, die):
        if (die.value == 1) and (1 not in self.qualifiers):
            self.qualifiers.append(die)

        elif (die.value == 4) and (4 not in self.qualifiers):
            self.qualifiers.append(die)

        elif self.dice.__len__() < 4:
            self.dice.append(die)
