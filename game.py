# game.py

from card import Card

class Solitaire:
    def __init__(self):
        self.deck = Card.shuffle_deck()
        self.tableau = [[] for _ in range(7)]  # Tableau has 7 piles
        self.foundation = {suit: [] for suit in Card.suits}  # A foundation for each suit
        self.stock = []  # Remaining cards
        self.waste = []  # The waste pile (from stock)
        self.setup_game()

    def setup_game(self):
        # Set up tableau (7 piles)
        for i in range(7):
            for j in range(i + 1):
                card = self.deck.pop()
                card.flip() if j == i else None  # Only the last card in a pile is face-up
                self.tableau[i].append(card)
        
        # The rest of the deck goes to the stock
        self.stock = self.deck

    def move_card_to_foundation(self, pile_idx):
        """Move card from tableau to foundation if valid"""
        # Implement logic to move the top card of a tableau pile to foundation
        pass

    def draw_from_stock(self):
        if self.stock:
            card = self.stock.pop()
            self.waste.append(card)
            return card
        return None

    def move_card_between_piles(self, from_pile_idx, to_pile_idx):
        """Move card between tableau piles"""
        # Implement logic for transferring a card between tableau piles
        pass

    def check_victory(self):
        """Check if the game has been won"""
        return all(len(pile) == 13 for pile in self.foundation.values())
