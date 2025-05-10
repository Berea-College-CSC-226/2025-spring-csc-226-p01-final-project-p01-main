import tkinter as tk


class TkinterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=100, height=100)
        self.root.maxsize(width=1000, height=500)
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8]
        self.columns = [1, 2, 3, 4, 5, 6, 7, 8]
        self.button = None
        # self.board = list(range(1, 65))
        # self.pieces = []

    def create_board(self):
        for row in self.rows:
            for col in self.columns:
                self.button = tk.Button(self.root, width=15, height=3)
                self.button.grid(row = row, column = col)

    def create_pieces(self):
        for row in self.rows[:3]: # Puts starting pieces in first 3 rows
            for col in self.columns:
                if (row + col) % 2 != 0: # Alternates spots for pieces
                    self.button = tk.Button(self.root, width=5, height=1)
                    self.button.grid(row=row, column=col)

            for row in self.rows[5:]: # Puts starting pieces in bottom 3 rows
                for col in self.columns:
                    if (row + col) % 2 != 0:
                        self.button = tk.Button(self.root, width=5, height=1)
                        self.button.grid(row=row, column=col)

            # for col in self.columns[1::2]:
            #     self.button = tk.Button(self.root, width=5, height=1)
            #     self.button.grid(row=row, column=col)












def main():
    myGUI = TkinterGUI()
    myGUI.create_board()
    myGUI.create_pieces()

    myGUI.root.mainloop()

if __name__ == "__main__":
    main()