# gui.py

import tkinter as tk
from tkinter import messagebox
from game import Solitaire
from card import Card

class SolitaireGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Solitaire")
        self.game = Solitaire()
        self.cards = {}  # Dictionary to keep track of card buttons in the UI
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas to draw the cards
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="green")
        self.canvas.pack()

        # Draw initial game layout
        self.draw_tableau()

        # Add a button for drawing a card from the stock
        self.draw_button = tk.Button(self.root, text="Draw Card", command=self.draw_card)
        self.draw_button.pack()

    def draw_tableau(self):
        """Draw the tableau (7 piles) and waste pile"""
        x_offset = 50
        y_offset = 50
        for idx, pile in enumerate(self.game.tableau):
            for card in pile:
                self.draw_card_on_tableau(card, x_offset + idx * 120, y_offset)

    def draw_card_on_tableau(self, card, x, y):
        """Draw a single card at (x, y) position"""
        color = "black" if card.suit in ['Spades', 'Clubs'] else "red"
        self.canvas.create_rectangle(x, y, x + 60, y + 90, fill="white", outline=color)
        text = f"{card.value[0]} {card.suit[0]}" if card.is_face_up() else "?"
        self.canvas.create_text(x + 30, y + 45, text=text, fill=color)

    def draw_card(self):
        """Handle drawing a card from the stock"""
        card = self.game.draw_from_stock()
        if card:
            self.canvas.create_rectangle(700, 50, 760, 140, fill="white", outline="black")
            text = f"{card.value[0]} {card.suit[0]}"
            self.canvas.create_text(730, 95, text=text, fill="black")
        else:
            messagebox.showinfo("Game Over", "No more cards in the stock!")

    def update_ui(self):
        """Update the UI to reflect changes in the game state"""
        self.canvas.delete("all")
        self.draw_tableau()

    def run(self):
        self.root.mainloop()
