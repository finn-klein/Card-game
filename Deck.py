from Card import Card
import random

class Deck:
    def __init__(self, cards:list[Card]):
        self.cards = cards

    def shuffle_deck(self):
        """Shuffle the cards in this deck"""
        random.shuffle(self.cards) # shuffle is an in-place operation
    
    def get_cards(self, n:int = 1) -> list[Card]:
        """Gets the top n cards from this deck"""
        if n > len(self.cards):
            raise ValueError("Cannot get more cards than in deck")
        # take the n last cards off the deck
        selected_cards = self.deck[-n:]
        self.deck = self.deck[:-n]
        return selected_cards
    
    def add_to_deck(self, cards:Card | list[Card]):
        """Adds cards on top of the deck, starting with the first in the list"""
        if type(cards) == Card:
            self.deck.append(cards)
            return
        for c in cards:
            self.deck.append(c)

def build_from_list(card_list:str) -> Deck:
    """Alternative constructor to build deck from list of cards"""
    # TODO
    pass