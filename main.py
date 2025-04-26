import tkinter as tk
from quizInterface import QuizInterface
import ctypes

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()
    app = QuizInterface(root)
    root.mainloop()
