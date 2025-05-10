import tkinter as tk

class Game:

    def __init__(self):
        """
        Handles the board state and its logic
        """

    def turn_switcher(self):
        """
        Switches turns when one's turn is over
        :return:
        """
        pass

    def game_won(self):
        """
        Notifies players who won when game is over
        :return:
        """
        pass

    def board_state(self):
        """
        Controls the board setup, and it's state when checkers have moved
        :return:
        """

        pass


class CheckerPiece:
    def __init__(self):
        """
        Initialize piece
        """
        self.board = [0, 1, 0, 2, 0, 3, 0, 4,
                      5, 0, 6, 0, 7, 0, 8, 0,
                      0, 9, 0, 10, 0, 11, 0, 12,
                      13, 0, 14, 0, 15, 0, 16, 0,
                      0, 17, 0, 18, 0, 19, 0, 20,
                      21, 0, 22, 0, 23, 0, 24, 0,
                      0, 25, 0, 26, 0, 27, 0, 28,
                      29, 0, 30, 0, 31, 0, 32, 0] # Sets up the checkers board, numbers other than 0 are the grids
                                                  # that pieces will be on
        self.pieces = []
        pass

    def piece_position(self):
        for num in self.board:
            if num != 0:
                self.pieces.append(num) # starting piece positions at all of these numbers



    def select_piece(self):
        """
        User clicks the piece, computer registers click
        :return:
        """
        pass

    def move_piece(self):
        """
        Moves the piece after empty grid is selected with checker "in hand"
        :return:
        """
        pass

    def make_piece_king(self):
        """
        Makes piece king when it reaches the opposite side of the board
        :return:
        """
        pass

class Sausage(CheckerPiece):
        def __init__(self):
            super().__init__()
            """
            Inherits all methods from CheckerPiece, is its own type of piece,
            starts on bottom
            """
            pass

class Pepperoni(CheckerPiece):
        def __init__(self):
            super().__init__()
            """
            Inherits all methods from CheckerPiece, is its own type of piece,
            starts on top
            """
            pass

