import tkinter as tk # Python's most commonly used GUI package.
from tkinter import messagebox


class MyTkinterApp:
    def __init__(self, windowtext="Exploring Tkinter"):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """
        self.root = tk.Tk()                         # Create the root window where all widgets go
        self.root.minsize(width=250, height=100)    # Sets the window's minimum size
        self.root.maxsize(width=250, height=100)    # Sets the window's maximum size
        self.root.title(windowtext) # Sets root window title


        self.count = 0                              # Click counter for myButton1
        self.myButton1 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()      # Makes a Tkinter string variable
        self.myTextLabel1 = None
        self.quit_button = None # quit button

    def create_button1(self, buttontext="Push"):
        """
        Creates a button with the given buttontext

        :param buttontext: The text on the button
        :return: None
        """
        self.myButton1 = tk.Button(self.root, text=buttontext, command=self.button1_handler)
        # Note that when myButton1 button is pushed, self.button1handler is called

        self.myButton1.grid(row = 0, column = 0)                       # pack means add to window

    def create_textbox1(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """

        self.myTextBox1.grid(row = 0, column = 1)                      # pack means add to window

    def create_label1(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel1Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.grid(row = 1 , column = 0)                  # pack means add to window

    def button1_handler(self):
        """
        Event handler for myButton1 above.
        Gets the text from the textbox and writes in myTextLabel1

        :return: None
        """
        txt = self.myTextBox1.get()                 # Retrieves the text entered by the user
        self.count += 1                             # increments each time the handler is called (button is pressed)
        if self.count % 10 == 0:
            message = "Wow, {1} clicks! Keep it up, {0}!".format(txt, self.count)
            response = messagebox.askquestion("Confirmation", "Do you want to continue?")
            if response == 'no':
                self.root.destroy()
        else:
            message = "Hey {0}, click it again!\nYou have clicked the button {1} times.".format(txt, self.count)
        self.myTextLabel1Text.set(message)

    def create_quit_button(self, t="QUIT"):
        self.quit_button = tk.Button(self.root, text=t, command=self.quit_handler)
        self.quit_button.grid(row = 1, column = 1)

    def quit_handler(self):
        self.root.destroy()


def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = MyTkinterApp("CSC226 Hello GUI")           # Create a new myTkinter object

    myGUI.create_button1("What is your name?")      # Calls the create button method to create a button
    myGUI.create_textbox1()                         # Calls the create textbox method for capturing user input
    myGUI.create_label1()                           # Create a label to writing text into (empty for now)
    myGUI.create_quit_button("QUIT")  # A button to quit the program
    myGUI.root.mainloop()                           # Needed to start the event loop


if __name__ == "__main__":
    main()
