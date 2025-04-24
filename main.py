import tkinter as tk
from quizInterface import QuizInterface
import ctypes

if __name__ == "__main__":
    """
    Starts the quiz game app. This code sets up the window, creates the quiz interface, and keeps the app running until 
    the user closes it.
    
    :return: None
    """
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()
    app = QuizInterface(root)
    root.mainloop()
