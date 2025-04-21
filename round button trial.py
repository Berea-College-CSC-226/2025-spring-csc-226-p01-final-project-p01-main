import tkinter as tk

def on_click(event):
    print("Circle button clicked!")

root = tk.Tk()

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()


circle = canvas.create_oval(10, 10, 90, 90, fill="skyblue", outline="")


canvas.tag_bind(circle, "<Button-1>", on_click)

root.mainloop()
