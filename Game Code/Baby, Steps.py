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

class GameManager:
    def __init__(self):
        self.player = TurtlePlayer()
        self.food = FoodItem()

        turtle.listen()
        turtle.onkey(self.player.move_left, "Left")
        turtle.onkey(self.player.move_right, "Right")

    def update(self):
        self.food.fall()

        if self.food.turtle.ycor() < -250:
            self.food.reset_position()            #resetting the food position

        turtle.ontimer(self.update, 100)


def main():
    screen = turtle.Screen()
    screen.title("Turtle Catch Game")
    screen.bgcolor("lightblue")
    screen.setup(width=600, height=600)

    game = GameManager()  # adding the GameManager class to the main
    game.update()

    turtle.done()



if __name__ == "__main__":
    main()

