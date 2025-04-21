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
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import tkinter as tk
from tkinter import ttk
import string

class Calculator:
    def __init__(self):
        """
        <write purpose of function>
        """
        # initialize application window
        self.master = tk.Tk()
        self.master.configure(background='#d9d9d9')
        self.master.title("Simple Calculator")
        self.master.geometry("400x600")
        # self.master.resizable(False, False)
        # create calculator frame and button frame
        self.calculator_frame, self.button_frame = self.create_frames()
        # create buttons
        self.create_buttons()
        self.result = 0
        #create label to display equation
        self.label_equation = tk.Label(self.calculator_frame, text="", font=('Arial',20), fg='white', anchor='e', bg= 'black')
        self.label_equation.pack(side='top', fill='x', expand=True)
        # create label to display result
        self.label_result = tk.Label(self.calculator_frame, text="", font=('Arial', 15),fg='white', anchor='e' , bg='black')
        self.label_result.pack(side='top', fill='x', expand=True)

    def create_frames(self):
        """
        <write purpose of function>
        :return:
        """
        calculator_frame = ttk.Frame(self.master)
        calculator_frame.pack(side='top', fill='x', padx=10, pady=10)
        button_frame = ttk.Frame(self.master)
        button_frame.pack(side='top', fill='both', expand = True, padx=10, pady=20)

        return calculator_frame, button_frame

    def create_buttons(self):
        """
        <write purpose of function>
        :param self:
        :return:
        """
        button_text = [
                        ['Del','C','(',')'],
                        ['7','8','9','+'],
                        ['4','5','6','-'],
                        ['1','2','3','÷'],
                        ['.','0','^','x'],
                        ['=']]
        buttons = []
        for row in button_text:
            button_row = []
            row_frame = tk.Frame(self.button_frame)
            row_frame.pack(side='top', fill='both', padx=10, expand=True)
            for text in row:
                button = tk.Button(row_frame, text = text, font=('Arial',20))
                button.pack(side=tk.LEFT,fill='both', padx=10, pady=10, expand=True)
                button.bind('<ButtonPress-1>', self.onclick)
                button_row.append(button)
            buttons.append(button_row)
        return buttons

    def onclick(self,event):
        """
        <write purpose of function>
        :param event:
        :return:
        """
        clicked_button = event.widget
        char = clicked_button['text']
        if self.label_equation['text'] != '':
            last_char = self.label_equation['text'][-1]
        else:
            last_char = ''
        #translate special characters
        if char == '÷':
            char = '/'
        if char == 'x':
            char = '*'
        if char == '=':
            try:
                self.result = eval(self.label_equation['text'].replace('^','**'))
                self.label_equation['text'] = str(self.result)
                self.label_result['text'] = ''
            except:
                self.label_equation['text'] = 'SYNTAX ERROR'
                self.label_result['text'] = ''

        elif char == 'C':
            self.label_equation['text'] = ""
            self.label_result['text'] = ""

        elif char in '+^*/':
            if last_char == '':
                self.label_equation['text'] = str(self.result) + char
            if last_char in string.digits+'()':
                self.label_equation['text'] += char
            elif last_char in '+^*/':
                self.label_equation['text'] = self.label_equation['text'][:-1] + char

        elif char in '-':
            if last_char in string.digits + '()':
                self.label_equation['text'] += char
            elif last_char in '+^*/-.':
                self.label_equation['text'] = self.label_equation['text'][:-1] + char

        elif char in '.':
            if last_char not in '.':
                self.label_equation['text'] += char
            else:
                self.label_equation['text'] = self.label_equation['text'][:-1] + char

        elif char == 'Del':
            if self.label_equation['text'] != "":
                self.label_equation['text'] = self.label_equation['text'][:-1]
            else:
                self.label_equation['text'] = ""
        else:
            try:
                self.label_equation['text'] += char
                self.result = eval(self.label_equation['text'].replace('^','**'))
                self.label_result['text'] = str(self.result)
            except:
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