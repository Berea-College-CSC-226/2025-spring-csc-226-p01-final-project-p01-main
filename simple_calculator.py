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
        self.master = tk.Tk() #initialize application window
        self.master.title("Simple Calculator")
        self.calculator_frame, self.turtle_frame = self.create_frames() #create calculator frame and turtle frame
        # create buttons
        self.addition, self.subtraction, self.multiplication, self.division, self.power, self.zero, self.one, self.two,
        self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine = self.create_buttons()
        self.result = 0
        #TODO CREATE SINGLE UPDATE LABEL


    def create_frames(self):
        """
        <write purpose of function>
        :return:
        """
        calculator_frame = tk.Frame(self.master)
        calculator_frame.grid(column=0, row=0)
        turtle_frame = tk.Frame(self.master)
        turtle_frame.grid(row=0, column=1)

        return calculator_frame, turtle_frame

    def create_buttons(self):
        """
        <write purpose of function>
        :param self:
        :return:
        """
        command_func_list = [add_event, sub_event, div_event, mul_event, power_event, zero_event, one_event, two_event,
                             three_event, four_event, five_event, six_event, seven_event, eight_event, nine_event]
        #TODO: CREATE A FUNCTION STUB FOR EACH FUNCTION REFERENCES IN THE command_func_list LIST
        buttons = []
        for command_func in command_func_list:
            button = tk.Button(self.calculator_frame, command=command_func)
            button.pack(side=tk.LEFT)
            buttons.append(button)
        return tuple(buttons)

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