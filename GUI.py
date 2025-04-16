import tkinter as tk
from functools import partial

class TkinterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=100, height=100)
        self.root.maxsize(width=1000, height=500)
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8]
        self.columns = [1, 2, 3, 4, 5, 6, 7, 8]
        self.square = None
        self.pepperoni = None
        self.sausage = None
        self.counter = 0
        # self.square_pos = []
        # self.pepperoni_pos = []
        # self.sausage_pos = []
        # self.piece = None
        # self.board = list(range(1, 65))
        # self.pieces = []

    def create_board(self):
        for row in self.rows:
            for col in self.columns:
                command = partial(self.square_handler, square_pos = row + col) # Using regular command or lambda would only store the last value at runtime. Using partial to evaluate each position as they go
                self.square = tk.Button(self.root, width=15, height=3, command=command)
                self.square.grid(row = row, column = col)

    def create_pieces(self):
        for row in self.rows[:3]: # Puts starting pieces in first 3 rows
            for col in self.columns:
                if (row + col) % 2 != 0: # Alternates spots for pieces
                    command = partial(self.pepperoni_handler, pep_pos = row + col)
                    self.pepperoni = tk.Button(self.root, width=5, height=1, command=command)
                    self.pepperoni.grid(row=row, column=col)

        for row in self.rows[5:]: # Puts starting pieces in bottom 3 rows
            for col in self.columns:
                if (row + col) % 2 != 0:
                    command = partial(self.sausage_handler, sausage_pos = row + col)
                    self.sausage = tk.Button(self.root, width=5, height=1, command=command)
                    self.sausage.grid(row=row, column=col)

    def pepperoni_handler(self, pep_pos):
        self.counter = pep_pos
        print(self.counter)

    def sausage_handler(self, sausage_pos):
        print(sausage_pos)

    def square_handler(self, square_pos):
         print(square_pos)
             # make button appear there, make other one disappear






















def main():
    myGUI = TkinterGUI()
    myGUI.create_board()
    myGUI.create_pieces()

    myGUI.root.mainloop()

if __name__ == "__main__":
    main()