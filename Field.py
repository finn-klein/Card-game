from typing import Optional
from Card import Card
from Player import Player

N_CARDS_PER_PLAYER = 3

class Field:
    def __init__(self, p1:Player, p2:Player):
        self.p1 = p1
        self.p2 = p2
        self.cards = {self.p1: [None]*N_CARDS_PER_PLAYER, self.p2: [None]*N_CARDS_PER_PLAYER}
    
    def get_card(self, p:Player, pos:int):
        """Low level getter function. Gets the card at index pos on player p's field. Performs no checks."""
        return self.cards[p][pos]
    
    def get_card_index(self, c:Card):
        """gets player, index of card c on playfield."""
        for i in range(N_CARDS_PER_PLAYER):
            if self.get_card(self.p1, i) == c:
                return (self.p1, i)
            if self.get_card(self.p2, i) == c:
                return (self.p2, i)
        raise ValueError("Card not found on field")

    def get_cards(self):
        """Return list-dict of all cards currently on the field"""
        return self.cards
    
    def get_cards_list(self):
        """Return list of all non-None cards currently on the field"""
        cards = [x for x in self.cards[self.p1] if x != None]
        cards += [x for x in self.cards[self.p2] if x != None]
        return cards

    def set_card(self, p:Player, pos:int, c:Optional[Card]):
        """Low level setter function. Sets the card at index pos on player p's field to c. Performs no checks."""
        self.cards[p][pos] = c
        return
    
    def remove_card(self, p:Player, pos:Optional[int]):
        """Removes card at index pos on player p's field."""
        self.set_card(p, pos, None)
        return
    
    def is_free(self, p:Player, pos:int):
        """Checks if a card is at index pos on player p's field."""
        return self.get_card(p, pos) is not None