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
import random

class Calculator:
   DIGITS = '0123456789'
   def __init__(self):
       """
       Initializes the Calculator application window and its components
       """
       # initialize application window
       self.master = tk.Tk()
       self.master.configure(background='#d9d9d9')
       self.master.title("Simple Calculator")
       self.master.geometry("450x600")
       self.master.resizable(False, False)
       # create calculator frame and button frame
       self.calculator_frame, self.button_frame= self.create_frames()
       # create buttons
       self.create_buttons()
       self.result = 0
       self.game_equation = ''
       #create label to display equation
       self.label_equation = tk.Label(self.calculator_frame, text="", font=('Arial',20), fg='white', anchor='e', bg= 'black')
       self.label_equation.pack(side='top', fill='x', expand=True)
       # create label to display result
       self.label_result = tk.Label(self.calculator_frame, text="", font=('Arial', 15),fg='white', anchor='e' , bg='black')
       self.label_result.pack(side='top', fill='x', expand=True)
       # Calculator mode: starts as a calculator but can be set to game mode
       self.mode = 'CAL'

   def create_frames(self):
       """
       Creates calculator and button frames.
       :return: Tuple containing calculator and turtle frames
       """
       calculator_frame = ttk.Frame(self.master)
       calculator_frame.pack(side='top', fill='x', padx=10, pady=10)
       button_frame = ttk.Frame(self.master)
       button_frame.pack(side='top', fill='both', expand = True, padx=10, pady=20)
       return calculator_frame, button_frame

   def create_buttons(self):
       """
       Creates calculator buttons
       :return: Returns list of buttons
       """
       button_text = [
                       ['MODE','Del','C','RESET'],
                       ['7','8','9','+'],
                       ['4','5','6','-'],
                       ['1','2','3','÷'],
                       ['.','0','^','x'],
                       ['(',')','=']]
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

   def generate_game_equation(self):
       """
       Creates random equation with missing values
       :return: Random equation string
       """
       equation_signs = '+-*//*' #additional multiplication and division symbols to increase odds
       templates = ['i=isi','i=isisi','isi=i','isi=isi','isisi=i','i=isisisi','isi=isisi','isisi=isi','isisisi=i']
       while True:
           equation = []
           for char in random.choice(templates):
               if char == 'i':
                   equation += [str(random.randint(1,99))]
               elif char == 's':
                   equation += [str(random.choice(equation_signs))]
               else:
                   equation += [char]
           if eval(''.join(equation).replace('=','==')):
               break
       #replaces part of equation with '__'
       equals_index = equation.index('=')
       equation[equals_index+1] = len(equation[equals_index+1]) * '_'
       return ' '.join(equation)

   def onclick(self,event):
       """
       Event handler for when button is clicked
       :param event: The GUI framework’s event object for clicked button
       :return: None
       """
       clicked_button = event.widget
       #get pressed character
       char = clicked_button['text']
       if self.label_equation['text'] != '':
           last_char = self.label_equation['text'][-1]
       else:
           last_char = ''
       # translate special characters
       if char == '÷':
           char = '/'
       if char == 'x':
           char = '*'

       #changes calculator mode when MODE button is clicked
       if clicked_button['text'] == 'MODE':
           self.label_result['text'] = ''
           if self.mode == 'GAME':
               self.mode = 'CAL'
               self.label_equation['text'] = ''
           else:
               self.mode = 'GAME'
               self.game_equation = self.generate_game_equation()
               self.label_equation['text'] = self.game_equation
       #functions as a regular calculator in CAL mode
       elif self.mode == 'CAL':
           if char == '=':
               try:
                   self.result = eval(self.label_equation['text'].replace('^','**'))
                   self.label_equation['text'] = str(self.result)
                   self.label_result['text'] = ''
               except:
                   self.label_equation['text'] = 'SYNTAX ERROR'
                   self.label_result['text'] = ''

           elif char == 'C' or char == 'RESET':
               self.label_equation['text'] = ""
               self.label_result['text'] = ""

           elif char in '+^*/':
               if last_char == '':
                   self.label_equation['text'] = str(self.result) + char
               if last_char in self.DIGITS+'()':
                   self.label_equation['text'] += char
               elif last_char in '+^*/':
                   self.label_equation['text'] = self.label_equation['text'][:-1] + char

           elif char in '-':
               if last_char in self.DIGITS + '()':
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
       else:
           if char in self.DIGITS:
               if self.label_equation['text'].find('_') != -1:
                   self.label_result['text'] += char
                   self.label_equation['text'] = self.label_equation['text'].replace('_',char,1)
           elif char == 'C':
               self.label_equation['text'] = self.game_equation
               self.label_result['text'] = ''
           elif char == 'RESET':
               self.label_result['text'] = ''
               self.game_equation = self.generate_game_equation()
               self.label_equation['text'] = self.game_equation
           elif char == 'Del':
               self.label_result['text'] = self.label_result['text'][:-1]
               equation = self.game_equation
               for char in self.label_result['text']:
                   equation = equation.replace("_", char, 1)
               self.label_equation['text'] = equation
           elif char == '=':
               if eval(self.label_equation['text'].replace('=','==')):
                   self.label_result['text'] = random.choice(["YOU'RE A MATH GENIUS :)",'CORRECT ANSWER :)','SCOTT HEGGENS TAUGHT YOU WELL :)'])
               else:
                   self.label_result['text'] = random.choice(['NOT QUITE!','CLEAR, AND TRY AGAIN!', 'INCORRECT ANSWER :(','SCOTT HEGGENS FACEPALMS :('])

def main():
   """
   Runs calculator program. Initializes the Calculator class and starts the Tkinter main loop.
   :return: None
   """
   calculator = Calculator()
   calculator.master.mainloop()

if __name__ == '__main__':
   main()
