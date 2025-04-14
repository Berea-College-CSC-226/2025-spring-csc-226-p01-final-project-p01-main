######################################################################
# Author: Hope Michael, Tafreed Sardar
# Username: michaelh, sadart
#
# Assignment: P01: Final Project
#
# Purpose: Building an interactive calculator and using a turtle object to write the result.
######################################################################
# Acknowledgements:
#
# some of the code is originally from: https://runestone.academy/ns/books/published/2025_Spring_CSC_226/gu-iand-event-driven-programming_a-programming-example.html

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import tkinter as tk
from tkinter import ttk
import turtle

class Calculator:
    def __init__(self):
        """
        <write purpose of function>
        """
        self.master = tk.Tk()
        self.master.title("Simple Calculator")
        self.calculator_frame, self.turtle_frame = self.create_frames()



    def create_frames(self):
        """
        <write purpose of function>
        :return:
        """
        calculator_frame = tk.Frame(self.master)
        calculator_frame.grid(column=2, row=1)
        turtle_frame = tk.Frame(self.master)
        turtle_frame.grid(row=0, column=1)

        return calculator_frame, turtle_frame

    def create_widgets(self):
        """
        <write purpose of function>
        :param self:
        :return:
        """
        pass
        # Create the buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 2)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("=", 4, 0)
        self.create_button("C", 5, 0)
        self.create_button("CE", 5, 1)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)

    def compute_equation(self):
        """
        <write purpose of function>
        :param self:
        :return:
        """
        pass

    def write_result(self):
        """
        <write purpose of function>
        :param self:
        :return:
        """
        pass

def main():
    """
    <write purpose of function>
    :return: None
    """
    calculator = Calculator()
    calculator.master.mainloop()


if __name__ == '__main__':
    main()