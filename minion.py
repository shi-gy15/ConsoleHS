
from signal_slot import *

class Minion:
    attack = 1
    health = 1
    race = ''

    def play(self):
        emit({
            type: 'play'
        })
        self.summon()


    def summon(self):
        emit({
            type: 'summon'
        })