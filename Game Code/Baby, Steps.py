# Import necessary modules
import turtle
import random

# Player class to represent the controllable turtle
class TurtlePlayer:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("brown")
        self.turtle.penup()
        self.turtle.goto(0, -200)  # Start at the bottom center

    def move_left(self):
        x = self.turtle.xcor()
        if x > -280:
            self.turtle.setx(x - 30)  # Move left within boundary

    def move_right(self):
        x = self.turtle.xcor()
        if x < 280:
            self.turtle.setx(x + 30)  # Move right within boundary

    def check_collision(self, food):
        return self.turtle.distance(food.turtle) < 30  # Collision threshold


# Falling food item
class FoodItem:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("red")
        self.turtle.penup()
        self.reset_position()  # Random start position at top
        self.speed = 5
        self.points = 1

    def fall(self):
        y = self.turtle.ycor()
        self.turtle.sety(y - self.speed)  # Move food down

    def reset_position(self):
        x = random.randint(-250, 250)
        y = 250
        self.turtle.goto(x, y)  # Reset food to top with new x

    def get_points(self):
        return self.points  # Return points earned


# Manages game state, score, and game loop
class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.player = TurtlePlayer()
        self.food = FoodItem()
        self.score = 0

        # Create a turtle to write the score
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-280, 240)
        self.update_score_display()

    def start_game(self):
        # Bind keys to player control
        self.screen.listen()
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")

        # Start update loop
        self.update()
        turtle.update()

    def update(self):
        # Move food
        self.food.fall()

        # Reset food if it falls off screen
        if self.food.turtle.ycor() < -250:
            self.food.reset_position()

        # Check for catching food
        if self.player.check_collision(self.food):
            self.score += self.food.get_points()
            self.food.reset_position()
            self.update_score_display()

        # Redraw screen and schedule next update
        turtle.update()
        turtle.ontimer(self.update, 100)

    def update_score_display(self):
        # Display the score at the top
        self.writer.clear()
        self.writer.write(f"Score: {self.score}", font=("Arial", 16, "normal"))


# Initial welcome screen before game starts
class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.game = None  # Will hold GameManager

        # Write welcome message
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
        self.screen.onkey(self.start_game, "Return")  # Start game on Enter

    def start_game(self):
        self.writer.clear()  # Clear welcome message
        self.game = GameManager(self.screen)
        self.game.start_game()  # Start game loop and controls


# Set up main game window

def main():
    screen = turtle.Screen()
    screen.title("Turtle Catch Game")
    screen.bgcolor("lightblue")
    screen.setup(width=620, height=620)

    turtle.tracer(0)  # Disable real-time drawing

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

    turtle.update()  # Show background and frame immediately

    StartScreen(screen)  # Launch the welcome screen

    turtle.done()


# Run main loop
if __name__ == "__main__":
    main()
