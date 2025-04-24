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
# https://chatgpt.com/share/67faccee-4d40-8008-bfc6-1197659d7563 reference for GUI Implementation

####################################################################################

import tkinter as tk
import turtle
import os
import datetime

class DrawingApp:
    def __init__(self, windowtext=""):
        self.root = tk.Tk()
        self.root.minsize(width=800, height=500)
        self.root.maxsize(width=800, height=500)
        self.root.title(windowtext)

        # Canvas for turtle
        self.canvas = tk.Canvas(self.root, width=800, height=400)
        self.canvas.pack()

        # Turtle setup
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.pen = turtle.RawTurtle(self.screen)
        self.pen.shape("circle")
        self.pen.speed(0)
        self.pen.pensize(2)
        self.pen.color("black")

        self.drawing = False
        self.erase_mode = False

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        # Create a frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        # Create textbox
        self.textbox = tk.Entry(self.root, width=60)
        self.textbox.pack(pady=5)

        # Create label
        self.status_text = tk.StringVar()
        self.status_label = tk.Label(self.root, textvariable=self.status_text)
        self.status_label.pack()

        # Buttons with functionality
        tk.Button(button_frame, text="Change Pen Color", command=self.change_pen_color).pack(side='left', padx=5)
        tk.Button(button_frame, text="Change Pen Size", command=self.change_pen_size).pack(side='left', padx=5)
        tk.Button(button_frame, text="Erase", command=self.set_erase_mode).pack(side='left', padx=5)
        tk.Button(button_frame, text="Save", command=self.save_drawing).pack(side='left', padx=5)
        tk.Button(button_frame, text="Clear All", command=self.clear_all).pack(side='left', padx=5)
        tk.Button(button_frame, text="Saved Drawings", command=self.show_saved_drawings).pack(side='left', padx=5)

    def start_draw(self, event):
        self.pen.penup()
        self.pen.goto(event.x - 400, 200 - event.y)
        self.pen.pendown()
        self.drawing = True

    def draw(self, event):
        if self.drawing:
            self.pen.goto(event.x - 400, 200 - event.y)

    def stop_draw(self, event):
        self.drawing = False

    def change_pen_color(self):
        color = self.textbox.get().strip().lower()
        try:
            self.pen.color(color)
            self.erase_mode = False
            self.status_text.set(f"Changed pen color to '{color}'")
        except turtle.TurtleGraphicsError:
            self.status_text.set("Invalid color. Try common names like 'red', 'blue', etc.")

    def change_pen_size(self):
        size_text = self.textbox.get().strip()
        try:
            size = int(size_text)
            self.pen.pensize(size)
            self.erase_mode = False
            self.status_text.set(f"Changed pen size to {size}")
        except ValueError:
            self.status_text.set("Please enter a valid number for pen size.")

    def set_erase_mode(self):
        self.pen.color("white")
        self.erase_mode = True
        self.status_text.set("Eraser ON (white color)")

    def clear_all(self):
        self.pen.clear()
        self.status_text.set("Canvas cleared.")

    def save_drawing(self):
        drawings = os.listdir("saved_drawings")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = "saved_drawings/drawing"+str(len(drawings) + 1)+"_"+current_date+".eps"

        self.screen.getcanvas().postscript(file=filename)
        self.status_text.set('Saved drawing to '+filename)

    def show_saved_drawings(self):
        # Placeholder: this just updates the label for now
        self.status_text.set("No saved drawings available.")


def main():
    DrawingApp("Welcome To The Drawing App").root.mainloop()


if __name__ == "__main__":
    main()