# Import necessary modules
import turtle
import random

# Global reference to the frame turtle
frame = None

# Food types and their properties
FOOD_TYPES = [
    {"name": "apple", "color": "green", "points": 10, "is_good": True},
    {"name": "carrot", "color": "orange", "points": 10, "is_good": True},
    {"name": "burger", "color": "brown", "points": -2, "is_good": False}
]

# Player class to represent the controllable turtle
class TurtlePlayer:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("brown")
        self.turtle.shapesize(stretch_wid=2, stretch_len=2)
        self.turtle.penup()
        self.turtle.goto(0, -200)
        self.velocity = 0

    def move_left(self):
        self.turtle.setheading(180)
        self.velocity = -15

    def move_right(self):
        self.turtle.setheading(0)
        self.velocity = 15

    def stop(self):
        self.velocity = 0

    def update_position(self):
        x = self.turtle.xcor()
        new_x = x + self.velocity
        if -280 <= new_x <= 280:
            self.turtle.setx(new_x)

    def check_collision(self, food):
        return self.turtle.distance(food.turtle) < 30


# Class representing falling food items
class FoodItem:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.speed = 5
        self.set_type(random.choice(FOOD_TYPES))
        self.reset_position()
        self.turtle.showturtle()

    def set_type(self, food_type):
        self.name = food_type["name"]
        self.points = food_type["points"]
        self.is_good = food_type["is_good"]
        self.turtle.color(food_type["color"])
        if self.is_good:
            self.turtle.shape("circle")
        else:
            self.turtle.shape("triangle")

    def fall(self):
        y = self.turtle.ycor()
        self.turtle.sety(y - self.speed)

    def reset_position(self):
        self.set_type(random.choice(FOOD_TYPES))
        x = random.randint(-250, 250)
        y = 360 + random.randint(0, 150)  # Add random vertical spacing to stagger food drops
        self.turtle.goto(x, y)

    def get_points(self):
        return self.points


# Manages game state
class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.player = TurtlePlayer()
        self.foods = [FoodItem() for _ in range(3)]
        self.score = 0
        self.lives = 5

        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-280, 260)
        self.writer.color("black")

        self.hearts = turtle.Turtle()
        self.hearts.hideturtle()
        self.hearts.penup()
        self.hearts.goto(140, -290)
        self.hearts.color("black")

        self.update_score_display()
        self.update_lives_display()

    def start_game(self):
        self.screen.listen()
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")
        self.screen.onkeyrelease(self.player.stop, "Left")
        self.screen.onkeyrelease(self.player.stop, "Right")
        self.update()
        turtle.update()

    def update(self):
        self.player.update_position()

        for food in self.foods:
            food.fall()

            if food.turtle.ycor() < -250:
                if food.is_good:
                    self.lives -= 1
                    self.update_lives_display()
                    if self.lives == 0:
                        self.game_over()
                        return
                food.reset_position()

            elif self.player.check_collision(food):
                self.score += food.get_points()
                food.reset_position()
                self.update_score_display()

        turtle.update()
        turtle.ontimer(self.update, 30)

    def update_score_display(self):
        self.writer.clear()
        self.writer.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

    def update_lives_display(self):
        self.hearts.clear()
        heart_str = " ".join(["❤️" for _ in range(self.lives)])
        self.hearts.write(heart_str, font=("Arial", 16, "normal"))

    def game_over(self):
        game_over_turtle = turtle.Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.penup()
        game_over_turtle.goto(0, 0)
        game_over_turtle.write("Game Over", align="center", font=("Arial", 24, "bold"))


# Initial welcome screen
class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.game = None

        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(0, 0)
        self.writer.write(
            "Welcome to Turtle Catch!\nPress Enter to start",
            align="center",
            font=("Comic Sans MS", 22, "bold")
        )

        self.screen.listen()
        self.screen.onkey(self.start_game, "Return")

    def start_game(self):
        self.writer.clear()
        self.game = GameManager(self.screen)
        self.game.start_game()


# Main screen setup

def main():
    global frame
    screen = turtle.Screen()
    screen.title("Turtle Catch Game")
    screen.bgcolor("lightblue")
    screen.setup(width=620, height=620)

    turtle.tracer(0)

    frame = turtle.Turtle()
    frame.hideturtle()
    frame.speed(0)
    frame.color("darkgreen", "darkgreen")
    frame.penup()
    frame.goto(-310, 310)
    frame.pendown()
    frame.begin_fill()
    for _ in range(4):
        frame.forward(620)
        frame.right(90)
    frame.end_fill()

    background = turtle.Turtle()
    background.hideturtle()
    background.speed(0)
    background.color("lightblue", "lightblue")
    background.penup()
    background.goto(-290, 290)
    background.pendown()
    background.begin_fill()
    for _ in range(4):
        background.forward(580)
        background.right(90)
    background.end_fill()

    turtle.update()

    StartScreen(screen)
    turtle.done()


if __name__ == "__main__":
    main()
