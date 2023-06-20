from MonsterCard import MonsterCard
from SpecialyCard import SpecialyCard
from Frontend import player_select_card
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Player import Player
    from Game import Game

class BasicMubarrachka(MonsterCard):
    def __init__(self, g:Game, p:Player):
        super().__init__(hp=self.hp, strength=self.strength, g=g, p=p)
        self.hp = 100
        self.strength = 27
        self.name = "Basic Mubarrachka"

class MubarrachkaCool(MonsterCard):
    def __init__(self, g:Game, p:Player):
        super().__init__(self.hp, self.strength, g, p)
        self.handled_events["start_of_turn"] = True
        self.hp = 200
        self.strength = 37
        self.name = "Mubarrachka (Cool)"
    
    def summon_check(self, g: Game):
        can_summon = False
        cards = g.field.get_cards()[self.player]
        for card in cards:
            if card != None:
                can_summon = can_summon or card.name == "Basic Mubarrachka"
        return can_summon
    
    def summon_preparation(self):
        c = player_select_card(self.game, self.player, name="Basic Mubarrachka")
        self.game.field.remove_card(c)
        c.on_tribute()



