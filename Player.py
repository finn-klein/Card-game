from Deck import Deck

class Player:
    def __init__(self, points:int, deck:Deck):
        self.points = points
        self.deck = deck
        self.hand = list()
    
    def get_points(self):
        """Getter function that returns the player's remaining points"""
    
    def set_points(self, val:int):
        """Setter function that updates the player's points"""
    
    def dec_points(self, delta=1):
        """Decrease points by 1"""
        self.points -= delta

    def draw(self, n=1):
        """Draw the top n cards from the deck"""
        self.hand.append(self.deck.get_cards(n))