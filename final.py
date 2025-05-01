######################################################################
# Author: Naz Tulegenova and Kushal Phuyel
# Username: tulegenovan and phuyelk
#
# Assignment: Final Project – Turtle Evasion Game
#
# Purpose: This is a simple reaction-based game where the player clicks
# on turtles to earn points while avoiding fake turtles (fish). The game
# features two difficulty levels, a countdown timer, and a popup scoreboard.
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import pygame, random, time
import tkinter as tk
from tkinter import messagebox

pygame.init()
root = tk.Tk()
root.withdraw()

# Screen setup
screen_width = 650
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Turtle Evasion!")

# Load background image
background = pygame.image.load('image/background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Load turtle image
turtle_image = pygame.image.load('image/turtle.png').convert_alpha()
turtle_image = pygame.transform.scale(turtle_image, (120, 120))
turtle_image.set_colorkey((255, 255, 255), pygame.RLEACCEL)

# Load turtle image
fake_image = pygame.image.load('image/fake.png').convert_alpha()
fake_image = pygame.transform.scale(fake_image, (120, 120))
fake_image.set_colorkey((255, 255, 255), pygame.RLEACCEL)

# Fonts
timer_font = pygame.font.SysFont('Comic Sans MS', 60)
score_font = pygame.font.SysFont('Comic Sans MS', 26)
button_font = pygame.font.SysFont('Comic Sans MS', 40)

class TurtleObject:
    """
     Represents the turtle object that appears and moves randomly.
    """
    def __init__(self, interval):
        """
        Initializes a TurtleObject with a set size and image, and sets its movement timing.
        :param interval: the number of seconds between each automatic movement of the object.
        """
        self.size = 120
        self.image = turtle_image
        self.x = 0
        self.y = 0

        # Whether the turtle is currently visible on screen
        self.visible = True

        # Time between automatic moves (depends on difficulty)
        self.move_interval = interval

        # Last time the turtle moved
        self.last_move_time = time.time()

        # Duration of the "pop" animation when turtle appears
        self.pop_duration = 0.2

    def move(self):
        """
        Moves the object to a random location on the screen and makes it visible.
        :return: None
        """
        self.x = random.randint(0, screen_width - self.size)
        self.y = random.randint(0, screen_height - self.size)

        # Update the time the turtle last moved
        self.last_move_time = time.time()

        # Make the turtle visible
        self.visible = True

    def draw(self, surface):
        """
        Draws the turtle on the screen
        :param surface: The Pygame surface to draw on.
        :return:        None
        """
        # Only draw if the turtle is visible
        if self.visible:
            elapsed = time.time() - self.last_move_time

            # Draw the pop animation if it just appeared
            if elapsed < self.pop_duration:
                scale = elapsed / self.pop_duration
                scale = max(0.2, min(1.0, scale)) # Clamp scale between 0.2 and 1.0
                size = int(self.size * scale)
                scaled_img = pygame.transform.smoothscale(self.image, (size, size))
                offset_x = (self.size - size) // 2
                offset_y = (self.size - size) // 2
                surface.blit(scaled_img, (self.x + offset_x, self.y + offset_y))
            else:
                # Draw normally after animation ends
                surface.blit(self.image, (self.x, self.y))

    def is_clicked(self, pos):
        """
        Check if the turtle was clicked while visible
        :param pos:  Mouse position as (x, y) coordinates.
        :return: True if clicked while visible, otherwise False.

        """
        if not self.visible:
            return False
        px, py = pos
        return self.x <= px <= self.x + self.size and self.y <= py <= self.y + self.size

    def update(self):
        """
        Updates the turtle’s visibility and position based on its move interval.
        :return: None
        """
        # Move turtle if interval time passed
        if time.time() - self.last_move_time > self.move_interval:
            self.move()

# Button setup
def draw_button(text, x, y, w, h, color):
    """
    Draws a rectangular button with centered text on the screen.

    :param text:The label to display on the button.
    :param x: X-coordinate of the button
    :param y: Y-coordinate of the button
    :param w: Width of the button.
    :param h: Height of the button.
    :param color: RGB color of the button.
    :return:The Rect object representing the button's area
    """
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = button_font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))
    return pygame.Rect(x, y, w, h)

def game_timer(s_time, dur=20):
    """
    Checks if the game time has elapsed and calculates remaining time.
    :param s_time: The timestamp when the game started.
    :param dur:  The total game duration in seconds.
    :return: bool: True if time is up, False otherwise.
             int: Seconds left until the game ends.
    """
    current_time = time.time()
    elapsed = current_time - s_time
    return elapsed >= dur, int(duration - elapsed)

