# main.py

import tkinter as tk
from gui import SolitaireGUI

def main():
    root = tk.Tk()
    game_gui = SolitaireGUI(root)
    game_gui.run()

if __name__ == "__main__":
    main()
