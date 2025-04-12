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
        self.screen.bgcolor("White")
        self.screen.tracer(0)


        self.t = RawTurtle(self.screen)
        self.t.shape('square')
        self.t.color('black')
        self.count = 0
        self.t.penup()

        #self.movement()
        self.root.title(windowtext)

        #Binding Key events
        self.screen.listen()
        self.screen.onkey(Up, "Up")
        self.screen.onkey(Down, "Down")
        self.screen.onkey(Left, "Left")
        self.screen.onkey(Right, "Right")


        self.key_event_handlers = {
            ('UP',): move_up,
            ('DOWN',): move_down,
            ('LEFT',): move_left,
            ('RIGHT',): move_right,
            ('RIGHT', 'UP'): move_up_right,
            ('DOWN', 'RIGHT'): move_down_right,
            ('LEFT', 'UP'): move_up_left,
            ('DOWN', 'LEFT'): move_down_left,
            }

        self.process_events()



def Up():
    key_events.add('UP')

def Down():
    key_events.add('DOWN')

def Left():
    key_events.add('LEFT')

def Right():
    key_events.add('RIGHT')

def process_events(self):
    events = tuple(sorted(key_events))

    if events and events in self.key_event_handlers:
        self.key_event_handlers[events]()

    key_events.clear()
    self.screen.update()
    self.screen.ontimer(process_events, 200)



def move_up(self):
    self.t.setheading(90)
    self.t.forward(25)

def move_down(self):
    self.t.setheading(270)
    self.t.forward(20)

def move_left(self):
    self.t.setheading(180)
    self.t.forward(20)

def move_right(self):
    self.t.setheading(0)
    self.t.forward(20)

def move_up_right(self):
    self.t.setheading(45)
    self.t.forward(20)

def move_down_right(self):
    self.t.setheading(-45)
    self.t.forward(20)

def move_up_left(self):
    self.t.setheading(135)
    self.t.forward(20)

def move_down_left(self):
    self.t.setheading(225)
    self.t.forward(20)










def main():
    myGUI = MyTkinterApp("SneakySnake")
    myGUI.root.mainloop()




if __name__ == "__main__":
    main()