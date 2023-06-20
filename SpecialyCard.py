from __future__ import annotations
from Card import Card
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game
    from Player import Player

class SpecialyCard(Card):
    def __init__(self):
        super().__init__()
        self.has_effect = True