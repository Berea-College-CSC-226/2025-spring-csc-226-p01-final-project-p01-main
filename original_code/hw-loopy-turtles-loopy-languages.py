# Program: Python
# Author: Faryal Fatima
# Created: 2025-01-28
# Assignment: HW02: Loopy Turtles, Loopy Languages
# # Purpose: To very simply demonstrate the turtle library to demo shapes

# importing the turtle
import turtle
wn = turtle.Screen()

#changing the background color and naming the turtle
wn.bgcolor("light green")
alex = turtle.Turtle()
#shifting the turtles location on the screen
alex.penup()
alex.goto(-90,-50)
#Hiding the turtle and giving it a color and size
alex.pendown()
alex.hideturtle()
alex.color("red")
alex.pensize(6)
#loop to make the square
for i in range(4):
    alex.color("yellow")
    alex.forward(200)
    alex.left(90)
alex.speed(0)
alex.forward(200)
alex.left(180)
# creating stack of square going into the first square

line_length = 300
decrement = 20  # How much the square size reduces
for _ in range(15):  # Reduce size in each iteration
    for _ in range(4):  # Draw square
        # alex.color ("yellow", "green", "purple")
        alex.forward(line_length)
        alex.left(90)
    alex.speed(0)
    line_length -= decrement  # Reduce the size for the next square
    alex.penup()
    alex.forward(decrement / 2)
    alex.right(90)
    alex.forward(decrement / 2)
    alex.left(90)
    alex.pendown()


wn.exitonclick()

######################################################################
# Author: Dr. Scott Heggen             TODO: Change this to your name, if modifying
# Username: heggens                    TODO: Change this to your username, if modifying#
#
# Assignment: HW02: Loopy Turtles, Loopy Languages
# Purpose: To demonstrate the turtle library and loops
######################################################################
# Acknowledgements:
#
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html
# first modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle
import random

wn = turtle.Screen()
wn.colormode(255)

tList = []                      # makes an empty list
head = 0                        # facilitates geometric angles
numTurtles = 10                 # since the turtles spiral, numTurtles = # spirals

for i in range(numTurtles):
    nt = turtle.Turtle()        # Make a new turtle, initialize values
    nt.setheading(head)
    nt.pensize(2)

    nt.color(random.randrange(256),random.randrange(256),random.randrange(256))
    nt.speed(10)
    wn.tracer(30,0)
    tList.append(nt)            # Add the new turtle to the list
    head = head + 360/numTurtles

dist = 15
for angle in range(100):        # moveTurtles(tList,dist,angle) function removed by Dr. Jan Pearce
    for tur in tList:           # Make every turtle on the list do the same actions.
        tur.forward(dist)
        tur.right(angle)

w = tList[0]
w.up()

w.setpos(0,40)  # was w.goto(-130,40) modified by by Dr. Pearce to make functional in Windows

# altered by Dr. Pearce to make font size work in Windows
w.write("How to Think Like a ",move=False,align='center',font=("Arial",30,("bold","normal")))
w.setpos(0,-35)    # was goto(-130,-35) modified by Dr. Pearce to make functional in Windows
w.write("Computer Scientist",move=False,align='center',font=("Arial",30,("bold","normal")))

wn.exitonclick()
