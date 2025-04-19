# Step 1, setting up the background

import turtle

class TurtlePlayer:
    #setting up the turtle shape, color and position
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.goto(0, -200)

    def move_left(self):
        x = self.turtle.xcor()
        self.turtle.setx(x - 30)

    def move_right(self):
        x = self.turtle.xcor()
        self.turtle.setx(x + 30)


def main():
    screen = turtle.Screen()
    screen.title("Turtle Catch Game")
    screen.bgcolor("lightblue")
    screen.setup(width=600, height=600)

    player = TurtlePlayer()

    # Adding KEYBOARD CONTROL
    turtle.listen()
    turtle.onkey(player.move_left, "Left")
    turtle.onkey(player.move_right, "Right")

    turtle.done()


if __name__ == "__main__":
    main()

