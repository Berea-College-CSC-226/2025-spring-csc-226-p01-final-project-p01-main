# main.py

from data_loader import load_flashcards
from flashcard import FlashcardSession
from gui import FlashcardApp

def main():
    # Step 1: Load flashcard data
    flashcards = load_flashcards()

    if not flashcards:
        print("No flashcards loaded. Exiting.")
        return

    # Step 2: Create a flashcard session
    session = FlashcardSession(flashcards)

    # Step 3: Start GUI with the session
    app = FlashcardApp(session)
    app.run()

if __name__ == "__main__":
    main()
