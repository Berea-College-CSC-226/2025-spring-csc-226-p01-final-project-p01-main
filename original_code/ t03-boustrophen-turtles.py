######################################################################
# Author: Dr. Scott Heggen             TODO: Change this to your name, if modifying
# Username: heggens                    TODO: Change this to your username, if modifying
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Modifications by Dr. Jan Pearce, Dr. Mario Nakazawa, and Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def create_turtle():
    """
    A fruitful function for creating a turtle.

    :return: a Turtle object
    """
    stamper = turtle.Turtle()
    stamper.shape("circle")
    stamper.color("green")
    stamper.penup()                 # raise the pen so that we do not have a trail
    return stamper                  # returns a turtle to the line of code where this function was called


def stamp_thirty(tur, size_increase):
    """
    A function for stamping thirty dots to the screen using a turtle.

    :param tur: a Turtle object
    :param size_increase: how much to increase each iteration of the loop
    :return: None
    """
    size = 4                        # initial stride length
    for i in range(30):             # we are going to create 30 stamps
       tur.stamp()                  # Leave an impression on the canvas
       size = size + size_increase          # Increase the move distance on every iteration
       tur.forward(size)            # Move stamper along
       tur.right(34)                #  ...  and turn her


def main():
    """
    The main function of the program, where all things begin

    :return: None
    """
    win = turtle.Screen()
    increase_size = int(input("How much is the stride increase? "))
    miss_turtle = create_turtle()  # Calls the function that creates the turtle. Saves the output of that function to a variable called miss_Turtle
    stamp_thirty(miss_turtle, increase_size)
    win.exitonclick()


main()      # Invokes the main() function

#####################################################################
# Author: Dr. Scott Heggen             TODO: Change this to your name, if modifying
# Username: heggens                    TODO: Change this to your username, if modifying
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# original from http://openbookproject.net/thinkcs/python/english3e/functions.html
#
# Modifications by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def draw_multicolor_square(t, sz):
    """
    Creates a multicolor square

    :param t: a Turtle object
    :param sz: size of a side of a square
    :return: None (void function)
    """
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)


def main():
    """
    Makes a multicolored spiralling set of squares

    :return: None
    """

    wn = turtle.Screen()        # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    wn.title("Dancing Squares!")

    tess = turtle.Turtle()      # Create tess and set some attributes
    tess.pensize(3)

    size = 20                   # Size of the smallest square
    for i in range(15):
        draw_multicolor_square(tess, size)  # Calls this function each iteration of the loop
        size = size + 10        # Increase the size for next iteration
        tess.forward(10)        # Move tess along a little
        tess.right(18)          # and give her some turn

    wn.exitonclick()


main()                          # Calls the main function

######################################################################
# Author: Dr. Scott Heggen               TODO: Change this to your name, if modifying
# Username: heggens                      TODO: Change this to your username, if modifying
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: Demonstrate the turtle library to demo shapes and using images for shapes
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Dr. Jan Pearce - this file is modified from her original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library


def make_roof(wn, shape):
    """
    A new roof! (Made from an image of bricks)

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """
    wn.register_shape("Bricks.gif")         # Registers a shape so it can be used by the turtle library
    shape.penup()
    shape.setpos(80, 80)
    shape.pendown()
    shape.shape("Bricks.gif")               # Sets the shape to the image registered above
    shape.stamp()

def make_main_house(shape):
    """
    Makes the main house rectangle.

    :param shape: a Turtle object
    :return: None
    """

    shape.setpos(30, 47)
    shape.color('#3333FF')
    shape.begin_fill()
    for side in range(2):
        shape.forward(100)
        shape.right(90)
        shape.forward(140)
        shape.right(90)
    shape.end_fill()


def make_window(shape, x, y):
    """
    Adds a window to the house.

    :param shape: a Turtle object
    :param x: the x coordinate of the window
    :param y: the y coordinate of the window
    :return: None
    """
    shape.penup()
    shape.setpos(x, y)             # TODO fix this to use X, Y
    shape.pendown()
    shape.color('#00ff22')
    shape.begin_fill()
    for side in range(2):
        shape.forward(30)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()


def make_door(shape):
    """
    Adds a door to the house.

    :param shape: a Turtle object
    :return: None
    """
    shape.penup()
    shape.setpos(70, -42)
    shape.pendown()
    shape.color('#00ff22')
    shape.begin_fill()
    for side in range(2):
        shape.forward(20)
        shape.right(90)
        shape.forward(50)
        shape.right(90)
    shape.end_fill()


def make_deck(wn, shape):
    """
    Adds a deck to the house.

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """
    wn.register_shape("deck.gif")
    shape.penup()
    shape.setpos(175, -47)
    shape.shape("deck.gif")
    shape.stamp()
    shape.up()


def make_text(shape, txt):
    """
    Writes text to the screen.

    :param shape: a Turtle object
    :return: None
    """
    shape.color("#0F00F0")
    shape.setpos(70,120)
    shape.write(txt, move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def main():
    """
    Draws a house at x, y on the screen.

    :return: None
    """
    wn = turtle.Screen()            # Makes a new turtle screen
    wn.colormode(255)  # change color modes
    wn.bgpic("Lighthouse.gif")      # Sets background to an image; must be a gif!
    shape = turtle.Turtle()
    shape.hideturtle()

    # Function calls for each part of the house
    make_roof(wn, shape)
    make_main_house(shape)
    make_window(shape, 45, 0)
    make_window(shape, 88, 0)
    make_door(shape)
    make_deck(wn, shape)
    make_text(shape, "Scott's Coastal Kentucky Chateau")

    wn.exitonclick()  # wait for a user click on the canvas


main() # call main()