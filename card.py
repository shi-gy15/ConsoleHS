
'''
type: minion / spell / weapon / mission / dk

'''
from signal_slot import *
from minion import *


class Card:
    type = ''
    origin_cost = 0
    cost = 0
    owner = None

    def __init__(self, type, cost, owner):
        self.type = type
        self.origin_cost = cost
        self.cost = cost
        self.owner = owner

    def use(self):
        pass

class MinionCard(Card):
    minion = None

    def __init__(self, type, cost, owner, minion):
        super(MinionCard, self).__init__(type=type, cost=cost, owner=owner)
        self.minion = minion

    def use(self):
        # only handles 'choose'
        emit(Signal.form(
            'use',
            card=self,
            index=0
        ))
        self.minion.play()
