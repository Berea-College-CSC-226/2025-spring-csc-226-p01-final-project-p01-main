import pygame
import random
import time

from test1 import move_interval

pygame.init()

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

# Fonts
timer_font = pygame.font.SysFont('Comic Sans MS', 60)
score_font = pygame.font.SysFont('Comic Sans MS', 30)

class TurtleObject:
    def __init__(self):
        self.size = 120
        self.image = turtle_image
        self.x = 0
        self.y = 0
        self.visible = True
        self.last_move_time = time.time()
        self.move_interval = move_interval
        self.pop_duration = 0.2  # seconds

    def move(self):
        self.x = random.randint(0, screen_width - self.size)
        self.y = random.randint(0, screen_height - self.size)
        self.last_move_time = time.time()
        self.visible = True

    def draw(self, screen):
        if self.visible:
            elapsed = time.time() - self.last_move_time
            if elapsed < self.pop_duration: #  If it’s still in pop window, scale it
                scale = elapsed / self.pop_duration  # value from 0 → 1
                scale = max(0.2, min(1.0, scale))
                size = int(self.size * scale)
                # This makes the turtle appear like it’s growing from the center.
                scaled_img = pygame.transform.smoothscale(self.image, (size, size))
                offset_x = (self.size - size) // 2 # This math shifts the turtle so it always grows from the middle.
                offset_y = (self.size - size) // 2
                screen.blit(scaled_img, (self.x + offset_x, self.y + offset_y))
            else:
                screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        if not self.visible:
            return False
        px, py = mouse_pos
        return self.x <= px <= self.x + self.size and self.y <= py <= self.y + self.size

    def update(self):
         if time.time() - self.last_move_time > self.move_interval:
             self.move()


# Initialize game
game_turtle = TurtleObject()
score = 0
start_time = time.time()
duration = 20

def game_timer(start_time, duration=20):
    current_time = time.time()
    elapsed = current_time - start_time
    return elapsed >= duration, int(duration - elapsed)

# Game loop

running = True
game_started = False  # NEW: Flag to track if the game has started

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True

            else:
                mouse_pos = pygame.mouse.get_pos()
                if game_turtle.is_clicked(mouse_pos):
                    score += 1
                    game_turtle.move()

    # Draw background
    screen.blit(background, (0, 0))

    if not game_started:
        # Start screen
        message_font = pygame.font.SysFont("Comic Sans MS", 40)
        message = message_font.render("Click anywhere to start", True, (255, 255, 255))
        screen.blit(message, (
            (screen_width - message.get_width()) // 2,
            screen_height // 2
        ))
    else:
        # Update and draw turtle
        game_turtle.update()
        game_turtle.draw(screen)

    # Timer and Score
    timer_done, time_left = game_timer(start_time, duration)

    # Timer position
    timer_text = timer_font.render(str(max(0, time_left)), True, (255, 255, 255))
    screen.blit(timer_text, ((screen_width - timer_text.get_width()) // 2, 20))

    # Score position
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (screen_width - score_text.get_width() - 20, 20))



    # End game check
    if timer_done:
        # print("Time's up")
        running = False

    pygame.display.flip()

pygame.quit()
