class Flashcard:

    def __init__(self, term, definition):

        self.term = term        #term: The word or phrase to be studied
        self.definition = definition   #definition: The explanation of the term

    def __str__(self):

        return f"{self.term}"   #returns string representation of the object