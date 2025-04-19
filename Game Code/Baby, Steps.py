# Step 1, setting up the background

import turtle

class TurtlePlayer:
    #setting up the turtle shape, color and position
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("brown")  #Changing turtles color
        self.turtle.penup()
        self.turtle.goto(0, -200)


    def move_left(self):
        x = self.turtle.xcor()
        if x > -280:                   #Adding screen boundaries
            self.turtle.setx(x - 30)

    def move_right(self):
        x = self.turtle.xcor()
        if x < 280:
            self.turtle.setx(x + 30)

import random  # Make sure this is at the top

class FoodItem:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")    #This is the shape of the food
        self.turtle.color("red")
        self.turtle.penup()
        self.reset_position()
        self.speed = 5
        self.points = 1

    def fall(self):
        y = self.turtle.ycor()
        self.turtle.sety(y - self.speed)

    def reset_position(self):
        x = random.randint(-250, 250)
        y = 250
        self.turtle.goto(x, y)

    def get_points(self):
        return self.points

def main():
    screen = turtle.Screen()
    screen.title("Turtle Catch Game")  #Title of the Game
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

