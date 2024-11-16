# card.py

import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.face_up = False

    def __repr__(self):
        return f'{self.value} of {self.suit}'
    
    def flip(self):
        self.face_up = not self.face_up

    def is_face_up(self):
        return self.face_up
    
    @classmethod
    def create_deck(cls):
        return [Card(suit, value) for suit in cls.suits for value in cls.values]
    
    @classmethod
    def shuffle_deck(cls):
        deck = cls.create_deck()
        random.shuffle(deck)
        return deck
