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
        # Initialize player turtle appearance and position
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("brown")
        self.turtle.penup()
        self.turtle.goto(0, -200)

    def move_left(self):
        # Move turtle left with boundary check
        x = self.turtle.xcor()
        if x > -280:
            self.turtle.setx(x - 30)

    def move_right(self):
        # Move turtle right with boundary check
        x = self.turtle.xcor()
        if x < 280:
            self.turtle.setx(x + 30)

    def check_collision(self, food):
        # Check distance between player and food for collision
        return self.turtle.distance(food.turtle) < 30


# Class representing falling food items
class FoodItem:
    def __init__(self):
        # Set up food turtle
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.speed = 7
        self.set_type(random.choice(FOOD_TYPES))
        self.reset_position()
        self.turtle.showturtle()

    def set_type(self, food_type):
        self.name = food_type["name"]
        self.points = food_type["points"]
        self.is_good = food_type["is_good"]
        self.turtle.color(food_type["color"])
        # Set shape depending on whether food is good or junk
        if self.is_good:
            self.turtle.shape("circle")  # Good food = circle
        else:
            self.turtle.shape("triangle")  # Junk food = triangle

    def fall(self):
        # Move food downward
        y = self.turtle.ycor()
        self.turtle.sety(y - self.speed)

    def reset_position(self):
        # Randomize food type and position
        self.set_type(random.choice(FOOD_TYPES))
        x = random.randint(-250, 250)
        y = 360
        self.turtle.goto(x, y)

    def get_points(self):
        # Return the point value of this food
        return self.points


# Manages game state
class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.player = TurtlePlayer()
        self.foods = [FoodItem() for _ in range(3)]  # Multiple falling food items
        self.score = 0
        self.lives = 5

        # Set up turtle to draw score
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-280, 260)
        self.writer.color("black")

        # Set up turtle to draw hearts
        self.hearts = turtle.Turtle()
        self.hearts.hideturtle()
        self.hearts.penup()
        self.hearts.goto(140, -290)  # Bottom right within the frame
        self.hearts.color("black")

        self.update_score_display()
        self.update_lives_display()

    def start_game(self):
        # Set up controls and begin update loop
        self.screen.listen()
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")
        self.update()
        turtle.update()

    def update(self):
        # Loop through each food and update their state
        for food in self.foods:
            food.fall()

            if food.turtle.ycor() < -250:
                # Handle missed good food
                if food.is_good:
                    self.lives -= 1
                    self.update_lives_display()
                    if self.lives == 0:
                        self.game_over()
                        return
                food.reset_position()

            elif self.player.check_collision(food):
                # Handle catching food
                self.score += food.get_points()
                food.reset_position()
                self.update_score_display()

        # Refresh screen and continue game loop
        turtle.update()
        turtle.ontimer(self.update, 100)

    def update_score_display(self):
        # Show the current score
        self.writer.clear()
        self.writer.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

    def update_lives_display(self):
        # Show remaining hearts
        self.hearts.clear()
        heart_str = " ".join(["❤️" for _ in range(self.lives)])  # Closer spacing
        self.hearts.write(heart_str, font=("Arial", 16, "normal"))

    def game_over(self):
        # Show Game Over message
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

        # Draw welcome message
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
        # Remove welcome text and start game
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

    # Draw outer frame
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

    # Draw inner background
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
