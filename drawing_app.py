######################################################################
# Author: Dingani Munsaka, Dumisani Chikomo, Abdou Diop
# Username: chikomod, munsakad, diopa
#
# P01: Drawing App
#
# Purpose: Use turtles and tkinter to design a drawing app
#

#######################################################################
# Acknowledgements: Dr Heggen
#
# Original code written by Dr. Jan Pearce

####################################################################################

import tkinter as tk

class DrawingApp:
    def __init__(self, windowtext=""):
        self.root = tk.Tk()
        self.root.minsize(width=800, height=500)
        self.root.maxsize(width=800, height=500)
        self.root.title(windowtext)
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()  # Makes a Tkinter string variable

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Place buttons side by side
        btn1 = tk.Button(button_frame, text="Change Pen Color")
        btn1.pack(side='left', padx=5)

        btn2 = tk.Button(button_frame, text="Change Pen Size")
        btn2.pack(side='left', padx=5)

        btn3 = tk.Button(button_frame, text="Erase")
        btn3.pack(side='left', padx=5)

        btn4 = tk.Button(button_frame, text="Save")
        btn4.pack(side='left', padx=5)

        btn5 = tk.Button(button_frame, text="Clear All")
        btn5.pack(side='left', padx=5)

        btn6 = tk.Button(button_frame, text="Saved Drawings")
        btn6.pack(side='left', padx=5)
    def create_textbox1(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """
        self.myTextBox1 = tk.Text(width =250, height = 250)
        self.myTextBox1.pack()                      # pack means add to window

    def create_label1(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel1Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.pack()

def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = DrawingApp("Welcome To The Drawing App")           # Create a new myTkinter object

    myGUI.create_textbox1()                         # Calls the create textbox method for capturing user input
    myGUI.create_label1()                           # Create a label to writing text into (empty for now)

    myGUI.root.mainloop()                           # Needed to start the event loop


if __name__ == "__main__":
    main()