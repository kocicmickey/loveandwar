"""A rough framework for characters, featuring joint combat and love resolution and ownership of the mechanics of combat and love by one of the participants.
"""

from random import randint

class Character:

    def __init__(self, name, aggro=50, fought=0, loved=0, reaction=(None, None)):
        self.name = name
        self.aggro = aggro
        self.fought = fought
        self.loved = loved
        self.reaction = reaction

    def react(self)
        reaction = randint(1,100) + self.fought - self.loved
        if reaction > self.aggro:
            flag = 1
        else:
            flag = -1
        self.reaction = (flag, reaction)

    def encounter(self, other):
        #Can be either self.encounter(other) or other.encounter(self)
        if self.reaction[0] + other.reaction[0] > 0:
            self.fought += 1
            self.aggro += 1
            other.fought += 1
            other.aggro += 1
        elif self.reaction[0] + other.reaction[0] < 0:
            self.loved += 1
            self.aggro -= 1
            other.loved += 1
            other.aggro -= 1
        else:
            #not yet implemented
            pass