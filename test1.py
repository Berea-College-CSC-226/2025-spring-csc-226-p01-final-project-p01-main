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

fake_image = pygame.image.load('image/fake.png').convert_alpha()
fake_image = pygame.transform.scale(fake_image, (120, 120))
fake_image.set_colorkey((255, 255, 255), pygame.RLEACCEL)

# Fonts
timer_font = pygame.font.SysFont('Comic Sans MS', 60)
score_font = pygame.font.SysFont('Comic Sans MS', 30)
button_font = pygame.font.SysFont('Comic Sans MS', 36)

class TurtleObject:
    def __init__(self, move_interval):
        self.size = 120
        self.image = turtle_image
        self.x = 0
        self.y = 0
        self.img = turtle_image
        self.visible = True
        self.move_interval = move_interval
        self.last_move_time = time.time()
        self.pop_duration = 0.2

    def move(self):
        self.x = random.randint(0, screen_width - self.size)
        self.y = random.randint(0, screen_height - self.size)
        self.last_move_time = time.time()
        self.visible = True


    def draw(self, screen):
        if self.visible:
            elapsed = time.time() - self.last_move_time
            if elapsed < self.pop_duration:
                scale = elapsed / self.pop_duration
                scale = max(0.2, min(1.0, scale))
                size = int(self.size * scale)
                scaled_img = pygame.transform.smoothscale(self.image, (size, size))
                offset_x = (self.size - size) // 2
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

# Button setup
def draw_button(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = button_font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))
    return pygame.Rect(x, y, w, h)

def game_timer(start_time, duration=20):
    current_time = time.time()
    elapsed = current_time - start_time
    return elapsed >= duration, int(duration - elapsed)

class FakeObject(TurtleObject):
    def __init__(self, interval):
        super().__init__(interval)
        self.image = fake_image
        self.visible = False
        self.show_time = 1  # Stay visible for 1 second
        self.next_appearance = time.time() + random.uniform(2, 5)  # First appearance random in 2-5 sec

    def update(self):
        current_time = time.time()
        if self.visible:
            if current_time - self.last_move_time > self.show_time:
                self.visible = False
                # Schedule next appearance randomly
                self.next_appearance = current_time + random.uniform(2, 4)
        else:
            if current_time >= self.next_appearance:
                self.move()
                self.visible = True
                self.last_move_time = current_time  # Start visibility timer

    def draw(self, screen):
        if self.visible:
            super().draw(screen)

    def is_clicked(self, mouse):
        if self.visible:
            return super().is_clicked(mouse)
        return False

# Initial game variables
score = 0
start_time = None
duration = 20
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
            mouse_pos = pygame.mouse.get_pos()

            if not game_started:
                if normal_button.collidepoint(mouse_pos):
                    move_interval = 1.3
                    game_turtle = TurtleObject(move_interval)
                    fake = None
                    start_time = time.time()
                    game_started = True
                elif hard_button.collidepoint(mouse_pos):
                    move_interval = 0.7
                    game_turtle = TurtleObject(move_interval)
                    fake = FakeObject(move_interval)
                    start_time = time.time()
                    game_started = True
            else:
                if game_turtle.is_clicked(mouse_pos):
                    score += 1
                    game_turtle.move()
                elif fake and fake.is_clicked(mouse_pos):
                    score -= 1
                    fake.move()

    if not game_started:
        title = button_font.render("Choose Difficulty to Start", True, (255, 255, 255))
        screen.blit(title, ((screen_width - title.get_width()) // 2, 180))
        draw_button("Normal", *normal_button, (0, 255, 0))
        draw_button("Hard", *hard_button, (255, 0, 0))
    else:
        game_turtle.update()
        game_turtle.draw(screen)
        if fake:
            fake.update()
            fake.draw(screen)

        timer_done, time_left = game_timer(start_time, duration)
        timer_text = timer_font.render(str(max(0, time_left)), True, (255, 255, 255))
        screen.blit(timer_text, ((screen_width - timer_text.get_width()) // 2, 20))

        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (screen_width - score_text.get_width() - 20, 20))

        if timer_done:
            # ✅ NEW: Save the score to a text file
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