def pre_game(dur=2):
    """
    Displays a short animated slider bar before the game begins.
    :param dur: How long the pre-game screen should be shown, in seconds.
    :return: None
    """
    popup_start = time.time()
    while time.time() - popup_start < dur:
        screen.blit(background, (0, 0))

        # Message text
        go_text = button_font.render("You have 20 seconds – GO!", True, (255, 255, 255))
        screen.blit(go_text, ((screen_width - go_text.get_width()) // 2, 250))

        # Loading bar
        elapsed = time.time() - popup_start
        bar_width = int((elapsed / dur) * 400)
        pygame.draw.rect(screen, (255, 255, 255), (125, 350, 400, 30), 2)  # Border
        pygame.draw.rect(screen, (0, 255, 0), (125, 350, bar_width, 30))   # Fill

        pygame.display.flip()
        pygame.time.delay(10)


class FakeObject(TurtleObject):
    def __init__(self, interval):
        super().__init__(interval)
        self.image = fake_image
        # Start off as invisible
        self.visible = False

        # How long the fake stays visible when it appears
        self.show_time = 1  # Stay visible for 1 second

        # Schedule the appearance randomly
        self.next_appearance = time.time() + random.uniform(2, 5)  # First appearance random in 2-5 sec

    def update(self):
        current_time = time.time()
        # If visible too long, hide it and schedule next appearance
        if self.visible:
            if current_time - self.last_move_time > self.show_time:
                self.visible = False
                # Schedule next appearance randomly
                self.next_appearance = current_time + random.uniform(2, 4)
        else:
            # Time to appear again
            if current_time >= self.next_appearance:
                self.move()
                self.visible = True
                self.last_move_time = current_time  # Start visibility timer

    def draw(self, surface):
        if self.visible:
            super().draw(surface)

    def is_clicked(self, mouse):
        if self.visible:
            return super().is_clicked(mouse)
        return False

# Initial game variables
score = 0
start_time = None
duration = 21
game_started = False
move_interval = 1.0  # Default to normal

# Buttons for difficulty selection
normal_button = pygame.Rect(150, 280, 150, 60)
hard_button = pygame.Rect(350, 280, 150, 60)

# Placeholder before turtle is created
game_turtle = None
fake = None

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # When user clicks the mouse, get the position
            mouse_pos = pygame.mouse.get_pos()

            if not game_started:
                # Player selects difficulty BEFORE game starts
                if normal_button.collidepoint(mouse_pos):
                    move_interval = 1
                    game_turtle = TurtleObject(move_interval)
                    fake = None
                    pre_game()
                    start_time = time.time()
                    game_started = True
                elif hard_button.collidepoint(mouse_pos):
                    move_interval = 0.7
                    game_turtle = TurtleObject(move_interval)
                    fake = FakeObject(move_interval)
                    pre_game()
                    start_time = time.time()
                    game_started = True
            else:
                # During game: check if player clicked turtle or fake
                if game_turtle.is_clicked(mouse_pos):
                    score += 1 # adds score points
                    game_turtle.move()
                elif fake and fake.is_clicked(mouse_pos):
                    score -= 1 # subtract score point for clicking on fake
                    fake.move()

    if not game_started:
        title = button_font.render("Turtle Evasion!", True, (0, 255, 255))
        screen.blit(title, ((screen_width - title.get_width()) // 2, 100))

        instructions1 = score_font.render("Click on turtles to gain points!", True, (255, 255, 255))
        screen.blit(instructions1, ((screen_width - instructions1.get_width()) // 2, 160))

        instructions2 = score_font.render("Avoid fish(lol) – lose points if clicked!", True, (255, 255, 255))
        screen.blit(instructions2, ((screen_width - instructions2.get_width()) // 2, 200))

        draw_button("Normal", *normal_button, (0, 255, 0))
        draw_button("Hard", *hard_button, (255, 0, 0))
    else:
        game_turtle.update()
        game_turtle.draw(screen)

        # Update and draw the fake object (if in hard mode)
        if fake:
            fake.update()
            fake.draw(screen)

        # Update timer
        timer_done, time_left = game_timer(start_time, duration)
        timer_text = timer_font.render(str(max(0, time_left)), True, (255, 255, 255))
        screen.blit(timer_text, ((screen_width - timer_text.get_width()) // 2, 20))

        # Display current score
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (screen_width - score_text.get_width() - 20, 20))

        # If time is up, show results
        if timer_done:
            # Save the score to a text file
            with open("score_log.txt", "a") as file:
                file.write(f"{score}\n")

            # Existing game over logic
            game_started = False

            # Create the result message
            if score < 5:
                msg = "Better luck next time!"
            elif score < 15:
                msg = "Nice try!"
            else:
                msg = "Turtle Master!"

            result = messagebox.askquestion("Game Over", f"Your Score: {score}\n{msg}\n\nDo you want to play again?")

            if result == 'yes':
                # Reset for new game
                score = 0
                start_time = None
                game_turtle = None
                fake = None
                game_started = False  # Let player choose difficulty again
            else:
                running = False


    pygame.display.flip()

pygame.quit()
