###########
# IMPORTS #
###########

from typing import Optional
from Player import Player
from Card import Card
from MonsterCard import MonsterCard
from SpecialyCard import SpecialyCard
from Deck import Deck
from Field import Field

from random import random

#############
# CONSTANTS #
#############

N_START_HAND = 5

###########
# METHODS #
###########
class Game:
    def __init__(self, p1:Player, p2:Player):
        self.p1 = p1
        self.p2 = p2
        self.field = Field(p1, p2)
        self.active_player = None
        self.turn_number = 0


    def summon_card(self, p:Player, c:Card, pos:int):
        """Implements game logic for summoning a card. Does no checks, but calls respective event handlers."""
        if type(c) == MonsterCard:
            c.summon_preparation()
        self.field.set_card(p, pos, c)
        if type(c) == MonsterCard:
            c.on_summon()
        if type(c) == SpecialyCard:
            c.on_activate()

    def attack(self, source:MonsterCard, target:MonsterCard):
        """Implements game logic for attacking. Calls event handlers and does math."""
        source.on_attack()
        target.on_attacked()
        # inflict damage
        target.on_damage(source, source.get_strength())

    def modify_points(self, p:Player, delta:int):
        """Modify a player's points. Delta positive means increase"""
        p.dec_points(delta)

        # TODO: Outsource this?
        if p.points <= 0:
            # p has lost
            if p == self.p1:
                print("Player 1 got chup b ningbo polix")
            else:
                print("Player 2 got chup b ningbo polix")

    def start_game(self, starting_player:Optional[Player] = None):
        # determine starting player
        if starting_player is not None:
            r = random()
            if r < .5:
                self.active_player = self.p1
            else:
                self.active_player = self.p2
        else:
            self.active_player = starting_player

        # initialize number of turns
        self.turn_number = 0

        # both players draw a starting hand

    def on_start_of_turn(self):
        # increase turn number and lifetime stat of each card
        self.turn_number += 1
        cards = self.field.get_cards()
        cards_notnone = [x for x in cards[self.p1] if x != None] + [x for x in cards[self.p2] if x != None]
        for c in cards_notnone:
            c.inc_time_on_field()
        
        # both players draw 1 card
        p1.draw()
        p2.draw()
