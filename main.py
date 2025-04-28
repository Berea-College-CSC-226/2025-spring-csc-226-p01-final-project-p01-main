from flashcard import FlashcardDeck
from GUIClass import FlashcardGUI

def main():
    deck = FlashcardDeck()
    app_gui = FlashcardGUI(deck)
    app_gui.run()

if __name__ == "__main__":
    main()
