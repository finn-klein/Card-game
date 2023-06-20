from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game
    from Player import Player
from EventHandlerDict import blank_dict

class Card:
    def __init__(self, g:Game, p:Player):
        self.handled_events = blank_dict()
        self.game = g
        self.player = p
        self.time_on_field = 0

    def set_event_flags(self):
        """Set entries of handled_events dictionary to specify which effects this card has"""
        pass

    def get_time_on_field(self):
        """Getter function that returns the time the card has been on the field"""
        return self.time_on_field
    
    def set_time_on_field(self, val:int):
        """Setter function that updates the card's time on the field"""
        self.time_on_field = val

    def inc_time_on_field(self):
        """Increment the card's time on the field by 1"""
        if self.time_on_field == None:
            raise ValueError("Card not yet on field.")
        self.time_on_field += 1

    
    ##################
    # EVENT HANDLERS #
    ##################
    
    def on_targeted_by_effect(self, source):
        """Event handler for when card is targeted by another card's effect"""
        pass

    def on_start_of_turn(self):
        """Event handler for when turn starts"""
        pass

    def on_end_of_turn(self):
        """Event handler for when turn ends"""
        pass

    def on_activate(self):
        """Event handler for when card's primary effect is activated"""
        pass
