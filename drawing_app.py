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
from PIL import ImageGrab, Image, ImageTk

import turtle

import os
from tkinter import messagebox
os.environ['PATH'] = r'C:\Program Files\gs\gs10.02.1\bin;' + os.environ['PATH']
import datetime
from PIL import ImageGrab

from PIL import ImageTk

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
        # Create "saved_drawings" folder if it doesn't exist
        if not os.path.exists("saved_drawings"):
            os.makedirs("saved_drawings")

        # Save the WHOLE WINDOW instead of just a crop
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        x1 = x + self.root.winfo_width()
        y1 = y + self.root.winfo_height()

        img = ImageGrab.grab(bbox=(x, y, x1, y1))  # Screenshot whole app window

        # Save the image
        current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"saved_drawings/drawing_{current_date}.png"
        img.save(filename)

        self.status_text.set('Saved drawing to ' + filename)

    def delete_all_drawings(self):
        confirm = messagebox.askyesno("Erase All", "Are you sure you want to delete all saved drawings?")
        if confirm:
            folder = "saved_drawings"
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            self.status_text.set("All drawings erased!")
            messagebox.showinfo("Success", "All saved drawings have been deleted!")

    def show_saved_drawings(self):
        # Create a new window
        saved_window = tk.Toplevel(self.root)
        saved_window.title("Saved Drawings")
        saved_window.geometry("800x600")

        # Check if folder exists
        if not os.path.exists("saved_drawings"):
            tk.Label(saved_window, text="No saved drawings found!").pack()
            return

        # Load all images
        drawings = [file for file in os.listdir("saved_drawings") if file.endswith(".png")]

        if not drawings:
            tk.Label(saved_window, text="No saved drawings found!").pack()
            return

        # Add "Delete All" Button at the top
        delete_button = tk.Button(saved_window, text="Delete All Saved Drawings", bg="red", fg="white",
                                  command=self.delete_all_drawings)
        delete_button.pack(pady=10)

        # Canvas with scrollbar
        canvas = tk.Canvas(saved_window)
        scrollbar = tk.Scrollbar(saved_window, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Store image references
        self.saved_images = []

        for filename in drawings:
            filepath = os.path.join("saved_drawings", filename)
            img = Image.open(filepath)
            img.thumbnail((300, 300))  # Resize for display
            img_tk = ImageTk.PhotoImage(img)

            label = tk.Label(scroll_frame, image=img_tk)
            label.image = img_tk  # Keep a reference to avoid garbage collection
            label.pack(pady=10)

            self.saved_images.append(img_tk)  # Keep all images referenced


def main():
    DrawingApp("Welcome To The Drawing App").root.mainloop()


if __name__ == "__main__":
    main()