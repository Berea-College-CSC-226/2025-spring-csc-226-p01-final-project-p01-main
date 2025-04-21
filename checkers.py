import tkinter as tk
from functools import partial

class TkinterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=100, height=100)
        self.root.maxsize(width=1000, height=500)
        self.rows = [1,2,3,4,5,6,7,8]
        self.columns = [1,2,3,4,5,6,7,8]
        self.pepperonis = {}
        self.sausages = {}
        self.pep_tag = 'pep'  # Tag to have pepperoni pieces be differentiated
        self.sas_tag = 'sas'  # Tag to have sausage pieces be differentiated
        self.current_tag = ''
        self.selected_piece = None

    def setup_board(self):
        '''
        Sets up the buttons for the board
        :return:
        '''
        for row in self.rows:
            for col in self.columns:
                if (row + col) % 2 != 0:
                    command = partial(self.square_handler, square_pos = [row, col]) # Command called when any square is clicked
                    square = tk.Button(self.root, width = 15, height = 3, command = command, bg = 'brown')
                    square.grid(row = row, column = col)
                else:
                    command = partial(self.square_handler, square_pos=[row, col])  # Command called when any square is clicked
                    square = tk.Button(self.root, width=15, height=3, command=command, bg='red')
                    square.grid(row=row, column=col)



    def square_handler(self, square_pos):
        '''
        When board square is clicked, this function executes
        :param square_pos:
        :return:
        '''
        self.create_new_piece(square_pos, self.current_tag) # Calls create_new_piece, passes the square position for piece to be created on, and the current type of piece




    def setup_pieces(self):
        '''
        Setting up all the initial pieces
        :return:
        '''
        for row in range(1, 4): # First 3 rows
            for col in range(1, 9):
                if (row + col) % 2 != 0: # Alternates Squares
                    command = partial(self.piece_handler, tag = self.pep_tag, piece_pos = [row, col])
                    pepperoni = tk.Button(self.root, width=5, height=1, command=command, bg = 'yellow')
                    pepperoni.grid(row=row, column=col)
                    pepperoni.tag = self.pep_tag # Gives pepperoni "tag" attribute, recognizes pieces as 'pep'
                    self.pepperonis[row, col] = pepperoni # Stores the position of pepperoni pieces in a dictionary; do print(self.pepperonis) to see result

        for row in range(6, 9): # Bottom 3 rows
            for col in range(1, 9):
                if (row + col) % 2 != 0: # Alternates squares
                    command = partial(self.piece_handler, tag = self.sas_tag, piece_pos = [row, col])
                    sausage = tk.Button(self.root, width=5, height=1,command=command, bg = 'grey')
                    sausage.grid(row=row, column=col)
                    sausage.tag = self.sas_tag # Gives sausage "tag" attribute, recognizes pieces as 'sas'
                    self.sausages[row,col] = sausage # Sausage pieces stored in dict

    def piece_handler(self, tag, piece_pos):
        '''
        Occurs when either sausage or pepperoni is clicked
        :param tag:
        :param piece_pos:
        :return:
        '''
        self.current_tag = tag # Tag flips between pepperoni and sausage, whatever one is clicked
        self.selected_piece = piece_pos # Clicked piece shows its position
        return piece_pos


    def create_new_piece(self, square_pos, current_tag):
        square_num = square_pos[0] + square_pos[1]
        selected_piece_pos = self.selected_piece[0] + self.selected_piece[1]
        square_pos_tuple = tuple(square_pos)  # Lists aren't hashable, use tuple key instead

        if self.current_tag == self.pep_tag:
            if square_num == selected_piece_pos or square_num == selected_piece_pos + 2 or square_num == selected_piece_pos + 4 or square_num == selected_piece_pos - 2 or square_num == selected_piece_pos - 4: # Pepperoni can move in all valid directions, including hops and kinged movement
                command = partial(self.piece_handler, tag = self.current_tag, piece_pos = square_pos)
                button = tk.Button(self.root, width=5, height=1, command=command, bg = 'yellow')
                button.grid(row=square_pos[0], column=square_pos[1])
                button.tag = current_tag
                self.pepperonis[square_pos_tuple] = button # Stores piece into the correct dictionary
                self.destroy_piece()  # Destroys the current piece so it appears to "move" to the selected square



        if self.current_tag == self.sas_tag:
            if square_num == selected_piece_pos or square_num == selected_piece_pos - 2 or square_num == selected_piece_pos - 4 or square_num == selected_piece_pos + 2 or square_num == selected_piece_pos + 4: # Sausage can move in all valid directions, including hops and kinged movement
                command = partial(self.piece_handler, tag = self.current_tag, piece_pos = square_pos)
                button = tk.Button(self.root, width=5, height=1, command=command, bg = 'grey')
                button.grid(row=square_pos[0], column=square_pos[1])
                button.tag = current_tag
                self.sausages[square_pos_tuple] = button
                self.destroy_piece()  # Destroys the current piece so it appears to "move" to the selected square

    def destroy_piece(self):
        piece_tuple = tuple(self.selected_piece)

        if self.current_tag == 'sas':
            selected_piece = self.sausages[piece_tuple]
            selected_piece.grid_forget()

        elif self.current_tag == 'pep':
            selected_piece = self.pepperonis[piece_tuple]
            selected_piece.grid_forget()












def main():
    game = TkinterGUI()
    game.setup_board()
    game.setup_pieces()

    game.root.mainloop()

if __name__ == "__main__":
    main()



