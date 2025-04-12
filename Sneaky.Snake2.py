import tkinter
import tkinter as tk
import tkinter.font as tkfont
from turtle import RawTurtle, TurtleScreen
import random
import pygame



key_events = set()

class MyTkinterApp:
    def __init__(self, windowtext="SneakySnake"):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.screen = TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.screen.tracer(0)

        self.t = RawTurtle(self.screen)
        self.t.shape('square')
        self.t.color('black')
        self.t.penup()

        self.root.title(windowtext)

        # Binding Key events to methods
        self.screen.listen()
        self.screen.onkey(self.Up, "Up")
        self.screen.onkey(self.Down, "Down")
        self.screen.onkey(self.Left, "Left")
        self.screen.onkey(self.Right, "Right")

        self.key_event_handlers = {
            ('UP',): self.move_up,
            ('DOWN',): self.move_down,
            ('LEFT',): self.move_left,
            ('RIGHT',): self.move_right,
            ('RIGHT', 'UP'): self.move_up_right,
            ('DOWN', 'RIGHT'): self.move_down_right,
            ('LEFT', 'UP'): self.move_up_left,
            ('DOWN', 'LEFT'): self.move_down_left,
        }

        self.process_events()

    # Key press handlers (just add to the event set)
    def Up(self):
        key_events.add('UP')

    def Down(self):
        key_events.add('DOWN')

    def Left(self):
        key_events.add('LEFT')

    def Right(self):
        key_events.add('RIGHT')

    def process_events(self):
        events = tuple(sorted(key_events))
        if events and events in self.key_event_handlers:
            self.key_event_handlers[events]()  # Call the function
        key_events.clear()
        self.screen.update()
        self.screen.ontimer(self.process_events, 200)

    # Movement handlers
    def move_up(self):
        self.t.setheading(90)
        self.t.forward(25)

    def move_down(self):
        self.t.setheading(270)
        self.t.forward(25)

    def move_left(self):
        self.t.setheading(180)
        self.t.forward(25)

    def move_right(self):
        self.t.setheading(0)
        self.t.forward(25)

    def move_up_right(self):
        self.t.setheading(45)
        self.t.forward(25)

    def move_down_right(self):
        self.t.setheading(-45)
        self.t.forward(25)

    def move_up_left(self):
        self.t.setheading(135)
        self.t.forward(25)

    def move_down_left(self):
        self.t.setheading(225)
        self.t.forward(25)


def main():
    myGUI = MyTkinterApp("SneakySnake")
    myGUI.root.mainloop()


if __name__ == "__main__":
    main()