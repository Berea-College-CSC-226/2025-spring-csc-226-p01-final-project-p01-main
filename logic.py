import random

class Flashcard:
    def __init__(self, term, definition):
        # Each flashcard has a term, a definition, and a score (default 0)
        self.term = term
        self.definition = definition
        self.score = 0


class FlashcardDeck:
    def __init__(self):
        # Holds a list of all flashcards
        self.flashcards = []

    def add_flashcard(self, term, definition):
        # Add a new flashcard to the deck
        self.flashcards.append(Flashcard(term, definition))

    def load_from_file(self, path):
        # Load flashcards from a file using the format: term::definition
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if "::" in line:
                        term, definition = line.strip().split("::", 1)
                        self.add_flashcard(term, definition)
            return True, ""
        except Exception as e:
            return False, str(e)

    def get_random_flashcard(self):
        # Return one flashcard using weighted random selection
        if not self.flashcards:
            return None
        weights = [1 / (1 + card.score) for card in self.flashcards]
        return random.choices(self.flashcards, weights=weights, k=1)[0]

    def get_total_score(self):
        # Return total score and number of cards
        total_cards = len(self.flashcards)
        total_score = sum(card.score for card in self.flashcards)
        return total_score, total_cards





















