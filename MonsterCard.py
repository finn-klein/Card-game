from __future__ import annotations
from Card import Card
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game
    from Player import Player

class MonsterCard(Card):
    def __init__(self, hp:int, strength:int, g:Game, p:Player):
        self.hp = hp
        self.strength = strength
        super().__init__(g=g, p=p)

    def get_hp(self):
        """Getter function that returns the card's HP"""
        return self.hp
    
    def set_hp(self, val:int):
        """Setter function that updates the card's HP"""
        self.hp = val

    def get_strength(self):
        """Getter function that returns the card's strength"""
        return self.strength

    def set_strength(self, val:int):
        """Setter function that updates the card's strength"""
        self.strength = val

    #############
    # SUMMONING #
    #############

    def summon_check():
        """Performs checks to see if this card can currently be summoned"""
        pass

    def summon_preparation():
        """Performs necessary preparation of summoning, e.g. tributes"""
        pass

    ##################
    # EVENT HANDLERS #
    ##################

    def on_summon(self):
        """Event handler for when card is summoned"""

    def on_die(self):
        """Event handler for when card leaves the field due to an attack"""
        self.game.modify_points(self.player, -1)
        pass
    
    def on_tribute(self):
        """Event handler for when card is offered as tribute and leaves the field"""
        pass

    def on_attack(self, target):
        """Event handler for when card attacks target"""
        pass

    def on_attacked(self, source):
        """Event handler for when card is attacked by source"""
        pass
    
    def on_hp_set(self):
        """Event handler for when set_hp is called"""
        pass

    def on_strength_set(self):
        """Event handler for when set_strength is called"""
        pass

    def on_damage(self, source, dmg):
        """Event handler for when card is damaged. Sets hp."""
        hp_before = self.get_hp()
        hp_after = max(0, hp_before - dmg)
        if hp_after == 0:
            self.on_die()