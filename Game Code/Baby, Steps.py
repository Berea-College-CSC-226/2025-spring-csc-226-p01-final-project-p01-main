# Step 1: Import turtle and random modules
import turtle
import random

# Step 2: Create the TurtlePlayer class (the player character)
class TurtlePlayer:
    def __init__(self):
        # Create and configure the player turtle
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("brown")         # Set turtle color
        self.turtle.penup()                # Prevent turtle from drawing lines
        self.turtle.goto(0, -200)          # Start position at bottom center

    def move_left(self):
        # Move the turtle to the left if not too far left
        x = self.turtle.xcor()
        if x > -280:                       # Add screen boundary check
            self.turtle.setx(x - 30)

    def move_right(self):
        # Move the turtle to the right if not too far right
        x = self.turtle.xcor()
        if x < 280:
            self.turtle.setx(x + 30)

    def check_collision(self, food):
        # Check if player is close enough to catch the food
        return self.turtle.distance(food.turtle) < 30


# Step 3: Create the FoodItem class (the falling object)
class FoodItem:
    def __init__(self):
        # Create and configure the food turtle
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")        # Food shape
        self.turtle.color("red")           # Food color
        self.turtle.penup()
        self.reset_position()              # Start at top
        self.speed = 5                     # Fall speed
        self.points = 1                    # Points per food

    def fall(self):
        # Move food downward
        y = self.turtle.ycor()
        self.turtle.sety(y - self.speed)

    def reset_position(self):
        # Send food back to the top at a random horizontal position
        x = random.randint(-250, 250)
        y = 250
        self.turtle.goto(x, y)

    def get_points(self):
        # Return point value
        return self.points


# Step 4: GameManager controls game logic, player, food, and score
class GameManager:
    def __init__(self):
        self.player = TurtlePlayer()       # Create player turtle
        self.food = FoodItem()             # Create falling food
        self.score = 0                     # Initialize score

        # Create a turtle to display the score
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-280, 260)
        self.update_score_display()

        # Bind keys to player movement
        turtle.listen()
        turtle.onkey(self.player.move_left, "Left")
        turtle.onkey(self.player.move_right, "Right")

    def update(self):
        # Game loop that runs every 100 milliseconds
        self.food.fall()

        # Reset food if it falls off screen
        if self.food.turtle.ycor() < -250:
            self.food.reset_position()

        # Check for collision between player and food
        if self.player.check_collision(self.food):
            self.score += self.food.get_points()   # Add points to score
            self.food.reset_position()             # Respawn food
            self.update_score_

